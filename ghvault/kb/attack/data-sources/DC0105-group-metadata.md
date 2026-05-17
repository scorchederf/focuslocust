---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0105 - Group Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0105` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Group metadata includes attributes like name, permissions, purpose, and associated user accounts or roles, which adversaries may exploit for privilege escalation. Examples:

- Active Directory: `Get-ADGroup -Identity "Domain Admins" -Properties Members, Description`
- Azure AD: `Get-AzureADGroup -ObjectId <GroupId>`
- Google Workspace: `GET https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>`
- AWS IAM: `aws iam list-group-policies --group-name <group_name>`
- Office 365: `GET https://graph.microsoft.com/v1.0/groups/<id>`

*Data Collection Measures:*

- Cloud Logging:
    - AWS CloudTrail for IAM group-related activities.
    - Azure AD Sign-In/Audit logs for metadata changes.
    - Google Admin Activity logs for API calls.
- Directory Logging: Log metadata access (e.g., Windows Event ID 4662).
- API Monitoring: Log API calls to modify group metadata (e.g., Microsoft Graph API).
- SIEM Integration: Centralize group metadata logs for analysis.

## Source Verification

[source record](../../sources/mitre/group-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Group metadata includes attributes like name, permissions, purpose, and associated user accounts or roles, which\
\ adversaries may exploit for privilege escalation. Examples:\n\n- Active Directory: `Get-ADGroup -Identity \"Domain Admins\"\
\ -Properties Members, Description`\n- Azure AD: `Get-AzureADGroup -ObjectId <GroupId>`\n- Google Workspace: `GET https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>`\n\
- AWS IAM: `aws iam list-group-policies --group-name <group_name>`\n- Office 365: `GET https://graph.microsoft.com/v1.0/groups/<id>`\n\
\n*Data Collection Measures:*\n\n- Cloud Logging:\n    - AWS CloudTrail for IAM group-related activities.\n    - Azure AD\
\ Sign-In/Audit logs for metadata changes.\n    - Google Admin Activity logs for API calls.\n- Directory Logging: Log metadata\
```
