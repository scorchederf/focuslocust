---
parsed_by: focuslocust
source: mitre
type: generated
---
# Group Modification

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

## Generated Concept Page

- [Group Modification](../../attack/data-sources/DC0094-group-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0094 |
| name | Group Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0094 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup).\
  \ Examples: \n\n- Active Directory:\n    - Event ID 4728: Member added to a global group.\n    - Event ID 4732: Member added\
  \ to a local group.\n- Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName \"New Name\"`\n- AWS IAM: `aws iam update-group\
  \ --group-name <GroupName> --new-path \"/admin/\"`\n- Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>`\n\
  - Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>`\n\n*Data Collection\
  \ Measures:*\n\n- Directory Logging:\n    - Windows: Log EIDs 4728 (add), 4729 (remove).\n    - Azure AD: Enable \"Audit\
  \ logs.\"\n    - Google Workspace: Enable Admin Activity logs.\n    - Office 365: Use Unified Audit Logs.\n- Cloud Monitoring:\n\
  \    - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`.\n    - Azure: Track modifications via Audit logs.\n\
  - API Monitoring: Log Google Admin SDK and Microsoft Graph API calls.\n- SIEM Integration: Centralize and monitor group\
  \ modification logs."
external_references:
- external_id: DC0094
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0094
id: x-mitre-data-component--05d5b5b4-ef93-4807-b05f-33d8c5a35bc5
modified: '2025-10-21T15:14:40.086Z'
name: Group Modification
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
- channel: Add member to group
  name: m365:unified
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
