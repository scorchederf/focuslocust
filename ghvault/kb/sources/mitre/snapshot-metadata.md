---
parsed_by: focuslocust
source: mitre
type: generated
---
# Snapshot Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0062` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Snapshot Metadata](../../attack/data-sources/DC0062-snapshot-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0062 |
| name | Snapshot Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0062 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Contextual data about a snapshot, which may include information such as ID, type, and status
external_references:
- external_id: DC0062
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0062
id: x-mitre-data-component--8bc66f94-54a9-4be4-bdd1-fe90df643774
modified: '2025-10-21T15:14:40.482Z'
name: Snapshot Metadata
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: DescribeSnapshots
  name: AWS:CloudTrail
- channel: compute.disks.insert with sourceSnapshot parameter
  name: gcp:audit
- channel: CopySnapshot
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
