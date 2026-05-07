---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0552
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0552-adfind
---

## Description

[[kb/mitre/attack/software/S0552-adfind|AdFind]] is a free command-line query tool that can be used for gathering information from Active Directory.[^1] [^3] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] can extract subnet information from Active Directory.[^1] [^3] [^2]  |
| [[kb/mitre/attack/techniques/T1018-remote-system-discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] has the ability to query Active Directory for computers.[^1] [^4] [^3] [^2]  |
| [[kb/mitre/attack/techniques/T1069.002-domain-groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] can enumerate domain groups.[^1] [^4] [^2] [^3]  |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] can enumerate domain users.[^1] [^5] [^3] [^2] [^4]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] can gather information about organizational units (OUs) and domain trusts from Active Directory.[^1] [^4] [^2] [^3]  |

 [^1]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
 [^2]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
 [^3]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
 [^4]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
 [^5]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
