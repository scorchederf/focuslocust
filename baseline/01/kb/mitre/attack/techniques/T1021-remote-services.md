---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1021
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1021-remote-services
tactic:
    - Lateral Movement
platforms:
    - Linux
    - macOS
    - Windows
    - IaaS
    - ESXi
permissions required:
    - none
---

## Description

Adversaries may use [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]] to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.<br><br>In an enterprise environment, servers and workstations can be organized into domains. Domains provide centralized identity management, allowing users to login using one set of credentials across the entire network. If an adversary is able to obtain a set of valid domain credentials, they could login to many different machines using remote access protocols such as secure shell (SSH) or remote desktop protocol (RDP).[^8] [^6]  They could also login to accessible SaaS or IaaS services, such as those that federate their identities to the domain, or management platforms for internal virtualization environments such as VMware vCenter. <br><br>Legitimate applications (such as [[kb/mitre/attack/techniques/T1072-software-deployment-tools|Software Deployment Tools]] and other administrative programs) may utilize [[kb/mitre/attack/techniques/T1021-remote-services|Remote Services]] to access remote hosts. For example, Apple Remote Desktop (ARD) on macOS is native software used for remote management. ARD leverages a blend of protocols, including [[kb/mitre/attack/techniques/T1021.005-vnc|VNC]] to send the screen and control buffers and [[kb/mitre/attack/techniques/T1021.004-ssh|SSH]] for secure file transfer.[^2] [^3] [^1]  Adversaries can abuse applications such as ARD to gain remote code execution and perform lateral movement. In versions of macOS prior to 10.14, an adversary can escalate an SSH session to an ARD session which enables an adversary to accept TCC (Transparency, Consent, and Control) prompts without user interaction and gain access to data.[^5] [^4] [^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0437](https://attack.mitre.org/software/S0437) | Kivars | Kivars has the ability to remotely trigger keyboard input and mouse clicks. [^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet can propagate via peer-to-peer communication and updates using RPC.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can manage remote screen sessions.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to use RPC for lateral movement.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit the accounts that may use remote services. Limit the permissions for accounts that are at higher risk of compromise; for example, configure SSH so users can only run specific programs. |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Do not reuse local administrator account passwords across systems. Ensure password complexity and uniqueness such that the passwords cannot be cracked or guessed. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication on remote service logons where possible. |
| [[kb/mitre/attack/mitigations/M1035-limit-access-to-resource-over-network\|M1035]] | Limit Access to Resource Over Network | Prevent unnecessary remote access to file shares, hypervisors, sensitive systems, etc. Mechanisms to limit access may include use of network concentrators, RDP gateways, etc.[^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | If remote services, such as the ability to make direct connections to cloud virtual machines, are not required, disable these connection types where feasible. On ESXi servers, consider enabling lockdown mode, which disables direct access to an ESXi host and requires that the host be managed remotely using vCenter.[^1] [^2]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1021.005-vnc\|T1021.005]] | VNC |
| [[kb/mitre/attack/techniques/T1021.004-ssh\|T1021.004]] | SSH |
| [[kb/mitre/attack/techniques/T1021.008-direct-cloud-vm-connections\|T1021.008]] | Direct Cloud VM Connections |
| [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares\|T1021.002]] | SMB／Windows Admin Shares |
| [[kb/mitre/attack/techniques/T1021.006-windows-remote-management\|T1021.006]] | Windows Remote Management |
| [[kb/mitre/attack/techniques/T1021.003-distributed-component-object-model\|T1021.003]] | Distributed Component Object Model |
| [[kb/mitre/attack/techniques/T1021.007-cloud-services\|T1021.007]] | Cloud Services |
| [[kb/mitre/attack/techniques/T1021.001-remote-desktop-protocol\|T1021.001]] | Remote Desktop Protocol |

 [^1]: [Apple Remote Desktop Admin Guide 3.3](https://images.apple.com/remotedesktop/pdf/ARD_Admin_Guide_v3.3.pdf)
 [^2]: [Remote Management MDM macOS](https://support.apple.com/en-us/HT209161)
 [^3]: [Kickstart Apple Remote Desktop commands](https://support.apple.com/en-us/HT201710)
 [^4]: [Lockboxx ARD 2019](http://lockboxx.blogspot.com/2019/07/macos-red-teaming-206-ard-apple-remote.html)
 [^5]: [FireEye 2019 Apple Remote Desktop](https://www.fireeye.com/blog/threat-research/2019/10/leveraging-apple-remote-desktop-for-good-and-evil.html)
 [^6]: [TechNet Remote Desktop Services](https://technet.microsoft.com/en-us/windowsserver/ee236407.aspx)
 [^7]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)
 [^8]: [SSH Secure Shell](https://www.ssh.com/ssh)
 [^9]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)
 [^10]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^11]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^12]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
 [^13]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)
 [^14]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)
 [^15]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
