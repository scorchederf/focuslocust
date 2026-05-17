---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Executing Code as a Control Panel Item through an Exported Cplapplet Function

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-executing-code-in-control-panel-item-through-an-exported-cplapplet-function` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/executing-code-in-control-panel-item-through-an-exported-cplapplet-function.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Executing Code as a Control Panel Item through an Exported Cplapplet Function](../../topics/offensive-security/executing-code-as-a-control-panel-item-through-an-exported-cplapplet-function.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-executing-code-in-control-panel-item-through-an-exported-cplapplet-function |
| name | Executing Code as a Control Panel Item through an Exported Cplapplet Function |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/executing-code-in-control-panel-item-through-an-exported-cplapplet-function.md |

## Preserved Source Material

````yaml
_asset_filenames:
- cplexecution.gif
- image (200).png
- image (202).png
- image (203).png
- image (204).png
_body: "# Executing Code as a Control Panel Item through an Exported Cplapplet Function\n\nThis is a quick note that shows\
  \ how to execute code in a .cpl file, which is a regular DLL file representing a Control Panel item.\n\nThe .cpl file needs\
  \ to export a function `CplApplet` in order to be recognized by Windows as a Control Panel item.\n\nOnce the DLL is compiled\
  \ and renamed to .CPL, it can simply be double clicked and executed like a regular Windows .exe file.\n\n## Code\n\n{% code\
  \ title=\"item.cpl\" %}\n```cpp\n// dllmain.cpp : Defines the entry point for the DLL application.\n#include \"stdafx.h\"\
  \n#include <Windows.h>\n\n//Cplapplet\nextern \"C\" __declspec(dllexport) LONG Cplapplet(\n\tHWND hwndCpl,\n\tUINT msg,\n\
  \tLPARAM lParam1,\n\tLPARAM lParam2\n)\n{\n\tMessageBoxA(NULL, \"Hey there, I am now your control panel item you know.\"\
  , \"Control Panel\", 0);\n\treturn 1;\n}\n\nBOOL APIENTRY DllMain( HMODULE hModule,\n                       DWORD  ul_reason_for_call,\n\
  \                       LPVOID lpReserved\n                     )\n{\n    switch (ul_reason_for_call)\n    {\n    case DLL_PROCESS_ATTACH:\n\
  \t{\n\t\tCplapplet(NULL, NULL, NULL, NULL);\n\t}\n    case DLL_THREAD_ATTACH:\n    case DLL_THREAD_DETACH:\n    case DLL_PROCESS_DETACH:\n\
  \        break;\n    }\n    return TRUE;\n}\n```\n{% endcode %}\n\nOnce the DLL is compiled, we can see our exported function\
  \ `Cplapplet`:\n\n![](<../../.gitbook/assets/image (200).png>)\n\n## Demo\n\nBelow shows that double-clicking the .cpl item\
  \ is enough to launch it:\n\n![](../../.gitbook/assets/cplexecution.gif)\n\n![](<../../.gitbook/assets/image (204).png>)\n\
  \nCPL file can also be launched with `control.exe <pathtothe.cpl>` like so:\n\n![](<../../.gitbook/assets/image (202).png>)\n\
  \nor with rundll32:\n\n{% code title=\"attacker@target\" %}\n```\nrundll32 shell32, Control_RunDLL \\\\VBOXSVR\\Experiments\\\
  cpldoubleclick\n\\cpldoubleclick\\Debug\\cpldoubleclick.cpl\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/image (203).png>)\n\
  \n## References\n\n{% embed url=\"https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html\"\
  \ %}\n\n{% embed url=\"https://github.com/fireeye/DueDLLigence/blob/master/DueDLLigence/DueDLLigence.cs\" %}\n\n{% embed\
  \ url=\"https://docs.microsoft.com/en-us/windows/win32/shell/using-cplapplet\" %}"
_relative_path: offensive-security/code-execution/executing-code-in-control-panel-item-through-an-exported-cplapplet-function.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/executing-code-in-control-panel-item-through-an-exported-cplapplet-function.md
````
