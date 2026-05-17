---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0018 - Host Status

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0018` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Logging, messaging, and other artifacts that highlight the health and operational state of host-based security sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate security control evasion by adversaries.

*Data Collection Measures:*

- Windows Event Logs:
    - Event ID 1074 (System Shutdown): Detects unexpected system reboots/shutdowns.
    - Event ID 6006 (Event Log Stopped): Logs when Windows event logging is stopped.
    - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering.
    - Event ID 12 (Windows Defender Status Change) – Detects changes in Windows Defender state.
- Linux/macOS Monitoring:
    - `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log`
    - Journald (journalctl) for kernel and system alerts.
- Endpoint Detection and Response (EDR) Tools:
    - Monitor agent health status, detect sensor tampering, and alert on missing telemetry.
- Mobile Threat Intelligence Logs:
    - Samsung Knox, SafetyNet, iOS Secure Enclave provide sensor health status for mobile endpoints.

## Source Verification

[source record](../../sources/mitre/host-status.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Logging, messaging, and other artifacts that highlight the health and operational state of host-based security\
\ sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring\
\ tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate\
\ security control evasion by adversaries.\n\n*Data Collection Measures:*\n\n- Windows Event Logs:\n    - Event ID 1074\
\ (System Shutdown): Detects unexpected system reboots/shutdowns.\n    - Event ID 6006 (Event Log Stopped): Logs when Windows\
\ event logging is stopped.\n    - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering.\n\
```
