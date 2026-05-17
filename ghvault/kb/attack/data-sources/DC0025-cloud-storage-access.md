---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0025 - Cloud Storage Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0025` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud storage access refers to the retrieval or interaction with data stored in cloud infrastructure. This data component includes activities such as reading, downloading, or accessing files and objects within cloud storage systems. Common examples include API calls like GetObject in AWS S3, which retrieves objects from cloud buckets. Examples: 

- AWS S3 Access: An adversary uses the `GetObject` API to retrieve sensitive data from an AWS S3 bucket.
- Azure Blob Storage Access: A user accesses a blob in Azure Storage using `Get Blob` or `Get Blob Properties`.
- Google Cloud Storage Access: An adversary uses `storage.objects.get` to download objects from - OpenStack Swift Storage Access: A user retrieves an object from OpenStack Swift using the `GET` method.

## Source Verification

[source record](../../sources/mitre/cloud-storage-access.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud storage access refers to the retrieval or interaction with data stored in cloud infrastructure. This data\
\ component includes activities such as reading, downloading, or accessing files and objects within cloud storage systems.\
\ Common examples include API calls like GetObject in AWS S3, which retrieves objects from cloud buckets. Examples: \n\n\
- AWS S3 Access: An adversary uses the `GetObject` API to retrieve sensitive data from an AWS S3 bucket.\n- Azure Blob Storage\
\ Access: A user accesses a blob in Azure Storage using `Get Blob` or `Get Blob Properties`.\n- Google Cloud Storage Access:\
\ An adversary uses `storage.objects.get` to download objects from - OpenStack Swift Storage Access: A user retrieves an\
```
