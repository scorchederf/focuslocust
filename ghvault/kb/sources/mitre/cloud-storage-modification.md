---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Storage Modification

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

## Generated Concept Page

- [Cloud Storage Modification](../../attack/data-sources/DC0023-cloud-storage-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0023 |
| name | Cloud Storage Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0023 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud Storage Modification involves tracking changes made to cloud storage infrastructure, including updates\
  \ to settings, permissions, or stored data. Examples include modifying object access control lists (ACLs), uploading new\
  \ objects, or updating bucket policies. Examples: \n\nAWS S3: An object is uploaded or its ACL is modified.\n- Azure Blob\
  \ Storage: A blob's metadata or permissions are updated.\n- Google Cloud Storage: An object's lifecycle policy is updated,\
  \ or a bucket policy is changed.\n- OpenStack Swift: Modifications to container settings or uploading of new objects."
external_references:
- external_id: DC0023
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0023
id: x-mitre-data-component--45977f14-1bcc-4ec4-ac14-a30fd3a11f44
modified: '2025-11-12T22:03:39.105Z'
name: Cloud Storage Modification
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
- channel: PutBucketLifecycle, PutLifecycleConfiguration, SetBucketLifecycle, storage.buckets.update
  name: AWS:CloudTrail
- channel: PutObject (with SSE-C), UploadPart (SSE-C)
  name: AWS:CloudTrail
- channel: PutBucketPolicy
  name: AWS:CloudTrail
- channel: SharingSet
  name: m365:unified
- channel: drive.permission.add
  name: saas:googledrive
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
