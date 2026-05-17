---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Word Library Add-Ins

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-word-library-add-ins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/word-library-add-ins.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It' possible to persist in the userland by abusing word library add-ins by putting your malicious DLL into a Word's trusted location. Once the DLL is there, the Word will load it next time it is run.

## Preserved Body

````markdown
It' possible to persist in the userland by abusing word library add-ins by putting your malicious DLL into a Word's trusted location. Once the DLL is there, the Word will load it next time it is run.

## Execution

Get Word's trusted locations where library add-ins can be dropped:
```csharp
 Get-ChildItem "hkcu:\Software\Microsoft\Office\16.0\Word\Security\Trusted Locations"
```
![](<../../_assets/Annotation 2019-06-22 121402.png>)

Those trusted locations are actually defined in Word's Security Center if you have access to the GUI:

![](<../../_assets/Annotation 2019-06-22 121426.png>)

Let's create a simple DLL that will launch a notepad.exe once the DLL addin is loaded:

![](<../../_assets/Annotation 2019-06-22 143558.png>)

Compile the DLL and copy it over to `Startup` folder and rename it to `evilm64.wll`:

![](<../../_assets/Annotation 2019-06-22 121537.png>)

```
mv .\evilm64.dll .\evilm64.wll
```

![](<../../_assets/Annotation 2019-06-22 144024.png>)

Next time the victim opens up Word, `evilm64.wll` will be loaded and executed:

![](<../../_assets/Annotation 2019-06-22 143432.png>)

Interesting to note that Process Explorer does not see the evilm64.wll loaded in any of the currently running processes:

![](<../../_assets/Annotation 2019-06-22 144128.png>)

...although we can definitely see that the add-in is now recognized by Word:

![](<../../_assets/Annotation 2019-06-22 144219.png>)
This technique did not work for me on Office 365 version, but worked on Office Professional. Not sure if there's a bug in the 365 version or it's just a limitation of that version.
## References
````

## Source Verification

[source record](../../sources/redteamingtactics/word-library-add-ins.md)

## Evidence Excerpt

```text
_asset_filenames:
- Annotation 2019-06-22 121402.png
- Annotation 2019-06-22 121426.png
- Annotation 2019-06-22 121537.png
- Annotation 2019-06-22 143432.png
- Annotation 2019-06-22 143558.png
- Annotation 2019-06-22 144024.png
- Annotation 2019-06-22 144128.png
```
