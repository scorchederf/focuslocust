---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Diantz.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `diantz.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diantz.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary that package existing files into a cabinet (.cab) file

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/diantz.md)
- Source verification: [source record](../../sources/lolbas/diantz.exe.md)

## Aliases

- `Diantz.exe`
- `diantz.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1036 - Masquerading](../../attack/techniques/T1036-masquerading.md) | explicit | source | Command metadata lists T1036: diantz /f {PATH:.ddf} |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: diantz.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: diantz.exe {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:targetFile.cab |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/diantz.exe.md)

## Source Verification

[source record](../../sources/lolbas/diantz.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@tim8288'
Person: Tamir Yehuda
- Handle: '@vakninhai'
Person: Hai Vaknin
Author: Tamir Yehuda
Commands:
- Category: ADS
```
