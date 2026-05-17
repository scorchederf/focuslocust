---
parsed_by: focuslocust
source: mitre
type: generated
---
# Scheduled Job Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Scheduled Job Metadata](../../attack/data-sources/DC0005-scheduled-job-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0005 |
| name | Scheduled Job Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0005 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Contextual data about a scheduled job, which may include information such as name, timing, command(s), etc.
external_references:
- external_id: DC0005
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0005
id: x-mitre-data-component--7b375092-3a61-448d-900a-77c9a4bde4dc
modified: '2025-11-12T22:03:39.105Z'
name: Scheduled Job Metadata
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
- ics-attack
x_mitre_log_sources:
- channel: None
  name: Scheduled Job
- channel: cron activity
  name: linux:cron
- channel: /Library/LaunchDaemons/*.plist, ~/Library/LaunchAgents/*.plist
  name: fs:fileevents
- channel: Task registration/execution shortly after a time discovery event
  name: WinEventLog:TaskScheduler
- channel: New/modified launchd plist (persistence/scheduling) within TimeWindow after time query
  name: macos:unifiedlog
- channel: /var/log/vpxa.log task invocations tied to time configuration
  name: esxi:syslog
- channel: EventCode=106, 200
  name: WinEventLog:System
- channel: launchd.plist and logs
  name: macos:launchd
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
