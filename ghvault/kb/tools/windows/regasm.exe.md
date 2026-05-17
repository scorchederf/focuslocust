---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regasm.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regasm.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regasm.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Part of .NET

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/regasm.md)
- Source verification: [source record](../../sources/lolbas/regasm.exe.md)

## Aliases

- `Regasm.exe`
- `regasm.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.009 - Regsvcs／Regasm](../../attack/techniques/T1218.009-regsvcs-regasm.md) | explicit | source | Command metadata lists T1218.009: regasm.exe /U {PATH:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/regasm.exe.md)

## Source Verification

[source record](../../sources/lolbas/regasm.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
Command: regasm.exe {PATH:.dll}
Description: Loads the target .NET DLL file and executes the RegisterClass function.
```
