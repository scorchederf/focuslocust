---
parsed_by: focuslocust
source: mitre
type: generated
---
# Snapshot Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0057` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Snapshot Creation](../../attack/data-sources/DC0057-snapshot-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0057 |
| name | Snapshot Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0057 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The process of taking a point-in-time copy of a cloud storage volume (files, settings, configurations, etc.),
  virtual machine (VM), or database that can be created and deployed in cloud environments.
external_references:
- external_id: DC0057
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0057
id: x-mitre-data-component--3da222e6-53f3-451c-a239-0b405c009432
modified: '2025-11-12T22:03:39.105Z'
name: Snapshot Creation
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
- channel: snapshot create/write events
  name: esxi:vmkernel
- channel: CreateSnapshot
  name: AWS:CloudTrail
- channel: MICROSOFT.COMPUTE/SNAPSHOTS/WRITE
  name: azure:activity
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
