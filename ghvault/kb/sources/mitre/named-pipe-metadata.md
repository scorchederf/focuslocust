---
parsed_by: focuslocust
source: mitre
type: generated
---
# Named Pipe Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0048` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Named Pipe Metadata](../../attack/data-sources/DC0048-named-pipe-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0048 |
| name | Named Pipe Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0048 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18)\n\
  \n*Data Collection Measures:*\n\n- Windows:\n    - Sysmon Event ID 17: Logs the creation of a named pipe.\n    - Sysmon\
  \ Event ID 18: Logs connection attempts to a named pipe.\n    - Windows Security Event ID 5145: Logs access attempts to\
  \ named pipes via SMB shares.\n    - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions.\n\
  - Linux/macOS:\n    - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage.\n\
  \    - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes.\n    - Strace (`strace\
  \ -e open <process>`): Monitors named pipe interactions.\n- Endpoint Detection & Response (EDR):\n    - Capture named pipe\
  \ events as part of process tracking.\n- Memory Forensics:\n    - Volatility Plugin (`pipescan`): Enumerates named pipes\
  \ in system memory.\n    - Rekall Framework: Identifies active named pipes and associated processes."
external_references:
- external_id: DC0048
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0048
id: x-mitre-data-component--b9a1578e-8653-4103-be23-cb52e0b1816e
modified: '2025-10-21T15:14:39.039Z'
name: Named Pipe Metadata
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: EventCode=17
  name: WinEventLog:Sysmon
- channel: XPC messages requesting privileged actions from untrusted or unsigned clients
  name: macos:unifiedlog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
