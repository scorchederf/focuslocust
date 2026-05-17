---
parsed_by: focuslocust
source: mitre
type: generated
---
# Process Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0034` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Metadata](../../attack/data-sources/DC0034-process-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0034 |
| name | Process Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0034 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Contextual data about a running process, which may include information such as environment variables, image name,
  user/owner, etc.
external_references:
- external_id: DC0034
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0034
id: x-mitre-data-component--ee575f4a-2d4f-48f6-b18b-89067760adc1
modified: '2026-04-16T17:01:33.771Z'
name: Process Metadata
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
- channel: subsystem=com.apple.process
  name: macos:unifiedlog
- channel: CodeIntegrity/WDAC events indicating unsigned/invalid DLL loads
  name: WinEventLog:Microsoft-Windows-CodeIntegrity/Operational
- channel: sudo or service accounts invoking loaders with suspicious env vars
  name: linux:syslog
- channel: Process Context
  name: macos:osquery
- channel: user session
  name: esxi:auth
- channel: Admin activity
  name: networkdevice:syslog
- channel: execve call for sudo where euid != uid
  name: auditd:SYSCALL
- channel: subsystem=com.apple.TCC
  name: macos:unifiedlog
- channel: exec of binary with setuid/setgid and EUID != UID
  name: macos:unifiedlog
- channel: process
  name: macos:unifiedlog
- channel: Use of fork/exec with DISPLAY unset or redirected
  name: auditd:SYSCALL
- channel: Process lineage and API usage enrichment (GetSystemTime, GetTimeZoneInformation, NtQuerySystemTime)
  name: EDR:Telemetry
- channel: /var/log/hostd.log API calls reading/altering time/ntp settings
  name: esxi:hostd
- channel: execve, prctl, or ptrace activity affecting process memory or command-line arguments
  name: auditd:SYSCALL
- channel: Cross-reference argv[0] with actual executable path and parent process metadata
  name: linux:osquery
- channel: AppLocker audit/blocks showing developer utilities executing scripts/binaries outside policy
  name: WinEventLog:AppLocker
- channel: Correlation of signer info, parent-child lineage, rare invocation context (user host role), and API surfaces (CreateProcess*,
    LoadLibrary*)
  name: EDR:hunting
- channel: ETW telemetry indicating ClickOnce deployment (dfsvc.exe) launching payloads
  name: WinEventLog:Microsoft-Windows-Security-Mitigations/KernelMode
- channel: 'provider: Event Tracing for Windows (ETW) events associated with ClickOnce deployment (dfsvc.exe activity)'
  name: etw:Microsoft-Windows-ClickOnce
- channel: Process session start/stop events for camera pipeline by unexpected executables
  name: WinEventLog:Microsoft-Windows-Windows Camera Frame Server/Operational
- channel: 'select: path LIKE ''/dev/video%'''
  name: linux:osquery
- channel: state=attached/debugged
  name: linux:osquery
- channel: Code Execution & Entitlement Access
  name: macos:unifiedlog
- channel: Process opening SSH_AUTH_SOCK or /tmp/ssh-* socket not owned by same UID
  name: macos:unifiedlog
- channel: code signature/memory protection
  name: macos:unifiedlog
- channel: execve with UID ≠ EUID
  name: auditd:SYSCALL
- channel: execve with escalated privileges
  name: auditd:SYSCALL
- channel: cross-account or unexpected assume role
  name: AWS:CloudTrail
- channel: log collect from launchd and process start
  name: macos:unifiedlog
- channel: Docker or containerd image pulls and process executions
  name: containerd:events
- channel: Kernel or daemon warnings of downgraded TLS or cryptographic settings
  name: linux:syslog
- channel: Modifications or writes to EFI system partition for downgraded bootloaders
  name: macos:unifiedlog
- channel: non-shell process tree accessing bash history
  name: macos:unifiedlog
- channel: process metadata mismatch between /proc and runtime attributes
  name: linux:osquery
- channel: process environment variables containing LD_PRELOAD
  name: linux:osquery
- channel: EventCode=400, 403
  name: WinEventLog:PowerShell
- channel: Process Execution + Hash
  name: macos:osquery
- channel: 'process_start: EventHeader.ProcessId true parent vs reported PPID mismatch'
  name: etw:Microsoft-Windows-Kernel-Process
- channel: ES_EVENT_TYPE_NOTIFY_EXEC, ES_EVENT_TYPE_NOTIFY_MMAP
  name: macos:endpointsecurity
- channel: Unsigned/invalid signature modules or images loaded by msbuild.exe or its children
  name: WinEventLog:Microsoft-Windows-CodeIntegrity/Operational
- channel: WDAC policy audit/block affecting msbuild.exe spawned payloads
  name: WinEventLog:Microsoft-Windows-DeviceGuard/Operational
- channel: Smart App Control decisions (audit/block) for msbuild.exe-launched executables
  name: WinEventLog:Microsoft-Windows-SmartAppControl/Operational
- channel: Unsigned or untrusted modules loaded during JamPlus.exe runtime
  name: WinEventLog:Microsoft-Windows-CodeIntegrity/Operational
- channel: Crash or abnormal termination of security agent or system extension host
  name: macos:unifiedlog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
