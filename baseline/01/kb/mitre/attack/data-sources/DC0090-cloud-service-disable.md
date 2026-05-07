---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0090
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0090-cloud-service-disable
---

## Description

This data component refers to monitoring actions that deactivate or stop a cloud service in a cloud control plane. Examples include disabling essential logging services like AWS CloudTrail (`StopLogging` API call), Microsoft Azure Monitor Logs, or Google Cloud's Operations Suite (formerly Stackdriver). Disabling such services can hinder visibility into adversary activities within the cloud environment. Examples: <br><br>- AWS CloudTrail StopLogging: This action stops logging of API activity for a particular trail, effectively reducing the monitoring and visibility of AWS resources and activities.<br>- Microsoft Azure Monitor Logs: Disabling these logs hinders the organization’s ability to detect anomalous activities and trace malicious actions.<br>- Google Cloud Logging: Disabling cloud logging removes visibility into resource activity, preventing monitoring of service access or configuration changes.<br>- SaaS Applications: Stopping logging removes visibility into user activities, such as email access or file downloads, enabling undetected malicious behavior.
