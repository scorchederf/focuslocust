---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# System Service Descriptor Table - SSDT

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-glimpse-into-ssdt-in-windows-x64-kernel` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/glimpse-into-ssdt-in-windows-x64-kernel.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Service Descriptor Table - SSDT](../../topics/miscellaneous-reversing-forensics/system-service-descriptor-table-ssdt.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-glimpse-into-ssdt-in-windows-x64-kernel |
| name | System Service Descriptor Table - SSDT |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel/glimpse-into-ssdt-in-windows-x64-kernel.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (134).png
- image (306).png
- image (481).png
- image (50).png
- image (501).png
- image (72).png
- retrieving-ssdt-routine-addresses.gif
_body: "# System Service Descriptor Table - SSDT\n\n## What is SSDT\n\nSystem Service Dispatch Table or SSDT, simply is an\
  \ array of addresses to kernel routines for 32 bit operating systems or an array of relative offsets to the same routines\
  \ for 64 bit operating systems. \n\nSSDT is the first member of the Service Descriptor Table kernel memory structure as\
  \ shown below:\n\n```cpp\ntypedef struct tagSERVICE_DESCRIPTOR_TABLE {\n    SYSTEM_SERVICE_TABLE nt; //effectively a pointer\
  \ to Service Dispatch Table (SSDT) itself\n    SYSTEM_SERVICE_TABLE win32k;\n    SYSTEM_SERVICE_TABLE sst3; //pointer to\
  \ a memory address that contains how many routines are defined in the table\n    SYSTEM_SERVICE_TABLE sst4;\n} SERVICE_DESCRIPTOR_TABLE;\n\
  ```\n\n{% hint style=\"info\" %}\nSSDTs used to be hooked by AVs as well as rootkits that wanted to hide files, registry\
  \ keys, network connections, etc. Microsoft introduced PatchGuard for x64 systems to fight SSDT modifications by BSOD'ing\
  \ the system.\n{% endhint %}\n\n## In Human Terms\n\nWhen a program in user space calls a function, say `CreateFile`, eventually\
  \ code execution is transfered to `ntdll!NtCreateFile` and via a **syscall** to the kernel routine `nt!NtCreateFile`.\n\n\
  Syscall is merely an index in the System Service Dispatch Table \\(SSDT\\) which contains an array of pointers for 32 bit\
  \ OS'es \\(or relative offsets to the Service Dispatch Table for 64 bit OSes\\) to all critical system APIs like `ZwCreateFile`,\
  \  `ZwOpenFile` and so on..\n\nBelow is a simplified diagram that shows how offsets in SSDT `KiServiceTable`  are converted\
  \ to absolute addresses of corresponding kernel routines:\n\n![](../../.gitbook/assets/image%20%28306%29.png)\n\nEffectively,\
  \ syscalls and SSDT \\(`KiServiceTable`\\) work togeher as a bridge between userland API calls and their corresponding kernel\
  \ routines, allowing the kernel to know which routine should be executed for a given syscall that originated in the user\
  \ space.\n\n## Service Descriptor Table\n\nIn WinDBG, we can check the Service Descriptor Table structure `KeServiceDescriptorTable`\
  \ as shown below. Note that the first member is recognized as `KiServiceTable` - this is a pointer to the SSDT itself -\
  \ the dispatch table \\(or simply an array\\) containing all those pointers/offsets:\n\n```erlang\n0: kd> dps nt!keservicedescriptortable\
  \ L4\nfffff801`9210b880  fffff801`9203b470 nt!KiServiceTable\nfffff801`9210b888  00000000`00000000\nfffff801`9210b890  00000000`000001ce\n\
  fffff801`9210b898  fffff801`9203bbac nt!KiArgumentTable\n```\n\nLet's try and print out a couple of values from the SSDT:\n\
  \n```erlang\n0: kd> dd /c1 KiServiceTable L2\nfffff801`9203b470  fd9007c4\nfffff801`9203b474  fcb485c0\n```\n\nAs mentioned\
  \ earlier, on x64 which is what I'm running in my lab, SSDT contains relative offsets to kernel routines. In order to get\
  \ the absolute address for a given offset, the following formula needs to be applied:\n\n$$\nRoutineAbsoluteAddress = KiServiceTableAddress\
  \ + (routineOffset >>> 4)\n$$\n\nUsing the above formula and the first offset `fd9007c4` we got from the `KiServiceTable`,\
  \ we can work out that this offset is pointing to `nt!NtAccessCheck`:\n\n```erlang\n0: kd> u KiServiceTable + (0xfd9007c4\
  \ >>> 4)\nnt!NtAccessCheck:\nfffff801`91dcb4ec 4c8bdc          mov     r11,rsp\nfffff801`91dcb4ef 4883ec68        sub  \
  \   rsp,68h\nfffff801`91dcb4f3 488b8424a8000000 mov     rax,qword ptr [rsp+0A8h]\nfffff801`91dcb4fb 4533d2          xor\
  \     r10d,r10d\n```\n\nWe can confirm it if we try to disassemble the `nt!NtAccessCheck` - routine addresses \\(fffff801\\\
  `91dcb4ec\\) and first instructions \\(mov r11, rsp\\) of the above and below commands match:\n\n```erlang\n0: kd> u nt!NtAccessCheck\
  \ L1\nnt!NtAccessCheck:\nfffff801`91dcb4ec 4c8bdc          mov     r11,rsp\n```\n\n![](../../.gitbook/assets/image%20%28481%29.png)\n\
  \nIf we refer back to the original drawing on how SSDT offsets are converted to absolute addresses, we can redraw it with\
  \ specific values for syscall 0x1:\n\n![](../../.gitbook/assets/image%20%2850%29.png)\n\n## Finding a Dispatch Routine for\
  \ a Given Userland Syscall\n\nAs a simple exercise, given a known syscall number, we can try to work out what kernel routine\
  \ will be called once that syscall is issued. Let's load the debugging symbols for `ntdll` module:\n\n```erlang\n.reload\
  \ /f ntdll.dll\nlm ntdll\n```\n\n![](../../.gitbook/assets/image%20%28501%29.png)\n\nLet's now find the syscall for `ntdll!NtCreateFile`:\
  \ \n\n```erlang\n0: kd> u ntdll!ntcreatefile L2\n```\n\n...we can see the syscall is 0x55:\n\n![](../../.gitbook/assets/image%20%28134%29.png)\n\
  \nOffsets in the `KiServiceTable` are 4 bytes in size, so we can work out the offset for syscall 0x55 by looking into the\
  \ value the `KiServiceTable` holds at position 0x55:\n\n```erlang\n0: kd> dd /c1 kiservicetable+4*0x55 L1\nfffff801`9203b5c4\
  \  01fa3007\n```\n\nWe see from the above that the offset for `NtCreateFile` is `01fa3007`. Using the formula discussed\
  \ previously for working out the absolute routine address, we confirm that we're looking at the `nt!tCreateFile` kernel\
  \ routine that will be called once `ntdll!NtCreateFile` issues the 0x55 syscall:\n\n```erlang\n0: kd> u kiservicetable +\
  \ (01fa3007>>>4) L1\nnt!NtCreateFile:\nfffff801`92235770 4881ec88000000  sub     rsp,88h\n```\n\nLet's redraw the earlier\
  \ diagram once more for the syscall 0x55 for `ntdll!NtCreateFile`:\n\n![](../../.gitbook/assets/image%20%2872%29.png)\n\n\
  ## Finding Address of All SSDT Routines\n\nAs another exercise, we could loop through all items in the service dispatch\
  \ table and print absolute addresses for all routines defined in the dispatch table:\n\n```erlang\n.foreach /ps 1 /pS 1\
  \ ( offset {dd /c 1 nt!KiServiceTable L poi(keservicedescriptortable+0x10) }){ dp kiservicetable + ( offset >>> 4 ) L1 }\n\
  ```\n\n![](../../.gitbook/assets/retrieving-ssdt-routine-addresses.gif)\n\nNice, but not very human readable. We can update\
  \ the loop a bit and print out the API names associated with those absolute addresses:\n\n```erlang\n0: kd> .foreach /ps\
  \ 1 /pS 1 ( offset {dd /c 1 nt!KiServiceTable L poi(nt!KeServiceDescriptorTable+10)}){ r $t0 = ( offset >>> 4) + nt!KiServiceTable;\
  \ .printf \"%p - %y\\n\", $t0, $t0 }\nfffff80191dcb4ec - nt!NtAccessCheck (fffff801`91dcb4ec)\nfffff80191cefccc - nt!NtWorkerFactoryWorkerReady\
  \ (fffff801`91cefccc)\nfffff8019218df1c - nt!NtAcceptConnectPort (fffff801`9218df1c)\nfffff801923f8848 - nt!NtMapUserPhysicalPagesScatter\
  \ (fffff801`923f8848)\nfffff801921afc10 - nt!NtWaitForSingleObject (fffff801`921afc10)\nfffff80191e54010 - nt!NtCallbackReturn\
  \ (fffff801`91e54010)\nfffff8019213cf60 - nt!NtReadFile (fffff801`9213cf60)\nfffff801921b2e80 - nt!NtDeviceIoControlFile\
  \ (fffff801`921b2e80)\nfffff80192212dc0 - nt!NtWriteFile (fffff801`92212dc0)\n.....cut for brewity.....\n```\n\n## References\n\
  \n{% embed url=\"https://www.codeproject.com/Articles/1191465/The-Quest-for-the-SSDTs\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/-printf\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/-foreach\" %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel/glimpse-into-ssdt-in-windows-x64-kernel.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/glimpse-into-ssdt-in-windows-x64-kernel.md
````
