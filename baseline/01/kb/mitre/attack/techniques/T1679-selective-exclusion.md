---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1679
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1679-selective-exclusion
tactic:
    - Stealth
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may intentionally exclude certain files, folders, directories, file types, or system components from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries may avoid encrypting include `.dll`, `.exe`, and `.lnk`.[^1]   <br><br>Adversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts, or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. <br><br>Exclusions may target files and components whose corruption would cause instability, break core services, or immediately expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators that could trigger alarms or otherwise inhibit achieving their goals. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has avoided specified files, file extensions and folders to ensure successful execution of the payload and continued operations of the impacted device.[^1] [^2] [^3]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has the capability to scan for file names, file extensions, and avoids pre-designated path names and file types.[^1] [^2]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has avoided encrypting specific files and directories by leveraging a regular expression within the ransomware binary.[^1]  |
| [S9030](https://attack.mitre.org/software/S9030) | SameCoin | SameCoin can avoid overwriting file names that contain “desktop.ini” and “conf.conf." [^1] <br> |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has recursively enumerated directories with the exception of the following: System32, Windows, Program Files, Program Files(x86), Temp, Recycle.Bin, $Recycle.Bin, Boot, PerfLogs, AppData, Documents and Settings.[^1] [^2]  |
| [S9039](https://attack.mitre.org/software/S9039) | LazyWiper | LazyWiper can enumerate the hostname of the system to determine if it is a domain controller and exclude it from being wiped if so.[^1]  |

 [^1]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^2]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^3]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
 [^4]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^5]: [ESET DynoWiper Update JAN 2026](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
 [^6]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^7]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^8]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^9]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
