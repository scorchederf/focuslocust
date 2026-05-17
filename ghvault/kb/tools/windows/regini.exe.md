---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regini.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regini.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regini.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to manipulate the registry

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/regini.md)
- Source verification: [source record](../../sources/lolbas/regini.exe.md)

## Aliases

- `Regini.exe`
- `regini.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: regini.exe {PATH}:hidden.ini |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/regini.exe.md)

## Source Verification

[source record](../../sources/lolbas/regini.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elisalem9'
Person: Eli Salem
Author: Oddvar Moe
Commands:
- Category: ADS
Command: regini.exe {PATH}:hidden.ini
Description: Write registry keys from data inside the Alternate data stream.
```
