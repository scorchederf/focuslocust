---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0049 - Snapshot Deletion

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

## Summary

The removal of a point-in-time backup of a cloud storage volume, virtual machine (VM), or database.

*Data Collection Measures:*

- AWS CloudTrail
    - Logs `DeleteSnapshot` API calls in EC2, RDS, and EBS services.
- Azure Monitor Logs
    - Tracks snapshot deletions via `Microsoft.Compute/snapshots/delete` API calls.
- Google Cloud Logging
    - Detects snapshot removal through `compute.disks.deleteSnapshot` events.

## Source Verification

[source record](../../sources/mitre/snapshot-deletion.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The removal of a point-in-time backup of a cloud storage volume, virtual machine (VM), or database.\n\n*Data\
\ Collection Measures:*\n\n- AWS CloudTrail\n    - Logs `DeleteSnapshot` API calls in EC2, RDS, and EBS services.\n- Azure\
\ Monitor Logs\n    - Tracks snapshot deletions via `Microsoft.Compute/snapshots/delete` API calls.\n- Google Cloud Logging\n\
\    - Detects snapshot removal through `compute.disks.deleteSnapshot` events."
external_references:
- external_id: DC0049
```
