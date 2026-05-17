---
parsed_by: focuslocust
source: mitre
type: generated
---
# Scheduled Job Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0012` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Scheduled Job Modification](../../attack/data-sources/DC0012-scheduled-job-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0012 |
| name | Scheduled Job Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0012 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Changes made to an existing scheduled job, including modifications to its execution parameters, command payload,
  or execution timing.
external_references:
- external_id: DC0012
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0012
id: x-mitre-data-component--faa34cf6-cf32-4dc9-bd6a-8f7a606ff65b
modified: '2025-10-21T15:14:38.292Z'
name: Scheduled Job Modification
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
  name: Scheduled Job
- channel: /var/log/audit/audit.log
  name: auditd:CONFIG_CHANGE
- channel: Remove-InboxRule, Clear-Mailbox
  name: m365:exchange
- channel: EventCode=4702
  name: WinEventLog:Security
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
