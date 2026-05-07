---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1529
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1529-system-shutdown-reboot
tactic:
    - Impact
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] (e.g. `reload`).[^5] [^2]  They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools.<br><br>Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.<br><br>Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot.[^9] [^7]  Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system.[^8] [^6] [^3]  In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via [[kb/mitre/attack/techniques/T1134-access-token-manipulation|Access Token Manipulation]]).[^7] <br> In some cases, the system may not be able to boot again. <br><br>Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as [[kb/mitre/attack/techniques/T1561.002-disk-structure-wipe|Disk Structure Wipe]] or [[kb/mitre/attack/techniques/T1490-inhibit-system-recovery|Inhibit System Recovery]], to hasten the intended effects on system availability.[^1] [^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon will reboot the infected system once the wiping functionality has been completed.[^1] [^2] 	 |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can shutdown and restart remote devices.[^1]  |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer will shut down the compromised system after it is done modifying system configuration settings.[^1] [^2]  |
| [S0368](https://attack.mitre.org/software/S0368) | NotPetya | NotPetya will reboot the system one hour after infection.[^1] [^2]  |
| [S0372](https://attack.mitre.org/software/S0372) | LockerGoga | LockerGoga has been observed shutting down infected systems.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has issued a shutdown command on a victim machine that, upon reboot, will run the ransomware within a VM.[^1]  |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack can shutdown and reboot the victim machine.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk attempts to reboot the machine by terminating specific processes.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can shutdown a compromised host through execution of `ExitWindowsEx` with the `EXW_SHUTDOWN` flag.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can initiate a system shutdown.[^1] [^2]  |
| [S1033](https://attack.mitre.org/software/S1033) | DCSrv | DCSrv has a function to sleep for two hours before rebooting the system.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker’s Linux variant has terminated ESXi virtual machines.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta has used `ShellExecuteA` to shut down and restart the victim system.[^1]   |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate has used the `shutdown`command to shut down and/or restart the victim system.[^1]   |
| [S1125](https://attack.mitre.org/software/S1125) | AcidRain | AcidRain reboots the target system once the various wiping processes are complete.[^1]  |
| [S1133](https://attack.mitre.org/software/S1133) | Apostle | Apostle reboots the victim machine following wiping and related activity.[^1]  |
| [S1135](https://attack.mitre.org/software/S1135) | MultiLayer Wiper | MultiLayer Wiper reboots the infected system following wiping and related tasks to prevent system recovery.[^1]  |
| [S1136](https://attack.mitre.org/software/S1136) | BFG Agonizer | BFG Agonizer uses elevated privileges to call `NtRaiseHardError` to induce a "blue screen of death" on infected systems, causing a system crash. Once shut down, the system is no longer bootable.[^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can reboot or shutdown the targeted system or logoff the current user.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | <br>Latrodectus has the ability to restart compromised hosts.[^1]  |
| [S1167](https://attack.mitre.org/software/S1167) | AcidPour | AcidPour includes functionality to reboot the victim system following wiping actions, similar to AcidRain.[^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker can restart the victim system if it encounters an error during execution, and will forcibly shutdown the system following encryption to lock out victim users.[^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can initiate a system reboot or shutdown.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can initiate a reboot of the backup server to hinder recovery.[^1]  |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has used the Microsoft Windows native `ExitWindowsEx()` function to log off the interactive user and shutdown the system.[^1]  |

 [^1]: [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
 [^2]: [alert_TA18_106A](https://www.cisa.gov/uscert/ncas/alerts/TA18-106A)
 [^3]: [NotMe-BSOD](https://github.com/lzcapp/NotMe-BSOD)
 [^4]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^5]: [Microsoft Shutdown Oct 2017](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown)
 [^6]: [NtRaiseHardError](https://ntdoc.m417z.com/ntraiseharderror)
 [^7]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
 [^8]: [SonicWall](https://www.sonicwall.com/blog/disarming-darkgate-a-deep-dive-into-thwarting-the-latest-darkgate-variant)
 [^9]: [CrowdStrike Blog](https://www.crowdstrike.com/en-us/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^10]: [AcidRain JAGS 2022](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)
 [^11]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^12]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^13]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^14]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
 [^15]: [Wired Lockergoga 2019](https://www.wired.com/story/lockergoga-ransomware-crippling-industrial-firms/)
 [^16]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)
 [^17]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
 [^18]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^19]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^20]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^21]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
 [^22]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^23]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^24]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^25]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^26]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
 [^27]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)
 [^28]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^29]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
 [^30]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^31]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
 [^32]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^33]: [Trend Micro AvosLocker Apr 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
