---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0023 - Cloud Storage Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0023` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud Storage Modification involves tracking changes made to cloud storage infrastructure, including updates to settings, permissions, or stored data. Examples include modifying object access control lists (ACLs), uploading new objects, or updating bucket policies. Examples: 

AWS S3: An object is uploaded or its ACL is modified.
- Azure Blob Storage: A blob's metadata or permissions are updated.
- Google Cloud Storage: An object's lifecycle policy is updated, or a bucket policy is changed.
- OpenStack Swift: Modifications to container settings or uploading of new objects.

## Source Verification

[source record](../../sources/mitre/cloud-storage-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud Storage Modification involves tracking changes made to cloud storage infrastructure, including updates\
\ to settings, permissions, or stored data. Examples include modifying object access control lists (ACLs), uploading new\
\ objects, or updating bucket policies. Examples: \n\nAWS S3: An object is uploaded or its ACL is modified.\n- Azure Blob\
\ Storage: A blob's metadata or permissions are updated.\n- Google Cloud Storage: An object's lifecycle policy is updated,\
\ or a bucket policy is changed.\n- OpenStack Swift: Modifications to container settings or uploading of new objects."
external_references:
```
