---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0099 - Group Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0099` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may exploit high-privilege groups or misconfigurations. Examples:

- AWS CLI: `aws iam list-groups`
- PowerShell: `Get-ADGroup -Filter *`
- (Saas) Google Workspace: Admin SDK Directory API
- Azure: `Get-AzureADGroup`
- Microsoft 365:  Graph API `GET https://graph.microsoft.com/v1.0/groups`

*Data Collection Measures:*

- Cloud Logging: Enable AWS CloudTrail, Azure Activity Logs, and Google Workspace Admin Logs for group-related actions.
- Directory Monitoring: Track logs like AD Event ID 4662 (object operations).
- API Monitoring: Log API activity like AWS IAM queries.
- SaaS Monitoring: Use platform logs (e.g., Office 365 Unified Audit Logs).
- SIEM Integration: Centralize group query tracking.

## Source Verification

[source record](../../sources/mitre/group-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may
exploit high-privilege groups or misconfigurations. Examples:
- AWS CLI: `aws iam list-groups`
- PowerShell: `Get-ADGroup -Filter *`
- (Saas) Google Workspace: Admin SDK Directory API
- Azure: `Get-AzureADGroup`
```
