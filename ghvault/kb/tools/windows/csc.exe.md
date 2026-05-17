---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Csc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `csc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Csc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary file used by .NET Framework to compile C# code

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/csc.md)
- Source verification: [source record](../../sources/lolbas/csc.exe.md)

## Aliases

- `Csc.exe`
- `csc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: csc -target:library {PATH:.cs} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/csc.exe.md)

## Source Verification

[source record](../../sources/lolbas/csc.exe.md)

## Evidence Excerpt

```text
Author: Oddvar Moe
Commands:
- Category: Compile
Command: csc.exe -out:{PATH:.exe} {PATH:.cs}
Description: Use csc.exe to compile C# code, targeting the .NET Framework, stored in the specified .cs file and output the
compiled version to the specified .exe path.
MitreID: T1127
OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
```
