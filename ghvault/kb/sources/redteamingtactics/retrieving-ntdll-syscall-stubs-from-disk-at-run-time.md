---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Retrieving ntdll Syscall Stubs from Disk at Run-time

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-retrieving-ntdll-syscall-stubs-at-run-time` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/retrieving-ntdll-syscall-stubs-at-run-time.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Retrieving ntdll Syscall Stubs from Disk at Run-time](../../topics/offensive-security/retrieving-ntdll-syscall-stubs-from-disk-at-run-time.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-retrieving-ntdll-syscall-stubs-at-run-time |
| name | Retrieving ntdll Syscall Stubs from Disk at Run-time |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/retrieving-ntdll-syscall-stubs-at-run-time.md |

## Preserved Source Material

````yaml
_asset_filenames:
- calling-syscall-stub.gif
- image (552).png
- image (553).png
- image (555).png
- resolving-function-names.gif
- syscall-stub-found.gif
_body: "# Retrieving ntdll Syscall Stubs from Disk at Run-time\n\n## Overview\n\nThe purpose of this lab was to play with\
  \ syscalls once more. More specifically, the goal was to be able to retrieve ntdll syscall stubs from the disk during run-time\
  \ (before AVs/EDRs get a chance to hook them), rather than hardcoding them, since they may change between different Windows\
  \ versions.\n\nThis lab was sparked by [am0nsec](https://twitter.com/am0nsec)'s and [RtlMateusz](https://twitter.com/RtlMateusz)'s\\\
  \n[https://github.com/am0nsec/HellsGate](https://github.com/am0nsec/HellsGate) although is very different in implementation\
  \ and execution.\n\nSee my previous post on syscalls too:\n\n{% content-ref url=\"using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md\"\
  \ %}\n[using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md](using-syscalls-directly-from-visual-studio-to-bypass-avs-edrs.md)\n\
  {% endcontent-ref %}\n\nI will write some crude code that will do the following:\n\n1. Read ntdll.dll file bytes from the\
  \ disk (before any AV/EDR has a chance to hook its functions) and write them to some memory location `m1`\n2. Parse out\
  \ `.rdata` and  `.text` sections of the ntdll.dll file\n   1. `.rdata` contains ntdll exported function names\n   2. `.text`\
  \ contains code that gets executed by those functions\n3. Locate the specified function's code (syscall) in the memory location\
  \ `m1`. In this lab I will find the location where the stub code for `NtCreateFile` resides\n4. Extract the stub (23 bytes)\
  \ of the `NtCreateFile` and write it to some memory location `m2`\n5. Declare a function prototype for `NtCreateFile`\n\
  6. Define a variable `v1` of function type `NtCreateFile` and point it to the memory location `m2`, where the syscall stub\
  \ for `NtCreateFile` is written, as mentioned in step 4.\n7. Invoke the `NtCreateFile` syscall by calling the syscall `v1`,\
  \ which actually points to `m2`, where `NtCreateFile` syscall stub is stored\n8. `NtCreate` syscall gets executed - profit\n\
  \n{% hint style=\"info\" %}\nNote, that the above process is just one way of achieving the same goal.\n{% endhint %}\n\n\
  ## Reminder\n\nAs a reminder, we can easily see the syscall IDs for NT functions via WinDBG or any other debugger.&#x20;\n\
  \nThe syscall ID is 2 bytes in length and starts 4 bytes into the function, so for example, the syscall ID for `NtCreateFile`\
  \ is `0x0055`, `NtQueryEvent` is `0x0056`, etc - see below image.&#x20;\n\nAlso - in green are the bytes, that I refer to\
  \ as syscall stub for`NtCreateFile` and these are the bytes that we want to be able to retrieve at run-time for any given\
  \ NT function, and hence this lab.\n\n![orange - syscall function name and its id, green - syscall stub](<../../.gitbook/assets/image\
  \ (552).png>)\n\n## Extracting the Syscall Stub\n\nI wrote a function `GetSyscallStub`, that is responsible for steps 3\
  \ and 4  of the processes that I outlined in the `Overview` section.\n\nIt allows me to find any given function's code location\
  \ inside the ntdll.dll and carve out its syscall stub (the first 23 bytes):\n\n![](<../../.gitbook/assets/image (553).png>)\n\
  \nSo, for example, if I wanted to retrieve the syscall stub for `NtCreateFile`, I would call `GetSyscallStub` like so:\n\
  \n```cpp\nGetSyscallStub(\n    // function name for which the syscall stub is to be retrieved\n    \"NtCreateFile\",\n \
  \   // ntdll export directory \n    exportDirectory, \n    // ntdll file bytes\n    fileData, \n    // ntdll .text section\
  \ descriptor - contains code of ntdll exported functions. Required for locating NtCreateFile syscall stub\n    textSection,\
  \ \n    // ntdll .rdata section descriptor - contains name of ntdll exported functions.\n    rdataSection, \n    // NtCreateFile\
  \ stub will be written here\n    syscallStub\n);\n```\n\nOnce `GetSyscallStub`is called, it will cycle through all the ntdll\
  \ exported function names (they are resolved to `functionNameResolved`) as well as exported function addresses simulatenously,\
  \ and look for the function we want to extract the syscall stub for, which in our case is the `NtCreateFile` (passed to\
  \ GetSycallStub via `functionName`):\n\n![](../../.gitbook/assets/resolving-function-names.gif)\n\nOnce the needed function\
  \ name is resolved, the given function's syscall stub is extracted and stored in the `syscallStub` variable.&#x20;\n\nIn\
  \ the below GIF, we can see the instruction `mov eax, 0x55` when viewing the `syscallStub` variable in a disassembly view.\
  \ Since we know that the `NtCreateFile` syscall ID is `0x0055`, this suggests we have extracted the syscall stub successfully:\n\
  \n![](../../.gitbook/assets/syscall-stub-found.gif)\n\n## Calling Syscall Stub\n\nIn order to be able to invoke the syscall,\
  \ we need to define a variable `NtCreateFile` of type `myNtCreateFile` (see code section for the function prototype), point\
  \ it to the `syscallStub` and make `syscallStub` executable:\n\n![](<../../.gitbook/assets/image (555).png>)\n\nWe can now\
  \ call `NtCreateFile`:\n\n```cpp\nNtCreateFile(\n\t&fileHandle, \n\tFILE_GENERIC_WRITE, \n    &oa, \n    &osb, \n    0,\
  \ \n    FILE_ATTRIBUTE_NORMAL, \n    FILE_SHARE_WRITE, \n    FILE_OVERWRITE_IF, \n    FILE_SYNCHRONOUS_IO_NONALERT, \n \
  \   NULL,\n    0\n);\n```\n\nBelow shows how `NtCreateFile` gets called on a file c:\\temp\\pw.log and a handle to that\
  \ file is opened, which confirms that `NtCreateFile` syscall stub was retrieved and called successfully:\n\n![](../../.gitbook/assets/calling-syscall-stub.gif)\n\
  \n## Code\n\n```cpp\n#include <iostream>\n#include \"Windows.h\"\n#include \"winternl.h\"\n#pragma comment(lib, \"ntdll\"\
  )\n\nint const SYSCALL_STUB_SIZE = 23;\nusing myNtCreateFile = NTSTATUS(NTAPI*)(PHANDLE FileHandle, ACCESS_MASK DesiredAccess,\
  \ POBJECT_ATTRIBUTES ObjectAttributes, PIO_STATUS_BLOCK IoStatusBlock, PLARGE_INTEGER AllocationSize, ULONG FileAttributes,\
  \ ULONG ShareAccess, ULONG CreateDisposition, ULONG CreateOptions, PVOID EaBuffer, ULONG EaLength);\n\nPVOID RVAtoRawOffset(DWORD_PTR\
  \ RVA, PIMAGE_SECTION_HEADER section)\n{\n\treturn (PVOID)(RVA - section->VirtualAddress + section->PointerToRawData);\n\
  }\n\nBOOL GetSyscallStub(LPCSTR functionName, PIMAGE_EXPORT_DIRECTORY exportDirectory, LPVOID fileData, PIMAGE_SECTION_HEADER\
  \ textSection, PIMAGE_SECTION_HEADER rdataSection, LPVOID syscallStub)\n{\n\tPDWORD addressOfNames = (PDWORD)RVAtoRawOffset((DWORD_PTR)fileData\
  \ + *(&exportDirectory->AddressOfNames), rdataSection);\n\tPDWORD addressOfFunctions = (PDWORD)RVAtoRawOffset((DWORD_PTR)fileData\
  \ + *(&exportDirectory->AddressOfFunctions), rdataSection);\n\tBOOL stubFound = FALSE; \n\n\tfor (size_t i = 0; i < exportDirectory->NumberOfNames;\
  \ i++)\n\t{\n\t\tDWORD_PTR functionNameVA = (DWORD_PTR)RVAtoRawOffset((DWORD_PTR)fileData + addressOfNames[i], rdataSection);\n\
  \t\tDWORD_PTR functionVA = (DWORD_PTR)RVAtoRawOffset((DWORD_PTR)fileData + addressOfFunctions[i + 1], textSection);\n\t\t\
  LPCSTR functionNameResolved = (LPCSTR)functionNameVA;\n\t\tif (std::strcmp(functionNameResolved, functionName) == 0)\n\t\
  \t{\n\t\t\tstd::memcpy(syscallStub, (LPVOID)functionVA, SYSCALL_STUB_SIZE);\n\t\t\tstubFound = TRUE;\n\t\t}\n\t}\n\n\treturn\
  \ stubFound;\n}\n\nint main(int argc, char* argv[]) {\n\tchar syscallStub[SYSCALL_STUB_SIZE] = {};\n\tSIZE_T bytesWritten\
  \ = 0;\n\tDWORD oldProtection = 0;\n\tHANDLE file = NULL;\n\tDWORD fileSize = NULL;\n\tDWORD bytesRead = NULL;\n\tLPVOID\
  \ fileData = NULL;\n\t\n\t// variables for NtCreateFile\n\tOBJECT_ATTRIBUTES oa;\n\tHANDLE fileHandle = NULL;\n\tNTSTATUS\
  \ status = NULL;\n\tUNICODE_STRING fileName;\n\tRtlInitUnicodeString(&fileName, (PCWSTR)L\"\\\\??\\\\c:\\\\temp\\\\pw.log\"\
  );\n\tIO_STATUS_BLOCK osb;\n\tZeroMemory(&osb, sizeof(IO_STATUS_BLOCK));\n\tInitializeObjectAttributes(&oa, &fileName, OBJ_CASE_INSENSITIVE,\
  \ NULL, NULL);\n\n\t// define NtCreateFile\n\tmyNtCreateFile NtCreateFile = (myNtCreateFile)(LPVOID)syscallStub;\n\tVirtualProtect(syscallStub,\
  \ SYSCALL_STUB_SIZE, PAGE_EXECUTE_READWRITE, &oldProtection);\n\t\n\tfile = CreateFileA(\"c:\\\\windows\\\\system32\\\\\
  ntdll.dll\", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);\n\tfileSize = GetFileSize(file,\
  \ NULL);\n\tfileData = HeapAlloc(GetProcessHeap(), 0, fileSize);\n\tReadFile(file, fileData, fileSize, &bytesRead, NULL);\n\
  \n\tPIMAGE_DOS_HEADER dosHeader = (PIMAGE_DOS_HEADER)fileData;\n\tPIMAGE_NT_HEADERS imageNTHeaders = (PIMAGE_NT_HEADERS)((DWORD_PTR)fileData\
  \ + dosHeader->e_lfanew);\n\tDWORD exportDirRVA = imageNTHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress;\n\
  \tPIMAGE_SECTION_HEADER section = IMAGE_FIRST_SECTION(imageNTHeaders);\n\tPIMAGE_SECTION_HEADER textSection = section;\n\
  \tPIMAGE_SECTION_HEADER rdataSection = section;\n\t\n\tfor (int i = 0; i < imageNTHeaders->FileHeader.NumberOfSections;\
  \ i++) \n\t{\n\t\tif (std::strcmp((CHAR*)section->Name, (CHAR*)\".rdata\") == 0) { \n\t\t\trdataSection = section;\n\t\t\
  \tbreak;\n\t\t}\n\t\tsection++;\n\t}\n\n\tPIMAGE_EXPORT_DIRECTORY exportDirectory = (PIMAGE_EXPORT_DIRECTORY)RVAtoRawOffset((DWORD_PTR)fileData\
  \ + exportDirRVA, rdataSection);\n\t\n\tGetSyscallStub(\"NtCreateFile\", exportDirectory, fileData, textSection, rdataSection,\
  \ syscallStub);\n\tNtCreateFile(&fileHandle, FILE_GENERIC_WRITE, &oa, &osb, 0, FILE_ATTRIBUTE_NORMAL, FILE_SHARE_WRITE,\
  \ FILE_OVERWRITE_IF, FILE_SYNCHRONOUS_IO_NONALERT, NULL,\t0);\n\n\treturn 0;\n}\n```\n\n## References\n\n{% embed url=\"\
  https://github.com/odzhan/injection/blob/ad8e7a11899ffb2d9467a8ea44c6f3755d13b00e/syscalls/inject_dll.c#L260\" %}\n\n{%\
  \ embed url=\"https://github.com/am0nsec/HellsGate\" %}"
_relative_path: offensive-security/defense-evasion/retrieving-ntdll-syscall-stubs-at-run-time.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/retrieving-ntdll-syscall-stubs-at-run-time.md
````
