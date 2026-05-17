---
parsed_by: focuslocust
source: mitre
type: generated
---
# Process Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0035` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Access](../../attack/data-sources/DC0035-process-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0035 |
| name | Process Access |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0035 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Refers to an event where one process attempts to open another process, typically to inspect or manipulate its\
  \ memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both\
  \ benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection.\n\n*Data Collection\
  \ Measures:*\n\n- Endpoint Detection and Response (EDR) Tools:\n    -  EDR solutions that provide telemetry on inter-process\
  \ access and memory manipulation.\n- Sysmon (Windows):\n    - Event ID 10: Captures process access attempts, including:\n\
  \        - Source process (initiator)\n        - Target process (victim)\n        - Access rights requested\n        - Process\
  \ ID correlation\n- Windows Event Logs:\n    - Event ID 4656 (Audit Handle to an Object): Logs access attempts to system\
  \ objects.\n    - Event ID 4690 (Attempted Process Modification): Can help identify unauthorized process changes.\n- Linux/macOS\
  \ Monitoring:\n    - AuditD: Monitors process access through syscall tracing (e.g., `ptrace`, `open`, `read`, `write`).\n\
  \    - eBPF/XDP: Used for low-level monitoring of kernel process access.\n    - OSQuery: Query process access behavior via\
  \ structured SQL-like logging.\n- Procmon (Process Monitor) and Debugging Tools:\n    - Windows Procmon: Captures real-time\
  \ process interactions.\n    - Linux strace / ptrace: Useful for tracking process behavior at the system call level."
external_references:
- external_id: DC0035
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0035
id: x-mitre-data-component--1887a270-576a-4049-84de-ef746b2572d6
modified: '2026-02-23T18:45:08.713Z'
name: Process Access
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
- mobile-attack
x_mitre_log_sources:
- channel: EventCode=10
  name: WinEventLog:Sysmon
- channel: Process State
  name: linux:osquery
- channel: ptrace attach
  name: auditd:SYSCALL
- channel: ptrace or task_for_pid
  name: macos:unifiedlog
- channel: process_open
  name: macos:osquery
- channel: High frequency of accept(), read(), or SSL_read() syscalls tied to nginx/apache processes
  name: auditd:SYSCALL
- channel: Microphone Access Events
  name: Apple TCC Logs
- channel: ptrace
  name: auditd:SYSCALL
- channel: syscalls (open, read, ioctl) on /dev/input or /proc/*/fd/*
  name: linux:syslog
- channel: EventCode=25
  name: WinEventLog:Sysmon
- channel: ES_EVENT_TYPE_NOTIFY_OPEN
  name: macos:endpointsecurity
- channel: Unexpected NSXPCConnection calls by non-Apple-signed or abnormal binaries
  name: macos:unifiedlog
- channel: EventCode=4663, 4670, 4656
  name: WinEventLog:Security
- channel: Unusual Mach port registration or access attempts between unrelated processes
  name: macos:unifiedlog
- channel: subsystem=com.apple.security, library=libsystem_kernel.dylib
  name: macos:unifiedlog
- channel: ptrace syscall or access to /proc/*/mem
  name: auditd:SYSCALL
- channel: vm_read, task_for_pid, or file open to cookie databases
  name: macos:unifiedlog
- channel: process_events
  name: linux:osquery
- channel: ACCESS
  name: auditd:SYSCALL
- channel: execve, fork, mmap, ptrace
  name: auditd:SYSCALL
- channel: ptrace or process_vm_readv
  name: auditd:SYSCALL
- channel: unexpected memory inspection
  name: macos:osquery
- channel: Code signing validation events referencing newly written local Mach-O/bundle prior to exec or dlopen
  name: iOS:unifiedlog
- channel: Runtime grant or manifest presence for MANAGE_EXTERNAL_STORAGE/READ_EXTERNAL_STORAGE/READ_MEDIA_*; legacy external
    storage mode detection
  name: android:logcat
- channel: Privacy (TCC) prompts/grants for Photos/Files or access changes indicating new visibility into user/app data
  name: iOS:unifiedlog
- channel: Activity/Process state change (mFocusedApp, onResume/onPause) identifying <pkg> as foreground
  name: android:logcat
- channel: Foreground/background transition for <bundle_id> to contextualize access timing
  name: iOS:unifiedlog
- channel: Grant/activation of BIND_ACCESSIBILITY_SERVICE, BIND_INPUT_METHOD, SYSTEM_ALERT_WINDOW, POST_NOTIFICATIONS for
    <pkg>
  name: android:logcat
- channel: Keyboard extension Full Access change; privacy grant touching input/keyboard categories for <bundle_id>
  name: iOS:unifiedlog
- channel: Grant/enablement for BIND_ACCESSIBILITY_SERVICE or BIND_INPUT_METHOD for <pkg>
  name: android:logcat
- channel: Keyboard extension Full Access change or related privacy grant for <bundle_id>
  name: iOS:unifiedlog
- channel: Grant/enablement of SYSTEM_ALERT_WINDOW, BIND_ACCESSIBILITY_SERVICE, POST_NOTIFICATIONS for <pkg>
  name: android:logcat
- channel: Scene/foreground transitions for <bundle_id> to contextualize timing
  name: iOS:unifiedlog
- channel: Reads/queries ops for PACKAGE_USAGE_STATS, QUERY_ALL_PACKAGES, BIND_DEVICE_ADMIN, BIND_VPN_SERVICE
  name: android:logcat
- channel: Sustained or high-frequency location sensor access, including background location usage
  name: EDR:telemetry
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '3.0'
```
