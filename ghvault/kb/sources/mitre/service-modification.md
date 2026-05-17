---
parsed_by: focuslocust
source: mitre
type: generated
---
# Service Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0065` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Service Modification](../../attack/data-sources/DC0065-service-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0065 |
| name | Service Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0065 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Changes made to an existing service or daemon, such as modifying the service name, start type, execution parameters,
  or security configurations.
external_references:
- external_id: DC0065
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0065
id: x-mitre-data-component--66531bc6-a509-4868-8314-4d599e91d222
modified: '2026-04-20T18:21:23.994Z'
name: Service Modification
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
- channel: service state change
  name: esxi:hostd
- channel: None
  name: Service
- channel: Module or ISAPI filter registration events
  name: WinEventLog:Microsoft-IIS-Configuration
- channel: EventCode=7040
  name: WinEventLog:System
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
