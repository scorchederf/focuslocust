---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Storage Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0022` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Storage Deletion](../../attack/data-sources/DC0022-cloud-storage-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0022 |
| name | Cloud Storage Deletion |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0022 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud Storage Deletion refers to the removal or destruction of cloud storage infrastructure, such as buckets,\
  \ containers, or directories, within a cloud environment. Monitoring this activity is critical to detecting potential unauthorized\
  \ or malicious actions, such as data destruction by adversaries or accidental deletions that may lead to data loss. Examples:\
  \ \n\n- AWS S3 Bucket Deletion: An AWS user deletes an S3 bucket using the `DeleteBucket` API call.\n- Azure Blob Storage\
  \ Container Deletion: A user deletes a container in Azure Blob Storage using the `Delete Container` operation.\n- Google\
  \ Cloud Storage Bucket Deletion: A Google Cloud user deletes a bucket using the `storage.buckets.delete` API.\n- OpenStack\
  \ Swift Container Deletion: A user deletes a container in OpenStack Swift using the `DELETE` method.\n\nThis data component\
  \ can be collected through the following measures:\n\nEnable Logging for Cloud Storage Services\n\n- AWS S3: Enable AWS\
  \ CloudTrail to log DeleteBucket API actions.\n- Azure Blob Storage: Enable Azure Monitor and Diagnostic Logs to capture\
  \ Delete Container operations. Use Azure Event Grid to capture and trigger alerts for container deletion.\n- Google Cloud\
  \ Storage: Enable Data Access logs in Cloud Audit Logs to monitor storage.buckets.delete API calls.\n- OpenStack Swift:\
  \ Configure Swift logging to capture DELETE requests for containers.\n\nCentralized Logging and Analysis\n\n- Use platforms\
  \ like Splunk or native SIEMs to forward and analyze logs for anomalies in cloud storage deletions."
external_references:
- external_id: DC0022
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0022
id: x-mitre-data-component--4c41e296-b8d2-4a37-b789-eb565c87c00c
modified: '2025-11-12T22:03:39.105Z'
name: Cloud Storage Deletion
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
- channel: DeleteBucket, DeleteDBCluster, DeleteSnapshot, TerminateInstances
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
