---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0359
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0359-nltest
---

## Description

[[kb/mitre/attack/software/S0359-nltest|Nltest]] is a Windows command-line utility used to list domain controllers and enumerate domain trusts.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0359-nltest\|Nltest]] may be used to enumerate the parent domain of a local machine using `/parentdomain`.[^1]  |
| [[kb/mitre/attack/techniques/T1018-remote-system-discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0359-nltest\|Nltest]] may be used to enumerate remote domain controllers using options such as `/dclist` and `/dsgetdc`.[^1]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0359-nltest\|Nltest]] may be used to enumerate trusted domains by using commands such as `nltest /domain_trusts`.[^1] [^2]  |

 [^1]: [Nltest Manual](https://ss64.com/nt/nltest.html)
 [^2]: [Fortinet TrickBot](https://www.fortinet.com/blog/threat-research/trickbot-s-new-reconnaissance-plugin.html)
