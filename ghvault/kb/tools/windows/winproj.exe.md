---
parsed_by: focuslocust
source: lolbas
type: generated
---
# WinProj.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winproj.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Winproj.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Project Executable

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/winproj.md)
- Source verification: [source record](../../sources/lolbas/winproj.exe.md)

## Aliases

- `WinProj.exe`
- `winproj.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: WinProj.exe {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/winproj.exe.md)

## Source Verification

[source record](../../sources/lolbas/winproj.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Download
Command: WinProj.exe {REMOTEURL}
Description: Downloads payload from remote server
```
