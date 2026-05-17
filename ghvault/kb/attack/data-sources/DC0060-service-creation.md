---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0060 - Service Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0060` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The registration of a new service or daemon on an operating system.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4697 - Captures the creation of a new Windows service.
    - Event ID 7045 - Captures services installed by administrators or adversaries.
    - Event ID 7034 - Could indicate malicious service modification or exploitation.
- Sysmon Logs
    - Sysmon Event ID 1 - Process Creation (captures service executables).
    - Sysmon Event ID 4 - Service state changes (detects service installation).
    - Sysmon Event ID 13 - Registry modifications (captures service persistence changes).
- PowerShell Logging
    - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script Block Logging).
- Linux/macOS Collection Methods
    - AuditD & Syslog Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`)
    - AuditD Rules:
        - `auditctl -w /etc/systemd/system -p wa -k service_creation`
        - Detects changes to `systemd` service configurations.
- Systemd Journals (`journalctl -u <service_name>`)
    - Captures newly created systemd services.
- LaunchDaemons & LaunchAgents (macOS)
    - Monitor `/Library/LaunchDaemons/` and `/Library/LaunchAgents/` for new plist files.

## Source Verification

[source record](../../sources/mitre/service-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The registration of a new service or daemon on an operating system.\n\n*Data Collection Measures:*\n\n- Windows\
\ Event Logs\n    - Event ID 4697 - Captures the creation of a new Windows service.\n    - Event ID 7045 - Captures services\
\ installed by administrators or adversaries.\n    - Event ID 7034 - Could indicate malicious service modification or exploitation.\n\
- Sysmon Logs\n    - Sysmon Event ID 1 - Process Creation (captures service executables).\n    - Sysmon Event ID 4 - Service\
\ state changes (detects service installation).\n    - Sysmon Event ID 13 - Registry modifications (captures service persistence\
\ changes).\n- PowerShell Logging\n    - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script\
```
