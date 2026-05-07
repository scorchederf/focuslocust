---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0048
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0048-named-pipe-metadata
---

## Description

Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18)<br><br>*Data Collection Measures:*<br><br>- Windows:<br>    - Sysmon Event ID 17: Logs the creation of a named pipe.<br>    - Sysmon Event ID 18: Logs connection attempts to a named pipe.<br>    - Windows Security Event ID 5145: Logs access attempts to named pipes via SMB shares.<br>    - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions.<br>- Linux/macOS:<br>    - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage.<br>    - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes.<br>    - Strace (`strace -e open <process>`): Monitors named pipe interactions.<br>- Endpoint Detection & Response (EDR):<br>    - Capture named pipe events as part of process tracking.<br>- Memory Forensics:<br>    - Volatility Plugin (`pipescan`): Enumerates named pipes in system memory.<br>    - Rekall Framework: Identifies active named pipes and associated processes.
