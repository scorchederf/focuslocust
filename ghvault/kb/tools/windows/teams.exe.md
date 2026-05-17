---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Teams.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `teams.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Teams.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Electron runtime binary which runs the Teams application

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/teams.md)
- Source verification: [source record](../../sources/lolbas/teams.exe.md)

## Aliases

- `Teams.exe`
- `teams.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.015 - Electron Applications](../../attack/techniques/T1218.015-electron-applications.md) | explicit | source | Command metadata lists T1218.015: teams.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/teams.exe.md)

## Source Verification

[source record](../../sources/lolbas/teams.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Andrew Kisliakov
- Handle: '@mrd0x'
Person: mr.d0x
Author: Andrew Kisliakov
Code_Sample:
- Code: https://github.com/lltltk/LOLBAS-research/tree/master/Teams
Commands:
```
