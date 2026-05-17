---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vsjitdebugger.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsjitdebugger.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Vsjitdebugger.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Just-In-Time (JIT) debugger included with Visual Studio

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/vsjitdebugger.md)
- Source verification: [source record](../../sources/lolbas/vsjitdebugger.exe.md)

## Aliases

- `vsjitdebugger.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: Vsjitdebugger.exe {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/vsjitdebugger.exe.md)

## Source Verification

[source record](../../sources/lolbas/vsjitdebugger.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Vsjitdebugger.exe {PATH:.exe}
Description: Executes specified executable as a subprocess of Vsjitdebugger.exe.
```
