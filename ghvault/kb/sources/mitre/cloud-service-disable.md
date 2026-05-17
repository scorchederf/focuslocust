---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Service Disable

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0090` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Service Disable](../../attack/data-sources/DC0090-cloud-service-disable.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0090 |
| name | Cloud Service Disable |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0090 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "This data component refers to monitoring actions that deactivate or stop a cloud service in a cloud control\
  \ plane. Examples include disabling essential logging services like AWS CloudTrail (`StopLogging` API call), Microsoft Azure\
  \ Monitor Logs, or Google Cloud's Operations Suite (formerly Stackdriver). Disabling such services can hinder visibility\
  \ into adversary activities within the cloud environment. Examples: \n\n- AWS CloudTrail StopLogging: This action stops\
  \ logging of API activity for a particular trail, effectively reducing the monitoring and visibility of AWS resources and\
  \ activities.\n- Microsoft Azure Monitor Logs: Disabling these logs hinders the organization’s ability to detect anomalous\
  \ activities and trace malicious actions.\n- Google Cloud Logging: Disabling cloud logging removes visibility into resource\
  \ activity, preventing monitoring of service access or configuration changes.\n- SaaS Applications: Stopping logging removes\
  \ visibility into user activities, such as email access or file downloads, enabling undetected malicious behavior."
external_references:
- external_id: DC0090
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0090
id: x-mitre-data-component--ec0612c5-2644-4c50-bcac-82586974fedd
modified: '2025-11-12T22:03:39.105Z'
name: Cloud Service Disable
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
- channel: Stop logging for an existing CloudTrail
  name: AWS:CloudTrail
- channel: Removal of CloudTrail trail
  name: AWS:CloudTrail
- channel: az monitor diagnostic-settings delete
  name: azure:activity
- channel: Log export integration removed or disabled
  name: saas:audit
- channel: StopLogging, DeleteTrail, or DisableSecurityService
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
