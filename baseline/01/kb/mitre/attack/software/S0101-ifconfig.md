---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0101
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0101-ifconfig
---

## Description

[[kb/mitre/attack/software/S0101-ifconfig|ifconfig]] is a Unix-based utility used to gather information about and interact with the TCP/IP settings on a system. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0101-ifconfig\|ifconfig]] can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP. |

 [^1]: [Wikipedia Ifconfig](https://en.wikipedia.org/wiki/Ifconfig)
