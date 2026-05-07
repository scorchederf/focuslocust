---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0105
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0105-dsquery
---

## Description

[[kb/mitre/attack/software/S0105-dsquery|dsquery]] is a command-line utility that can be used to query Active Directory for information from a system within a domain. [^1]  It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle.

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1069.002-domain-groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] can be used to gather information on permission groups within a domain.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.[^1]  |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] can be used to gather information on user accounts within a domain.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] can be used to gather information on domain trusts with `dsquery * -filter "(objectClass=trustedDomain)" -attr *`.[^1]  |

 [^1]: [TechNet Dsquery](https://technet.microsoft.com/en-us/library/cc732952.aspx)
 [^2]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^3]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)
