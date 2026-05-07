---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0066
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0066-active-directory-object-modification
---

## Description

Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute Changes). Examples:<br><br>- User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts).<br>- Group Membership: Adding/removing members.<br>- OU: Changing properties/permissions (e.g., delegation).<br>- Service Account: Modifying SPNs or other attributes.<br>- Object Attributes: Changes to passwords, logon hours, or control flags.
