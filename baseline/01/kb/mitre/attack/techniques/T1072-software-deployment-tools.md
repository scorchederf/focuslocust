---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1072
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1072-software-deployment-tools
tactic:
    - Execution
    - Lateral Movement
platforms:
    - Linux
    - macOS
    - Network Devices
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may gain access to and use centralized software suites installed within an enterprise to execute commands and move laterally through the network. Configuration management and software deployment applications may be used in an enterprise network or cloud environment for routine administration purposes. These systems may also be integrated into CI/CD pipelines. Examples of such solutions include: SCCM, HBSS, Altiris, AWS Systems Manager, Microsoft Intune, Azure Arc, and GCP Deployment Manager.  <br><br>Access to network-wide or enterprise-wide endpoint management software may enable an adversary to achieve remote code execution on all connected systems. The access may be used to laterally move to other systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.<br><br>SaaS-based configuration management services may allow for broad [[kb/mitre/attack/techniques/T1651-cloud-administration-command|Cloud Administration Command]] on cloud-hosted instances, as well as the execution of arbitrary commands on on-premises endpoints. For example, Microsoft Configuration Manager allows Global or Intune Administrators to run scripts as SYSTEM on on-premises devices joined to Entra ID.[^2]  Such services may also utilize [[kb/mitre/attack/techniques/T1071.001-web-protocols|Web Protocols]] to communicate back to adversary owned infrastructure.[^3] <br><br>Network infrastructure devices may also have configuration management tools that can be similarly abused by adversaries.[^1] <br><br>The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the third-party system, or specific domain credentials may be required. However, the system may require an administrative account to log in or to access specific functionality.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0041](https://attack.mitre.org/software/S0041) | Wiper | It is believed that a patch management system for an anti-virus product commonly installed among targeted companies was used to distribute the Wiper malware.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1015-active-directory-configuration\|M1015]] | Active Directory Configuration | Ensure proper system and access isolation for critical network systems through use of group policy. |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Have a strict approval policy for use of deployment systems. |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Ensure that any accounts used by third-party providers to access these systems are traceable to the third-party and are not used throughout the network or used by other third-party providers in the same environment. Ensure there are regular reviews of accounts provisioned to these systems to verify continued business need, and ensure there is governance to trace de-provisioning of access that is no longer required. Ensure proper system and access isolation for critical network systems through use of account privilege separation. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Grant access to application deployment systems only to a limited number of authorized administrators. |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Verify that account credentials that may be used to access deployment systems are unique and not used throughout the enterprise network. |
| [[kb/mitre/attack/mitigations/M1029-remote-data-storage\|M1029]] | Remote Data Storage | If the application deployment system can be configured to deploy only signed binaries, then ensure that the trusted signing certificates are not co-located with the application deployment system and are instead located on a system that cannot be accessed remotely or to which remote access is tightly controlled. |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Ensure proper system isolation for critical network systems through use of firewalls. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Ensure proper system and access isolation for critical network systems through use of multi-factor authentication. |
| [[kb/mitre/attack/mitigations/M1033-limit-software-installation\|M1033]] | Limit Software Installation | Restrict the use of third-party software suites installed within an enterprise network.  |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Patch deployment systems regularly to prevent potential remote access through [[kb/mitre/attack/techniques/T1068-exploitation-for-privilege-escalation\|Exploitation for Privilege Escalation]]. |

 [^1]: [Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^2]: [SpecterOps Lateral Movement from Azure to On-Prem AD 2020](https://posts.specterops.io/death-from-above-lateral-movement-from-azure-to-on-prem-ad-d18cb3959d4d)
 [^3]: [Mitiga Security Advisory: SSM Agent as Remote Access Trojan](https://www.mitiga.io/blog/mitiga-security-advisory-abusing-the-ssm-agent-as-a-remote-access-trojan)
 [^4]: [Dell Wiper](http://www.secureworks.com/cyber-threat-intelligence/threats/wiper-malware-analysis-attacking-korean-financial-sector/)
