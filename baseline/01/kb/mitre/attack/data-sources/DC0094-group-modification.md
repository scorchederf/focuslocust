---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0094
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0094-group-modification
---

## Description

Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup). Examples: <br><br>- Active Directory:<br>    - Event ID 4728: Member added to a global group.<br>    - Event ID 4732: Member added to a local group.<br>- Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName "New Name"`<br>- AWS IAM: `aws iam update-group --group-name <GroupName> --new-path "/admin/"`<br>- Google Workspace: Modify permissions via Admin SDK API: `PATCH  Office 365: Modify groups via Graph API: `PATCH  Collection Measures:*<br><br>- Directory Logging:<br>    - Windows: Log EIDs 4728 (add), 4729 (remove).<br>    - Azure AD: Enable "Audit logs."<br>    - Google Workspace: Enable Admin Activity logs.<br>    - Office 365: Use Unified Audit Logs.<br>- Cloud Monitoring:<br>    - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`.<br>    - Azure: Track modifications via Audit logs.<br>- API Monitoring: Log Google Admin SDK and Microsoft Graph API calls.<br>- SIEM Integration: Centralize and monitor group modification logs.
