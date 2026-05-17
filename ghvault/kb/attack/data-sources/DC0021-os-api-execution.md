---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0021 - OS API Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0021` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Calls made by a process to operating system-provided Application Programming Interfaces (APIs). These calls are essential for interacting with system resources such as memory, files, and hardware, or for performing system-level tasks. Monitoring these calls can provide insight into a process's intent, especially if the process is malicious.

## Source Verification

[source record](../../sources/mitre/os-api-execution.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Calls made by a process to operating system-provided Application Programming Interfaces (APIs). These calls are
essential for interacting with system resources such as memory, files, and hardware, or for performing system-level tasks.
Monitoring these calls can provide insight into a process's intent, especially if the process is malicious.
external_references:
- external_id: DC0021
source_name: mitre-attack
```
