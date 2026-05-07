---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1543
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/containers
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1543-create-or-modify-system-process
tactic:
    - Persistence
    - Privilege Escalation
platforms:
    - Containers
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may create or modify system-level processes to repeatedly execute malicious payloads as part of persistence. When operating systems boot up, they can start processes that perform background system functions. On Windows and Linux, these system processes are referred to as services.[^2]  On macOS, launchd processes known as [[kb/mitre/attack/techniques/T1543.004-launch-daemon|Launch Daemon]] and [[kb/mitre/attack/techniques/T1543.001-launch-agent|Launch Agent]] are run to finish system initialization and load user specific parameters.[^1]  <br><br>Adversaries may install new services, daemons, or agents that can be configured to execute at startup or a repeatable interval in order to establish persistence. Similarly, adversaries may modify existing services, daemons, or agents to achieve the same effect.  <br><br>Services, daemons, or agents may be created with administrator privileges but executed under root/SYSTEM privileges. Adversaries may leverage this functionality to create or modify system processes in order to escalate privileges.[^3]   

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0401](https://attack.mitre.org/software/S0401) | Exaramel for Linux | Exaramel for Linux has a hardcoded location that it uses to achieve persistence if the startup system is Upstart or System V and it is running as root.[^1]  |
| [S1121](https://attack.mitre.org/software/S1121) | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can initialize itself as a daemon to run persistently in the background.[^1]  |
| [S1142](https://attack.mitre.org/software/S1142) | LunarMail | LunarMail can create an arbitrary process with a specified command line and redirect its output to a staging directory.[^1]  |
| [S1152](https://attack.mitre.org/software/S1152) | IMAPLoader | IMAPLoader modifies Windows tasks on the victim machine to reference a retrieved PE file through a path modification.[^1]  |
| [S1184](https://attack.mitre.org/software/S1184) | BOLDMOVE | BOLDMOVE can free all resources and terminate itself on victim machines.[^1]  |
| [S1194](https://attack.mitre.org/software/S1194) | Akira _v2 | <br>Akira _v2 can create a child process for encryption.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has created a new background session and has spawned a child process of a parent process when it determines it is not running in its intended state.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with system-level process changes and service configurations. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Restrict read/write access to system-level process files to only select privileged users who have a legitimate need to manage system services. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Ensure that Driver Signature Enforcement is enabled to restrict unsigned drivers from being installed.  |
| [[kb/mitre/attack/mitigations/M1033-limit-software-installation\|M1033]] | Limit Software Installation | Restrict software installation to trusted repositories only and be cautious of orphaned software packages. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent an application from writing a signed vulnerable driver to the system.[^1]  On Windows 10 and 11, enable Microsoft Vulnerable Driver Blocklist to assist in hardening against third party-developed drivers.[^2]    |
| [[kb/mitre/attack/mitigations/M1045-code-signing\|M1045]] | Code Signing | Enforce registration and execution of only legitimately signed service drivers where possible. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them. |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Where possible, consider enforcing the use of container services in rootless mode to limit the possibility of privilege escalation or malicious effects on the host running the container. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1543.003-windows-service\|T1543.003]] | Windows Service |
| [[kb/mitre/attack/techniques/T1543.004-launch-daemon\|T1543.004]] | Launch Daemon |
| [[kb/mitre/attack/techniques/T1543.005-container-service\|T1543.005]] | Container Service |
| [[kb/mitre/attack/techniques/T1543.001-launch-agent\|T1543.001]] | Launch Agent |
| [[kb/mitre/attack/techniques/T1543.002-systemd-service\|T1543.002]] | Systemd Service |

 [^1]: [AppleDocs Launch Agent Daemons](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
 [^2]: [TechNet Services](https://technet.microsoft.com/en-us/library/cc772408.aspx)
 [^3]: [OSX Malware Detection](https://papers.put.as/papers/macosx/2016/RSA_OSX_Malware.pdf)
 [^4]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
 [^5]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)
 [^6]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
 [^7]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
 [^8]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
 [^9]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^10]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^11]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^12]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
