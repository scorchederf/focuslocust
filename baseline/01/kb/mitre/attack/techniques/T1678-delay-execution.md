---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1678
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1678-delay-execution
tactic:
    - Stealth
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny. Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems. <br><br>Adversaries may utilize programmatic `sleep` commands or native system scheduling functionality, for example [[kb/mitre/attack/techniques/T1053-scheduled-task-job|Scheduled Task/Job]]. Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time to execute properly. Loops or otherwise needless repetitions of commands, such as `ping`, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments.[^3] [^4]  Another variation, commonly referred to as API hammering, involves making various calls to Native API functions in order to delay execution (while also potentially overloading analysis environments with junk data).[^1] [^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT can use a sleep function to delay execution.[^2] [^1]  |
| [S1230](https://attack.mitre.org/software/S1230) | HIUPAN | HIUPAN has used a config file “$.ini” to store a sleep multiplier to execute at a set interval value prior to initiating a watcher function that checks for a specific running process, that checks for removable drives and installs itself and supporting files if one is available.[^1] [^2]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has the ability to pause operations for a specified duration prior to follow-on execution of activities.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin has the ability to delay execution.[^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has leveraged the Sleep functions before and after commands to ensure execution using the hexadecimal values within commands to include `Sleep(0x2710u)` that waits 10 seconds, and `Sleep(0xEA60u)` for 60 seconds.[^1]    |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has delayed execution of its larger payloads by forking itself into background process.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has used a timeout function set to `9e5` which delays execution 900,000 milliseconds or 15 minutes to avoid detection.[^1]  |
| [S9014](https://attack.mitre.org/software/S9014) | PHASEJAM | PHASEJAM has used the `sleep` command within its code to generate a fake HTML upgrade progress bar that mimics a running process.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has embedded delayed-start logic that attempts to circumvent detection for long-term persistence.[^1] [^2]  BRICKSTORM has been observed configured with a “delay” timer built-in that waited for a hard-coded date months in the future before beginning to beacon to the configured C2 domain.[^3]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter has the ability to delay for a specified number of seconds before execution.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has used delayed execution to pause for a defined interval before performing environment discovery, repeatedly checking for specific processes, such as the `dslogserver` process, prior to continuing execution. [^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | AshTag can use a set sleep time to delay C2 beaconing.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has the ability to sleep for a certain amount of time, with the default being one minute.[^1]       |
| [S9033](https://attack.mitre.org/software/S9033) | Fooder | Fooder has used a custom delay function (`delayExecution(integer)`) and Sleep API calls (`Sleep(integer)`) to slow code execution.[^1]      |
| [S9037](https://attack.mitre.org/software/S9037) | RustyWater | RustyWater has generated random sleep intervals between C2 communication.[^1]  |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has utilized a five-second delay using `Sleep(5000)` between two of the three phases of the attack that involves file overwriting, file deletion, and system reboot.[^1] [^2]  |

 [^1]: [Joe Sec Nymaim](https://www.joesecurity.org/blog/3660886847485093803)
 [^2]: [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)
 [^3]: [Revil Independence Day](https://news.sophos.com/en-us/2021/07/04/independence-day-revil-uses-supply-chain-exploit-to-attack-hundreds-of-businesses/)
 [^4]: [Netskope Nitol](https://www.netskope.com/blog/nitol-botnet-makes-resurgence-evasive-sandbox-analysis-technique)
 [^5]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^6]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^7]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
 [^8]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
 [^9]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
 [^10]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^11]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
 [^12]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)
 [^13]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^14]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^15]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
 [^16]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
 [^17]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^18]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
 [^19]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^20]: [ESET DynoWiper Update JAN 2026](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
 [^21]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^22]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^23]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^24]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
