---
parsed_by: focuslocust
source: lolbas
type: generated
---
# rdrleakdiag.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rdrleakdiag.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rdrleakdiag.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Windows resource leak diagnostic tool

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/rdrleakdiag.md)
- Source verification: [source record](../../sources/lolbas/rdrleakdiag.exe.md)

## Aliases

- `rdrleakdiag.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003 - OS Credential Dumping](../../attack/techniques/T1003-os-credential-dumping.md) | explicit | source | Command metadata lists T1003: rdrleakdiag.exe /p 940 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1 |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | Command metadata lists T1003.001: rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /snap |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/rdrleakdiag.exe.md)

## Source Verification

[source record](../../sources/lolbas/rdrleakdiag.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0gtweet'
Person: Grzegorz Tworek
Author: John Dwyer
Commands:
- Category: Dump
Command: rdrleakdiag.exe /p 940 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1
Description: Dump process by PID and create a dump file (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`).
```
