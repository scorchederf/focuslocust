---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1120
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1120-peripheral-device-discovery
tactic:
    - Discovery
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to gather information about attached peripheral devices and components connected to a computer system.[^1] [^2]  Peripheral devices could include auxiliary resources that support a variety of functionalities such as keyboards, printers, cameras, smart card readers, or removable storage. The information may be used to enhance their awareness of the system and network environment or may be used for further actions.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX can identify removable media attached to compromised hosts.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL can list connected devices.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky can detect connected USB devices.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy can gather very specific information about attached USB devices, to include device instance ID and drive geometry.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 searches through connected drives for removable storage devices.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | A module in Prikormka collects information on available printers and disk drives.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson has the ability to discover pluggable/removable drives to extract files from.[^1] [^2]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | BADNEWS checks for new hard drives on the victim, such as USB devices, by listening for the WM_DEVICECHANGE window message.[^1] [^2]  |
| [S0136](https://attack.mitre.org/software/S0136) | USBStealer | USBStealer monitors victims for insertion of removable drives. When dropped onto a second victim, it also enumerates drives connected to the system.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can obtain a list of smart card readers attached to the victim.[^1] [^2]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind obtains the number of removable drives from the victim.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook can detect USB devices.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy enumerates information about connected storage devices.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can map UPnP ports.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry contains a thread that will attempt to scan for new attached drives every few seconds. If one is identified, it will encrypt the files on the attached device.[^1]  |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy will attempt to detect if a usable smart card is current inserted into a card reader.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT will attempt to detect if the victim system has a camera during the initial infection. njRAT can also detect any removable drives connected to the system.[^1] [^2]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete detects the insertion of new devices by listening for the WM_DEVICECHANGE window message.[^1]    |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor has a plugin that collects information about inserted storage devices, modems, and phone devices.[^1]  |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can check for connected USB devices.[^1]  |
| [S0454](https://attack.mitre.org/software/S0454) | Cadelspy | Cadelspy has the ability to steal information about printers and the documents sent to printers.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can scan for removable media which may contain documents for collection.[^1] [^2] 	 |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to identify connected Apple devices.[^1]  |
| [S0481](https://attack.mitre.org/software/S0481) | Ragnar Locker | Ragnar Locker may attempt to connect to removable drives and mapped network drives.[^1]  |
| [S0538](https://attack.mitre.org/software/S0538) | Crutch | Crutch can monitor for removable drives being plugged into the compromised machine.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet enumerates removable drives for infection.[^1]  |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker can enumerate removable drives prior to the encryption process.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT can discover pluggable/removable drives to extract files from.[^1]  |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian can scan for removable media to collect data.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can identify peripheral devices on targeted systems.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can list signed PnP drivers for smartcard readers.[^1]  |
| [S0679](https://attack.mitre.org/software/S0679) | Ferocious | Ferocious can run `GET.WORKSPACE` in Microsoft Excel to check if a mouse is present.[^1]  |
| [S0686](https://attack.mitre.org/software/S0686) | QuietSieve | QuietSieve can identify and search removable drives for specific file name extensions.[^1]  |
| [S1026](https://attack.mitre.org/software/S1026) | Mongall | Mongall can identify removable media attached to compromised hosts.[^1] <br> |
| [S1027](https://attack.mitre.org/software/S1027) | Heyoka Backdoor | Heyoka Backdoor can identify removable media attached to victim's machines.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | The FunnyDream FilepakMonitor component can detect removable drive insertion.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can check for the number of devices plugged into an infected host.[^1]  |
| [S1089](https://attack.mitre.org/software/S1089) | SharpDisco | SharpDisco has dropped a plugin to monitor external drives to `C:\Users\Public\It3.exe`.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub has the ability to monitor removable drives.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can identify external USB and hard drives for encryption and printers to print ransom notes.[^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can monitor for removable drives.[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP can identify removable drives attached to the victim's machine.[^1]  |
| [S1167](https://attack.mitre.org/software/S1167) | AcidPour | AcidPour includes functionality to identify MMC and SD cards connected to the victim device.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 has the ability to identify mounted external storage devices.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 has the ability to discover external storage devices.[^1]  |
| [S1230](https://attack.mitre.org/software/S1230) | HIUPAN | HIUPAN has checked periodically for removable drives and installs itself when a drive is detected.[^1] [^2]  |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has enumerated and overwritten files on all removeable and fixed drives.[^1]    |

 [^1]: [Peripheral Discovery Linux](https://linuxhint.com/list-usb-devices-linux/)
 [^2]: [Peripheral Discovery macOS](https://ss64.com/osx/system_profiler.html)
 [^3]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^4]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^5]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
 [^6]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^7]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^8]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^9]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^10]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^11]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^12]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
 [^13]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^14]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^15]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^16]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^17]: [EFF Manul Aug 2016](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)
 [^18]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
 [^19]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^20]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^21]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^22]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^23]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
 [^24]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^25]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^26]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^27]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^28]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^29]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^30]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^31]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^32]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
 [^33]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^34]: [Sentinel Labs WastedLocker July 2020](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
 [^35]: [ESET DynoWiper JAN 2026](https://www.eset.com/us/about/newsroom/research/eset-research-russian-sandwormapt-attacks-energy-company-poland-with-dynowiper/)
 [^36]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^37]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
 [^38]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^39]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^40]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)
 [^41]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^42]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
 [^43]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
 [^44]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^45]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^46]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^47]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^48]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^49]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
 [^50]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^51]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^52]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
