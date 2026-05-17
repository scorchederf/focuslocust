---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0024 - Cloud Storage Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0024` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud Storage Creation refers to the initial creation of a new cloud storage resource, such as buckets, containers, or directories, within a cloud environment. This action is critical to track as it might indicate the legitimate provisioning of resources or unauthorized actions taken by adversaries to stage, store, or exfiltrate data. Examples: 

- AWS S3 Bucket Creation: An AWS user creates a new S3 bucket using the `CreateBucket` API call.
- Azure Blob Storage Container Creation: A user creates a new container in Azure Blob Storage using the `Create Container` operation.
- Google Cloud Storage Bucket Creation: A Google Cloud user creates a new bucket using `storage.buckets.create`.
- OpenStack Swift Container Creation: A user creates a new container in OpenStack Swift using the `PUT` method.

## Source Verification

[source record](../../sources/mitre/cloud-storage-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud Storage Creation refers to the initial creation of a new cloud storage resource, such as buckets, containers,\
\ or directories, within a cloud environment. This action is critical to track as it might indicate the legitimate provisioning\
\ of resources or unauthorized actions taken by adversaries to stage, store, or exfiltrate data. Examples: \n\n- AWS S3\
\ Bucket Creation: An AWS user creates a new S3 bucket using the `CreateBucket` API call.\n- Azure Blob Storage Container\
\ Creation: A user creates a new container in Azure Blob Storage using the `Create Container` operation.\n- Google Cloud\
\ Storage Bucket Creation: A Google Cloud user creates a new bucket using `storage.buckets.create`.\n- OpenStack Swift Container\
```
