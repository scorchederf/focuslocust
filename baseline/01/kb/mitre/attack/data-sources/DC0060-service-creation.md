---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0060
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0060-service-creation
---

## Description

The registration of a new service or daemon on an operating system.<br><br>*Data Collection Measures:*<br><br>- Windows Event Logs<br>    - Event ID 4697 - Captures the creation of a new Windows service.<br>    - Event ID 7045 - Captures services installed by administrators or adversaries.<br>    - Event ID 7034 - Could indicate malicious service modification or exploitation.<br>- Sysmon Logs<br>    - Sysmon Event ID 1 - Process Creation (captures service executables).<br>    - Sysmon Event ID 4 - Service state changes (detects service installation).<br>    - Sysmon Event ID 13 - Registry modifications (captures service persistence changes).<br>- PowerShell Logging<br>    - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script Block Logging).<br>- Linux/macOS Collection Methods<br>    - AuditD & Syslog Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`)<br>    - AuditD Rules:<br>        - `auditctl -w /etc/systemd/system -p wa -k service_creation`<br>        - Detects changes to `systemd` service configurations.<br>- Systemd Journals (`journalctl -u <service_name>`)<br>    - Captures newly created systemd services.<br>- LaunchDaemons & LaunchAgents (macOS)<br>    - Monitor `/Library/LaunchDaemons/` and `/Library/LaunchAgents/` for new plist files.
