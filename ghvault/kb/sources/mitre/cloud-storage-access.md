---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Storage Access

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

## Generated Concept Page

- [Cloud Storage Access](../../attack/data-sources/DC0025-cloud-storage-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0025 |
| name | Cloud Storage Access |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0025 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud storage access refers to the retrieval or interaction with data stored in cloud infrastructure. This data\
  \ component includes activities such as reading, downloading, or accessing files and objects within cloud storage systems.\
  \ Common examples include API calls like GetObject in AWS S3, which retrieves objects from cloud buckets. Examples: \n\n\
  - AWS S3 Access: An adversary uses the `GetObject` API to retrieve sensitive data from an AWS S3 bucket.\n- Azure Blob Storage\
  \ Access: A user accesses a blob in Azure Storage using `Get Blob` or `Get Blob Properties`.\n- Google Cloud Storage Access:\
  \ An adversary uses `storage.objects.get` to download objects from - OpenStack Swift Storage Access: A user retrieves an\
  \ object from OpenStack Swift using the `GET` method."
external_references:
- external_id: DC0025
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0025
id: x-mitre-data-component--58ef998c-f3bf-4985-b487-b1005f5c05d1
modified: '2025-11-12T22:03:39.105Z'
name: Cloud Storage Access
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
- channel: GetObject, CopyObject
  name: AWS:CloudTrail
- channel: 'PutObject: S3 writes with .sql/.csv extension by same identity or within 5 min of DB access'
  name: AWS:CloudTrail
- channel: Accessed SharePoint files or pages
  name: m365:unified
- channel: FileAccessed, FileDownloaded, ConsentGranted
  name: m365:unified
- channel: download, authorization_grant
  name: gcp:workspaceaudit
- channel: AnonymousLinkCreated, FileDownloaded
  name: m365:sharepoint
- channel: App-only or delegated access patterns where client_id != known enterprise apps
  name: m365:unified
- channel: Artifact generated includes base64/encoded exfil payload or URL
  name: saas:github
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
