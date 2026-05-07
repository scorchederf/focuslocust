---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1554
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1554-compromise-host-software-binary
tactic:
    - Persistence
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.<br><br>Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [[kb/mitre/attack/techniques/T1556-modify-authentication-process|Modify Authentication Process]]).[^1] <br><br>An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)[^2]  prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.[^3] <br><br>After modifying a binary, an adversary may attempt to impair defenses by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury modifies the `keyutils` library to add malicious behavior to the OpenSSH client and the curl library.[^1] [^2]  |
| [S0486](https://attack.mitre.org/software/S0486) | Bonadan | Bonadan has maliciously altered the OpenSSH binary on targeted systems to create a backdoor.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel has maliciously altered the OpenSSH binary on targeted systems to create a backdoor.[^1]  |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest searches through the `/Users/` folder looking for executable files. For each executable, ThiefQuest prepends a copy of itself to the beginning of the file. When the file is executed, the ThiefQuest code is executed first. ThiefQuest creates a hidden file, copies the original target executable to the file, then executes the new hidden file to maintain the appearance of normal behavior. [^1] [^2]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer has used a Trojanized version of the Windows Notepad application for an additional backdoor persistence mechanism.[^1]  |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos replaced the SSH client with a trojanized SSH client to steal credentials on compromised systems.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET uses a malicious browser application to replace the legitimate browser in order to continuously capture credentials, monitor web traffic, and download additional modules.[^1]  |
| [S1104](https://attack.mitre.org/software/S1104) | SLOWPULSE | SLOWPULSE is applied in compromised environments through modifications to legitimate Pulse Secure files.[^1]  |
| [S1115](https://attack.mitre.org/software/S1115) | WIREFIRE | WIREFIRE can modify the `visits.py` component of Ivanti Connect Secure VPNs for file download and arbitrary command execution.[^1] [^2]  |
| [S1116](https://attack.mitre.org/software/S1116) | WARPWIRE | WARPWIRE can embed itself into a legitimate file on compromised Ivanti Connect Secure VPNs.[^1]  |
| [S1118](https://attack.mitre.org/software/S1118) | BUSHWALK | BUSHWALK can embed into the legitimate `querymanifest.cgi` file on compromised Ivanti Connect Secure VPNs.[^2] [^1]  |
| [S1119](https://attack.mitre.org/software/S1119) | LIGHTWIRE | LIGHTWIRE can imbed itself into the legitimate `compcheckresult.cgi` component of Ivanti Connect Secure VPNs to enable command execution.[^2] [^1]  |
| [S1120](https://attack.mitre.org/software/S1120) | FRAMESTING | FRAMESTING can embed itself in the CAV Python package of an Ivanti Connect Secure VPN located in `/home/venv3/lib/python3.6/site-packages/cav-0.1-py3.6.egg/cav/api/resources/category.py.`[^1]  |
| [S1121](https://attack.mitre.org/software/S1121) | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can append malicious components to the `tmp/tmpmnt/bin/samba_upgrade.tar` archive inside the factory reset partition in attempt to persist post reset.[^1]  |
| [S1136](https://attack.mitre.org/software/S1136) | BFG Agonizer | BFG Agonizer uses DLL unhooking to remove user mode inline hooks that security solutions often implement. BFG Agonizer also uses IAT unhooking to remove user-mode IAT hooks that security solutions also use.[^1]  |
| [S1184](https://attack.mitre.org/software/S1184) | BOLDMOVE | BOLDMOVE contains a watchdog-like feature that monitors a particular file for modification. If modification is detected, the legitimate file is backed up and replaced with a trojanized file to allow for persistence through likely system upgrades.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm can modify hardware wallet applications.[^1]  |
| [S9014](https://attack.mitre.org/software/S9014) | PHASEJAM | PHASEJAM has modified legitimate components to enable persistence and execution, including inserting a web shell into `getComponent.cgi` and `restAuth.cgi`, modifying `DSUpgrade.pm` to block system upgrades, and overwriting `remotedebug` to execute arbitrary commands when specific parameters are provided.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1045-code-signing\|M1045]] | Code Signing | Ensure all application component binaries are signed by the correct application developers. |

 [^1]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^2]: [Unit42 Banking Trojans Hooking 2022](https://unit42.paloaltonetworks.com/banking-trojan-techniques/#post-125550-_rm3d6xxbk52n)
 [^3]: [ESET FontOnLake Analysis 2021](https://web-assets.esetstatic.com/wls/2021/10/eset_fontonlake.pdf)
 [^4]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^5]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^6]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^7]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
 [^8]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^9]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
 [^10]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^11]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^12]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
 [^13]: [reed thiefquest ransomware analysis](https://blog.malwarebytes.com/mac/2020/07/mac-thiefquest-malware-may-not-be-ransomware-after-all/)
 [^14]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
 [^15]: [ESET Ebury Feb 2014](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)
 [^16]: [ESET Ebury May 2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
 [^17]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
 [^18]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^19]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
 [^20]: [Volexity Ivanti Zero-Day Exploitation January 2024](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
