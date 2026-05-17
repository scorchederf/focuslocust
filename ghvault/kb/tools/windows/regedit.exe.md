---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regedit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regedit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regedit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to manipulate registry

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/regedit.md)
- Source verification: [source record](../../sources/lolbas/regedit.exe.md)

## Aliases

- `Regedit.exe`
- `regedit.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: regedit {PATH_ABSOLUTE}:regfile.reg |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/regedit.exe.md)

## Source Verification

[source record](../../sources/lolbas/regedit.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
Command: regedit /E {PATH_ABSOLUTE}:regfile.reg HKEY_CURRENT_USER\MyCustomRegKey
Description: Export the target Registry key to the specified .REG file.
```
