---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1490
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1490-inhibit-system-recovery
tactic:
    - Impact
platforms:
    - Containers
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery.[^4] [^2]  This may deny access to available backups and recovery options.<br><br>Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of [[kb/mitre/attack/techniques/T1485-data-destruction|Data Destruction]] and [[kb/mitre/attack/techniques/T1486-data-encrypted-for-impact|Data Encrypted for Impact]].[^4] [^2]  Furthermore, adversaries may disable recovery notifications, then corrupt backups.[^9] <br><br>A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:<br><br>* `vssadmin.exe` can be used to delete all volume shadow copies on a system - `vssadmin.exe delete shadows /all /quiet`<br>* [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation|Windows Management Instrumentation]] can be used to delete volume shadow copies - `wmic shadowcopy delete`<br>* `wbadmin.exe` can be used to delete the Windows Backup Catalog - `wbadmin.exe delete catalog -quiet`<br>* `bcdedit.exe` can be used to disable automatic Windows recovery features by modifying boot configuration data - `bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no`<br>* `REAgentC.exe` can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected system<br>* `diskshadow.exe` can be used to delete all volume shadow copies on a system - `diskshadow delete shadows all` [^5]  [^6] <br><br>On network devices, adversaries may leverage [[kb/mitre/attack/techniques/T1561-disk-wipe|Disk Wipe]] to delete backup firmware images and reformat the file system, then [[kb/mitre/attack/techniques/T1529-system-shutdown-reboot|System Shutdown/Reboot]] to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations.<br><br>On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support [[kb/mitre/attack/techniques/T1486-data-encrypted-for-impact|Data Encrypted for Impact]], preventing them from being leveraged as backups (e.g., via ` vim-cmd vmsvc/snapshot.removeall`).[^3] <br><br>Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or through folders that sync to cloud services.[^8]  In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios.[^1] [^7] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0132](https://attack.mitre.org/software/S0132) | H1N1 | H1N1 disable recovery options and deletes shadow copies from the victim.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can can remove all system restore points.[^1]  |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer uses the native Windows utilities `vssadmin`, `wbadmin`, and `bcdedit` to delete and disable operating system recovery features such as the Windows backup catalog and Windows Automatic Repair.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry uses `vssadmin`, `wbadmin`, `bcdedit`, and `wmic` to delete and disable operating system recovery features.[^3] [^1] [^2]  |
| [S0389](https://attack.mitre.org/software/S0389) | JCry | JCry has been observed deleting shadow copies to ensure that data cannot be restored easily.[^1] 	 |
| [S0400](https://attack.mitre.org/software/S0400) | RobbinHood | RobbinHood deletes shadow copies to ensure that all the data cannot be restored easily.[^1]   |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has used `vssadmin Delete Shadows /all /quiet` to to delete volume shadow copies and `vssadmin resize shadowstorage` to force deletion of shadow copies created by third-party applications.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has attempted to delete the shadow volumes of infected machines, once before and once after the encryption process.[^1] [^2]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can delete the infected system's Shadow Volumes to prevent recovery.[^1] [^2]  |
| [S0481](https://attack.mitre.org/software/S0481) | Ragnar Locker | Ragnar Locker can delete volume shadow copies using `vssadmin delete shadows /all /quiet`.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can use vssadmin to delete volume shadow copies and bcdedit to disable recovery features.[^5] [^3] [^8] [^1] [^6] [^4] [^7] [^2] [^9]  |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer attempts to remove the backup shadow files from the host using `vssadmin.exe Delete Shadows /All /Quiet`.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can delete Windows Volume Shadow Copies using `vssadmin`.[^1]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex has deleted volume shadow copies using `vssadmin.exe`.[^1]  |
| [S0583](https://attack.mitre.org/software/S0583) | Pysa | Pysa has the functionality to delete shadow copies.[^1]   |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS removes backups of Volume Shadow Copies to disable any restoration capabilities.[^1] [^2]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker resets system restore points and deletes backup files.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop can delete the shadow volumes with `vssadmin Delete Shadows /all /quiet` and can use bcdedit to disable recovery options.[^1]  |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker can delete shadow volumes.[^1] [^2] [^3]   |
| [S0616](https://attack.mitre.org/software/S0616) | DEATHRANSOM | DEATHRANSOM can delete volume shadow copies on compromised hosts.[^1]  |
| [S0617](https://attack.mitre.org/software/S0617) | HELLOKITTY | HELLOKITTY can delete volume shadow copies on compromised hosts.[^1]  |
| [S0618](https://attack.mitre.org/software/S0618) | FIVEHANDS | FIVEHANDS has the ability to delete volume shadow copies on compromised hosts.[^1] [^2]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk has the ability to delete shadow volumes using `vssadmin.exe delete shadows /all /quiet`.[^1] [^2]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon deletes backups and shadow copies using native system tools.[^1] [^2]  |
| [S0654](https://attack.mitre.org/software/S0654) | ProLock | ProLock can use vssadmin.exe to remove volume shadow copies.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can delete shadow copies using the `IVssBackupComponents` COM object to call the `DeleteSnapshots` method.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can delete shadow volumes using `vssadmin.exe`.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor can use `bcdedit` to delete different boot identifiers on a compromised host; it can also use `vssadmin.exe delete shadows /all /quiet` and `C:\\Windows\\system32\\wbem\\wmic.exe shadowcopy delete`.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can disable the VSS service on a compromised host using the service control manager.[^3] [^2] [^1]  |
| [S1058](https://attack.mitre.org/software/S1058) | Prestige | Prestige can delete the backup catalog from the target system using: `c:\Windows\System32\wbadmin.exe delete catalog -quiet` and can also delete volume shadow copies using: `\Windows\System32\vssadmin.exe delete shadows /all /quiet`.[^1] <br> |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can delete shadow copies using `vssadmin.exe delete shadows /all /quiet` and `wmic.exe Shadowcopy Delete`; it can also modify the boot loader using `bcdedit /set {default} recoveryenabled No`.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can delete shadow copies using vssadmin.exe.[^9] [^3] [^5] [^1] [^6] [^8] [^4] [^7] [^7] [^2]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can delete shadow copy backups with vssadmin.exe using the command `delete shadows /all /quiet`.[^2] [^3] [^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate can delete system restore points through the command `cmd.exe /c vssadmin delete shadows /for=c: /all /quiet”`.[^1]  |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira will delete system volume shadow copies via PowerShell commands.[^2] [^1]  |
| [S1135](https://attack.mitre.org/software/S1135) | MultiLayer Wiper | MultiLayer Wiper wipes the boot sector of infected systems to inhibit system recovery.[^1]  |
| [S1136](https://attack.mitre.org/software/S1136) | BFG Agonizer | BFG Agonizer wipes the boot sector of infected machines to inhibit system recovery.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can delete volume shadow copy backups from victim machines.[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP has the ability to disable `SystemRestore` and Volume Shadow Copies.[^2] [^1]  |
| [S1162](https://attack.mitre.org/software/S1162) | Playcrypt | Playcrypt can use AlphaVSS to delete shadow copies.[^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware deletes all volume shadow copies and restore points among other actions to inhibit system recovery following ransomware deployment.[^1]  |
| [S1181](https://attack.mitre.org/software/S1181) | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware modifies volume shadow copies during execution in a way that destroys them on the victim machine.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 has the ability to delete volume shadow copies on targeted hosts.[^2] [^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can delete volume shadow copies.[^1] [^2] [^3]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub has used `vssadmin.exe` to delete volume shadow copies.[^2] [^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can execute `vssadmin.exe delete shadows /all /quiet` to remove volume shadow copies and can disable High Availability (HA) and Distributed Resource Scheduler (DRS) in vCenter clusters.[^3] [^2] [^1] [^4]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has deleted recovery files such as shadow copies using `vssadmin.exe`.[^1] [^2] [^3] [^4]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has cleared files from the recycle bin by invoking `SHEmptyRecycleBinW()` and disabled Windows recovery through `C:\Windows\System32\cmd.exe /q /c bcdedit /set {default} recoveryenabled no`.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit the user accounts that have access to backups to only those required. In AWS environments, consider using Service Control Policies to restrict API calls to delete backups, snapshots, and images.  |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. Additionally, ensure that WinRE is enabled using the following command: `reagentc /enable`.[^1]  |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Consider using application control configured to block execution of utilities such as `diskshadow.exe` that may not be required for a given system or network to prevent potential misuse by adversaries.  |
| [[kb/mitre/attack/mitigations/M1053-data-backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^3]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. In cloud environments, enable versioning on storage objects where possible, and copy backups to other accounts or regions to isolate them from the original copies.[^1]  On ESXi servers, ensure that disk images and snapshots of virtual machines are regularly taken, with copies stored off system.[^2]  |

 [^1]: [Dark Reading Code Spaces Cyber Attack](https://www.darkreading.com/attacks-breaches/code-hosting-service-shuts-down-after-cyber-attack)
 [^2]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
 [^3]: [Cybereason](https://www.cybereason.com/blog/cybereason-vs.-blackcat-ransomware)
 [^4]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^5]: [Diskshadow](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow)
 [^6]: [Crytox Ransomware](https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware)
 [^7]: [Rhino Security Labs AWS S3 Ransomware](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)
 [^8]: [ZDNet Ransomware Backups 2020](https://www.zdnet.com/article/ransomware-victims-thought-their-backups-were-safe-they-were-wrong/)
 [^9]: [disable_notif_synology_ransom](https://x.com/TheDFIRReport/status/1498657590259109894)
 [^10]: [Avertium Black Basta June 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
 [^11]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
 [^12]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^13]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
 [^14]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
 [^15]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
 [^16]: [Trend Micro Black Basta Spotlight September 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)
 [^17]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
 [^18]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
 [^19]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
 [^20]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^21]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
 [^22]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
 [^23]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^24]: [Sentinel Labs WastedLocker July 2020](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
 [^25]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
 [^26]: [CarbonBlack RobbinHood May 2019](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
 [^27]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^28]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^29]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^30]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
 [^31]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
 [^32]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^33]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
 [^34]: [Palo Alto Unit 42 EKANS](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)
 [^35]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^36]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^37]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^38]: [CISA Royal AA23-061A March 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)
 [^39]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^40]: [Kroll Royal Deep Dive February 2023](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
 [^41]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^42]: [Hornet Security Avaddon June 2020](https://www.hornetsecurity.com/en/security-information/avaddon-from-seeking-affiliates-to-in-the-wild-in-2-days/)
 [^43]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^44]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
 [^45]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^46]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^47]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^48]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^49]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)
 [^50]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
 [^51]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^52]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^53]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^54]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^55]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^56]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^57]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
 [^58]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^59]: [CISA RansomHub AUG 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)
 [^60]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^61]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^62]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
 [^63]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
 [^64]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^65]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
 [^66]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)
 [^67]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^68]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
 [^69]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
 [^70]: [Talos Sodinokibi April 2019](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)
 [^71]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^72]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^73]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^74]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)
 [^75]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^76]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
 [^77]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^78]: [Tetra Defense Sodinokibi March 2020](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)
 [^79]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^80]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
 [^81]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^82]: [Sophos Qilin MSP APR 2025](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)
 [^83]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^84]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^85]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^86]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
 [^87]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^88]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
 [^89]: [Carbon Black JCry May 2019](https://www.carbonblack.com/2019/05/14/cb-tau-threat-intelligence-notification-jcry-ransomware-pretends-to-be-adobe-flash-player-update-installer/)
 [^90]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
 [^91]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^92]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^93]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)
 [^94]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
 [^95]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)
 [^96]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^97]: [Cybereason Lockbit 2.0](https://www.cybereason.com/blog/threat-analysis-report-lockbit-2.0-all-paths-lead-to-ransom)
 [^98]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
