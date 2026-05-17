---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Jsc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `jsc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Jsc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary file used by .NET to compile JavaScript code to .exe or .dll format

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/jsc.md)
- Source verification: [source record](../../sources/lolbas/jsc.exe.md)

## Aliases

- `Jsc.exe`
- `jsc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: jsc.exe /t:library {PATH:.js} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/jsc.exe.md)

## Source Verification

[source record](../../sources/lolbas/jsc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@DissectMalware'
Person: Malwrologist
Author: Oddvar Moe
Commands:
- Category: Compile
Command: jsc.exe {PATH:.js}
Description: Use jsc.exe to compile JavaScript code stored in the provided .JS file and generate a .EXE file with the same
```
