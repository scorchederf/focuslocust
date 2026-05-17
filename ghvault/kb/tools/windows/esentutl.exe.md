---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Esentutl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `esentutl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary for working with Microsoft Joint Engine Technology (JET) database

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/esentutl.md)
- Source verification: [source record](../../sources/lolbas/esentutl.exe.md)

## Aliases

- `Esentutl.exe`
- `esentutl.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | Command metadata lists T1003.003: esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d {PATH_ABSOLUTE:.dit} |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: esentutl.exe /y {PATH_ABSOLUTE:.source.vbs} /d {PATH_ABSOLUTE:.dest.vbs} /o |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: esentutl.exe /y {PATH_SMB:.source.exe} /d {PATH_SMB:.dest.exe} /o |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/esentutl.exe.md)

## Source Verification

[source record](../../sources/lolbas/esentutl.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@egre55'
Person: egre55
- Handle: '@grayfold3d'
Person: Mike Cary
Author: Oddvar Moe
Commands:
- Category: Copy
```
