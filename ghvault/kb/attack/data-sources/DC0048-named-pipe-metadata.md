---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0048 - Named Pipe Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0048` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18)

*Data Collection Measures:*

- Windows:
    - Sysmon Event ID 17: Logs the creation of a named pipe.
    - Sysmon Event ID 18: Logs connection attempts to a named pipe.
    - Windows Security Event ID 5145: Logs access attempts to named pipes via SMB shares.
    - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions.
- Linux/macOS:
    - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage.
    - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes.
    - Strace (`strace -e open <process>`): Monitors named pipe interactions.
- Endpoint Detection & Response (EDR):
    - Capture named pipe events as part of process tracking.
- Memory Forensics:
    - Volatility Plugin (`pipescan`): Enumerates named pipes in system memory.
    - Rekall Framework: Identifies active named pipes and associated processes.

## Source Verification

[source record](../../sources/mitre/named-pipe-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18)\n\
\n*Data Collection Measures:*\n\n- Windows:\n    - Sysmon Event ID 17: Logs the creation of a named pipe.\n    - Sysmon\
\ Event ID 18: Logs connection attempts to a named pipe.\n    - Windows Security Event ID 5145: Logs access attempts to\
\ named pipes via SMB shares.\n    - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions.\n\
- Linux/macOS:\n    - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage.\n\
\    - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes.\n    - Strace (`strace\
```
