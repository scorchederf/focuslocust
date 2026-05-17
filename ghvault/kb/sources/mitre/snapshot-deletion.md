---
parsed_by: focuslocust
source: mitre
type: generated
---
# Snapshot Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0049` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Snapshot Deletion](../../attack/data-sources/DC0049-snapshot-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0049 |
| name | Snapshot Deletion |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0049 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The removal of a point-in-time backup of a cloud storage volume, virtual machine (VM), or database.\n\n*Data\
  \ Collection Measures:*\n\n- AWS CloudTrail\n    - Logs `DeleteSnapshot` API calls in EC2, RDS, and EBS services.\n- Azure\
  \ Monitor Logs\n    - Tracks snapshot deletions via `Microsoft.Compute/snapshots/delete` API calls.\n- Google Cloud Logging\n\
  \    - Detects snapshot removal through `compute.disks.deleteSnapshot` events."
external_references:
- external_id: DC0049
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0049
id: x-mitre-data-component--16e07530-764b-4d83-bae0-cdbfc31bf21d
modified: '2025-10-21T15:14:39.893Z'
name: Snapshot Deletion
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
- channel: DeleteSnapshot
  name: AWS:CloudTrail
- channel: snapshot.removeall or snapshot file deletion
  name: esxi:hostd
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
