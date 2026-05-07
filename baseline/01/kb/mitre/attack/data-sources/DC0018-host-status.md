---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0018
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0018-host-status
---

## Description

Logging, messaging, and other artifacts that highlight the health and operational state of host-based security sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate security control evasion by adversaries.<br><br>*Data Collection Measures:*<br><br>- Windows Event Logs:<br>    - Event ID 1074 (System Shutdown): Detects unexpected system reboots/shutdowns.<br>    - Event ID 6006 (Event Log Stopped): Logs when Windows event logging is stopped.<br>    - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering.<br>    - Event ID 12 (Windows Defender Status Change) – Detects changes in Windows Defender state.<br>- Linux/macOS Monitoring:<br>    - `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log`<br>    - Journald (journalctl) for kernel and system alerts.<br>- Endpoint Detection and Response (EDR) Tools:<br>    - Monitor agent health status, detect sensor tampering, and alert on missing telemetry.<br>- Mobile Threat Intelligence Logs:<br>    - Samsung Knox, SafetyNet, iOS Secure Enclave provide sensor health status for mobile endpoints.
