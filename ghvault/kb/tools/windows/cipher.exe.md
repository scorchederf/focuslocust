---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cipher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cipher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cipher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

File Encryption Utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cipher.md)
- Source verification: [source record](../../sources/lolbas/cipher.exe.md)

## Aliases

- `Cipher.exe`
- `cipher.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1485 - Data Destruction](../../attack/techniques/T1485-data-destruction.md) | explicit | source | Command metadata lists T1485: cipher /w:{PATH_ABSOLUTE:folder} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cipher.exe.md)

## Source Verification

[source record](../../sources/lolbas/cipher.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@i_am_tutu'
Person: Ade Ogunsowo
- Handle: '@conitrade'
Person: Alexander Sennhauser
Author: Adetutu Ogunsowo
Commands:
- Category: Tamper
```
