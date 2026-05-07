---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0099
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0099-group-enumeration
---

## Description

Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may exploit high-privilege groups or misconfigurations. Examples:<br><br>- AWS CLI: `aws iam list-groups`<br>- PowerShell: `Get-ADGroup -Filter *`<br>- (Saas) Google Workspace: Admin SDK Directory API<br>- Azure: `Get-AzureADGroup`<br>- Microsoft 365:  Graph API `GET  Collection Measures:*<br><br>- Cloud Logging: Enable AWS CloudTrail, Azure Activity Logs, and Google Workspace Admin Logs for group-related actions.<br>- Directory Monitoring: Track logs like AD Event ID 4662 (object operations).<br>- API Monitoring: Log API activity like AWS IAM queries.<br>- SaaS Monitoring: Use platform logs (e.g., Office 365 Unified Audit Logs).<br>- SIEM Integration: Centralize group query tracking.
