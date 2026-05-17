---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Storage Metadata

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

## Generated Concept Page

- [Cloud Storage Metadata](../../attack/data-sources/DC0027-cloud-storage-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0027 |
| name | Cloud Storage Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0027 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud Storage Metadata provides contextual information about cloud storage infrastructure and its associated\
  \ activity. This data may include attributes such as storage name, size, owner, permissions, creation date, region, and\
  \ activity metadata. It is essential for monitoring, auditing, and identifying anomalies in cloud storage environments.\
  \ Examples: \n\n- AWS S3 Bucket Metadata: Metadata about an S3 bucket includes the bucket name, region, creation date, owner,\
  \ storage class, and permissions.\n- Azure Blob Storage Metadata: Metadata for an Azure Blob container includes container\
  \ name, access level (e.g., private or public), size, and tags.\n- Google Cloud Storage Metadata: Metadata includes bucket\
  \ name, storage class, location, labels, lifecycle policies, and versioning status.\n- OpenStack Swift Metadata: Metadata\
  \ for a Swift container includes name, access level, quota, and custom attributes."
external_references:
- external_id: DC0027
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0027
id: x-mitre-data-component--e214eb6d-de8f-4154-9015-6d47915fbed1
modified: '2025-11-12T22:03:39.105Z'
name: Cloud Storage Metadata
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
- channel: Post-authentication metadata enumeration from GUI session
  name: AWS:CloudTrail
- channel: AnonymousLinkCreated
  name: m365:unified
- channel: collaboration.invite
  name: saas:box
- channel: Shared link created to external account
  name: saas:dropbox
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
