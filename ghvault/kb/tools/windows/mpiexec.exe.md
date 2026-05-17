---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mpiexec.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mpiexec.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mpiexec.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command-line tool for running Message Passing Interface (MPI) applications.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/mpiexec.md)
- Source verification: [source record](../../sources/lolbas/mpiexec.exe.md)

## Aliases

- `Mpiexec.exe`
- `mpiexec.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: mpiexec.exe {CMD} |

## Source Verification

[source record](../../sources/lolbas/mpiexec.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: mpiexec.exe {CMD}
Description: Executes a command via MPI command-line tool.
```
