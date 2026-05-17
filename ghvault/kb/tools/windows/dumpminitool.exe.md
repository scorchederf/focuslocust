---
parsed_by: focuslocust
source: lolbas
type: generated
---
# DumpMinitool.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dumpminitool.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DumpMinitool.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Dump tool part Visual Studio 2022

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dumpminitool.md)
- Source verification: [source record](../../sources/lolbas/dumpminitool.exe.md)

## Aliases

- `DumpMinitool.exe`
- `dumpminitool.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | Command metadata lists T1003.001: DumpMinitool.exe --file {PATH_ABSOLUTE} --processId 1132 --dumpType Full |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/dumpminitool.exe.md)

## Source Verification

[source record](../../sources/lolbas/dumpminitool.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mrd0x'
Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Dump
Command: DumpMinitool.exe --file {PATH_ABSOLUTE} --processId 1132 --dumpType Full
Description: Creates a memory dump of the lsass process
```
