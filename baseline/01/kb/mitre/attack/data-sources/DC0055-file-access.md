---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0055
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0055-file-access
---

## Description

To events where a file is opened or accessed, making its contents available to the requester. This includes reading, executing, or interacting with files by authorized or unauthorized entities. Examples include logging file access events (e.g., Windows Event ID 4663), monitoring file reads, and detecting unusual file access patterns. Examples: <br><br>- File Read Operations: A user opens a sensitive document (e.g., financial_report.xlsx) on a shared drive.<br>- File Execution: A script or executable file is accessed and executed (e.g., malware.exe is run from a temporary directory).<br>- Unauthorized File Access: An unauthorized user attempts to access a protected configuration file (e.g., `/etc/passwd` on Linux or `System32` files on Windows).<br>- File Access Patterns: Bulk access to multiple files in a short time (e.g., mass access to documents on a file server).<br>- File Access via Network: Files on a network share are accessed remotely (e.g., logs of SMB file access).
