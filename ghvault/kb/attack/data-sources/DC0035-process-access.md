---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0035 - Process Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0035` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Refers to an event where one process attempts to open another process, typically to inspect or manipulate its memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection.

*Data Collection Measures:*

- Endpoint Detection and Response (EDR) Tools:
    -  EDR solutions that provide telemetry on inter-process access and memory manipulation.
- Sysmon (Windows):
    - Event ID 10: Captures process access attempts, including:
        - Source process (initiator)
        - Target process (victim)
        - Access rights requested
        - Process ID correlation
- Windows Event Logs:
    - Event ID 4656 (Audit Handle to an Object): Logs access attempts to system objects.
    - Event ID 4690 (Attempted Process Modification): Can help identify unauthorized process changes.
- Linux/macOS Monitoring:
    - AuditD: Monitors process access through syscall tracing (e.g., `ptrace`, `open`, `read`, `write`).
    - eBPF/XDP: Used for low-level monitoring of kernel process access.
    - OSQuery: Query process access behavior via structured SQL-like logging.
- Procmon (Process Monitor) and Debugging Tools:
    - Windows Procmon: Captures real-time process interactions.
    - Linux strace / ptrace: Useful for tracking process behavior at the system call level.

## Source Verification

[source record](../../sources/mitre/process-access.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Refers to an event where one process attempts to open another process, typically to inspect or manipulate its\
\ memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both\
\ benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection.\n\n*Data Collection\
\ Measures:*\n\n- Endpoint Detection and Response (EDR) Tools:\n    -  EDR solutions that provide telemetry on inter-process\
\ access and memory manipulation.\n- Sysmon (Windows):\n    - Event ID 10: Captures process access attempts, including:\n\
\        - Source process (initiator)\n        - Target process (victim)\n        - Access rights requested\n        - Process\
```
