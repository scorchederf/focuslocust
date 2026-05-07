---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1531
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1531-account-access-removal
tactic:
    - Impact
platforms:
    - Linux
    - macOS
    - Windows
    - SaaS
    - IaaS
    - Office Suite
    - ESXi
permissions required:
    - none
---

## Description

Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: changed credentials, revoked permissions for SaaS platforms such as Sharepoint) to remove access to accounts.[^3]  Adversaries may also subsequently log off and/or perform a [[kb/mitre/attack/techniques/T1529-system-shutdown-reboot|System Shutdown/Reboot]] to set malicious changes into place.[^1] [^2] <br><br>In Windows, [[kb/mitre/attack/software/S0039-net|Net]] utility, `Set-LocalUser` and `Set-ADAccountPassword` [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] cmdlets may be used by adversaries to modify user accounts. Accounts could also be disabled by Group Policy. In Linux, the `passwd` utility may be used to change passwords. On ESXi servers, accounts can be removed or modified via esxcli (`system account set`, `system account remove`).<br><br>Adversaries who use ransomware or similar attacks may first perform this and other Impact behaviors, such as [[kb/mitre/attack/techniques/T1485-data-destruction|Data Destruction]] and [[kb/mitre/attack/techniques/T1491-defacement|Defacement]], in order to impede incident response/recovery before completing the [[kb/mitre/attack/techniques/T1486-data-encrypted-for-impact|Data Encrypted for Impact]] objective. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0372](https://attack.mitre.org/software/S0372) | LockerGoga | LockerGoga has been observed changing account passwords and logging off current users.[^1] [^2]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex has changed user account passwords and logged users off the system.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor has the ability to change the password of local users on compromised hosts and can log off users.[^1]  |
| [S1134](https://attack.mitre.org/software/S1134) | DEADWOOD | DEADWOOD changes the password for local and domain users via `net.exe` to a random 32 character string to prevent these accounts from logging on. Additionally, DEADWOOD will terminate the `winlogon.exe` process to prevent attempts to log on to the infected system.[^1]  |

 [^1]: [CarbonBlack LockerGoga 2019](https://www.carbonblack.com/2019/03/22/tau-threat-intelligence-notification-lockergoga-ransomware/)
 [^2]: [Unit42 LockerGoga 2019](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)
 [^3]: [Obsidian Security SaaS Ransomware June 2023](https://web.archive.org/web/20230608061141/https://www.obsidiansecurity.com/blog/saas-ransomware-observed-sharepoint-microsoft-365/)
 [^4]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^5]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^6]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
