---
parsed_by: focuslocust
source: lolbas
type: generated
---
# VSDiagnostics.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsdiagnostics.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSDiagnostics.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command-line tool used for performing diagnostics.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/vsdiagnostics.md)
- Source verification: [source record](../../sources/lolbas/vsdiagnostics.exe.md)

## Aliases

- `VSDiagnostics.exe`
- `vsdiagnostics.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: VSDiagnostics.exe start 2 /launch:{PATH:.exe} /launchArgs:"{CMD:args}" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/vsdiagnostics.exe.md)

## Source Verification

[source record](../../sources/lolbas/vsdiagnostics.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0xBoku'
Person: Bobby Cooke
Author: Bobby Cooke
Commands:
- Category: Execute
Command: VSDiagnostics.exe start 1 /launch:{PATH:.exe}
Description: Starts a collection session with sessionID 1 and calls kernelbase.CreateProcessW to launch specified executable.
```
