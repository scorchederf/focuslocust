---
parsed_by: focuslocust
source: mitre
type: generated
---
# Process Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0020` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Modification](../../attack/data-sources/DC0020-process-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0020 |
| name | Process Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0020 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Changes made to a running process, such as writing data into memory, modifying execution behavior, or injecting
  code into an existing process. Adversaries frequently modify processes to execute malicious payloads, evade detection, or
  gain escalated privileges.
external_references:
- external_id: DC0020
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0020
id: x-mitre-data-component--d5fca4e4-e47a-487b-873f-3d22f8865e96
modified: '2025-11-12T22:03:39.105Z'
name: Process Modification
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
- channel: rename, chmod
  name: auditd:SYSCALL
- channel: mprotect
  name: auditd:SYSCALL
- channel: ES_EVENT_MMAP
  name: macos:endpointsecurity
- channel: kill syscalls targeting auditd process
  name: auditd:SYSCALL
- channel: memory mapping
  name: macos:unifiedlog
- channel: EventCode=8
  name: WinEventLog:Sysmon
- channel: Memory Mappings
  name: macos:osquery
- channel: Runtime memory overwrite of argv[] memory region
  name: ebpf:tracepoints
- channel: Memory Modification / Unmapped module load or suspicious RWX allocations in the process space of a browser process
  name: etw:Microsoft-Windows-Kernel-Process
- channel: Anomalous dyld dynamic library loads or RWX memory mappings in browser process
  name: macos:unifiedlog
- channel: open, rename
  name: auditd:SYSCALL
- channel: SYSCALL ptrace/mprotect
  name: auditd:SYSCALL
- channel: ES_EVENT_TYPE_NOTIFY_MMAP
  name: macos:endpointsecurity
- channel: process, library load, memory operations
  name: macos:unifiedlog
- channel: rename
  name: auditd:SYSCALL
- channel: Detection of bitwise operations or custom encryption functions in memory traces
  name: linux:osquery
- channel: Abnormal memory operations (XOR/bitwise loops) during archive generation
  name: macos:unifiedlog
- channel: change from PROT_READ|PROT_WRITE to PROT_EXEC
  name: auditd:memprotect
- channel: /proc/[pid]/maps, /proc/[pid]/mem
  name: linux:procfs
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
