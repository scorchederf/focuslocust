---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ComputerDefaults.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `computerdefaults.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/ComputerDefaults.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ComputerDefaults.exe is a Windows system utility for managing default applications for tasks like web browsing, emailing, and media playback.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/computerdefaults.md)
- Source verification: [source record](../../sources/lolbas/computerdefaults.exe.md)

## Aliases

- `ComputerDefaults.exe`
- `computerdefaults.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | Command metadata lists T1548.002: ComputerDefaults.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/computerdefaults.exe.md)

## Source Verification

[source record](../../sources/lolbas/computerdefaults.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Eron Clarke
Author: Eron Clarke
Commands:
- Category: UAC Bypass
Command: ComputerDefaults.exe
Description: Upon execution, ComputerDefaults.exe checks two registry values at HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command;
if these are set by an attacker, the set command will be executed as a high-integrity process without a UAC prompt being
```
