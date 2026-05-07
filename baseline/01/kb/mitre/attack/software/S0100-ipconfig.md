---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0100
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0100-ipconfig
---

## Description

[[kb/mitre/attack/software/S0100-ipconfig|ipconfig]] is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0100-ipconfig\|ipconfig]] can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP. |

 [^1]: [TechNet Ipconfig](https://technet.microsoft.com/en-us/library/bb490921.aspx)
