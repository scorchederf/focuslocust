---
parsed_by: focuslocust
source: mitre
type: generated
---
# Group Enumeration

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

## Generated Concept Page

- [Group Enumeration](../../attack/data-sources/DC0099-group-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0099 |
| name | Group Enumeration |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0099 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may
  exploit high-privilege groups or misconfigurations. Examples:


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

  - SIEM Integration: Centralize group query tracking.'
external_references:
- external_id: DC0099
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0099
id: x-mitre-data-component--8e44412e-3238-4d64-8878-4f11e27784fe
modified: '2026-03-13T22:21:38.311Z'
name: Group Enumeration
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
- channel: ListGroups, ListAttachedRolePolicies
  name: AWS:CloudTrail
- channel: az ad user get-member-groups, Get-AzRoleAssignment
  name: azure:audit
- channel: cloudidentity.groups.list
  name: gcp:audit
- channel: GET /services/data/vXX.X/groups
  name: saas:salesforce
- channel: GET /orgs/:org/teams, GET /teams/:team/members
  name: saas:github
- channel: EventCode=4798, 4799
  name: WinEventLog:Security
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
