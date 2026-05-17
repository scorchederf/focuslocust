---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Windows API Hooking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-how-to-hook-windows-api-using-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/how-to-hook-windows-api-using-c++.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows API Hooking](../../topics/offensive-security/windows-api-hooking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-how-to-hook-windows-api-using-c |
| name | Windows API Hooking |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/how-to-hook-windows-api-using-c++.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-06-30 185043.png
- Annotation 2019-06-30 185215.png
- Annotation 2019-06-30 185320.png
- Annotation 2019-06-30 190323.png
- hookedmessagebox (1).gif
- image (1).png
- image (2).png
- originalbytes.gif
- patchingMessageBoxa.gif
_body: "# Windows API Hooking\n\nThis lab is a quick look into how userland WinAPIs can be hooked. A `MessageBoxA` function\
  \ will be hooked in this instance, but it could be any.\n\n> &#x20;**API hooking** is a technique by which we can instrument\
  \ and modify the behavior and flow of **API**calls.\\\n> [https://resources.infosecinstitute.com/api-hooking/](https://resources.infosecinstitute.com/api-hooking/)\n\
  \nWindows API hooking is one of the techniques used by AV/EDR solutions to determine if code is malicious. You can read\
  \ some of my notes on bypassing EDRs by leveraging unhooking - [Bypassing Cylance and other AVs/EDRs by Unhooking Windows\
  \ APIs](../defense-evasion/bypassing-cylance-and-other-avs-edrs-by-unhooking-windows-apis.md)\n\nFor this lab, I will write\
  \ a simple C++ program that will work follows:\n\n1. Get memory address of the `MessageBoxA` function\n2. Read the first\
  \ 6 bytes of the `MessageBoxA` - will need these bytes for unhooking the function\n3. Create a `HookedMessageBox` function\
  \ that will be executed when the original `MessageBoxA` is called\n4. Get memory address of the `HookedMessageBox`\n5. Patch\
  \ / redirect `MessageBoxA` to `HookedMessageBox`\n6. Call `MessageBoxA`. Code gets redirected to `HookedMessageBox`\n7.\
  \ `HookedMessageBox` executes its code, prints the supplied arguments, unhooks the `MessageBoxA` and transfers the code\
  \ control to the actual `MessageBoxA`\n\n## Execution\n\nPop the message box before the function is hooked - just to make\
  \ sure it works and to prove that no functions are hooked so far -  it's the first instruction of the program:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-06-30 185043.png>)\n\nGet the memory address of the `MessageBoxA` function:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-06-30 185215.png>)\n\nIf we dissasemble the bytes at that address, we can definitely see that there is code for `MessageBoxA`:\n\
  \n![](<../../.gitbook/assets/Annotation 2019-06-30 185320.png>)\n\nNote the first 6 bytes `8b ff 55 8b ec 6a`(mind the endian-ness).\
  \ We need to save these bytes for future when we want to unhook `MessageBoxA`:\n\n![](../../.gitbook/assets/originalbytes.gif)\n\
  \nLet's now build the patch (hook) bytes:\\\n\n\n![](<../../.gitbook/assets/Annotation 2019-06-30 190323.png>)\n\n...that\
  \ will translate into the following assembly instructions:\n\n```csharp\n// push HookedMessageBox memory address onto the\
  \ stack\npush HookedMessageBox\n// jump to HookedMessageBox\nret\n```\n\nWe can now patch the `MessageBoxA` - memory pane\
  \ in the bottom right shows the patch being written to the beginning of `MessageBoxA` function and the top right shows the\
  \ beginning of the same function is re-written with a `push 3e1474h; ret` instructions:\n\n![](../../.gitbook/assets/patchingMessageBoxa.gif)\n\
  \nIf we disassemble the address `3e1474h`, we can see it contains a jmp to our `HookedMessageBox`:\n\n![](<../../.gitbook/assets/image\
  \ (1).png>)\n\nThe `HookedMessageBox` intercepts and prints out the arguments supplied to `MessageBoxA`, then unhooks ~~`MessageBoxA`~~\
  \ by swaping back the first 6 bytes to the original bytes of the `MessageBoxA` function and then calls the `MessageBoxA`\
  \ with the supplied arguments:\n\n![](<../../.gitbook/assets/image (2).png>)\n\n## Demo\n\nOnce the function is hooked,\
  \ we can call the `MessageBoxA(NULL, \"hi\", \"hi\", MB_OK);` which will invoke the `HookedMessageBox`, print the intercepted\
  \ values and display the original message box:\n\n![](<../../.gitbook/assets/hookedmessagebox (1).gif>)\n\n## Code\n\n{%\
  \ code title=\"api-hooking.cpp\" %}\n```cpp\n#include \"pch.h\"\n#include <iostream>\n#include <Windows.h>\n\nFARPROC messageBoxAddress\
  \ = NULL;\nSIZE_T bytesWritten = 0;\nchar messageBoxOriginalBytes[6] = {};\n\nint __stdcall HookedMessageBox(HWND hWnd,\
  \ LPCSTR lpText, LPCSTR lpCaption, UINT uType) {\n\t\n\t// print intercepted values from the MessageBoxA function\n\tstd::cout\
  \ << \"Ohai from the hooked function\\n\";\n\tstd::cout << \"Text: \" << (LPCSTR)lpText << \"\\nCaption: \" << (LPCSTR)lpCaption\
  \ << std::endl;\n\t\n\t// unpatch MessageBoxA\n\tWriteProcessMemory(GetCurrentProcess(), (LPVOID)messageBoxAddress, messageBoxOriginalBytes,\
  \ sizeof(messageBoxOriginalBytes), &bytesWritten);\n\t\n\t// call the original MessageBoxA\n\treturn MessageBoxA(NULL, lpText,\
  \ lpCaption, uType);\n}\n\nint main()\n{\n\t// show messagebox before hooking\n\tMessageBoxA(NULL, \"hi\", \"hi\", MB_OK);\n\
  \n\tHINSTANCE library = LoadLibraryA(\"user32.dll\");\n\tSIZE_T bytesRead = 0;\n\t\n\t// get address of the MessageBox function\
  \ in memory\n\tmessageBoxAddress = GetProcAddress(library, \"MessageBoxA\");\n\n\t// save the first 6 bytes of the original\
  \ MessageBoxA function - will need for unhooking\n\tReadProcessMemory(GetCurrentProcess(), messageBoxAddress, messageBoxOriginalBytes,\
  \ 6, &bytesRead);\n\t\n\t// create a patch \"push <address of new MessageBoxA); ret\"\n\tvoid *hookedMessageBoxAddress =\
  \ &HookedMessageBox;\n\tchar patch[6] = { 0 };\n\tmemcpy_s(patch, 1, \"\\x68\", 1);\n\tmemcpy_s(patch + 1, 4, &hookedMessageBoxAddress,\
  \ 4);\n\tmemcpy_s(patch + 5, 1, \"\\xC3\", 1);\n\n\t// patch the MessageBoxA\n\tWriteProcessMemory(GetCurrentProcess(),\
  \ (LPVOID)messageBoxAddress, patch, sizeof(patch), &bytesWritten);\n\n\t// show messagebox after hooking\n\tMessageBoxA(NULL,\
  \ \"hi\", \"hi\", MB_OK);\n\n\treturn 0;\n}\n```\n{% endcode %}\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-messageboxa\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/how-to-hook-windows-api-using-c++.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/how-to-hook-windows-api-using-c++.md
````
