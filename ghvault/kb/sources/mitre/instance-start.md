---
parsed_by: focuslocust
source: mitre
type: generated
---
# Instance Start

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0080` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Instance Start](../../attack/data-sources/DC0080-instance-start.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0080 |
| name | Instance Start |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0080 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The initiation or activation of a virtual machine instance within a cloud infrastructure. This action typically\
  \ involves starting an existing instance that had been stopped or paused, allowing it to resume operation. Examples: \n\n\
  - Google Cloud Platform (GCP): Starting an instance through `instance.start` API activity.\n- AWS: Logging of `StartInstances`\
  \ in AWS CloudTrail for EC2 instances.\n- Azure: `Microsoft.Compute/virtualMachines/start` entries indicate a VM instance\
  \ being started."
external_references:
- external_id: DC0080
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0080
id: x-mitre-data-component--f8213cde-6b3a-420d-9ab7-41c9af1a919f
modified: '2025-11-12T22:03:39.105Z'
name: Instance Start
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
- channel: StartInstances
  name: AWS:CloudTrail
- channel: RunInstances
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
