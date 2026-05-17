---
parsed_by: focuslocust
source: mitre
type: generated
---
# Volume Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0097` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Volume Creation](../../attack/data-sources/DC0097-volume-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0097 |
| name | Volume Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0097 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The initial provisioning of block storage volumes in cloud or on-prem environments, typically used for data storage,
  backup, or workload scaling.
external_references:
- external_id: DC0097
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0097
id: x-mitre-data-component--dad75cc7-5bae-4175-adb4-ca1962d8650e
modified: '2025-11-12T22:03:39.105Z'
name: Volume Creation
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
- channel: CreateVolume
  name: AWS:CloudTrail
- channel: Volume Shadow Copy Creation
  name: WinEventLog:Microsoft-Windows-VSS
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
