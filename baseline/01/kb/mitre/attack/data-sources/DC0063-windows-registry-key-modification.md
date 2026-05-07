---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0063
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0063-windows-registry-key-modification
---

## Description

Changes made to an existing registry key or its values. These modifications can include altering permissions, modifying stored data, or updating configuration settings.<br><br>*Data Collection Measures:*<br><br>- Windows Event Logs<br>    - Event ID 4657 - Registry Value Modified: Logs changes to registry values, including modifications to startup entries, security settings, or system configurations.<br>- Sysmon (System Monitor) for Windows<br>    - Sysmon Event ID 13 - Registry Value Set: Captures changes to specific registry values.<br>    - Sysmon Event ID 14 - Registry Key & Value Renamed: Logs renaming of registry keys, which may indicate evasion attempts.<br>- Endpoint Detection and Response (EDR) Solutions<br>    - Monitor registry modifications for suspicious behavior.
