---
parsed_by: focuslocust
source: mitre
type: generated
---
# Snapshot Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0047` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Snapshot Enumeration](../../attack/data-sources/DC0047-snapshot-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0047 |
| name | Snapshot Enumeration |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0047 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The process of listing or retrieving metadata about existing snapshots in a cloud environment.\n\n*Data Collection\
  \ Measures:*\n\n- AWS CloudTrail\n    - Logs API calls such as `DescribeSnapshots`, `ListSnapshots`, and `GetSnapshotAttributes`.\n\
  - Azure Monitor Logs\n    - Tracks snapshot enumeration via `Microsoft.Compute/snapshots/read`.\n- Google Cloud Logging\n\
  \    - Detects snapshot listing through `compute.disks.listSnapshots`.\n"
external_references:
- external_id: DC0047
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0047
id: x-mitre-data-component--ffd73905-2e51-4f2d-8549-e72fb0eb6c38
modified: '2025-10-21T15:10:28.402Z'
name: Snapshot Enumeration
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
