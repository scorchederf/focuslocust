---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dump64.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dump64.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dump64.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Memory dump tool that comes with Microsoft Visual Studio

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dump64.md)
- Source verification: [source record](../../sources/lolbas/dump64.exe.md)

## Aliases

- `Dump64.exe`
- `dump64.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | Command metadata lists T1003.001: dump64.exe {PID} out.dmp |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/dump64.exe.md)

## Source Verification

[source record](../../sources/lolbas/dump64.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mrd0x'
Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Dump
Command: dump64.exe {PID} out.dmp
Description: Creates a memory dump of the LSASS process.
```
