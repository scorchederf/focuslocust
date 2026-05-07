---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1688
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1688-safe-mode-boot
tactic:
    - Defense Impairment
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may abuse Windows safe mode to disable endpoint defenses. Safe mode starts up the Windows operating system with a limited set of drivers and services. Third-party security software such as endpoint detection and response (EDR) tools may not start after booting Windows in safe mode. There are two versions of safe mode: Safe Mode and Safe Mode with Networking. It is possible to start additional services after a safe mode boot.[^4] [^2] <br><br>Adversaries may abuse safe mode to disable endpoint defenses that may not start with a limited boot. Hosts can be forced into safe mode after the next reboot via modifications to Boot Configuration Data (BCD) stores, which are files that manage boot application settings.[^5] <br><br>Adversaries may also add their malicious applications to the list of minimal services that start in safe mode by modifying relevant Registry values (i.e. [[kb/mitre/attack/techniques/T1112-modify-registry|Modify Registry]]). Malicious [[kb/mitre/attack/techniques/T1559.001-component-object-model|Component Object Model]] (COM) objects may also be registered and loaded in safe mode.[^6] [^3] [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can force a reboot in safe mode with networking.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker can restart a compromised machine in safe mode.[^2] [^1]   |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can reboot victim machines in safe mode with networking via `bcdedit /set safeboot network`.[^5] [^2] [^4] [^1] [^3]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can reboot the infected host into Safe Mode.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub can reboot targeted systems into Safe Mode prior to encryption.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can reboot targeted systems in safe mode to avoid detection.[^1] [^2]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has used a DLL variant of MDeployer to disable security solutions through Safe Mode.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Restrict administrator accounts to as few individuals as possible, following least privilege principles, that may be abused to remotely boot a machine in safe mode.[^1]  |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Ensure that endpoint defenses run in safe mode.[^1]  |

 [^1]: [BleepingComputer REvil 2021](https://www.bleepingcomputer.com/news/security/revil-ransomware-has-a-new-windows-safe-mode-encryption-mode/)
 [^2]: [Sophos Safe Mode Boot](https://www.sophos.com/en-us/blog/snatch-ransomware-reboots-pcs-into-safe-mode-to-bypass-protection)
 [^3]: [Cybereason safe mode boot](https://www.cybereason.com/blog/research/medusalocker-ransomware)
 [^4]: [Microsoft Windows Startup Settings](https://support.microsoft.com/en-us/windows/windows-startup-settings-1af6ec8c-4d4a-4b23-adb7-e76eef0b847f)
 [^5]: [Microsoft bcdedit](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit)
 [^6]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)
 [^7]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
 [^8]: [Costa AvosLocker May 2022](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
 [^9]: [Trend Micro AvosLocker Apr 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
 [^10]: [Avertium Black Basta June 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
 [^11]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^12]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
 [^13]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
 [^14]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
 [^15]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^16]: [BushidoToken Qilin RaaS JUN 2024](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)
 [^17]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^18]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
