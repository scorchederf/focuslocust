---
parsed_by: focuslocust
source: mitre
type: generated
---
# Image Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0036` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Image Modification](../../attack/data-sources/DC0036-image-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0036 |
| name | Image Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0036 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Changes made to a virtual machine image, including setting and/or control data (ex: Azure Compute Service Images
  PATCH)'
external_references:
- external_id: DC0036
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0036
id: x-mitre-data-component--071a09b1-8945-46fd-8bb7-6bcc89400963
modified: '2025-10-21T15:14:40.151Z'
name: Image Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: push event of new image version from unrecognized user or context
  name: docker:registry
- channel: ModifyImageAttribute
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
