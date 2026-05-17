---
parsed_by: focuslocust
source: lolbas
type: generated
---
# dnx.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dnx.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dnx.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

.NET Execution environment file included with .NET.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dnx.md)
- Source verification: [source record](../../sources/lolbas/dnx.exe.md)

## Aliases

- `dnx.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: dnx.exe {PATH_ABSOLUTE:folder} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/dnx.exe.md)

## Source Verification

[source record](../../sources/lolbas/dnx.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@enigma0x3'
Person: Matt Nelson
Author: Oddvar Moe
Commands:
- Category: Execute
Command: dnx.exe {PATH_ABSOLUTE:folder}
Description: Execute C# code located in the specified folder via 'Program.cs' and 'Project.json' (Note - Requires dependencies)
```
