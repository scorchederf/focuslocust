---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0521
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0521-bloodhound
---

## Description

[[kb/mitre/attack/software/S0521-bloodhound|BloodHound]] is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.[^3] [^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1018-remote-system-discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can enumerate and collect the properties of domain computers, including domain controllers.[^1]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can collect information on user sessions.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can use PowerShell to pull Active Directory information from the target environment.[^1]  |
| [[kb/mitre/attack/techniques/T1069.001-local-groups\|T1069.001]] | Local Groups | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can collect information about local groups and members.[^1]  |
| [[kb/mitre/attack/techniques/T1069.002-domain-groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can collect information about domain groups and members.[^1]  |
| [[kb/mitre/attack/techniques/T1087.001-local-account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can identify users with local administrator rights.[^1]  |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can collect information about domain users, including identification of domain admin accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1106-native-api\|T1106]] | Native API | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can use .NET API calls in the SharpHound ingestor component to pull Active Directory data.[^1]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] has the ability to map domain trusts and identify misconfigurations for potential abuse.[^1]  |
| [[kb/mitre/attack/techniques/T1560-archive-collected-data\|T1560]] | Archive Collected Data | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1615-group-policy-discovery\|T1615]] | Group Policy Discovery | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] has the ability to collect local admin information via GPO.[^1]  |

 [^1]: [FoxIT Wocao December 2019](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
 [^2]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
 [^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)
 [^4]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
