---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0104
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0104-netstat
---

## Description

[[kb/mitre/attack/software/S0104-netstat|netstat]] is an operating system utility that displays active TCP connections, listening ports, and network statistics. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0104-netstat\|netstat]] can be used to enumerate local network connections, including active TCP connections and other network statistics.[^1]  |

 [^1]: [TechNet Netstat](https://technet.microsoft.com/en-us/library/bb490947.aspx)
