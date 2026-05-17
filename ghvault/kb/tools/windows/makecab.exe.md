---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Makecab.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `makecab.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Makecab.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary to package existing files into a cabinet (.cab) file

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/makecab.md)
- Source verification: [source record](../../sources/lolbas/makecab.exe.md)

## Aliases

- `Makecab.exe`
- `makecab.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1036 - Masquerading](../../attack/techniques/T1036-masquerading.md) | explicit | source | Command metadata lists T1036: makecab /F {PATH:.ddf} |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: makecab {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: makecab {PATH_SMB:.exe} {PATH_ABSOLUTE}:file.cab |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/makecab.exe.md)

## Source Verification

[source record](../../sources/lolbas/makecab.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
Command: makecab {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:autoruns.cab
Description: Compresses the target file into a CAB file stored in the Alternate Data Stream (ADS) of the target file.
```
