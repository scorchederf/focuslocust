---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0094 - Group Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0094` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup). Examples: 

- Active Directory:
    - Event ID 4728: Member added to a global group.
    - Event ID 4732: Member added to a local group.
- Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName "New Name"`
- AWS IAM: `aws iam update-group --group-name <GroupName> --new-path "/admin/"`
- Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>`
- Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>`

*Data Collection Measures:*

- Directory Logging:
    - Windows: Log EIDs 4728 (add), 4729 (remove).
    - Azure AD: Enable "Audit logs."
    - Google Workspace: Enable Admin Activity logs.
    - Office 365: Use Unified Audit Logs.
- Cloud Monitoring:
    - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`.
    - Azure: Track modifications via Audit logs.
- API Monitoring: Log Google Admin SDK and Microsoft Graph API calls.
- SIEM Integration: Centralize and monitor group modification logs.

## Source Verification

[source record](../../sources/mitre/group-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup).\
\ Examples: \n\n- Active Directory:\n    - Event ID 4728: Member added to a global group.\n    - Event ID 4732: Member added\
\ to a local group.\n- Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName \"New Name\"`\n- AWS IAM: `aws iam update-group\
\ --group-name <GroupName> --new-path \"/admin/\"`\n- Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>`\n\
- Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>`\n\n*Data Collection\
\ Measures:*\n\n- Directory Logging:\n    - Windows: Log EIDs 4728 (add), 4729 (remove).\n    - Azure AD: Enable \"Audit\
```
