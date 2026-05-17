---
parsed_by: focuslocust
source: mitre
type: generated
---
# WMI Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0008` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WMI Creation](../../attack/data-sources/DC0008-wmi-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0008 |
| name | WMI Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0008 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Initial construction of a WMI object, such as a filter, consumer, subscription, binding, or providers.
external_references:
- external_id: DC0008
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0008
id: x-mitre-data-component--05645013-2fed-4066-8bdc-626b2e201dd4
modified: '2025-11-12T22:03:39.105Z'
name: WMI Creation
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
- channel: Creation or modification of __EventFilter, __FilterToConsumerBinding, or CommandLineEventConsumer
  name: WinEventLog:WMI
- channel: EventCode=5857, 5858, 5860, 5861
  name: WinEventLog:WMI
- channel: WMI Object Creation Events
  name: WinEventLog:Application
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
