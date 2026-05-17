---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0047 - Snapshot Enumeration

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

## Summary

The process of listing or retrieving metadata about existing snapshots in a cloud environment.

*Data Collection Measures:*

- AWS CloudTrail
    - Logs API calls such as `DescribeSnapshots`, `ListSnapshots`, and `GetSnapshotAttributes`.
- Azure Monitor Logs
    - Tracks snapshot enumeration via `Microsoft.Compute/snapshots/read`.
- Google Cloud Logging
    - Detects snapshot listing through `compute.disks.listSnapshots`.

## Source Verification

[source record](../../sources/mitre/snapshot-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The process of listing or retrieving metadata about existing snapshots in a cloud environment.\n\n*Data Collection\
\ Measures:*\n\n- AWS CloudTrail\n    - Logs API calls such as `DescribeSnapshots`, `ListSnapshots`, and `GetSnapshotAttributes`.\n\
- Azure Monitor Logs\n    - Tracks snapshot enumeration via `Microsoft.Compute/snapshots/read`.\n- Google Cloud Logging\n\
\    - Detects snapshot listing through `compute.disks.listSnapshots`.\n"
external_references:
- external_id: DC0047
```
