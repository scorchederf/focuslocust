---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0108
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0108-netsh
---

## Description

[[kb/mitre/attack/software/S0108-netsh|netsh]] is a scripting utility used to interact with networking components on local or remote systems. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1090-proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to set up a proxy tunnel to allow remote host access to an infected host.[^1]  |
| [[kb/mitre/attack/techniques/T1518.001-security-software-discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to discover system firewall settings.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1546.007-netsh-helper-dll\|T1546.007]] | Netsh Helper DLL | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used as a persistence proxy technique to execute a helper DLL when netsh.exe is executed.[^1]  |
| [[kb/mitre/attack/techniques/T1686-disable-or-modify-system-firewall\|T1686]] | Disable or Modify System Firewall | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to disable local firewall settings.[^1] [^2]  |

 [^1]: [TechNet Netsh](https://technet.microsoft.com/library/bb490939.aspx)
 [^2]: [TechNet Netsh Firewall](https://technet.microsoft.com/en-us/library/cc771046(v=ws.10).aspx)
 [^3]: [Demaske Netsh Persistence](https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html)
 [^4]: [Securelist fileless attacks Feb 2017](https://securelist.com/fileless-attacks-against-enterprise-networks/77403/)
