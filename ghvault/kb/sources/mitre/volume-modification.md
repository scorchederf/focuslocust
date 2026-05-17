---
parsed_by: focuslocust
source: mitre
type: generated
---
# Volume Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0092` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Volume Modification](../../attack/data-sources/DC0092-volume-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0092 |
| name | Volume Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0092 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Changes made to a cloud volume, including its settings and control data (ex: AWS modify-volume)'
external_references:
- external_id: DC0092
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0092
id: x-mitre-data-component--d46272ce-a0fe-4256-855e-738de7bb63ee
modified: '2025-10-21T15:14:39.109Z'
name: Volume Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: Pod spec with hostPath or privileged securityContext
  name: kubernetes:apiserver
- channel: ModifyVolume
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
