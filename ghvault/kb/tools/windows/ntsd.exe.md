---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ntsd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ntsd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntsd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Symbolic Debugger for Windows.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ntsd.md)
- Source verification: [source record](../../sources/lolbas/ntsd.exe.md)

## Aliases

- `Ntsd.exe`
- `ntsd.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: ntsd.exe -g {CMD} |

## Source Verification

[source record](../../sources/lolbas/ntsd.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: ntsd.exe -g {CMD}
Description: Launches command through the debugging process; optionally add `-G` to exit the debugger automatically.
```
