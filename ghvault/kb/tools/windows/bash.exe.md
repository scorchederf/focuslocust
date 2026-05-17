---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Bash.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `bash.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

File used by Windows subsystem for Linux

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/bash.md)
- Source verification: [source record](../../sources/lolbas/bash.exe.md)

## Aliases

- `Bash.exe`
- `bash.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: bash.exe -c "{CMD}" |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: bash.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/bash.exe.md)

## Source Verification

[source record](../../sources/lolbas/bash.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@aionescu'
Person: Alex Ionescu
- Handle: '@d1r4c'
Person: Asif Matadar
- Person: Liran Ravich, CardinalOps
Author: Oddvar Moe
Commands:
```
