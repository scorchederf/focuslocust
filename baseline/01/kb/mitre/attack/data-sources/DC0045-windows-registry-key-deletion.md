---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0045
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0045-windows-registry-key-deletion
---

## Description

The removal of a registry key within the Windows operating system.<br><br>*Data Collection Measures:*<br><br>- Windows Event Logs<br>    - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which may indicate deletion.<br>    - Event ID 4660 - Object Deleted: Logs when a registry key is deleted.<br>- Sysmon (System Monitor) for Windows<br>    - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed.<br>    - Sysmon Event ID 13 - Registry Value Deleted: Captures removal of specific registry values.<br>- Endpoint Detection and Response (EDR) Solutions<br>    - Monitor registry deletions for suspicious behavior.
