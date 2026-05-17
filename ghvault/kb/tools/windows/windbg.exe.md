---
parsed_by: focuslocust
source: lolbas
type: generated
---
# WinDbg.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `windbg.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/WinDbg.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Debugger for advanced user-mode and kernel-mode debugging.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/windbg.md)
- Source verification: [source record](../../sources/lolbas/windbg.exe.md)

## Aliases

- `WinDbg.exe`
- `windbg.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: windbg.exe -g {CMD} |

## Source Verification

[source record](../../sources/lolbas/windbg.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: windbg.exe -g {CMD}
Description: Launches a command line through the debugging process; optionally add `-G` to exit the debugger automatically.
```
