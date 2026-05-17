---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Tar.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `tar.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tar.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to extract and create archives.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/tar.md)
- Source verification: [source record](../../sources/lolbas/tar.exe.md)

## Aliases

- `Tar.exe`
- `tar.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: tar -xf {PATH_SMB:.tar} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: tar -xf {PATH}:ads |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/tar.exe.md)

## Source Verification

[source record](../../sources/lolbas/tar.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@Cyber_Sorcery'
Person: Brian Lucero
- Person: Avester Fahimipour
Author: Brian Lucero
Commands:
- Category: ADS
Command: tar -cf {PATH}:ads {PATH_ABSOLUTE:folder}
```
