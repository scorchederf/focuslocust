---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0008
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0008-gsecdump
---

## Description

[[kb/mitre/attack/software/S0008-gsecdump|gsecdump]] is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.002-security-account-manager\|T1003.002]] | Security Account Manager | [[kb/mitre/attack/software/S0008-gsecdump\|gsecdump]] can dump Windows password hashes from the SAM.[^1]  |
| [[kb/mitre/attack/techniques/T1003.004-lsa-secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0008-gsecdump\|gsecdump]] can dump LSA secrets.[^1]  |

 [^1]: [TrueSec Gsecdump](https://web.archive.org/web/20140328102838/https://www.truesec.se/sakerhet/verktyg/saakerhet/gsecdump_v2.0b5)
 [^2]: [Microsoft Gsecdump](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=HackTool:Win32/Gsecdump)
