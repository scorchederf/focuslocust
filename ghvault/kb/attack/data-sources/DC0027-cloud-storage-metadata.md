---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0027 - Cloud Storage Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0027` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud Storage Metadata provides contextual information about cloud storage infrastructure and its associated activity. This data may include attributes such as storage name, size, owner, permissions, creation date, region, and activity metadata. It is essential for monitoring, auditing, and identifying anomalies in cloud storage environments. Examples: 

- AWS S3 Bucket Metadata: Metadata about an S3 bucket includes the bucket name, region, creation date, owner, storage class, and permissions.
- Azure Blob Storage Metadata: Metadata for an Azure Blob container includes container name, access level (e.g., private or public), size, and tags.
- Google Cloud Storage Metadata: Metadata includes bucket name, storage class, location, labels, lifecycle policies, and versioning status.
- OpenStack Swift Metadata: Metadata for a Swift container includes name, access level, quota, and custom attributes.

## Source Verification

[source record](../../sources/mitre/cloud-storage-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud Storage Metadata provides contextual information about cloud storage infrastructure and its associated\
\ activity. This data may include attributes such as storage name, size, owner, permissions, creation date, region, and\
\ activity metadata. It is essential for monitoring, auditing, and identifying anomalies in cloud storage environments.\
\ Examples: \n\n- AWS S3 Bucket Metadata: Metadata about an S3 bucket includes the bucket name, region, creation date, owner,\
\ storage class, and permissions.\n- Azure Blob Storage Metadata: Metadata for an Azure Blob container includes container\
\ name, access level (e.g., private or public), size, and tags.\n- Google Cloud Storage Metadata: Metadata includes bucket\
```
