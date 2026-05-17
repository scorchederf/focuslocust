---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0055 - File Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0055` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

To events where a file is opened or accessed, making its contents available to the requester. This includes reading, executing, or interacting with files by authorized or unauthorized entities. Examples include logging file access events (e.g., Windows Event ID 4663), monitoring file reads, and detecting unusual file access patterns. Examples: 

- File Read Operations: A user opens a sensitive document (e.g., financial_report.xlsx) on a shared drive.
- File Execution: A script or executable file is accessed and executed (e.g., malware.exe is run from a temporary directory).
- Unauthorized File Access: An unauthorized user attempts to access a protected configuration file (e.g., `/etc/passwd` on Linux or `System32` files on Windows).
- File Access Patterns: Bulk access to multiple files in a short time (e.g., mass access to documents on a file server).
- File Access via Network: Files on a network share are accessed remotely (e.g., logs of SMB file access).

## Source Verification

[source record](../../sources/mitre/file-access.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "To events where a file is opened or accessed, making its contents available to the requester. This includes\
\ reading, executing, or interacting with files by authorized or unauthorized entities. Examples include logging file access\
\ events (e.g., Windows Event ID 4663), monitoring file reads, and detecting unusual file access patterns. Examples: \n\n\
- File Read Operations: A user opens a sensitive document (e.g., financial_report.xlsx) on a shared drive.\n- File Execution:\
\ A script or executable file is accessed and executed (e.g., malware.exe is run from a temporary directory).\n- Unauthorized\
\ File Access: An unauthorized user attempts to access a protected configuration file (e.g., `/etc/passwd` on Linux or `System32`\
```
