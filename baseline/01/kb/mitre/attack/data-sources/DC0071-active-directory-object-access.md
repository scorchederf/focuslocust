---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0071
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0071-active-directory-object-access
---

## Description

Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or queried. Example: Windows Event ID 4661 logs object access attempts. Examples:<br><br>- Attribute Access: e.g., `userPassword`, `memberOf`, `securityDescriptor`.<br>- Group Enumeration: Enumerating critical group members (e.g., Domain Admins).<br>- User Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`.<br>- Policy Access: Accessing GPOs to understand security settings.<br><br>*Data Collection Measures:*<br><br>- Audit Policies:<br>    - Enable "Audit Directory Service Access" under Advanced Audit Policies (Success and Failure).<br>    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object AccessEnable: Audit Directory Service Access` (Success and Failure).<br>    - Captured Events: IDs 4661, 4662.<br>- Event Forwarding: Use WEF to centralize logs for SIEM analysis.<br>- SIEM Integration: Collect and parse logs (e.g., 4661, 4662) using tools like Splunk or Azure Sentinel.<br>- Log Filtering:<br>- Focus on sensitive objects/attributes like:<br>    - `Domain Admins` group.<br>    - `userPassword`, `ntSecurityDescriptor`.<br>- Enable EDR Monitoring:<br>    - Detect processes accessing sensitive AD objects (e.g., samAccountName, securityDescriptor).<br>    - Log all attempts to enumerate critical groups (e.g., "Domain Admins").
