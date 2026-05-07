---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S1071
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S1071-rubeus
---

## Description

[[kb/mitre/attack/software/S1071-rubeus|Rubeus]] is a C# toolset designed for raw Kerberos interaction that has been used since at least 2020, including in ransomware operations.[^1] [^2] [^4] [^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S1071-rubeus\|Rubeus]] can gather information about domain trusts.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1558.001-golden-ticket\|T1558.001]] | Golden Ticket | [[kb/mitre/attack/software/S1071-rubeus\|Rubeus]] can forge a ticket-granting ticket.[^1]  |
| [[kb/mitre/attack/techniques/T1558.002-silver-ticket\|T1558.002]] | Silver Ticket | [[kb/mitre/attack/software/S1071-rubeus\|Rubeus]] can create silver tickets.[^1]  |
| [[kb/mitre/attack/techniques/T1558.003-kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S1071-rubeus\|Rubeus]] can use the `KerberosRequestorSecurityToken.GetRequest` method to request kerberoastable service tickets.[^1]  |
| [[kb/mitre/attack/techniques/T1558.004-as-rep-roasting\|T1558.004]] | AS-REP Roasting | [[kb/mitre/attack/software/S1071-rubeus\|Rubeus]] can reveal the credentials of accounts that have Kerberos pre-authentication disabled through AS-REP roasting.[^1] [^3] [^2]   |

 [^1]: [GitHub Rubeus March 2023](https://github.com/GhostPack/Rubeus)
 [^2]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)
 [^3]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)
 [^4]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)
