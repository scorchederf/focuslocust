---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1078
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/tactic/stealth
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1078-valid-accounts
tactic:
    - Initial Access
    - Persistence
    - Privilege Escalation
    - Stealth
platforms:
    - Containers
    - ESXi
    - IaaS
    - Identity Provider
    - Linux
    - macOS
    - Network Devices
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, network devices, and remote desktop.[^1]  Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.<br><br>In some cases, adversaries may abuse inactive accounts: for example, those belonging to individuals who are no longer part of an organization. Using these accounts may allow the adversary to evade detection, as the original account user will not be present to identify any anomalous activity taking place on their account.[^2] <br><br>The overlap of permissions for local, domain, and cloud accounts across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise.[^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | Adversaries can instruct Duqu to spread laterally by copying itself to shares it has enumerated and for which it has obtained legitimate credentials (via keylogging or other means). The remote host is then infected by using the compromised credentials to schedule a task on remote machines that executes the malware.[^1]  |
| [S0053](https://attack.mitre.org/software/S0053) | SeaDuke | Some SeaDuke samples have a module to extract email from Microsoft Exchange servers using compromised credentials.[^1]  |
| [S0362](https://attack.mitre.org/software/S0362) | Linux Rabbit | Linux Rabbit acquires valid SSH accounts through brute force. [^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack used hard-coded credentials to gain access to a network share.[^1]  |
| [S0599](https://attack.mitre.org/software/S0599) | Kinsing | Kinsing has used valid SSH credentials to access remote hosts.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer can use supplied user credentials to execute processes and stop services.[^1]  |
| [S9036](https://attack.mitre.org/software/S9036) | LP-Notes | LP-Notes has used stolen Windows credentials to log in as the users.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-application-developer-guidance\|M1013]] | Application Developer Guidance | Ensure that applications do not store sensitive data or credentials insecurely. (e.g. plaintext credentials in code, published credentials in repositories, or credentials in public cloud storage). |
| [[kb/mitre/attack/mitigations/M1015-active-directory-configuration\|M1015]] | Active Directory Configuration | Disable legacy authentication, which does not support MFA, and require the use of modern authentication protocols instead. |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Applications may send push notifications to verify a login as a form of multi-factor authentication (MFA). Train users to only accept valid push notifications and to report suspicious push notifications. |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Regularly audit user accounts for activity and deactivate or remove any that are no longer needed. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^1]  [^2]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not been authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [^3]  |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Applications and appliances that utilize default username and password should be changed immediately after the installation, and before deployment to a production environment.[^1]  When possible, applications that use SSH keys should be updated periodically and properly secured.<br><br>Policies should minimize (if not eliminate) reuse of passwords between different user accounts, especially employees using the same credentials for personal accounts that may not be defended by enterprise security resources. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Implement multi-factor authentication (MFA) across all account types, including default, local, domain, and cloud accounts, to prevent unauthorized access, even if credentials are compromised. MFA provides a critical layer of security by requiring multiple forms of verification beyond just a password. This measure significantly reduces the risk of adversaries abusing valid accounts to gain initial access, escalate privileges, maintain persistence, or evade defenses within your network. |
| [[kb/mitre/attack/mitigations/M1036-account-use-policies\|M1036]] | Account Use Policies | Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1078.001-default-accounts\|T1078.001]] | Default Accounts |
| [[kb/mitre/attack/techniques/T1078.002-domain-accounts\|T1078.002]] | Domain Accounts |
| [[kb/mitre/attack/techniques/T1078.004-cloud-accounts\|T1078.004]] | Cloud Accounts |
| [[kb/mitre/attack/techniques/T1078.003-local-accounts\|T1078.003]] | Local Accounts |

 [^1]: [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
 [^2]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)
 [^3]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)
 [^4]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
 [^5]: [Symantec Seaduke 2015](http://www.symantec.com/connect/blogs/forkmeiamfamous-seaduke-latest-weapon-duke-armory)
 [^6]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^7]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^8]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^9]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
 [^10]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)
 [^11]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)
 [^12]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)
 [^13]: [Anomali Linux Rabbit 2018](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
 [^14]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)
