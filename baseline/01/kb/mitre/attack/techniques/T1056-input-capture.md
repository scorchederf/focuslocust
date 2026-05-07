---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1056
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/collection
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1056-input-capture
tactic:
    - Collection
    - Credential Access
platforms:
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [[kb/mitre/attack/techniques/T1056.004-credential-api-hooking|Credential API Hooking]]) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [[kb/mitre/attack/techniques/T1056.003-web-portal-capture|Web Portal Capture]]).

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy can collect mouse events.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has a module to perform any API hooking it desires.[^1]   |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos has used a compromised SSH client to capture the hostname, port, username and password used to establish an SSH connection from the compromised host.[^1] [^2]   |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can log mouse events.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can conduct mouse event logging.[^1]  |
| [[kb/mitre/attack/software/S1131-nppspy\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has collected mouse and keyboard events using “pyWinhook”.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging |
| [[kb/mitre/attack/techniques/T1056.003-web-portal-capture\|T1056.003]] | Web Portal Capture |
| [[kb/mitre/attack/techniques/T1056.002-gui-input-capture\|T1056.002]] | GUI Input Capture |
| [[kb/mitre/attack/techniques/T1056.004-credential-api-hooking\|T1056.004]] | Credential API Hooking |

 [^1]: [Adventures of a Keystroke](http://opensecuritytraining.info/Keylogging_files/The%20Adventures%20of%20a%20Keystroke.pdf)
 [^2]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^3]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^4]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^5]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^6]: [ESET Kobalos Feb 2021](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)
 [^7]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^8]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
