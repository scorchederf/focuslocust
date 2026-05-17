---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Schtasks.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `schtasks.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Schtasks.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Schedule periodic tasks

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/schtasks.md)
- Source verification: [source record](../../sources/lolbas/schtasks.exe.md)

## Aliases

- `Schtasks.exe`
- `schtasks.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | Command metadata lists T1053.005: schtasks /create /s targetmachine /tn "MyTask" /tr "{CMD}" /sc daily |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/schtasks.exe.md)

## Source Verification

[source record](../../sources/lolbas/schtasks.exe.md)

## Evidence Excerpt

```text
Author: Oddvar Moe
Commands:
- Category: Execute
Command: schtasks /create /sc minute /mo 1 /tn "Reverse shell" /tr "{CMD}"
Description: Create a recurring task to execute every minute.
MitreID: T1053.005
OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
Privileges: User
```
