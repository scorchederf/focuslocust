---
parsed_by: focuslocust
source: lolbas
type: generated
---
# fltMC.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `fltmc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/FltMC.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Filter Manager Control Program used by Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/fltmc.md)
- Source verification: [source record](../../sources/lolbas/fltmc.exe.md)

## Aliases

- `fltMC.exe`
- `fltmc.exe`

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/fltmc.exe.md)

## Source Verification

[source record](../../sources/lolbas/fltmc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@Carlos_Perez'
Person: Carlos Perez
Author: John Lambert
Commands:
- Category: Tamper
Command: fltMC.exe unload SysmonDrv
Description: Unloads a driver used by security agents
```
