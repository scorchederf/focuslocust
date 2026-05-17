---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Finding Kernel32 Base and Function Addresses in Shellcode

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-finding-kernel32-base-and-function-addresses-in-shellcode` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/finding-kernel32-base-and-function-addresses-in-shellcode.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Finding Kernel32 Base and Function Addresses in Shellcode](../../topics/offensive-security/finding-kernel32-base-and-function-addresses-in-shellcode.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-finding-kernel32-base-and-function-addresses-in-shellcode |
| name | Finding Kernel32 Base and Function Addresses in Shellcode |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/finding-kernel32-base-and-function-addresses-in-shellcode.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (100).png
- image (101).png
- image (102).png
- image (103).png
- image (104).png
- image (106).png
- image (29).png
- image (31).png
- image (32).png
- image (34).png
- image (35).png
- image (36).png
- image (37).png
- image (38).png
- image (39).png
- image (40).png
- image (42).png
- image (43).png
- image (44).png
- image (45).png
- image (46).png
- image (47).png
- image (48).png
- image (49).png
- image (50).png
- image (51).png
- image (53).png
- image (54).png
- image (55).png
- image (56).png
- image (58).png
- image (59).png
- image (60).png
- image (61).png
- image (64).png
- image (65).png
- image (66).png
- image (67).png
- image (68).png
- image (69).png
- image (70).png
- image (71).png
- image (72).png
- image (73).png
- image (74).png
- image (80).png
- image (81).png
- image (84).png
- image (86).png
- image (87).png
- image (93).png
- image (95).png
- image (96).png
- image (97).png
- image (98).png
- image (99).png
- winexec (1).gif
- winexec-pop.gif
_body: "# Finding Kernel32 Base and Function Addresses in Shellcode\n\nThe purpose of this lab is to understand how shellcode\
  \ finds kernel32 base address in memory of the process it's running in and then uses to find addresses of other functions\
  \ that it requires in order to achieve its goal.&#x20;\n\nIn this lab I will write some assembly to find the kernel32 dll's\
  \ base address, resolve `WinExec` function address in memory and call it to open `calc.exe`.\n\n## Finding Kernel32 Base\
  \ Address\n\nIt's well known that shellcode usually leverages the following chain of internal Windows OS memory structures\
  \ in order to resolve the kernel32 base address which I am going to walk through in WinDBG:\n\n```\nTEB->PEB->Ldr->InMemoryOrderLoadList->currentProgram->ntdll->kernel32.BaseDll\n\
  ```\n\nOne important thing to keep in mind is that kernel32.dll is always loaded into the same address for all the processes\
  \ - regardless if you open a calc.exe, notepad.exe, or any other Windows process. Below shows my program for this lab on\
  \ the left and another random program on the right - in both cases, the kernel32.dll (and ntdll...) got loaded into the\
  \ same memory address:\n\n![](<../../.gitbook/assets/image (29).png>)\n\nLet's get back to the:\n\n```\nTEB->PEB->Ldr->InMemoryOrderLoadList->currentProgram->ntdll->kernel32.BaseDll\n\
  ```\n\n...and go into these with more detail.\n\n### Structures\n\nThe first important OS structure of the chain is called\
  \ a Thread Environment Block (TEB) which contains information about the process's thread, including one member that is a\
  \ pointer to another very important structure called Process Environment Block (PEB, offset 0x30) where information about\
  \ the process itself (image path, commandline arguments, loaded modules and similar) is stored:\n\n```\ndt _teb\n```\n\n\
  ![](<../../.gitbook/assets/image (32).png>)\n\nInside the `PEB` structure, there is a member `Ldr` which points to a `PEB_LDR_DATA`\
  \ structure (offset 0x00c):\n\n```\ndt _peb\n```\n\n![](<../../.gitbook/assets/image (31).png>)\n\n`PEB_LDR_DATA` contains\
  \ a pointer to `InMemoryOrderModuleList` (offset 0x14) that contains information about the modules that were loaded in the\
  \ process:\n\n```\ndt _PEB_LDR_DATA\n```\n\n![](<../../.gitbook/assets/image (34).png>)\n\n`InMemoryOrderModuleList` points\
  \ to another structure we're interested in - `LDR_DATA_TABLE_ENTRY` even though WinDBG suggests the structure type is `LIST_ENTRY`.\
  \ As confusing as it may seem at first, this is actually right, since `InMemoryOrderModuleList` is a doubly linked list\
  \ where each list item points to an `LDR_DATA_TABLE_ENTRY` structure.&#x20;\n\nRemember, since the shellcode is looking\
  \ for the kernel32.dll base address, the `LDR_DATA_TABLE_ENTRY` is the last structure in the chain of structures it needs\
  \ to locate. Once the structure is located, the member `DllBase` at offset 0x18 stores the base address of the module:\n\
  \n```\ndt _LDR_DATA_TABLE_ENTRY\n```\n\n![](<../../.gitbook/assets/image (35).png>)\n\n### Initialized Structures\n\nLet's\
  \ now repeat the same exercise as above, but this time using real memory addresses so we can see how those memory structures\
  \ look like in a real process with real data. Let's check the `PEB` and note the `Ldr` pointer (77de0c40):\n\n```\n!peb\n\
  ```\n\n![](<../../.gitbook/assets/image (37).png>)\n\nWe can achieve the same result by overlaying the @$peb address over\
  \ the PEB structure:\n\n```\ndt _peb @$peb\n```\n\n![Ldr points to 0x77de0c40](<../../.gitbook/assets/image (36).png>)\n\
  \nFrom the above, we can see that the `PEB.Ldr` (`Ldr` member is at offset 0x00c) points to an `PEB_LDR_DATA` structure\
  \ at 0x77de0c40.&#x20;\n\nWe can view the `PEB_LDR_DATA` structure at 0x77de0c40 by overlaying it with address pointed to\
  \ by the PEB.Ldr (0xc) structure like so:\n\n```\ndt _PEB_LDR_DATA poi(@$peb+0xc)\n```\n\n![](<../../.gitbook/assets/image\
  \ (38).png>)\n\nRemember that `PEB.Ldr` was pointing to 0x77de0c40. We can double check that what we're doing so far is\
  \ correct by dereferrencing the pointer @$PEB+0xC which should be equal to 0x77de0c40, which we see it is:\n\n```\n? poi(@$peb+0xc)\n\
  dt _PEB_LDR_DATA 77de0c40\n```\n\n![](<../../.gitbook/assets/image (40).png>)\n\nProceeding on with the `InMemoryOrderModuleList`\
  \ pointing to `Peb.LDR.InMemoryOrderModuleList`, since we know it's at offset 0x14, we can get it like so:\n\n```\n? poi(poi(@$peb+0xc)+0x14)\n\
  ```\n\n![](<../../.gitbook/assets/image (39).png>)\n\n...which tells us that the first `LDR_DATA_TABLE_ENTRY` structure\
  \ is located at 0x00d231d8. If we try looking inside it, we can see that the `BaseDllName` indicates an error while reading\
  \ the memory:\n\n```\ndt _LDR_DATA_TABLE_ENTRY 0xd231d8\n```\n\n![](<../../.gitbook/assets/image (42).png>)\n\n{% hint style=\"\
  info\" %}\nThe reason for the above error is because although `InMemoryOrderModuleList` points to an `LDR_DATA_TABLE_ENTRY`,\
  \ we need to keep in mind that it's pointing 8 bytes into the structure itself since the structure is a doubly linked list.\
  \ See the above screenshot for reference - `InMemoryOrderLinks` is at offset 0x8 of the `LDR_DATA_TABLE_ENTRY`.\n{% endhint\
  \ %}\n\nWe now know that in order to read the `LDR_DATA_TABLE_ENTRY` structure correctly, we need to subtract 8 bytes from\
  \ the initial pointer 00d231d8:\n\n```\ndt _LDR_DATA_TABLE_ENTRY 0xd231d8-8\n```\n\n![No reading errors this time](<../../.gitbook/assets/image\
  \ (43).png>)\n\nNote how `InMemoryOrderLinks` now points to 0xd230d0 (which is an ntdll module as seen later) - which is\
  \ the second module loaded by this process. This means that we can easily walk through **all** the loaded modules, since\
  \ inspecting `LDR_DATA_TABLE_ENTRY` of one module will reveal the address of the structure for the next loaded module in\
  \ `InMemoryOrderLinks` member. To confirm this - if we inspect the 0xd230d0, `InMemoryOrderLinks` now points to yet another\
  \ structure for another module at 0xd235b8 (which as we will later see is the `LDR_DATA_TABLE_ENTRY` for the kernel32 module):\n\
  \n```\ndt _LDR_DATA_TABLE_ENTRY 0xd230d0-8\n```\n\n![](<../../.gitbook/assets/image (44).png>)\n\nLet's check the 0xd235b8\
  \ and note that we finally found the kernel32 base address which is 0x76670000:\n\n```\ndt _LDR_DATA_TABLE_ENTRY 0xd235b8-8\n\
  ```\n\n![](<../../.gitbook/assets/image (45).png>)\n\nTo summarize - if we wanted a one-liner to view the first `LDR_DATA_TABLE_ENTRY`,\
  \ we could view it like so:\n\n```\ndt _LDR_DATA_TABLE_ENTRY poi(poi(@$peb+0xc)+0x14)-8\n```\n\n![](<../../.gitbook/assets/image\
  \ (46).png>)\n\nGetting the pointer to `Ldr` and cross-checking it with !peb:\n\n```\n? poi(poi(@$peb+0xc)+0x14)\n!peb\n\
  ```\n\n![](<../../.gitbook/assets/image (47).png>)\n\nViewing the first and second `LIST_ENTRY` structures at 00d23d8 and\
  \ 00d230d0:\n\n```\ndt _list_entry 00d231d8\ndt _list_entry 0x00d230d0\n```\n\n![](<../../.gitbook/assets/image (48).png>)\n\
  \nThe second `LIST_ENTRY` at 00d230d0 points to 00d235b8 - which is the `LDR_DATA_TABLE_ENTRY` for kernel32 module (again\
  \ doing the same stuff we learned earlier in a different way):\n\n```\ndt _ldr_data_table_entry 0x00d235b8-8\n```\n\n![](<../../.gitbook/assets/image\
  \ (49).png>)\n\nBases address of the kernel32.dll as seen above is at 76670000. Note that we can read the value by reading\
  \ a double-word pointing at the start of `LDR_DATA_TABLE_ENTRY` minus the 8 bytes (reminder - because we're 8 bytes into\
  \ the structure) and adding 18 bytes since this is where the DLLBase member is located in the `LDR_DATA_TABLE_ENTRY`:\n\n\
  ```\ndd 0x00d235b8-8+18 L1\n// or dd 0x00d235b8+10 L1\n```\n\nNote that by doing the above, we still get the same DllBase\
  \ address - 76670000:\n\n![](<../../.gitbook/assets/image (50).png>)\n\n## Finding Kernel32 Address in Assembly\n\nLet's\
  \ try finding the kernel32 dll base address in the process memory using all the information learned above using assembly\
  \ - exactly as the shellcode would. You will notice that this is where all the offsets of various structures and members\
  \ come into play:\n\n```c\n.386 \n.model flat, stdcall \n.stack 4096\nassume fs:nothing\n\n.code \n\tmain proc\n\t\t\tmov\
  \ eax, [fs:30h]\t\t    ; Pointer to PEB (https://en.wikipedia.org/wiki/Win32_Thread_Information_Block)\n\t\t\tmov eax, [eax\
  \ + 0ch]\t\t; Pointer to Ldr\n\t\t\tmov eax, [eax + 14h]\t\t; Pointer to InMemoryOrderModuleList\n\t\t\tmov eax, [eax]\t\
  \t\t\t  ; this program's module\n\t\t\tmov eax, [eax]\t\t\t\t  ; ntdll module\n\t\t\tmov eax, [eax -8h + 18h]; kernel32.DllBase\n\
  \t\t\t\n\t\t\tmov ebx, 0\t\t\t\t      ; just so we can put a breakpoint on this\n\tmain endp\n\tend main\n```\n\nBelow shows\
  \ a compiled and executed assembly with a highlighted eax register that points to a  memory address 76670000, which indicates\
  \ that we got the base address of the kernel32 using assembly successfully:\n\n![](<../../.gitbook/assets/image (51).png>)\n\
  \n## Finding Function Address\n\nOnce we have the kernel32 base address, we can then loop through all the exported functions\
  \ of the module to find the function we're interested in (`WinExec`) - or in other words - the function we want to call\
  \ from the shellcode. This process requires a number of steps to be performed which are well known, so let's try and follow\
  \ them alongside with some visuals and a bit of PE parsing action.\n\nSee my previous lab about parsing PE files and some\
  \ terminology on what is Virtual Address (VA) and Relative Virtual Address (RVA) which is used extensively in this exercise:\
  \ &#x20;\n\n{% content-ref url=\"../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md\"\
  \ %}\n[pe-file-header-parser-in-c++.md](../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md)\n\
  {% endcontent-ref %}\n\n### Offsets in Tables\n\nBefore going into the visuals - the below table represents well known offsets\
  \ of the kernel32 image and what data they contain or point to that we will reference a lot:\n\n| Offset               \
  \         | Description                                                         |\n| ----------------------------- | -------------------------------------------------------------------\
  \ |\n| 0x3c into the file            | RVA of PE signature                                                 |\n| 0x78 bytes\
  \ after PE signature | RVA of Export Table                                                 |\n| 0x14 into the Export Table\
  \    | Number of functions exported by a module                            |\n| 0x1c into the Export Table    | RVA of Address\
  \ Table - addresses of exported functions              |\n| 0x20 into the Export Table    | RVA of Name Pointer Table -\
  \ addresses of exported function names    |\n| 0x24 into the Export Table    | RVA of Ordinal Table - function order number\
  \ as listed in the table |\n\n### Offsets in Visuals\n\nLet's look at the kernel32.dll file offsets mentioned in the above\
  \ table through a PE parser so we have an idea of what we're dealing with.\n\n### 0x3c into the File\n\n0x3c into the file\
  \ contains the RVA of the PE signature. In our case, the RVA for the PE signature is F8:\n\n![](<../../.gitbook/assets/image\
  \ (54).png>)\n\nSanity checking - F8 bytes into the file does indeed contain the PE signature 4550:\n\n![](<../../.gitbook/assets/image\
  \ (53).png>)\n\n### 0x78 after PE Signature\n\nF8 + 0x78 = 0x170 bytes into the file as mentioned earlier in the table,\
  \ points to a RVA of Export Table. In our case the RVA of Export Table is 972c0:\n\n![](<../../.gitbook/assets/image (55).png>)\n\
  \nExport Table starts at 972c0:\n\n![](<../../.gitbook/assets/image (104).png>)\n\n### 0x14 into the Export Table - Number\
  \ of Exported Functions\n\n0x972c0 + 0x14 = 0x972d4 RVA contains a value that signifies how many functions kernel32 module\
  \ exports - 0x643 in my case:\n\n![](<../../.gitbook/assets/image (56).png>)\n\n### 0x1c into the Export Table - Address\
  \ Of Exported Functions\n\n0x972c0 + 0x1c = 0x‭972DC‬ RVA contains an RVA to Exported functions Address Table which in my\
  \ case is 972e8:\n\n![](<../../.gitbook/assets/image (80).png>)\n\nIndeed at 972e8 we see an RVA for the first exported\
  \ function:\n\n![](<../../.gitbook/assets/image (81).png>)\n\n### 0x20 into the Export Table - Name Pointer Table\n\n0x972c0\
  \ + 0x20 = 0x972e0 RVA contains a pointer to an RVA to exported functions Name Pointer Table - 0x98bf4 in my case:&#x20;\n\
  \n![](<../../.gitbook/assets/image (58).png>)\n\nIf we check the Name Pointer Table at 0x98bf4, we can confirm we see RVAs\
  \ of exported function names:\n\n![](<../../.gitbook/assets/image (59).png>)\n\n### 0x24 into the Export Table - Functions'\
  \ Ordinal Table\n\n0x972c0 + 0x24 = 0x972e4 RVA points to an RVA of functions' Ordinal Table, which in my case is 9a500:\n\
  \n![](<../../.gitbook/assets/image (60).png>)\n\nAgain, confirming that ordinals are present at RVA 9a500:\n\n![](<../../.gitbook/assets/image\
  \ (61).png>)\n\n### Finding WinExec Position in the Name Pointer Table\n\nKnowing all of the above, let's try to find a\
  \ `WinExec` function address manually, so we know how to implement it in assembly.\n\nFirs of, we would need to loop through\
  \ the Name Pointer table, read the exported function's name and check if it is == `WinExec` and remembering how many iterations\
  \ it took for us to find the function.&#x20;\n\nIt would have taken 0x5ff iterations for me to find the WinExec (0x602 -\
  \ 0x3 = 0x5ff):\n\n![](<../../.gitbook/assets/image (64).png>)\n\nNote that:\n\n* we start counting indexes from 0\n* 0x3\
  \ was subtracted because the first function in the Name Pointer Table started from 4 as seen below:\n\n![](<../../.gitbook/assets/image\
  \ (65).png>)\n\n### Finding WinExec Ordinal Number\n\nIn the Ordinal Table (starting at 0x9a500), we can find the WinExec\
  \ Ordinal RVA with a simple formula. Note that the reason for multiplying the `WinExec` location (0x5ff) by two is because\
  \ each ordinal is 2 bytes in size:\n\n$$\nOrdinalRVA = 0x9a500 + 0x5ff * 2 = 0x9B0FE\n$$\n\n![](<../../.gitbook/assets/image\
  \ (66).png>)\n\nNow from the `WinExec` Ordinal RVA location (9B0FE) we can read 2 bytes and get the actual `WinExec` Ordinal\
  \ which is 0x0600:\n\n![](<../../.gitbook/assets/image (67).png>)\n\n### Finding WinExec RVA in the Export Address Table\n\
  \nTo get the RVA of the WinExec function from the Export Address Table, we use a simple formula:\n\n$$\nWinExecRVA = ExportAddressTableRVA\
  \ + (Ordinal * 4)\n$$\n\nwhich translates to:\n\n$$\nWinExecRVA = 0x972e8 + (0x600 * 4) = 0x98AE8‬\n$$\n\n![](<../../.gitbook/assets/image\
  \ (68).png>)\n\nFrom the above screenshot, we know that the RVA of WinExec is 0x5d220. Let's check this in WinDBG by first\
  \ getting getting the kernel32 base address which is 75690000:\n\n![](<../../.gitbook/assets/image (69).png>)\n\nIf we add\
  \ the `WinExec` RVA 0x5d220 to the kernel32 base address 0x75690000, we should land on the WinExec function, so let's try\
  \ to disassemble that address and also disassemble the kernel32!WinExec symbol to confirm that the assembly instructions\
  \ match:\n\n```\n//disassemble kernel32 base address + WinExec RVA\nu 75690000+5d220\n\n//disassemble kernel32!WinExec routine\n\
  u kernel32!WinExec\n```\n\nFrom the below, we can see that the disassembly matches confirming our calculations of `WinExec`\
  \ RVA are correct:\n\n![](<../../.gitbook/assets/image (70).png>)\n\n## Rinse and Repeat In Assembly\n\nWe are now ready\
  \ to start implementing this in assembly.\n\n### 0x3c into the Image\n\nAs per the visuals earlier that showed that 0x3c\
  \ into the file is a PE signature, which contains a value F8:\n\n![](<../../.gitbook/assets/image (53).png>)\n\nLines 1-13\
  \ are the same as seen earlier -  they find the kernel32 dll base address. In line 15 we move kernel32 base address to ebx\
  \ holding our kernel32 base address. Then we shift that address by 3c bytes, read its contents and move it to eax. After\
  \ this operation, the eax should hold the value F8, which we see it does:\n\n![](<../../.gitbook/assets/image (71).png>)\n\
  \nNow, we can find the address of PE signature by adding kernel32 base address and the PE signature RVA F8: 75690000 + F8\
  \ = 756900F8 and we find the PE signature there:\n\n![](<../../.gitbook/assets/image (72).png>)\n\n### 0x78 after PE Signature\n\
  \nIn line 20, we get an RVA of the Export Table by moving the eax register that contains an address of the PE signature\
  \ by 78 bytes where we find an RVA of the Export Table which is stored in eax = 972C0:\n\n![](<../../.gitbook/assets/image\
  \ (73).png>)\n\nTo find the address of the Export Table, we add kernel32 base address 75690000 and Export Table RVA 972C0\
  \ which results in the address 757272C0:\n\n![](<../../.gitbook/assets/image (74).png>)\n\n### &#x20;0x14 into the Export\
  \ Table - Number of Exported Functions\n\nTo check if our calculations in assembly are correct at this point, we can add\
  \ the Export Table address and 0x14 (offset into the Export Table showing how many functions kernel32 module exports) and\
  \ if we cross-reference the value found there with the results we got via the visual PE parsing approach, we should have\
  \ 0x643 exported functions:\n\n![](<../../.gitbook/assets/image (56).png>)\n\nLet's add Export Table address 757272C0 and\
  \ the offset 0x14, which equals to 0x757272D4. If we check that memory address, we see that indeed we have 0x643 value in\
  \ there:\n\n![](<../../.gitbook/assets/image (84).png>)\n\n### 0x1c into the Export Table - Address Of Exported Functions\n\
  \nAt offset 1c into the Export Table 757272C0, we find an RVA of Exported Functions Address table, which in my case is 000972E8:\n\
  \n![](<../../.gitbook/assets/image (86).png>)\n\nTo verify the calculation is correct - we can inspect the memory at address\
  \ kernel32 base 75690000 + 0x972e8 = 0x757272E8 where we should see an RVA of the first exported function address which\
  \ is 20400h as seen in the above screenshot.\n\nUpon memory inspection at 0x757272E8, we see that indeed the value at that\
  \ memory location is 20400h:\n\n![](<../../.gitbook/assets/image (87).png>)\n\n### 0x20 into the Export Table - Name Pointer\
  \ Table\n\nSame way, we can double check if 757272C0 (address of Export Table) + 0x20 bytes contains an RVA of the exported\
  \ function names table which is 00098BF4:\n\n![](<../../.gitbook/assets/image (99).png>)\n\nLet's get its address now by\
  \ adding the Name Pointer Table RVA 00098BF4 and kernel32 base address 75690000, which results in 75728BF4 where we can\
  \ see the name of an RVA of the first exported function:\n\n![](<../../.gitbook/assets/image (100).png>)\n\nIf we follow\
  \ that address 75690000 + 0x9b1f2, we find the first function name:\n\n![](<../../.gitbook/assets/image (106).png>)\n\n\
  ### 0x24 into the Export Table - Functions' Ordinal Table\n\n757272C0 (address of Export Table) + 0x24 bytes contains an\
  \ RVA of the exported function Ordinals Table which is 0009A500:\n\n![](<../../.gitbook/assets/image (101).png>)\n\nGetting\
  \ the ordinal table address by adding kernel32 base 75690000 + the RVA of ordinal table at 0009A500 we arrive at 0x7572A500.\
  \ Inspecting it, we indeed see that we're looking at the function Ordinal Table:\n\n![](<../../.gitbook/assets/image (102).png>)\n\
  \n### Finding WinExec Position in the Name Pointer Table\n\n#### Pushing WinExec onto the Stack\n\nNow, in order to find\
  \ the `WinExec` position, before we proceed with looping and comparing each function name in the Name Pointer table with\
  \ the string `WinExec`, we actually need to push the string `WinExec` to memory first.\n\nWe need to store it as a sequence\
  \ of reversed bytes (indiannes). `WinExec` in hex is `57696e45 786563`. Let's push it to the stack in two pushes. First\
  \ let's push the bytes `45 6e 69 57` - which pushes the `WinE` onto the stack:\n\n![](<../../.gitbook/assets/image (93).png>)\n\
  \nLet's now push the remaining bytes. Remember that we need a null byte at the end to terminate the string. Also, remember\
  \ that data needs to be pushed onto the stack in reverse order:\n\n![](<../../.gitbook/assets/winexec (1).gif>)\n\n####\
  \ Finding WinExec Location in Name Pointer Table\n\nAfter looping through the exported function Names Table and comparing\
  \ each function name in there with `WinExec`, once `WinExec` is found, the loop breaks and the eax contains the number of\
  \ iterations it took to find the `WinExec`. In this case it's 0x5ff - exactly the same number as previously seen when [doing\
  \ this exercise manually](finding-kernel32-base-and-function-addresses-in-shellcode.md#finding-winexec-position-in-the-name-pointer-table):&#x20;\n\
  \n![](<../../.gitbook/assets/image (95).png>)\n\n### Finding WinExec Ordinal Number\n\nAdding Ordinal Table Address 0x7572A500\
  \ and `WinExec` location 0x5FF multiplied by 2 (an ordinal is 2 bytes in size), results in `WinExec` ordinal 0x600:\n\n\
  ![](<../../.gitbook/assets/image (96).png>)\n\n### Finding WinExec RVA in the Export Address Table\n\nGet the `WinExec`\
  \ RVA from the Export Address Table by multiplying location of the `WinExec` 0x5ff by 4 (address is of 4 bytes in size for\
  \ 32 bit binaries) and adding it to the Export Address Table at 0x757272E8, which results in 0x757272E8 + 5ff\\*4 = 0x75728AE8\
  \ which contains `WinExec` RVA value - 5d220:\n\n![](<../../.gitbook/assets/image (97).png>)\n\n### Finding WinExec Virtual\
  \ Address\n\nWe can now resolve the `WinExec` function address' location in the kernel32 dll module by adding the `WinExec`\
  \ RVA 5d220 and kernel32 base address 75690000, which equals to 756ED220:&#x20;\n\n![](<../../.gitbook/assets/image (98).png>)\n\
  \n## Calling WinExec\n\nSince we now have the address of the `WinExec` function, we can invoke it. Firstly, we need to push\
  \ the 2 arguments that will be consumed by the WinExec:\n\n```cpp\nUINT WinExec(\n  LPCSTR lpCmdLine,\n  UINT   uCmdShow\n\
  );\n```\n\nWe push a null terminated `calc` string and the value `10` that corresponds to a constant `SW_SHOWDEFAULT` and\
  \ then invoke the function by calling its address with the keyword `call`:\n\n![](<../../.gitbook/assets/image (103).png>)\n\
  \nBelow shows our assembly in a debugger. The calculator pops after `call eax` instruction is executed:\n\n![](../../.gitbook/assets/winexec-pop.gif)\n\
  \n{% hint style=\"info\" %}\nWe used `WinExec` function in this lab, but shellcode can and usually does use this technique\
  \ to resolve addresses for `GetProcAddress` and `LoadLibrary` functions to make resolving other required functions easier.\n\
  {% endhint %}\n\n## Code\n\n```c\n.386 \n.model flat, stdcall \n.stack 4096\nassume fs:nothing\n\n.code \n\tmain proc\n\t\
  \t; form new stack frame\n\t\tpush ebp\n\t\tmov ebp, esp\n\n\t\t; allocate local variables and initialize them to 0\n\t\t\
  sub esp, 1ch\n\t\txor eax, eax\n\t\tmov [ebp - 04h], eax\t\t\t; will store number of exported functions\n\t\tmov [ebp -\
  \ 08h], eax\t\t\t; will store address of exported functions addresses table\n\t\tmov [ebp - 0ch], eax\t\t\t; will store\
  \ address of exported functions name table\n\t\tmov [ebp - 10h], eax\t\t\t; will store address of exported functions ordinal\
  \ table\n\t\tmov [ebp - 14h], eax\t\t\t; will store a null terminated byte string WinExec\n\t\tmov [ebp - 18h], eax\t\t\t\
  ; will store address to WinExec function\n\t\tmov [ebp - 1ch], eax\t\t\t; reserved\n\n\t\t; push WinExec to stack and save\
  \ it to a local variable\n\t\tpush 00636578h\t\t\t\t    ; pushing null,c,e,x\n\t\tpush 456e6957h\t\t\t\t    ; pushing E,n,i,W\n\
  \t\tmov [ebp - 14h], esp\t\t\t; store pointer to WinExec\n\n\t\t; get kernel32 base address\n\t\tmov eax, [fs:30h]\t\t \
  \   \t; Pointer to PEB (https://en.wikipedia.org/wiki/Win32_Thread_Information_Block)\n\t\tmov eax, [eax + 0ch]\t\t\t; Pointer\
  \ to Ldr\n\t\tmov eax, [eax + 14h]\t\t\t; Pointer to InMemoryOrderModuleList\n\t\tmov eax, [eax]\t\t\t\t  \t; this program's\
  \ module\n\t\tmov eax, [eax]  \t\t\t\t\t; ntdll module\n\t\tmov eax, [eax -8h + 18h]\t; kernel32.DllBase\n\n\t\t; kernel32\
  \ base address\n\t\tmov ebx, eax\t\t\t\t\t\t\t; store kernel32.dll base address in ebx\n\n\t\t; get address of PE signature\n\
  \t\tmov eax, [ebx + 3ch]\t\t\t; 0x3c into the image - RVA of PE signature\n\t\tadd eax, ebx\t\t\t\t    \t; address of PE\
  \ signature: eax = eax + kernel32 base -> eax = 0xf8 + kernel32 base\n\n\t\t; get address of Export Table\n\t\tmov eax,\
  \ [eax + 78h]\t\t\t; 0x78 bytes after the PE signature is an RVA of Export Table\n\t\tadd eax, ebx\t\t\t\t\t    ; address\
  \ of Export Table = Export Table RVA + kernel32 base\n  \n\t\t; get number of exported functions\n\t\tmov ecx, [eax + 14h]\t\
  \t\n\t\tmov [ebp - 4h], ecx\t\t\t\t; store number of exported functions\n\n\t\t; get address of exported functions table\n\
  \t\tmov ecx, [eax + 1ch]\t\t\t; get RVA of exported functions table\n\t\tadd ecx, ebx\t\t\t\t    \t; get address of exported\
  \ functions table\n\t\tmov [ebp - 8h], ecx\t\t\t\t; store address of exported functions table\n\n\t\t; get address of name\
  \ pointer table\n\t\tmov ecx, [eax + 20h]\t\t\t; get RVA of Name Pointer Table\n\t\tadd ecx, ebx\t\t\t\t\t    ; get address\
  \ of Name Pointer Table\n\t\tmov [ebp - 0ch], ecx\t\t\t; store address of Name Pointer Table\n\n\t\t; get address of functions\
  \ ordinal table\n\t\tmov ecx, [eax + 24h]\t\t\t; get RVA of functions ordinal table\n\t\tadd ecx, ebx\t\t\t\t\t    ; get\
  \ address of functions ordinal table\n\t\tmov [ebp - 10h], ecx\t\t\t; store address of functions ordinal table\n\t\n\t\t\
  ; loop through exported function name pointer table and find position of WinExec\n\t\txor eax, eax\n\t\txor ecx, ecx\n\t\
  \t\t\n\t\tfindWinExecPosition:\n\t\t\tmov esi, [ebp - 14h]\t\t; esi = pointer to WinExec\n\t\t\tmov edi, [ebp - 0ch]\t\t\
  ; edi = pointer to exported function names table\n\t\t\tcld\t\t\t\t\t\t\t\t\t\t\t; https://en.wikipedia.org/wiki/Direction_flag\n\
  \t\t\tmov edi, [edi + eax*4]\t; get RVA of the next function name in the exported function names table\n\t\t\tadd edi, ebx\t\
  \t\t\t    ; get address of the next function name in the exported function names table\n\n\t\t\tmov cx, 8\t\t\t\t\t    \
  \  ; tell the next-comparison instruction to compare first 8 bytes\n\t\t\trepe cmpsb\t\t\t\t\t    ; check if esi == edi\n\
  \t\t\t\t\n\t\t\tjz WinExecFound\n\t\t\tinc eax\t\t\t\t\t\t\t\t\t; increase the counter\n\t\t\tcmp eax, [ebp - 4h]\t\t\t\
  ; check if we have looped over all the exported function names\n\t\t\tjne findWinExecPosition\t\n\t\t\t\t\n\t\tWinExecFound:\t\
  \t\n\t\t\tmov ecx, [ebp - 10h]\t\t; ecx = ordinal table\n\t\t\tmov edx, [ebp - 8h]\t\t\t; edx = export address table\n\n\
  \t\t\t; get address of WinExec ordinal\n\t\t\tmov ax, [ecx + eax * 2]\t; get WinExec ordinal\n\t\t\tmov eax, [edx + eax\
  \ * 4]; get RVA of WinExec function\n\t\t\tadd eax, ebx\t\t\t\t    ; get VA of WinExec\n\n\t\t\tjmp InvokeWinExec\n\n\t\t\
  InvokeWinExec:\n\t\t  xor edx, edx\t\t\t\t  \t; null byte\n\t\t\tpush edx\t\t\t\t\t\n\t\t\tpush 636c6163h\t\t\t\t  ; push\
  \ calc on the stack\n\t\t\tmov ecx, esp\t\t\t    \t; ecx = calc\n\t\n\t\t\tpush 10  \t\t\t\t\t      ; uCmdSHow = SW_SHOWDEFAULT\n\
  \t\t\tpush ecx\t\t\t\t\t\t\t\t; lpCmdLine = calc\n\t\t\tcall eax \t\t\t\t\t\t\t\t; call WinExec\n\t\t\t\n\t\t; clear stack\n\
  \t\tadd esp, 1ch\t\t\t\t\t\t\t; local variables\t\t\t\t\n\t\tadd esp, 0ch\t\t\t\t\t\t\t; pushes for ebp and WinExec\n\t\t\
  add esp, 4h\t\t\t\t\t\t\t\t; pushes for WinExec invokation\n\t\tpop ebp\n\t\tret\n\tmain endp\n\tend main\n```\n\n## References\n\
  \n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb_ldr_data\" %}\n\n{% embed url=\"\
  https://0xevilc0de.com/locating-dll-name-from-the-process-environment-block-peb/\" %}\n\n{% embed url=\"https://en.wikipedia.org/wiki/Win32_Thread_Information_Block\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-winexec\" %}\n\n{% embed url=\"\
  https://en.wikibooks.org/wiki/X86_Disassembly/Functions_and_Stack_Frames\" %}\n\n{% embed url=\"https://idafchev.github.io/exploit/2017/09/26/writing_windows_shellcode.html\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/finding-kernel32-base-and-function-addresses-in-shellcode.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/finding-kernel32-base-and-function-addresses-in-shellcode.md
````
