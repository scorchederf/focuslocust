---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0058 - Snapshot Modification

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

## Summary

Changes made to a cloud snapshot's metadata, attributes, or control settings. These modifications may involve adjusting access permissions, changing retention policies, or altering encryption settings. 

*Data Collection Measures:*

- AWS CloudTrail
    - Tracks API calls such as `ModifySnapshotAttribute`, `ResetSnapshotAttribute`, and `ModifySnapshotTier`.
- Azure Monitor Logs
    - Logs changes via `Microsoft.Compute/snapshots/write`.
- Google Cloud Logging
    - Captures modifications through `compute.snapshots.setIamPolicy` and `compute.snapshots.patch`.

## Source Verification

[source record](../../sources/mitre/snapshot-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to a cloud snapshot's metadata, attributes, or control settings. These modifications may involve\
\ adjusting access permissions, changing retention policies, or altering encryption settings. \n\n*Data Collection Measures:*\n\
\n- AWS CloudTrail\n    - Tracks API calls such as `ModifySnapshotAttribute`, `ResetSnapshotAttribute`, and `ModifySnapshotTier`.\n\
- Azure Monitor Logs\n    - Logs changes via `Microsoft.Compute/snapshots/write`.\n- Google Cloud Logging\n    - Captures\
\ modifications through `compute.snapshots.setIamPolicy` and `compute.snapshots.patch`."
external_references:
```
