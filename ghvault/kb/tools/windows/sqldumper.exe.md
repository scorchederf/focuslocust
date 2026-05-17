---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Sqldumper.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `sqldumper.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Sqldumper.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Debugging utility included with Microsoft SQL.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/sqldumper.md)
- Source verification: [source record](../../sources/lolbas/sqldumper.exe.md)

## Aliases

- `Sqldumper.exe`
- `sqldumper.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003 - OS Credential Dumping](../../attack/techniques/T1003-os-credential-dumping.md) | explicit | source | Command metadata lists T1003: sqldumper.exe 464 0 0x0110 |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | Command metadata lists T1003.001: sqldumper.exe 540 0 0x01100:40 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/sqldumper.exe.md)

## Source Verification

[source record](../../sources/lolbas/sqldumper.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@countuponsec'
Person: Luis Rocha
Author: Oddvar Moe
Commands:
- Category: Dump
Command: sqldumper.exe 464 0 0x0110
Description: Dump process by PID and create a dump file (Appears to create a dump file called SQLDmprXXXX.mdmp).
```
