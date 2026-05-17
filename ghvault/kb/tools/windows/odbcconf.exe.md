---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Odbcconf.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `odbcconf.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Odbcconf.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used in Windows for managing ODBC connections

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/odbcconf.md)
- Source verification: [source record](../../sources/lolbas/odbcconf.exe.md)

## Aliases

- `Odbcconf.exe`
- `odbcconf.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.008 - Odbcconf](../../attack/techniques/T1218.008-odbcconf.md) | explicit | source | Command metadata lists T1218.008: odbcconf -f {PATH:.rsp} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/odbcconf.exe.md)

## Source Verification

[source record](../../sources/lolbas/odbcconf.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@Hexacorn'
Person: Adam
Author: Oddvar Moe
Code_Sample:
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/58b5eb751379501aa237275f14381f0902e979a5/Archive-Old-Version/OSBinaries/Payload/file.rsp
```
