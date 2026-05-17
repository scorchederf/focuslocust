---
parsed_by: focuslocust
source: mitre
type: generated
---
# Lifecycle-Triggered Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1485.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lifecycle-Triggered Deletion](../../attack/techniques/T1485.001-lifecycle-triggered-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1485.001 |
| name | Lifecycle-Triggered Deletion |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1485/001 |

## Preserved Source Material

```yaml
created: '2024-09-25T13:16:14.166Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within.\
  \  \n\nCloud storage buckets often allow users to set lifecycle policies to automate the migration, archival, or deletion\
  \ of objects after a set period of time.(Citation: AWS Storage Lifecycles)(Citation: GCP Storage Lifecycles)(Citation: Azure\
  \ Storage Lifecycles) If a threat actor has sufficient permissions to modify these policies, they may be able to delete\
  \ all objects at once. \n\nFor example, in AWS environments, an adversary with the `PutLifecycleConfiguration` permission\
  \ may use the `PutBucketLifecycle` API call to apply a lifecycle policy to an S3 bucket that deletes all objects in the\
  \ bucket after one day.(Citation: Palo Alto Cloud Ransomware)(Citation: Halcyon AWS Ransomware 2025) In addition to destroying\
  \ data for purposes of extortion and [Financial Theft](https://attack.mitre.org/techniques/T1657), adversaries may also\
  \ perform this action on buckets storing cloud logs for [Indicator Removal](https://attack.mitre.org/techniques/T1070).(Citation:\
  \ Datadog S3 Lifecycle CloudTrail Logs)"
external_references:
- external_id: T1485.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1485/001
- description: AWS. (n.d.). Managing the lifecycle of objects. Retrieved September 25, 2024.
  source_name: AWS Storage Lifecycles
  url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
- description: Google Cloud. (n.d.). Object Lifecycle Management. Retrieved September 25, 2024.
  source_name: GCP Storage Lifecycles
  url: https://cloud.google.com/storage/docs/lifecycle
- description: 'Halcyon RISE Team. (2025, January 13). Abusing AWS Native Services: Ransomware Encrypting S3 Buckets with
    SSE-C. Retrieved March 18, 2025.'
  source_name: Halcyon AWS Ransomware 2025
  url: https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c
- description: Microsoft Azure. (2024, July 3). Configure a lifecycle management policy. Retrieved September 25, 2024.
  source_name: Azure Storage Lifecycles
  url: https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure?tabs=azure-portal
- description: 'Ofir Balassiano and Ofir Shaty. (2023, November 29). Ransomware in the Cloud: Breaking Down the Attack Vectors.
    Retrieved September 25, 2024.'
  source_name: Palo Alto Cloud Ransomware
  url: https://www.paloaltonetworks.com/blog/prisma-cloud/ransomware-data-protection-cloud/
- description: Stratus Red Team. (n.d.). CloudTrail Logs Impairment Through S3 Lifecycle Rule. Retrieved September 25, 2024.
  source_name: Datadog S3 Lifecycle CloudTrail Logs
  url: https://stratus-red-team.cloud/attack-techniques/AWS/aws.defense-evasion.cloudtrail-lifecycle-rule/
id: attack-pattern--1001e0d6-ee09-4dfc-aa90-e9320ffc8fe4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-04-15T19:58:06.787Z'
name: Lifecycle-Triggered Deletion
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '1.1'
```
