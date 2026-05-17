---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Listing Open Handles and Finding Kernel Object Addresses

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-get-all-open-handles-and-kernel-object-address-from-userland` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/get-all-open-handles-and-kernel-object-address-from-userland.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Listing Open Handles and Finding Kernel Object Addresses](../../topics/miscellaneous-reversing-forensics/listing-open-handles-and-finding-kernel-object-addresses.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-get-all-open-handles-and-kernel-object-address-from-userland |
| name | Listing Open Handles and Finding Kernel Object Addresses |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/get-all-open-handles-and-kernel-object-address-from-userland.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (600).png
- image (601).png
- image (602).png
- image (603).png
- image (605).png
_body: "# Listing Open Handles and Finding Kernel Object Addresses\n\nIt's possible to enumerate all open handles (processes,\
  \ files, mutexes, keys, sections, etc) on a system (no admin rights required), which means it is possible to get a virtual\
  \ address of any kernel object (for example `EPROCESS` for a process object) in the kernel space from user space.\n\nBeing\
  \ able to locate a virtual address of a kernel object (like `EPROCESS`) is useful in kernel exploitation. For example, if\
  \ you compromise a machine and discover there is a vulnerable driver, through which you  can read/write kernel memory from\
  \ userland, you could exploit it for privilege escalation by locating a kernel object `EPROCESS` of a privileged process,\
  \ for example `winlogon.exe`, stealing its security token and applying it to your low privileged `cmd.exe` process to gain\
  \ a shell with `SYSTEM` privileges.\n\nA list of all the open handles on the system is retrieved by using a `NtQuerySystemInformation`\
  \ API and a couple of undocumented, but well known structures `SYSTEM_HANDLE_INFORMATION` and `SYSTEM_HANDLE_TABLE_ENTRY_INFO`.\n\
  \n## Code\n\nBelow code retrieves all handles opened by the `SYSTEM` process (PID 4):\n\n{% hint style=\"danger\" %}\n*\
  \ Below code does not handle errors\n* `SystemHandleInformationSize` is a hardcoded value, which you should not do in production\
  \ code. Instead, you should:\n  * start with an arbitrary size for `SystemHandleInformationSize`\n  * call `NtQuerySystemInformation`\
  \ in a loop, until it no longer returns `0xc0000004` (`STATUS_INFO_LENGTH_MISMATCH`)\n  * if `0xc0000004` is returned, increase\
  \ `SystemHandleInformationSize`\n{% endhint %}\n\n```cpp\n#include <iostream>\n#include <Windows.h>\n#include <winternl.h>\n\
  \n#define SystemHandleInformation 0x10\n#define SystemHandleInformationSize 1024 * 1024 * 2\n\nusing fNtQuerySystemInformation\
  \ = NTSTATUS(WINAPI*)(\n    ULONG SystemInformationClass,\n    PVOID SystemInformation,\n    ULONG SystemInformationLength,\n\
  \    PULONG ReturnLength\n);\n\n// handle information\ntypedef struct _SYSTEM_HANDLE_TABLE_ENTRY_INFO\n{\n    USHORT UniqueProcessId;\n\
  \    USHORT CreatorBackTraceIndex;\n    UCHAR ObjectTypeIndex;\n    UCHAR HandleAttributes;\n    USHORT HandleValue;\n \
  \   PVOID Object;\n    ULONG GrantedAccess;\n} SYSTEM_HANDLE_TABLE_ENTRY_INFO, *PSYSTEM_HANDLE_TABLE_ENTRY_INFO;\n\n// handle\
  \ table information\ntypedef struct _SYSTEM_HANDLE_INFORMATION\n{\n    ULONG NumberOfHandles;\n    SYSTEM_HANDLE_TABLE_ENTRY_INFO\
  \ Handles[1];\n} SYSTEM_HANDLE_INFORMATION, *PSYSTEM_HANDLE_INFORMATION;\n\n\nint main()\n{\n    ULONG returnLenght = 0;\n\
  \    fNtQuerySystemInformation NtQuerySystemInformation = (fNtQuerySystemInformation)GetProcAddress(GetModuleHandle(L\"\
  ntdll\"), \"NtQuerySystemInformation\");\n    PSYSTEM_HANDLE_INFORMATION handleTableInformation = (PSYSTEM_HANDLE_INFORMATION)HeapAlloc(GetProcessHeap(),\
  \ HEAP_ZERO_MEMORY, SystemHandleInformationSize);\n    NtQuerySystemInformation(SystemHandleInformation, handleTableInformation,\
  \ SystemHandleInformationSize, &returnLenght);\n\n    for (int i = 0; i < handleTableInformation->NumberOfHandles; i++)\n\
  \    {\n        SYSTEM_HANDLE_TABLE_ENTRY_INFO handleInfo = (SYSTEM_HANDLE_TABLE_ENTRY_INFO)handleTableInformation->Handles[i];\n\
  \n        if (handleInfo.UniqueProcessId == 4)\n        {\n            printf_s(\"Handle 0x%x at 0x%p, PID: %x\\n\", handleInfo.HandleValue,\
  \ handleInfo.Object, handleInfo.UniqueProcessId);\n        }\n        else \n        {\n            break;\n        }\n\
  \    }\n\n    return 0;\n}\n```\n\n{% hint style=\"info\" %}\n**Remember**\\\nThe above code could be easily modified to\
  \ find an object's location in kernel given its handle.\n{% endhint %}\n\n## Validation\n\nLet's see if the code above lists\
  \ out the handles and the object addresses those handles point to in the kernel memory correctly.\n\nIf we compile and run\
  \ the code, we will get a list of all the handles for the process with PID 4:\n\n![](<../../.gitbook/assets/image (600).png>)\n\
  \nWe can cross-check and ensure that our listed handles are accurate with Process Hacker by inspecting the `Handles` tab\
  \ of the `SYSTEM` process (PID 4). Let's check the first handle 0x4:\n\n![](<../../.gitbook/assets/image (601).png>)\n\n\
  The above shows:\n\n* in green - handle id (0x4)\n* in blue - process id (4) of the process which has the handle 0x4 opened\
  \ (SYSTEM process has a handle to itself)\n* in red - object's (pointed to by the handle) location in kernel memory (`0xffff87077c882300`)\n\
  \nWe can easily check the object at `0xffff8f077c882300` in WinDBG:\n\n```\n!object 0xffff8f077c882300\n```\n\nThe above\
  \ command indicates that `0xffff8f077c882300` is a valid object address and it's of type Process:\n\n![Output of !object\
  \ 0xffff8f077c882300](<../../.gitbook/assets/image (602).png>)\n\nWe can confirm `0xffff8f077c882300` is a process object\
  \ by using a `!process` command in WinDBG:\n\n```\n!process 0xffff8f077c882300 0\n```\n\nBelow confirms that it's indeed\
  \ a process object:\n\n* in red - process object location in kernel memory (0xffff8f077c882300)\n* in blue - process id\
  \ (4)\n* in lime - process name (system)\n\n![Output of !process 0xffff8f077c882300 0](<../../.gitbook/assets/image (603).png>)\n\
  \nFinally, we can overlay the `_EPROCESS` over `ffff8f077c882300` and print the `UniqueProcessId` and `ImageFileNames`,\
  \ that again confirm it's a `SYSTEM` process with PID 4:\n\n```\ndt _eprocess ffff8f077c882300 uniqueprocessid imagefilename\n\
  ```\n\n![](<../../.gitbook/assets/image (605).png>)\n\n## References\n\n{% embed url=\"https://processhacker.sourceforge.io/doc/struct___s_y_s_t_e_m___h_a_n_d_l_e___i_n_f_o_r_m_a_t_i_o_n.html\"\
  \ %}\n\n{% embed url=\"https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/ex/sysinfo/handle.htm\" %}\n\n{% embed\
  \ url=\"https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/ex/sysinfo/handle_table_entry.htm?ts=0,81\" %}\n\n\
  {% embed url=\"https://blez.wordpress.com/2012/09/17/enumerating-opened-handles-from-a-process/\" %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/get-all-open-handles-and-kernel-object-address-from-userland.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/get-all-open-handles-and-kernel-object-address-from-userland.md
````
