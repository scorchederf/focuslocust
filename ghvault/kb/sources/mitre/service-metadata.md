---
parsed_by: focuslocust
source: mitre
type: generated
---
# Service Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0041` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Service Metadata](../../attack/data-sources/DC0041-service-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0041 |
| name | Service Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0041 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Contextual data about a service/daemon, which may include information such as name, service executable, start
  type, etc.
external_references:
- external_id: DC0041
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0041
id: x-mitre-data-component--74fa567d-bc90-425c-8a41-3c703abb221c
modified: '2026-04-16T16:59:19.254Z'
name: Service Metadata
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Service
- channel: EventCode=4
  name: WinEventLog:Sysmon
- channel: service stopped messages
  name: linux:syslog
- channel: launchctl disable or bootout calls
  name: macos:unifiedlog
- channel: Stop VM or disable service events via vim-cmd
  name: esxi:hostd
- channel: auditd service stopped or disabled
  name: linux:syslog
- channel: launchd
  name: macos:osquery
- channel: scheduled/real-time
  name: linux:osquery
- channel: subsystem=com.apple.launchservices
  name: macos:unifiedlog
- channel: registers services with legitimate-sounding names
  name: esxi:hostd
- channel: EventCode=7035
  name: WinEventLog:System
- channel: Service restart with modified executable path
  name: linux:syslog
- channel: Observed loading of new LaunchAgent or LaunchDaemon plist
  name: macos:unifiedlog
- channel: seccomp or AppArmor profile changes
  name: kubernetes:audit
- channel: Service stopped or RecoveryDisabled set via REAgentC
  name: WinEventLog:System
- channel: Service events
  name: esxi:hostd
- channel: EventCode=6
  name: WinEventLog:WinRM
- channel: 'delete: Modification of systemd unit files or config for security agents'
  name: auditd:CONFIG_CHANGE
- channel: Modification of system configuration profiles affecting security tools
  name: macos:unifiedlog
- channel: kubectl delete or patch of security pods/admission controllers
  name: kubernetes:audit
- channel: 'write: Startup configuration changes disabling security checks'
  name: networkdevice:config
- channel: auditd stopped, config changed, logging suspended
  name: auditd:DAEMON
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
