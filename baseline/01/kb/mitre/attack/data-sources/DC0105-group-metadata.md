---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0105
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0105-group-metadata
---

## Description

Group metadata includes attributes like name, permissions, purpose, and associated user accounts or roles, which adversaries may exploit for privilege escalation. Examples:<br><br>- Active Directory: `Get-ADGroup -Identity "Domain Admins" -Properties Members, Description`<br>- Azure AD: `Get-AzureADGroup -ObjectId <GroupId>`<br>- Google Workspace: `GET  AWS IAM: `aws iam list-group-policies --group-name <group_name>`<br>- Office 365: `GET  Collection Measures:*<br><br>- Cloud Logging:<br>    - AWS CloudTrail for IAM group-related activities.<br>    - Azure AD Sign-In/Audit logs for metadata changes.<br>    - Google Admin Activity logs for API calls.<br>- Directory Logging: Log metadata access (e.g., Windows Event ID 4662).<br>- API Monitoring: Log API calls to modify group metadata (e.g., Microsoft Graph API).<br>- SIEM Integration: Centralize group metadata logs for analysis.<br>
