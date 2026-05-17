---
parsed_by: focuslocust
source: lolbas
type: generated
---
# rcsi.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rcsi.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Rcsi.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Non-Interactive command line inerface included with Visual Studio.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/rcsi.md)
- Source verification: [source record](../../sources/lolbas/rcsi.exe.md)

## Aliases

- `rcsi.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: rcsi.exe {PATH:.csx} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/rcsi.exe.md)

## Source Verification

[source record](../../sources/lolbas/rcsi.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@enigma0x3'
Person: Matt Nelson
Author: Oddvar Moe
Commands:
- Category: Execute
Command: rcsi.exe {PATH:.csx}
Description: Use embedded C# within the csx script to execute the code.
```
