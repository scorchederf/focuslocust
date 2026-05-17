---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mavinject.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mavinject.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mavinject.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by App-v in Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/mavinject.md)
- Source verification: [source record](../../sources/lolbas/mavinject.exe.md)

## Aliases

- `Mavinject.exe`
- `mavinject.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.013 - Mavinject](../../attack/techniques/T1218.013-mavinject.md) | explicit | source | Command metadata lists T1218.013: MavInject.exe 3110 /INJECTRUNNING {PATH_ABSOLUTE:.dll} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: Mavinject.exe 4172 /INJECTRUNNING {PATH_ABSOLUTE}:file.dll |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/mavinject.exe.md)

## Source Verification

[source record](../../sources/lolbas/mavinject.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@gN3mes1s'
Person: Giuseppe N3mes1s
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Execute
```
