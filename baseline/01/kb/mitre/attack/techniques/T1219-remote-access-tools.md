---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1219
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1219-remote-access-tools
tactic:
    - Command And Control
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard, Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software permissions. This software is commonly used for troubleshooting, software installation, and system management.[^5] [^1] [^2]  Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.<br><br>Remote access tools may be installed and used post-compromise as an alternate communications channel for redundant access or to establish an interactive remote desktop session with the target system. It may also be used as a malware component to establish a reverse connection or back-connect to a service or adversary-controlled system.<br><br>Installation of many remote access tools may also include persistence (e.g., the software's installation routine creates a [[kb/mitre/attack/techniques/T1543.003-windows-service|Windows Service]]). Remote access modules/features may also exist as part of otherwise existing software (e.g., Google Chrome’s Remote Desktop).[^3] [^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0030](https://attack.mitre.org/software/S0030) | Carbanak | Carbanak has a plugin for VNC and Ammyy Admin Tool.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM has the capability to download a VNC module from command and control (C2).[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot uses vncDll module to remote control the victim machine.[^1] [^2]  |
| [S0384](https://attack.mitre.org/software/S0384) | Dridex | Dridex contains a module for VNC.[^1]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has checked for the LogMein event log in an attempt to encrypt files in remote machines.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has established tmate sessions for C2 communications.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has utilized remote access software including AnyDesk client through the “adc” module.[^1] [^2] [^4]  InvisibleFerret has also downloaded the AnyDesk client should it not already exist on the compromised host by searching for `C:/Program Files(x86)/AnyDesk/AnyDesk.exe`.[^3]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services. |
| [[kb/mitre/attack/mitigations/M1034-limit-hardware-installation\|M1034]] | Limit Hardware Installation | Block the use of IP-based KVM devices within the network if they are not required.  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Properly configure firewalls, application firewalls, and proxies to limit outgoing traffic to sites and services used by remote access software. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Use application control to mitigate installation and use of unapproved software that can be used for remote access. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Consider disabling unnecessary remote connection functionality, including both unapproved software installations and specific features built into supported applications. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1219.001-ide-tunneling\|T1219.001]] | IDE Tunneling |
| [[kb/mitre/attack/techniques/T1219.003-remote-access-hardware\|T1219.003]] | Remote Access Hardware |
| [[kb/mitre/attack/techniques/T1219.002-remote-desktop-software\|T1219.002]] | Remote Desktop Software |

 [^1]: [CrowdStrike 2015 Global Threat Report](https://go.crowdstrike.com/rs/281-OBQ-266/images/15GlobalThreatReport.pdf)
 [^2]: [CrySyS Blog TeamSpy](https://blog.crysys.hu/2013/03/teamspy/)
 [^3]: [Google Chrome Remote Desktop](https://support.google.com/chrome/answer/1649523)
 [^4]: [Chrome Remote Desktop](https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708)
 [^5]: [Symantec Living off the Land](https://www.symantec.com/content/dam/symantec/docs/security-center/white-papers/istr-living-off-the-land-and-fileless-attack-techniques-en.pdf)
 [^6]: [Dell Dridex Oct 2015](https://www.secureworks.com/research/dridex-bugat-v5-botnet-takeover-operation)
 [^7]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^8]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
 [^9]: [ESET Trickbot Oct 2020](https://www.welivesecurity.com/2020/10/12/eset-takes-part-global-operation-disrupt-trickbot/)
 [^10]: [Bitdefender Trickbot March 2020](https://www.bitdefender.com/files/News/CaseStudies/study/316/Bitdefender-Whitepaper-TrickBot-en-EN-interactive.pdf)
 [^11]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^12]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^13]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^14]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^15]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^16]: [Cyble Egregor Oct 2020](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)
