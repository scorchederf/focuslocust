---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Eudcedit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `eudcedit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eudcedit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Private Character Editor Windows Utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/eudcedit.md)
- Source verification: [source record](../../sources/lolbas/eudcedit.exe.md)

## Aliases

- `Eudcedit.exe`
- `eudcedit.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | Command metadata lists T1548.002: eudcedit |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/eudcedit.exe.md)

## Source Verification

[source record](../../sources/lolbas/eudcedit.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@Bl4ckShad3'
Person: Matan Bahar
Author: Matan Bahar
Commands:
- Category: UAC Bypass
Command: eudcedit
Description: Once executed, the Private Charecter Editor will be opened - click OK, then click File -> Font Links. In the
```
