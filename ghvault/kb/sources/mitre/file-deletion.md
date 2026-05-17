---
parsed_by: focuslocust
source: mitre
type: generated
---
# File Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0040` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [File Deletion](../../attack/data-sources/DC0040-file-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0040 |
| name | File Deletion |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0040 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Refers to events where files are removed from a system or storage device. These events can indicate legitimate
  housekeeping activities or malicious actions such as attackers attempting to cover their tracks. Monitoring file deletions
  helps organizations identify unauthorized or suspicious activities.
external_references:
- external_id: DC0040
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0040
id: x-mitre-data-component--e905dad2-00d6-477c-97e8-800427abd0e8
modified: '2026-04-23T18:19:16.114Z'
name: File Deletion
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
- mobile-attack
x_mitre_log_sources:
- channel: None
  name: File
- channel: unlink/unlinkat on service binaries or data targets
  name: auditd:SYSCALL
- channel: file deletion
  name: auditd:SYSCALL
- channel: file_events
  name: macos:osquery
- channel: shell history
  name: esxi:shell
- channel: EventCode=23
  name: WinEventLog:Sysmon
- channel: PATH
  name: auditd:SYSCALL
- channel: /var/log/shell.log
  name: esxi:shell
- channel: delete action
  name: esxi:hostd
- channel: unlink, unlinkat, openat, write
  name: auditd:SYSCALL
- channel: exec rm -rf|dd if=/dev|srm|file unlink
  name: macos:unifiedlog
- channel: unlink, unlinkat, rmdir
  name: auditd:SYSCALL
- channel: unlink, rename, open
  name: auditd:SYSCALL
- channel: EventCode=23
  name: linux:Sysmon
- channel: unlink, fs_delete
  name: fs:fsusage
- channel: container file operations
  name: docker:daemon
- channel: rm, clearlogs, logrotate
  name: esxi:hostd
- channel: Datastore file operations
  name: esxi:hostd
- channel: 'CREATE, DELETE, WRITE: Stored data manipulation attempts by unauthorized processes'
  name: macos:osquery
- channel: unlink/unlinkat
  name: auditd:SYSCALL
- channel: Windows Backup Catalog deletion or catalog corruption
  name: WinEventLog:Microsoft-Windows-Backup
- channel: /etc/fstab, /etc/systemd/*
  name: auditd:CONFIG_CHANGE
- channel: application deletes, alters, renames, relocates, or suppresses local artifacts relevant to detection, including
    files, hidden media, compromise markers, or app-local evidence, before later continued execution or transfer
  name: MobileEDR:telemetry
- channel: application deletes package files, cleanup artifacts, or app-local state immediately before disappearance from
    installed inventory or runtime
  name: MobileEDR:telemetry
- channel: application deletes, truncates, or removes user, operational, or evidence-bearing files after prior access or staging
    and before later continued execution or communication
  name: MobileEDR:telemetry
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '3.0'
```
