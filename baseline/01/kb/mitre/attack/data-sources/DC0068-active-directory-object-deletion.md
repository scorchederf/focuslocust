---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0068
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0068-active-directory-object-deletion
---

## Description

Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples:<br><br>- User Account: Deleted user.<br>- Group: Deleted security/distribution group.<br>- Organizational Unit (OU): Loss of configurations or policies.<br>- Service Account: Disrupted operations or cover tracks.<br>- Trust Object: Removed domain trust, disrupting connectivity.<br><br>*Data Collection Measures:*<br><br>- Audit Policy:<br>    - Enable "Audit Directory Service Changes" (Success and Failure).<br>    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Directory Service Changes`.<br>    - Key Event: Event ID 5141.<br>- Log Forwarding: Use WEF to centralize logs for SIEM tools (e.g., Splunk).<br>- Enable EDR Monitoring:<br>    - Detect processes or users that initiate unauthorized object deletions.<br>    - Monitor tools and scripts that may delete key directory objects.
