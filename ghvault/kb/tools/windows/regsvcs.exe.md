---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regsvcs.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regsvcs.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvcs.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Regsvcs and Regasm are Windows command-line utilities that are used to register .NET Component Object Model (COM) assemblies

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/regsvcs.md)
- Source verification: [source record](../../sources/lolbas/regsvcs.exe.md)

## Aliases

- `Regsvcs.exe`
- `regsvcs.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.009 - Regsvcs／Regasm](../../attack/techniques/T1218.009-regsvcs-regasm.md) | explicit | source | Command metadata lists T1218.009: regsvcs.exe {PATH:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/regsvcs.exe.md)

## Source Verification

[source record](../../sources/lolbas/regsvcs.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Execute
Command: regsvcs.exe {PATH:.dll}
Description: Loads the target .NET DLL file and executes the RegisterClass function.
```
