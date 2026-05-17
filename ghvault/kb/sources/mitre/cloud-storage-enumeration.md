---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Storage Enumeration

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

## Generated Concept Page

- [Cloud Storage Enumeration](../../attack/data-sources/DC0017-cloud-storage-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0017 |
| name | Cloud Storage Enumeration |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0017 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Cloud Storage Enumeration involves retrieving a list of available cloud storage infrastructure, such as buckets,
  containers, or objects, within a cloud environment. This activity may be performed for legitimate administrative purposes
  or malicious reconnaissance by adversaries seeking to identify accessible storage resources.Examples:


  - AWS S3 Bucket Enumeration: An AWS user lists all buckets using the `ListBuckets` API call.

  - Azure Blob Storage Container Enumeration: A user retrieves a list of all containers within a storage account using the
  Azure Storage SDK or API.

  - Google Cloud Storage Bucket Enumeration: A Google Cloud user lists all buckets within a project using the `storage.buckets.list`
  API.

  - OpenStack Swift Container Enumeration: A user retrieves a list of containers in OpenStack Swift using the `GET` method
  on the storage endpoint.'
external_references:
- external_id: DC0017
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0017
id: x-mitre-data-component--fcc4811f-9cc8-4db5-8097-4d8242a380de
modified: '2025-11-12T22:03:39.105Z'
name: Cloud Storage Enumeration
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
- channel: ListBuckets
  name: AWS:CloudTrail
- channel: ListObjectsV2
  name: AWS:CloudTrail
- channel: List Blobs
  name: azure:activity
- channel: storage.objects.list
  name: gcp:storage
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
