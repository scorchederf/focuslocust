---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0098 - Volume Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0098` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated storage and may result in data loss if not backed up.

*Data Collection Measures:*

- Cloud Logging & APIs
    - AWS CloudTrail Logs
        - `eventName: DeleteVolume` (tracks volume deletions)
    - Azure Monitor Logs
        - `operationName: Microsoft.Compute/disks/delete`
        - `status: Success | Failure` (flag unauthorized delete attempts)
    - Google Cloud Audit Logs
        - `protoPayload.methodName: "v1.compute.disks.delete"`
        - `authenticationInfo.principalEmail` (identifies the user deleting the volume)
- System & Host-Based Logging
    - Linux & macOS Logs:
        - `/var/log/syslog` or `/var/log/messages` for volume detach/deletion actions
    - Windows Event Logs:
        - Event ID 98 (Storage Class Memory)
        - Event ID 225 (Volume Removal Detected)
        - Event ID 12 (Disk Removal Notification)

## Source Verification

[source record](../../sources/mitre/volume-deletion.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated\
\ storage and may result in data loss if not backed up.\n\n*Data Collection Measures:*\n\n- Cloud Logging & APIs\n    -\
\ AWS CloudTrail Logs\n        - `eventName: DeleteVolume` (tracks volume deletions)\n    - Azure Monitor Logs\n       \
\ - `operationName: Microsoft.Compute/disks/delete`\n        - `status: Success | Failure` (flag unauthorized delete attempts)\n\
\    - Google Cloud Audit Logs\n        - `protoPayload.methodName: \"v1.compute.disks.delete\"`\n        - `authenticationInfo.principalEmail`\
\ (identifies the user deleting the volume)\n- System & Host-Based Logging\n    - Linux & macOS Logs:\n        - `/var/log/syslog`\
```
