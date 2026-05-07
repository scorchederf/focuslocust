---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1098
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
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
mitre-attack: kb/mitre/attack/techniques/T1098-account-manipulation
tactic:
    - Persistence
    - Privilege Escalation
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

Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups.[^1]  These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. <br><br>In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0002-mimikatz\|S0002]] | Mimikatz | The [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The `LSADUMP::ChangeNTLM` and `LSADUMP::SetNTLM` modules can also manipulate the password hash of an account without knowing the clear text value.[^1] [^2]  |
| [S0274](https://attack.mitre.org/software/S0274) | Calisto | Calisto adds permissions and remote logins to all users.[^1]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has modified GitHub account settings for private repositories and changed them to public.[^1] [^2] [^3] [^4]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Ensure that low-privileged user accounts do not have permissions to modify accounts or account-related policies. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Restrict access to potentially sensitive files that deal with authentication and/or authorization. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Protect domain controllers by ensuring proper security configuration for critical servers to limit access by potentially unnecessary protocols and services, such as SMB file sharing. |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Configure access controls and firewalls to limit access to critical systems and domain controllers. Most cloud environments support separate virtual private cloud (VPC) instances that enable further segmentation of cloud systems. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Remove unnecessary and potentially abusable authentication and authorization mechanisms where possible. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1098.003-additional-cloud-roles\|T1098.003]] | Additional Cloud Roles |
| [[kb/mitre/attack/techniques/T1098.006-additional-container-cluster-roles\|T1098.006]] | Additional Container Cluster Roles |
| [[kb/mitre/attack/techniques/T1098.007-additional-local-or-domain-groups\|T1098.007]] | Additional Local or Domain Groups |
| [[kb/mitre/attack/techniques/T1098.004-ssh-authorized-keys\|T1098.004]] | SSH Authorized Keys |
| [[kb/mitre/attack/techniques/T1098.005-device-registration\|T1098.005]] | Device Registration |
| [[kb/mitre/attack/techniques/T1098.001-additional-cloud-credentials\|T1098.001]] | Additional Cloud Credentials |
| [[kb/mitre/attack/techniques/T1098.002-additional-email-delegate-permissions\|T1098.002]] | Additional Email Delegate Permissions |

 [^1]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
 [^2]: [Microsoft Security Event 4670](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4670)
 [^3]: [Microsoft User Modified Event](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738)
 [^4]: [InsiderThreat ChangeNTLM July 2017](https://blog.stealthbits.com/manipulating-user-passwords-with-mimikatz-SetNTLM-ChangeNTLM)
 [^5]: [GitHub Mimikatz Issue 92 June 2017](https://github.com/gentilkiwi/mimikatz/issues/92)
 [^6]: [Adsecurity Mimikatz Guide](https://adsecurity.org/?page_id=1821)
 [^7]: [Metcalf 2015](http://adsecurity.org/?p=1275)
 [^8]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
 [^9]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^10]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
 [^11]: [Microsoft Shai-Hulud December 2025](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
 [^12]: [Symantec Calisto July 2018](https://web.archive.org/web/20190111082249/https://www.symantec.com/security-center/writeup/2018-073014-2512-99?om_rssid=sr-latestthreats30days)
