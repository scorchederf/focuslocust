---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Extrac32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `extrac32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extrac32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Extract to ADS, copy or overwrite a file with Extrac32.exe

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/extrac32.md)
- Source verification: [source record](../../sources/lolbas/extrac32.exe.md)

## Aliases

- `Extrac32.exe`
- `extrac32.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: extrac32.exe /C {PATH_ABSOLUTE:.source.exe} {PATH_ABSOLUTE:.dest.exe} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/extrac32.exe.md)

## Source Verification

[source record](../../sources/lolbas/extrac32.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@egre55'
Person: egre55
- Handle: '@oddvarmoe'
Person: Oddvar Moe
- Handle: '@VakninHai'
Person: Hai Vaknin(Lux
- Handle: '@tim8288'
```
