---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Bcp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `bcp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bcp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft SQL Server Bulk Copy Program utility for importing and exporting data between SQL Server instances and data files.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/bcp.md)
- Source verification: [source record](../../sources/lolbas/bcp.exe.md)

## Aliases

- `Bcp.exe`
- `bcp.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost -T -c |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/bcp.exe.md)

## Source Verification

[source record](../../sources/lolbas/bcp.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mahiralikhan07'
Person: Mahir Ali Khan
Author: Mahir Ali Khan
Commands:
- Category: Download
Command: bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost
-T -c
```
