---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0102
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0102-nbtstat
---

## Description

[[kb/mitre/attack/software/S0102-nbtstat|nbtstat]] is a utility used to troubleshoot NetBIOS name resolution. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0102-nbtstat\|nbtstat]] can be used to discover local NetBIOS domain names. |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0102-nbtstat\|nbtstat]] can be used to discover current NetBIOS sessions. |

 [^1]: [TechNet Nbtstat](https://technet.microsoft.com/en-us/library/cc940106.aspx)
