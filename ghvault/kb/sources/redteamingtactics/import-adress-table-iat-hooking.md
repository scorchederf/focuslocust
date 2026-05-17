---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Import Adress Table (IAT) Hooking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-import-adress-table-iat-hooking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/import-adress-table-iat-hooking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Import Adress Table (IAT) Hooking](../../topics/offensive-security/import-adress-table-iat-hooking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-import-adress-table-iat-hooking |
| name | Import Adress Table (IAT) Hooking |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/import-adress-table-iat-hooking.md |

## Preserved Source Material

````yaml
_asset_filenames:
- iat-hook-demo.gif
- image (277).png
- image (278).png
- image (279).png
- image (280).png
- image (282).png
- image (285).png
- image (286).png
- image (287).png
- image (288).png
_body: "# Import Adress Table (IAT) Hooking\n\n## Overview\n\n* Windows portable executable contains a structure called `Import\
  \ Address Table (IAT)`&#x20;\n* IAT contains pointers to information that is critical for an executable to do its job:&#x20;\n\
  \  * a list of DLLs it depends on for providing the expected functionality\n  * a list of function names and their addresses\
  \ from those DLLs that may be called by the binary at some point\n* It is possible to hook function pointers specified in\
  \ the IAT by overwriting the target function's address with a rogue function address and optionally to execute the originally\
  \ intended function\n\nBelow is a simplified diagram that attempts to visualize the flow of events before and after a function\
  \ \\\n(`MessageBoxA` in this example, but could be any) is hooked:\n\n![](<../../.gitbook/assets/image (280).png>)\n\n**Before\
  \ hooking**\n\n1. the target program calls a WinAPI `MessageBoxA` function\n2. the program looks up the `MessageBoxA` address\
  \ in the IAT&#x20;\n3. code execution jumps to the  `kernel32!MessageBoxA` address resolved in step 2 where legitimate code\
  \ for displaying the `MessageBoxA` (green box) lives\n\n**After hooking**\n\n1. the target program calls `MessageBoxA` like\
  \ before hooking\n2. the program looks up the `MessageBoxA` address in the IAT&#x20;\n3. this time, because the IAT has\
  \ been tampered with, the `MessageBoxA` address in the IAT is pointing to a rogue `hookedMessageBox` function (red box)&#x20;\n\
  4. the program jumps to the `hookedMessageBox` retrieved in step 3\n5. `hookedMessageBox` intercepts the `MessageBoxA` parameters\
  \ and executes some malicous code&#x20;\n6. `hookedMessageBox` calls the legitimate `kernel32!MessageBoxA` routine\n\n##\
  \ Walkthrough\n\nIn this lab I'm going to write a simple executable that will hook `MessageBoxA` in its process memory space\
  \ by leveraging the IAT hooking technique and redirect it to a function called `hookedMessageBox` as per above visualisation\
  \ and then transfer the code execution back to the intended `MessageBoxA` routine.\n\n{% hint style=\"warning\" %}\nIAT\
  \ hooking is usually performed by a DLL injected into a target process, but for the sake of simplicity and illustration,\
  \ in this lab, the IAT hooking is implemented in the local process.\n{% endhint %}\n\nTo hook the `MessageBoxA` we need\
  \ to:\n\n1. Save memory address of the original `MessageBoxA`\n2. Define a `MessageBoxA` function prototype\n3. Create a\
  \ `hookedMessageBox` (rogue `MessageBoxA`) function with the above prototype. This is the function that intercepts the original\
  \ `MessageBoxA` call, executes some malicious code (in my case, it invokes a `MessageBoxW`) and transfers code execution\
  \ to the original `MessageBoxA` routine for which the address is retrieved in step 1\n4. Parse IAT table until address of\
  \ `MessageBoxA` is found\n   1. More about PE parsing in [Parsing PE File Headers with C++](../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md)\n\
  \   2. More about Import Address Table parsing in [Reflective DLL Injection](reflective-dll-injection.md#resolving-import-address-table)\n\
  5. Replace `MessageBoxA` address with address of the `hookedMessageBox`\n\nAs a reminder, we can check the IAT of any binary\
  \ using CFF Explorer or any other PE parser. Below highlighted is one of the IAT entries - the target function `MessageBoxA`\
  \ that will be patched during runtime and swapped with `hookedMessageBox`:\n\n![IAT table, CFF Explorer](<../../.gitbook/assets/image\
  \ (282).png>)\n\n## Code\n\nBelow is the code and key comments showing how IAT hooking could be implemented:\n\n```cpp\n\
  #include <iostream>\n#include <Windows.h>\n#include <winternl.h>\n\n// define MessageBoxA prototype\nusing PrototypeMessageBox\
  \ = int (WINAPI *)(HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType);\n\n// remember memory address of the original\
  \ MessageBoxA routine\nPrototypeMessageBox originalMsgBox = MessageBoxA;\n\n// hooked function with malicious code that\
  \ eventually calls the original MessageBoxA\nint hookedMessageBox(HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType)\n\
  {\n\tMessageBoxW(NULL, L\"Ola Hooked from a Rogue Senor .o.\", L\"Ola Senor o/\", 0);\n\t// execute the original NessageBoxA\n\
  \treturn originalMsgBox(hWnd, lpText, lpCaption, uType);\n}\n\nint main()\n{\n\t// message box before IAT unhooking\n\t\
  MessageBoxA(NULL, \"Hello Before Hooking\", \"Hello Before Hooking\", 0);\n\t\n\tLPVOID imageBase = GetModuleHandleA(NULL);\n\
  \tPIMAGE_DOS_HEADER dosHeaders = (PIMAGE_DOS_HEADER)imageBase;\n\tPIMAGE_NT_HEADERS ntHeaders = (PIMAGE_NT_HEADERS)((DWORD_PTR)imageBase\
  \ + dosHeaders->e_lfanew);\n\n\tPIMAGE_IMPORT_DESCRIPTOR importDescriptor = NULL;\n\tIMAGE_DATA_DIRECTORY importsDirectory\
  \ = ntHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT];\n\timportDescriptor = (PIMAGE_IMPORT_DESCRIPTOR)(importsDirectory.VirtualAddress\
  \ + (DWORD_PTR)imageBase);\n\tLPCSTR libraryName = NULL;\n\tHMODULE library = NULL;\n\tPIMAGE_IMPORT_BY_NAME functionName\
  \ = NULL; \n\n\twhile (importDescriptor->Name != NULL)\n\t{\n\t\tlibraryName = (LPCSTR)importDescriptor->Name + (DWORD_PTR)imageBase;\n\
  \t\tlibrary = LoadLibraryA(libraryName);\n\n\t\tif (library)\n\t\t{\n\t\t\tPIMAGE_THUNK_DATA originalFirstThunk = NULL,\
  \ firstThunk = NULL;\n\t\t\toriginalFirstThunk = (PIMAGE_THUNK_DATA)((DWORD_PTR)imageBase + importDescriptor->OriginalFirstThunk);\n\
  \t\t\tfirstThunk = (PIMAGE_THUNK_DATA)((DWORD_PTR)imageBase + importDescriptor->FirstThunk);\n\n\t\t\twhile (originalFirstThunk->u1.AddressOfData\
  \ != NULL)\n\t\t\t{\n\t\t\t\tfunctionName = (PIMAGE_IMPORT_BY_NAME)((DWORD_PTR)imageBase + originalFirstThunk->u1.AddressOfData);\n\
  \t\t\t\t\t\n\t\t\t\t// find MessageBoxA address\n\t\t\t\tif (std::string(functionName->Name).compare(\"MessageBoxA\") ==\
  \ 0)\n\t\t\t\t{\n\t\t\t\t\tSIZE_T bytesWritten = 0;\n\t\t\t\t\tDWORD oldProtect = 0;\n\t\t\t\t\tVirtualProtect((LPVOID)(&firstThunk->u1.Function),\
  \ 8, PAGE_READWRITE, &oldProtect);\n\t\t\t\t\t\t\n\t\t\t\t\t// swap MessageBoxA address with address of hookedMessageBox\n\
  \t\t\t\t\tfirstThunk->u1.Function = (DWORD_PTR)hookedMessageBox;\n\t\t\t\t}\n\t\t\t\t++originalFirstThunk;\n\t\t\t\t++firstThunk;\n\
  \t\t\t}\n\t\t}\n\n\t\timportDescriptor++;\n\t}\n\n\t// message box after IAT hooking\n\tMessageBoxA(NULL, \"Hello after\
  \ Hooking\", \"Hello after Hooking\", 0);\n\t\n\treturn 0;\n}\n```\n\n## Demo\n\nOur binary's base address (ImageBase) in\
  \ memory is at `0x00007FF69C010000`:\n\n![](<../../.gitbook/assets/image (285).png>)\n\nBefore IAT manipulation, `MessageBoxA`\
  \ points to `0x00007ffe78071d30`:\n\n![Line 58 in provided code - MessageBoxA is located at 0x00007ffe78071d30 before hooking\
  \ ](<../../.gitbook/assets/image (288).png>)\n\nIf interested, we can manually work out that `MessageBoxA` is located at\
  \ `0x00007ffe78071d30` by:\n\n1. adding the ImageBase `0x00007FF69C010000` and Relative Virtual Address (RVA) of the First\
  \ Thunk of `MessageBoxA` `0x000271d0` which equals to `0x00007FF69C0371D0`\n2. dereferrencing `0x00007FF69C0371D0`\n\n![RVA\
  \ of the function MessageBoxA](<../../.gitbook/assets/image (286).png>)\n\nDereferrencing `0x00007FF69C0371D0 (0x00007FF69C010000\
  \ + 0x000271d0)` reveals the `MessageBoxA` location in memory `0x00007ffe78071d30`:\n\n![0x00007FF69C0371D0 points to MessageBoxA\
  \ at 0x00007ffe78071d30 ](<../../.gitbook/assets/image (287).png>)\n\nNow, our `hookedMessageBox` is located at `0x00007ff396d5440`:\n\
  \n![](<../../.gitbook/assets/image (277).png>)\n\nAfter the IAT manipulation code executes, `MessageBoxA` points to `hookedMessageBox`\
  \ at `0x00007ff396d5440`\n\n![](<../../.gitbook/assets/image (278).png>)\n\nOnce the function pointers are swapped, we can\
  \ see that calling the `MessageBoxA` with an argument `Hello after Hooking` does not print `Hello after Hooking`, rather,\
  \ the message text is that seen in the `hookedMessageBox` routine, confirming that the IAT hook was successful and the rouge\
  \ function was called first:\n\n![](<../../.gitbook/assets/image (279).png>)\n\nBelow shows the entire flow of key events\
  \ that happen in this program:\n\n1. Before hooking, `MessageBoxA` is called with an argument `Hello Before Hooking` and\
  \ the program displays the message as expected\n2. After IAT hooking, `MessageBoxA` is called with an argument `Hello after\
  \ Hooking`, but the program gets redirected to a `hookedMessageBox` function and displays `Ola Hooked from a Rogue Senor\
  \ .o.`\n3. Finally, `hookedMessageBox` calls the original `MessageBoxA` which prints out the intended `Hello after Hooking`\n\
  \n![](../../.gitbook/assets/iat-hook-demo.gif)\n\n## References\n\n{% content-ref url=\"../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md\"\
  \ %}\n[pe-file-header-parser-in-c++.md](../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md)\n\
  {% endcontent-ref %}\n\n{% content-ref url=\"reflective-dll-injection.md\" %}\n[reflective-dll-injection.md](reflective-dll-injection.md)\n\
  {% endcontent-ref %}\n\n{% content-ref url=\"how-to-hook-windows-api-using-c++.md\" %}\n[how-to-hook-windows-api-using-c++.md](how-to-hook-windows-api-using-c++.md)\n\
  {% endcontent-ref %}"
_relative_path: offensive-security/code-injection-process-injection/import-adress-table-iat-hooking.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/import-adress-table-iat-hooking.md
````
