---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mftrace.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mftrace.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mftrace.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Trace log generation tool for Media Foundation Tools.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/mftrace.md)
- Source verification: [source record](../../sources/lolbas/mftrace.exe.md)

## Aliases

- `Mftrace.exe`
- `mftrace.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: Mftrace.exe {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/mftrace.exe.md)

## Source Verification

[source record](../../sources/lolbas/mftrace.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0rbz_'
Person: fabrizio
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Mftrace.exe {PATH:.exe}
Description: Launch specified executable as a subprocess of Mftrace.exe.
```
