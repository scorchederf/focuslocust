---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Storage Object Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1619` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Storage Object Discovery](../../attack/techniques/T1619-cloud-storage-object-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1619 |
| name | Cloud Storage Object Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1619 |

## Preserved Source Material

```yaml
created: '2021-10-01T17:58:26.445Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during
  automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar
  to [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) on a local host, after identifying available
  storage services (i.e. [Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580)) adversaries may access
  the contents/objects stored in cloud infrastructure.


  Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2
  in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .'
external_references:
- external_id: T1619
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1619
- description: Amazon - ListObjectsV2. Retrieved October 4, 2021.
  source_name: ListObjectsV2
  url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html
- description: Microsoft - List Blobs. (n.d.). Retrieved October 4, 2021.
  source_name: List Blobs
  url: https://docs.microsoft.com/en-us/rest/api/storageservices/list-blobs
id: attack-pattern--8565825b-21c8-4518-b75e-cbc4c717a156
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:03.853Z'
name: Cloud Storage Object Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Regina Elwell
- Isif Ibrahima, Mandiant
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '1.0'
```
