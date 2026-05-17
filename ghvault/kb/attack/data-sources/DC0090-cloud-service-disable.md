---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0090 - Cloud Service Disable

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

## Summary

This data component refers to monitoring actions that deactivate or stop a cloud service in a cloud control plane. Examples include disabling essential logging services like AWS CloudTrail (`StopLogging` API call), Microsoft Azure Monitor Logs, or Google Cloud's Operations Suite (formerly Stackdriver). Disabling such services can hinder visibility into adversary activities within the cloud environment. Examples: 

- AWS CloudTrail StopLogging: This action stops logging of API activity for a particular trail, effectively reducing the monitoring and visibility of AWS resources and activities.
- Microsoft Azure Monitor Logs: Disabling these logs hinders the organization’s ability to detect anomalous activities and trace malicious actions.
- Google Cloud Logging: Disabling cloud logging removes visibility into resource activity, preventing monitoring of service access or configuration changes.
- SaaS Applications: Stopping logging removes visibility into user activities, such as email access or file downloads, enabling undetected malicious behavior.

## Source Verification

[source record](../../sources/mitre/cloud-service-disable.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "This data component refers to monitoring actions that deactivate or stop a cloud service in a cloud control\
\ plane. Examples include disabling essential logging services like AWS CloudTrail (`StopLogging` API call), Microsoft Azure\
\ Monitor Logs, or Google Cloud's Operations Suite (formerly Stackdriver). Disabling such services can hinder visibility\
\ into adversary activities within the cloud environment. Examples: \n\n- AWS CloudTrail StopLogging: This action stops\
\ logging of API activity for a particular trail, effectively reducing the monitoring and visibility of AWS resources and\
\ activities.\n- Microsoft Azure Monitor Logs: Disabling these logs hinders the organization’s ability to detect anomalous\
```
