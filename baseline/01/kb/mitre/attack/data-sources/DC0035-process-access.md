---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0035
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0035-process-access
---

## Description

Refers to an event where one process attempts to open another process, typically to inspect or manipulate its memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection.<br><br>*Data Collection Measures:*<br><br>- Endpoint Detection and Response (EDR) Tools:<br>    -  EDR solutions that provide telemetry on inter-process access and memory manipulation.<br>- Sysmon (Windows):<br>    - Event ID 10: Captures process access attempts, including:<br>        - Source process (initiator)<br>        - Target process (victim)<br>        - Access rights requested<br>        - Process ID correlation<br>- Windows Event Logs:<br>    - Event ID 4656 (Audit Handle to an Object): Logs access attempts to system objects.<br>    - Event ID 4690 (Attempted Process Modification): Can help identify unauthorized process changes.<br>- Linux/macOS Monitoring:<br>    - AuditD: Monitors process access through syscall tracing (e.g., `ptrace`, `open`, `read`, `write`).<br>    - eBPF/XDP: Used for low-level monitoring of kernel process access.<br>    - OSQuery: Query process access behavior via structured SQL-like logging.<br>- Procmon (Process Monitor) and Debugging Tools:<br>    - Windows Procmon: Captures real-time process interactions.<br>    - Linux strace / ptrace: Useful for tracking process behavior at the system call level.
