---
parsed_by: focuslocust
source: lolbas
type: generated
---
# iscsicpl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `iscsicpl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iscsicpl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft iSCSI Initiator Control Panel tool

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/iscsicpl.md)
- Source verification: [source record](../../sources/lolbas/iscsicpl.exe.md)

## Aliases

- `iscsicpl.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | Command metadata lists T1548.002: iscsicpl.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/iscsicpl.exe.md)

## Source Verification

[source record](../../sources/lolbas/iscsicpl.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: hacker.house
- Handle: '@eki_erk'
Person: Ekitji
Author: Ekitji
Commands:
- Category: UAC Bypass
Command: c:\windows\syswow64\iscsicpl.exe
```
