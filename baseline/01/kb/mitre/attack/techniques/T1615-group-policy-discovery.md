---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1615
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1615-group-policy-discovery
tactic:
    - Discovery
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.[^4] [^1] <br><br>Adversaries may use commands such as `gpresult` or various publicly available PowerShell functions, such as `Get-DomainGPO` and `Get-DomainGPOLocalGroup`, to gather information on Group Policy settings.[^2] [^3]  Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [[kb/mitre/attack/techniques/T1484-domain-or-tenant-policy-modification|Domain or Tenant Policy Modification]]) for their benefit.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0082](https://attack.mitre.org/software/S0082) | Emissary | Emissary has the capability to execute `gpresult`.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] includes various modules for enumerating Group Policy.[^1]  |
| [[kb/mitre/attack/software/S0521-bloodhound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] has the ability to collect local admin information via GPO.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can capture information on group policy settings[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can identify victim environment Group Policy information.[^1]  |

 [^1]: [ADSecurity GPO Persistence 2016](https://adsecurity.org/?p=2716)
 [^2]: [Microsoft gpresult](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)
 [^3]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^4]: [TechNet Group Policy Basics](https://blogs.technet.microsoft.com/musings_of_a_technical_tam/2012/02/13/group-policy-basics-part-1-understanding-the-structure-of-a-group-policy-object/)
 [^5]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^6]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^7]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)
 [^8]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
