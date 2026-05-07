---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1204
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1204-user-execution
tactic:
    - Execution
platforms:
    - Linux
    - Windows
    - macOS
    - IaaS
    - Containers
permissions required:
    - none
---

## Description

An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of [[kb/mitre/attack/techniques/T1566-phishing|Phishing]].<br><br>While [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]] frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [[kb/mitre/attack/techniques/T1534-internal-spearphishing|Internal Spearphishing]].<br><br>Adversaries may also deceive users into performing actions such as:<br><br>* Enabling [[kb/mitre/attack/techniques/T1219-remote-access-tools|Remote Access Tools]], allowing direct control of the system to the adversary<br>* Running malicious JavaScript in their browser, allowing adversaries to [[kb/mitre/attack/techniques/T1539-steal-web-session-cookie|Steal Web Session Cookie]]s[^4] [^1] <br>* Downloading and executing malware for [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]]<br>* Coerceing users to copy, paste, and execute malicious code manually[^2] [^5] <br><br>For example, tech support scams can be facilitated through [[kb/mitre/attack/techniques/T1566-phishing|Phishing]], vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or [[kb/mitre/attack/techniques/T1219-remote-access-tools|Remote Access Tools]].[^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin execution can rely on users directly interacting with malicious LNK files.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has been distributed through a fake CAPTCHA that presents instructions to the victim to open Windows Run window (“Windows Button + R”) and paste clipboard contents (“CTRL + V”) and press “Enter” to execute a Base64-encoded PowerShell.[^3] [^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious files. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | If a link is being visited by a user, network intrusion prevention systems and systems designed to scan and remove malicious downloads can be used to block activity. |
| [[kb/mitre/attack/mitigations/M1033-limit-software-installation\|M1033]] | Limit Software Installation | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Application control may be able to prevent the running of executables masquerading as other files. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent executable files from running unless they meet a prevalence, age, or trusted list criteria and to prevent Office applications from creating potentially malicious executable content by blocking malicious code from being written to disk. Note: cloud-delivered protection must be enabled to use certain rules. [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1204.002-malicious-file\|T1204.002]] | Malicious File |
| [[kb/mitre/attack/techniques/T1204.005-malicious-library\|T1204.005]] | Malicious Library |
| [[kb/mitre/attack/techniques/T1204.003-malicious-image\|T1204.003]] | Malicious Image |
| [[kb/mitre/attack/techniques/T1204.004-malicious-copy-and-paste\|T1204.004]] | Malicious Copy and Paste |
| [[kb/mitre/attack/techniques/T1204.001-malicious-link\|T1204.001]] | Malicious Link |

 [^1]: [Krebs Discord Bookmarks 2023](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)
 [^2]: [Reliaquest-execution](https://www.reliaquest.com/blog/new-execution-technique-in-clearfake-campaign/)
 [^3]: [Telephone Attack Delivery](https://www.proofpoint.com/us/blog/threat-insight/caught-beneath-landline-411-telephone-oriented-attack-delivery)
 [^4]: [Talos Roblox Scam 2023](https://blog.talosintelligence.com/roblox-scam-overview/)
 [^5]: [proofpoint-selfpwn](https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn)
 [^6]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^7]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
 [^8]: [Netskope LummaStealer 2025](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)
 [^9]: [Qualys LummaStealer 2024](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha)
 [^10]: [Microsoft RaspberryRobin 2022](https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/)
