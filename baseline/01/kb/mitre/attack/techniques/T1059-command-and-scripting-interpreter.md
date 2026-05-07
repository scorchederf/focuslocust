---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1059
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
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
mitre-attack: kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter
tactic:
    - Execution
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

Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of [[kb/mitre/attack/techniques/T1059.004-unix-shell|Unix Shell]] while Windows installations include the [[kb/mitre/attack/techniques/T1059.003-windows-command-shell|Windows Command Shell]] and [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]].<br><br>There are also cross-platform interpreters such as [[kb/mitre/attack/techniques/T1059.006-python|Python]], as well as those commonly associated with client applications such as [[kb/mitre/attack/techniques/T1059.007-javascript|JavaScript]] and [[kb/mitre/attack/techniques/T1059.005-visual-basic|Visual Basic]].<br><br>Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in [[kb/mitre/attack/tactics/TA0001-initial-access|Initial Access]] payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells, as well as utilize various [[kb/mitre/attack/techniques/T1021-remote-services|Remote Services]] in order to achieve remote Execution.[^3] [^2] [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | CHOPSTICK is capable of performing remote command execution.[^1] [^2]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT is able to open a remote shell to execute commands.[^1] [^2]  |
| [S0167](https://attack.mitre.org/software/S0167) | Matryoshka | Matryoshka is capable of providing Meterpreter shell access.[^1]  |
| [S0219](https://attack.mitre.org/software/S0219) | WINERACK | WINERACK can create a reverse shell that utilizes statically-linked Wine cmd.exe code to emulate Windows command prompt commands.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook can support commands to execute Java-based payloads.[^1]   |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda can launch remote scripts on the victim’s machine.[^1] 	 |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can execute various types of scripts on the victim’s machine.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] uses a command-line interface to interact with systems.[^1]  |
| [S0374](https://attack.mitre.org/software/S0374) | SpeakUp | SpeakUp uses Perl scripts.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a CommandPromptPacket and ScriptPacket module(s) for creating a remote shell and executing scripts.[^1]  |
| [S0460](https://attack.mitre.org/software/S0460) | Get2 | Get2 has the ability to run executables with command-line arguments.[^1]  |
| [S0486](https://attack.mitre.org/software/S0486) | Bonadan | Bonadan can create bind and reverse shells on the infected system.[^1] 	 |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel can create a reverse shell between the infected host and a specified system.[^1] 	 |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell has the ability to create reverse shells with Perl scripts.[^1]  |
| [S0618](https://attack.mitre.org/software/S0618) | FIVEHANDS | FIVEHANDS can receive a command line argument to limit file encryption to specified directories.[^1] [^2]  |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate shellcode outputs that execute via Ruby.[^1] 	 |
| [S1110](https://attack.mitre.org/software/S1110) | SLIGHTPULSE | SLIGHTPULSE contains functionality to execute arbitrary commands passed to it.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin variants can be delivered via highly obfuscated Windows Script Files (WSF) for initial execution.[^1]  |
| [S1151](https://attack.mitre.org/software/S1151) | ZeroCleare | ZeroCleare can receive command line arguments from an operator to corrupt the file system using the [[kb/mitre/attack/software/S0364-rawdisk\|RawDisk]] driver.[^1]  |
| [S1154](https://attack.mitre.org/software/S1154) | VersaMem | VersaMem was delivered as a Java Archive (JAR) that runs by attaching itself to the Apache Tomcat Java servlet and web server.[^1]  |
| [S1192](https://attack.mitre.org/software/S1192) | NICECURL | NICECURL has provided an arbitrary command execution interface.[^1]   |
| [S1227](https://attack.mitre.org/software/S1227) | StarProxy | StarProxy has used the command line for execution of commands.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has launched a reverse shell using a provided command line.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Script blocking extensions can help prevent the execution of scripts and HTA files that may commonly be used during the exploitation process. For malicious code served up through ads, adblockers can help prevent that code from executing in the first place. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | When PowerShell is necessary, consider restricting PowerShell execution policy to administrators. Be aware that there are methods of bypassing the PowerShell execution policy, depending on environment configuration.[^2] <br><br>PowerShell JEA (Just Enough Administration) may also be used to sandbox administration and limit what commands admins/users can execute through remote PowerShell sessions.[^1]  |
| [[kb/mitre/attack/mitigations/M1033-limit-software-installation\|M1033]] | Limit Software Installation | Prevent user installation of unrequired command and scripting interpreters. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^1]  |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent [[kb/mitre/attack/techniques/T1059.005-visual-basic\|Visual Basic]] and [[kb/mitre/attack/techniques/T1059.007-javascript\|JavaScript]] scripts from executing potentially malicious downloaded content [^1] . |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Disable or remove any unnecessary or unused shells or interpreters. |
| [[kb/mitre/attack/mitigations/M1045-code-signing\|M1045]] | Code Signing | Where possible, only permit execution of signed scripts. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Inventory systems for unauthorized command and scripting interpreter installations. |
| [[kb/mitre/attack/mitigations/M1049-antivirus-antimalware\|M1049]] | Antivirus/Antimalware | Anti-virus can be used to automatically quarantine suspicious files.  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1059.007-javascript\|T1059.007]] | JavaScript |
| [[kb/mitre/attack/techniques/T1059.002-applescript\|T1059.002]] | AppleScript |
| [[kb/mitre/attack/techniques/T1059.010-autohotkey-and-autoit\|T1059.010]] | AutoHotKey & AutoIT |
| [[kb/mitre/attack/techniques/T1059.009-cloud-api\|T1059.009]] | Cloud API |
| [[kb/mitre/attack/techniques/T1059.008-network-device-cli\|T1059.008]] | Network Device CLI |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell |
| [[kb/mitre/attack/techniques/T1059.004-unix-shell\|T1059.004]] | Unix Shell |
| [[kb/mitre/attack/techniques/T1059.011-lua\|T1059.011]] | Lua |
| [[kb/mitre/attack/techniques/T1059.013-container-cli-api\|T1059.013]] | Container CLI／API |
| [[kb/mitre/attack/techniques/T1059.006-python\|T1059.006]] | Python |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell |
| [[kb/mitre/attack/techniques/T1059.012-hypervisor-cli\|T1059.012]] | Hypervisor CLI |
| [[kb/mitre/attack/techniques/T1059.005-visual-basic\|T1059.005]] | Visual Basic |

 [^1]: [Remote Shell Execution in Python](https://www.thepythoncode.com/article/executing-bash-commands-remotely-in-python)
 [^2]: [Cisco IOS Software Integrity Assurance - Command History](https://tools.cisco.com/security/center/resources/integrity_assurance.html#23)
 [^3]: [Powershell Remote Commands](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.1)
 [^4]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^5]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^6]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)
 [^7]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^8]: [Donut Github](https://github.com/TheWover/donut)
 [^9]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^10]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
 [^11]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)
 [^12]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^13]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^14]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^15]: [FireEye Hacking Team](https://www.fireeye.com/blog/threat-research/2015/07/demonstrating_hustle.html)
 [^16]: [Nccgroup Gh0st April 2018](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)
 [^17]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^18]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^19]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
 [^20]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)
 [^21]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^22]: [Lumen Versa 2024](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)
 [^23]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^24]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
 [^25]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
 [^26]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)
 [^27]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)
 [^28]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^29]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^30]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^31]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^32]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
