---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Print.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `print.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Print.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to send files to the printer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/print.md)
- Source verification: [source record](../../sources/lolbas/print.exe.md)

## Aliases

- `Print.exe`
- `print.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_SMB:.source.exe} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: print /D:{PATH_ABSOLUTE}:file.exe {PATH_ABSOLUTE:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/print.exe.md)

## Source Verification

[source record](../../sources/lolbas/print.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
Command: print /D:{PATH_ABSOLUTE}:file.exe {PATH_ABSOLUTE:.exe}
Description: Copy file.exe into the Alternate Data Stream (ADS) of file.txt.
```
