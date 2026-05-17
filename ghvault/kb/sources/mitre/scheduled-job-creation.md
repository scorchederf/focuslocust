---
parsed_by: focuslocust
source: mitre
type: generated
---
# Scheduled Job Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Scheduled Job Creation](../../attack/data-sources/DC0001-scheduled-job-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0001 |
| name | Scheduled Job Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0001 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The establishment of a task or job that will execute at a predefined time or based on specific triggers.
external_references:
- external_id: DC0001
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0001
id: x-mitre-data-component--f42df6f0-6395-4f0c-9376-525a031f00c3
modified: '2026-04-09T17:05:23.355Z'
name: Scheduled Job Creation
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
  name: Scheduled Job
- channel: EventCode=4698
  name: WinEventLog:Security
- channel: Execution of non-standard script or binary by cron
  name: linux:syslog
- channel: EventCode=106
  name: WinEventLog:TaskScheduler
- channel: crontab, systemd_timers
  name: linux:osquery
- channel: launchd_jobs
  name: macos:osquery
- channel: Startup script and task execution logs
  name: esxi:vmkernel
- channel: verb=create, resource=cronjobs, group=batch
  name: kubernetes:apiserver
- channel: file_events
  name: linux:osquery
- channel: 'process: crontab edits, launch of cron job'
  name: macos:unifiedlog
- channel: file_events - cron, launchd
  name: macos:osquery
- channel: execution of scheduled job
  name: esxi:cron
- channel: task creation events
  name: esxi:hostd
- channel: cron/launchd
  name: macos:cron
- channel: EventCode=4699
  name: WinEventLog:Security
- channel: Scheduled execution of unknown or unusual script/binary
  name: linux:cron
- channel: Scheduled task execution creates cache, staged payload, local output, or collected data artifact immediately after
    wake or job trigger
  name: MobiledEDR:telemetry
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '3.0'
```
