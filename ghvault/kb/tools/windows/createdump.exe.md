---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Createdump.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `createdump.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Createdump.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft .NET Runtime Crash Dump Generator (included in .NET Core)

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/createdump.md)
- Source verification: [source record](../../sources/lolbas/createdump.exe.md)

## Aliases

- `Createdump.exe`
- `createdump.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003 - OS Credential Dumping](../../attack/techniques/T1003-os-credential-dumping.md) | explicit | source | Command metadata lists T1003: createdump.exe -n -f {PATH:.dmp} {PID} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/createdump.exe.md)

## Source Verification

[source record](../../sources/lolbas/createdump.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bopin2020'
Person: bopin
Author: mr.d0x, Daniel Santos
Commands:
- Category: Dump
Command: createdump.exe -n -f {PATH:.dmp} {PID}
Description: Dump process by PID and create a minidump file. If "-f dump.dmp" is not specified, the file is created as '%TEMP%\dump.%p.dmp'
```
