---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0017 - Cloud Storage Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0017` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud Storage Enumeration involves retrieving a list of available cloud storage infrastructure, such as buckets, containers, or objects, within a cloud environment. This activity may be performed for legitimate administrative purposes or malicious reconnaissance by adversaries seeking to identify accessible storage resources.Examples:

- AWS S3 Bucket Enumeration: An AWS user lists all buckets using the `ListBuckets` API call.
- Azure Blob Storage Container Enumeration: A user retrieves a list of all containers within a storage account using the Azure Storage SDK or API.
- Google Cloud Storage Bucket Enumeration: A Google Cloud user lists all buckets within a project using the `storage.buckets.list` API.
- OpenStack Swift Container Enumeration: A user retrieves a list of containers in OpenStack Swift using the `GET` method on the storage endpoint.

## Source Verification

[source record](../../sources/mitre/cloud-storage-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Cloud Storage Enumeration involves retrieving a list of available cloud storage infrastructure, such as buckets,
containers, or objects, within a cloud environment. This activity may be performed for legitimate administrative purposes
or malicious reconnaissance by adversaries seeking to identify accessible storage resources.Examples:
- AWS S3 Bucket Enumeration: An AWS user lists all buckets using the `ListBuckets` API call.
- Azure Blob Storage Container Enumeration: A user retrieves a list of all containers within a storage account using the
Azure Storage SDK or API.
```
