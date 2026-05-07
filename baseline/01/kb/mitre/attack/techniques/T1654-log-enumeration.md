---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1654
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1654-log-enumeration
tactic:
    - Discovery
platforms:
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records ([[kb/mitre/attack/techniques/T1087-account-discovery|Account Discovery]]), security or vulnerable software ([[kb/mitre/attack/techniques/T1518-software-discovery|Software Discovery]]), or hosts within a compromised network ([[kb/mitre/attack/techniques/T1018-remote-system-discovery|Remote System Discovery]]).<br><br>Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] on Windows to access and/or export security event information.[^4] [^3]  In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure.[^2] <br><br>Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis.<br><br>In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can collect CloudTrail event histories and CloudWatch logs.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can identify infected system log information.[^1]  |
| [S1191](https://attack.mitre.org/software/S1191) | Megazord | Megazord has the ability to print the trace, debug, error, info, and warning logs.[^1]  |
| [S1194](https://attack.mitre.org/software/S1194) | Akira _v2 | Akira _v2 can enumerate the trace, debug, error, info, and warning logs on targeted systems.[^1] [^2]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has identified .ldb and .log files stored in browser extension directories for collection and exfiltration.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit the ability to access and export sensitive logs to privileged accounts where possible. |

 [^1]: [Permiso GUI-Vil 2023](https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor/)
 [^2]: [SIM Swapping and Abuse of the Microsoft Azure Serial Console](https://www.mandiant.com/resources/blog/sim-swapping-abuse-azure-serial)
 [^3]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
 [^4]: [WithSecure Lazarus-NoPineapple Threat Intel Report 2023](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf)
 [^5]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^6]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^7]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
 [^8]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
 [^9]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
