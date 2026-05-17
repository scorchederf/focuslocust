---
parsed_by: focuslocust
source: mitre
type: generated
---
# Snapshot Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0058` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Snapshot Modification](../../attack/data-sources/DC0058-snapshot-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0058 |
| name | Snapshot Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0058 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to a cloud snapshot's metadata, attributes, or control settings. These modifications may involve\
  \ adjusting access permissions, changing retention policies, or altering encryption settings. \n\n*Data Collection Measures:*\n\
  \n- AWS CloudTrail\n    - Tracks API calls such as `ModifySnapshotAttribute`, `ResetSnapshotAttribute`, and `ModifySnapshotTier`.\n\
  - Azure Monitor Logs\n    - Logs changes via `Microsoft.Compute/snapshots/write`.\n- Google Cloud Logging\n    - Captures\
  \ modifications through `compute.snapshots.setIamPolicy` and `compute.snapshots.patch`."
external_references:
- external_id: DC0058
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0058
id: x-mitre-data-component--f1eb6ea9-f3ab-414f-af35-2d5427199984
modified: '2025-10-21T15:14:39.957Z'
name: Snapshot Modification
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
- channel: ModifySnapshotAttribute
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
