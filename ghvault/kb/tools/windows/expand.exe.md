---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Expand.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `expand.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Expand.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary that expands one or more compressed files

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/expand.md)
- Source verification: [source record](../../sources/lolbas/expand.exe.md)

## Aliases

- `Expand.exe`
- `expand.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: expand {PATH_ABSOLUTE:.source.ext} {PATH_ABSOLUTE:.dest.ext} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: expand {PATH_SMB:.bat} {PATH_ABSOLUTE}:file.bat |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/expand.exe.md)

## Source Verification

[source record](../../sources/lolbas/expand.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@infosecn1nja'
Person: Rahmat Nurfauzi
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Download
```
