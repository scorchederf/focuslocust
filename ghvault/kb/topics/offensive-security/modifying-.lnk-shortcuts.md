---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Modifying .lnk Shortcuts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-modifying-.lnk-shortcuts` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/modifying-.lnk-shortcuts.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This is a quick lab showing how .lnk (shortcut files) can be used for persistence.

## Preserved Body

````markdown
This is a quick lab showing how .lnk (shortcut files) can be used for persistence.

## Execution

Say, there's a shortcut on the compromised system for a program HxD64 as shown below:

![](<../../_assets/image (432).png>)

. That shortcut can be hijacked and used for persistence. Let's change the shortcut's target to this simple powershell:

```csharp
powershell.exe -c "invoke-item \\VBOXSVR\Tools\HxD\HxD64.exe; invoke-item c:\windows\system32\calc.exe"
```

It will launch the HxD64, but will also launch a program of our choice - a calc.exe in this case. Notice how the shortcut icon changed to powershell - that is expected:

![](<../../_assets/image (433).png>)

We can change it back by clicking "Change Icon" and specifying the original .exe of HxD64.exe:

![](<../../_assets/image (434).png>)

The original icon is now back:

![](<../../_assets/image (435).png>)

## Demo

Below shows the hijack demo in action:

![](<../../_assets/lnk-hijacking.gif>)

In the above gif, we can see the black cmd prompt for a brief moment, however, it can be easily be hidden by changing the `Run` option of the shortcut to `Minimized`:

![](<../../_assets/image (436).png>)

Running the demo again with the `Run: Minimized` shows the black prompt went away:

![](<../../_assets/lnk-hijacking-minimized.gif>)
Note that hovering the shortcut reveals that the program to be launched is the powershell.
## Reference
````

## Source Verification

[source record](../../sources/redteamingtactics/modifying-.lnk-shortcuts.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (432).png
- image (433).png
- image (434).png
- image (435).png
- image (436).png
- lnk-hijacking-minimized.gif
- lnk-hijacking.gif
```
