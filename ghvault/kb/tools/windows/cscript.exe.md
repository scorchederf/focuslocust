---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cscript.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cscript.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cscript.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary used to execute scripts in Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cscript.md)
- Source verification: [source record](../../sources/lolbas/cscript.exe.md)

## Aliases

- `Cscript.exe`
- `cscript.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: cscript //e:vbscript {PATH_ABSOLUTE}:script.vbs |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cscript.exe.md)

## Source Verification

[source record](../../sources/lolbas/cscript.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
Command: cscript //e:vbscript {PATH_ABSOLUTE}:script.vbs
Description: Use cscript.exe to exectute a Visual Basic script stored in an Alternate Data Stream (ADS).
```
