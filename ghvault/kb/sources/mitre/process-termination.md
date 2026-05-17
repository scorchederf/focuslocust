---
parsed_by: focuslocust
source: mitre
type: generated
---
# Process Termination

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0033` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Termination](../../attack/data-sources/DC0033-process-termination.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0033 |
| name | Process Termination |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0033 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The exit or termination of a running process on a system. This can occur due to normal operations, user-initiated
  commands, or malicious actions such as process termination by malware to disable security controls.
external_references:
- external_id: DC0033
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0033
id: x-mitre-data-component--61f1d40e-f3d0-4cc6-aa2d-937b6204194f
modified: '2025-11-12T22:03:39.105Z'
name: Process Termination
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- mobile-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Process
- channel: EventCode=5
  name: WinEventLog:Sysmon
- channel: Unexpected termination of daemons or critical services not aligned with admin change tickets
  name: linux:syslog
- channel: 'process_termination: Unexpected termination of processes tied to vulnerable or high-value services'
  name: macos:osquery
- channel: Log entries indicating VM powered off or forcibly terminated
  name: esxi:hostd
- channel: Terminal process killed (killall Terminal) immediately after sudoers modification
  name: macos:unifiedlog
- channel: exit_group
  name: auditd:SYSCALL
- channel: process.*exit.*code
  name: macos:unifiedlog
- channel: unexpected termination of syslog or rsyslog processes
  name: linux:osquery
- channel: Process segfault or abnormal termination after invoking vulnerable syscall sequence
  name: auditd:SYSCALL
- channel: kill syscalls targeting logging/security processes
  name: auditd:SYSCALL
- channel: Termination of syspolicyd or XProtect processes
  name: macos:unifiedlog
- channel: Termination of monitoring sidecar or security container
  name: docker:runtime
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
