---
parsed_by: focuslocust
source: mitre
type: generated
---
# Host Status

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0018` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Host Status](../../attack/data-sources/DC0018-host-status.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0018 |
| name | Host Status |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0018 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Logging, messaging, and other artifacts that highlight the health and operational state of host-based security\
  \ sensors, such as Endpoint Detection and Response (EDR) agents, antivirus software, logging services, and system monitoring\
  \ tools. Monitoring sensor health is essential for detecting misconfigurations, sensor failures, tampering, or deliberate\
  \ security control evasion by adversaries.\n\n*Data Collection Measures:*\n\n- Windows Event Logs:\n    - Event ID 1074\
  \ (System Shutdown): Detects unexpected system reboots/shutdowns.\n    - Event ID 6006 (Event Log Stopped): Logs when Windows\
  \ event logging is stopped.\n    - Event ID 16 (Sysmon): Detects configuration state changes that may indicate log tampering.\n\
  \    - Event ID 12 (Windows Defender Status Change) – Detects changes in Windows Defender state.\n- Linux/macOS Monitoring:\n\
  \    - `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log`\n    - Journald (journalctl) for kernel and system alerts.\n\
  - Endpoint Detection and Response (EDR) Tools:\n    - Monitor agent health status, detect sensor tampering, and alert on\
  \ missing telemetry.\n- Mobile Threat Intelligence Logs:\n    - Samsung Knox, SafetyNet, iOS Secure Enclave provide sensor\
  \ health status for mobile endpoints."
external_references:
- external_id: DC0018
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0018
id: x-mitre-data-component--85a533a4-5fa4-4dba-b45d-f0717bedd6e6
modified: '2026-04-20T18:17:23.974Z'
name: Host Status
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- mobile-attack
- enterprise-attack
x_mitre_log_sources:
- channel: no logging host, no aaa new-model, no snmp-server, commit
  name: networkdevice:syslog
- channel: ACCESS_FINE_LOCATION|NEARBY_DEVICES|BLUETOOTH_SCAN used in close proximity to network-context queries
  name: android:appops
- channel: SafetyNet attestation with CTSProfileMatch=false or BasicIntegrity=false
  name: AndroidAttestation:SafetyNet
- channel: Verified Boot or dm-verity reports partition hash mismatch, non-green boot state, or integrity failure
  name: AndroidAttestation:VerifiedBoot
- channel: Crash or abnormal restart of privileged system services (for example, system_server, mediaserver, installd) followed
    shortly by new privileged process activity or binder connections from a single app UID
  name: AndroidLogs:Crash
- channel: Application or system process crash/restart patterns temporally associated with remote service communications
  name: AndroidLogs:Crash
- channel: firmware_update, kexec_load
  name: auditd:SYSCALL
- channel: Autoscaling, memory/cpu alarms, or instance unhealthiness
  name: AWS:CloudMetrics
- channel: Sustained spike in CPU usage on EC2 instance with web service role
  name: AWS:CloudWatch
- channel: StatusCheckFailed or StatusCheckFailed_System for burstable instances (t2/t3)
  name: AWS:CloudWatch
- channel: Sustained EC2 CPU usage above normal baseline
  name: AWS:CloudWatch
- channel: NetworkOut spike beyond baseline
  name: AWS:CloudWatch
- channel: Sudden spike in network output without a corresponding inbound request ratio
  name: AWS:CloudWatch
- channel: Unusual CPU burst or metric anomalies
  name: AWS:CloudWatch
- channel: Powering off or restarting host
  name: esxi:hostd
- channel: Device risk, compliance, or security posture changes after trusted host pairing or developer-state transition
  name: iOS:MDMLog
- channel: code signature validation failure / exec of invalidly-signed payload from sandboxed app
  name: iOS:unifiedlog
- channel: Application crash logs, watchdog terminations, or abnormal execution events associated with service communication
  name: iOS:unifiedlog
- channel: Secure Boot failure, firmware version change
  name: journald:boot
- channel: CrashLoopBackOff, OOMKilled, container restart count exceeds threshold
  name: kubernetes:events
- channel: Sustained high /proc/[pid]/stat usage
  name: linux:procfs
- channel: Out of memory killer invoked or kernel panic entries
  name: linux:syslog
- channel: Service stop or disable messages for security tools not reflected in SIEM alerts
  name: linux:syslog
- channel: system is powering down
  name: linux:syslog
- channel: 'interface_details '
  name: macos:osquery
- channel: Hardware UUID or device list drift
  name: macos:syslog
- channel: Web service process (e.g., httpd) entering crash loop or consuming excessive CPU
  name: macos:unifiedlog
- channel: Spike in CPU or memory use from non-user-initiated processes
  name: macos:unifiedlog
- channel: Termination or disabling of XProtect, Gatekeeper, or third-party AV daemons
  name: macos:unifiedlog
- channel: network stack resource exhaustion, tcp_accept queue overflow, repeated resets
  name: macos:unifiedlog
- channel: EFI firmware integrity check failed
  name: macos:unifiedlog
- channel: System Integrity Protection (SIP) state reported as disabled
  name: macos:unifiedlog
- channel: System shutdown or reboot requested
  name: macos:unifiedlog
- channel: jailbreak/root compromise indicators or integrity attestation failures enabling process visibility
  name: MDM:DeviceIntegrity
- channel: System reboot scheduled or performed
  name: networkdevice:syslog
- channel: 'TCP: possible SYN flood or backlog limit exceeded'
  name: NSM:Flow
- channel: Samsung Knox attestation shows attestation_state=COMPROMISED or warranty bit set
  name: OEMAttestation:Knox
- channel: Container CPU/Memory usage exceeding threshold
  name: prometheus:metrics
- channel: Outbound network saturation with minimal process activity
  name: sar:network
- channel: None
  name: Sensor Health
- channel: Sustained CPU/memory exhaustion by service process (e.g., w3wp.exe)
  name: Windows:perfmon
- channel: High sustained CPU usage by a single process
  name: Windows:perfmon
- channel: Sudden spike in outbound throughput without corresponding inbound traffic
  name: Windows:perfmon
- channel: Sudden spikes in CPU/Memory usage linked to specific application processes
  name: Windows:perfmon
- channel: Connection queue overflow or failure to allocate TCP state object
  name: WinEventLog:Microsoft-Windows-TCPIP
- channel: EventCode=1166, 7045
  name: WinEventLog:Security
- channel: EventCode=1074
  name: WinEventLog:Security
- channel: EventCode=6006
  name: WinEventLog:Security
- channel: EventCode=16
  name: WinEventLog:Sysmon
- channel: System shutdowns due to bugcheck (Event ID 1001) or watchdog timer expirations
  name: WinEventLog:System
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
