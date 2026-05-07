---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1680
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1680-local-storage-discovery
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

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform Lateral Movement, or as a precursor to [[kb/mitre/attack/techniques/T1006-direct-volume-access|Direct Volume Access]]. <br><br>On ESXi systems, adversaries may use [[kb/mitre/attack/techniques/T1059.012-hypervisor-cli|Hypervisor CLI]] commands such as `esxcli` to list storage connected to the host as well as `.vmdk` files.[^7] [^5] <br><br>On Windows systems, adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive` in PowerShell to retrieve drives and may additionally use Windows API functions such as `GetDriveType`.[^6] [^1] <br><br>Linux has commands such as `parted`, `lsblk`, `fdisk`, `lshw`, and `df` that can list information about disk partitions such as size, type, file system types, and free space. The command `diskutil` on MacOS can be used to list disks while `system_profiler SPStorageDataType` can additionally show information such as a volume’s mount path, file system, and the type of drive in the system. <br><br>Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as `describe volume` in AWS, `gcloud compute disks list` in GCP, and `az disk list` in Azure.[^2] [^4] [^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has collected a list of all mapped drives on the infected host.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | JHUHUGIT obtains a build identifier as well as victim hard drive information from Windows registry key `HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum`. Another JHUHUGIT variant gathers the victim storage volume serial number and the storage device name.[^1] [^2]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic collects disk space information.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains a command to collect disk drive information.[^2] [^1] [^3]  |
| [S0137](https://attack.mitre.org/software/S0137) | CORESHELL | CORESHELL collects the volume serial number from the victim and sends the information to its C2 server.[^1]  |
| [S0172](https://attack.mitre.org/software/S0172) | Reaver | Reaver collects volume serial number from the victim.[^1]  |
| [S0181](https://attack.mitre.org/software/S0181) | FALLCHILL | FALLCHILL can collect information about installed disks from the victim.[^1]  |
| [S0208](https://attack.mitre.org/software/S0208) | Pasam | Pasam creates a backdoor through which remote attackers can retrieve information like free disk space.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook can collect information about the drives available on the system.[^1]   |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc collects volume information for all drives on the system.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot gathers disk type and disk free space.[^1] [^2]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty gathers the the serial number of the main disk volume.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy collects the serial number for the storage volume C:\.[^7] [^5] [^4] [^6] [^3] [^1] [^2]  |
| [S0253](https://attack.mitre.org/software/S0253) | RunningRAT | RunningRAT gathers logical drives information and volume information.[^1]  |
| [S0259](https://attack.mitre.org/software/S0259) | InnaputRAT | InnaputRAT gathers volume drive information.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can gather information on the mapped drives and system volume serial number.[^1] [^2]  |
| [S0263](https://attack.mitre.org/software/S0263) | TYPEFRAME | TYPEFRAME can gather the disk volume information.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar gathers information on local drives.[^1]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT collects the victim’s volume serial number.[^2] [^1]  |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE has the capability to collect information on disk devices.[^1]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can collect system drive and disk size information.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can gather drive information from the victim's machine.[^1] [^2]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI can gather information on drives on the victim’s machine.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI can gather information on connected drives and disk space from the victim’s machine.[^2] [^1] [^3]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has been observed collecting victim machine volume information.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor monitors the free disk space on the system.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has called `GetLogicalDrives` to emumerate all mounted drives, and `GetDriveTypeW` to determine the drive type.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can detect drive information, including drive type, total number of bytes on disk, total number of free bytes on disk, and name of a specified volume.[^1] 	 |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to identify disk information on a compromised host.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can detect system information--including disk names, total space, and remaining space--to create a hardware profile GUID which acts as a system identifier for operators.[^2] [^1] 	 |
| [S0471](https://attack.mitre.org/software/S0471) | build_downer | build_downer has the ability to send system volume information to C2.[^1]  |
| [S0472](https://attack.mitre.org/software/S0472) | down_new | down_new has the ability to identify the system volume information of a compromised host.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger has the ability to identify the host volume ID.[^1]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can enumerate the system drives and associated system name.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can identify the hard disk volume serial number on a compromised host.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can identify system drive information on a compromised host.[^5] [^2] [^7] [^6] [^6] [^4] [^3] [^1]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang can collect disk space information on victim machines by executing [[kb/mitre/attack/software/S0096-systeminfo\|Systeminfo]].[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN has collected disk information, including type and free space available.[^1]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY can collect drive information from a compromised host.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has collected disk information from a victim machine.[^1]  |
| [S0564](https://attack.mitre.org/software/S0564) | BlackMould | BlackMould can enumerate local drives on a compromised host.[^1]  |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | TAINTEDSCRIBE can use `DriveList` to retrieve drive information.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin can report the disk space of a compromised host to C2.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has discovered system information including volume serial numbers.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk retrieves the hard disk name by calling the `CreateFileA to \\.\PHYSICALDRIVE0` API.[^1]  |
| [S0616](https://attack.mitre.org/software/S0616) | DEATHRANSOM | DEATHRANSOM can enumerate logical drives on a target system.[^1]  |
| [S0617](https://attack.mitre.org/software/S0617) | HELLOKITTY | HELLOKITTY can enumerate logical drives on a target system.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can enumerate local drives, disk type, and disk free space.[^1]  |
| [S0630](https://attack.mitre.org/software/S0630) | Nebulae | Nebulae can discover logical drive information including the drive type, free space, and volume information.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk can enumerate disk volumes, get disk information, and query service status.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can collect a system's drive information.[^2] [^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme has the ability to list drives.[^1]  |
| [S0672](https://attack.mitre.org/software/S0672) | Zox | Zox can enumerate attached drives.[^1]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma can use `GetlogicalDrives` to get a bitmask of all drives available on a compromised system. It can also use `GetDriveType` to determine if a new drive is a CD-ROM drive.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower has the ability to list local drives.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate has the ability to enumerate fixed logical drives on a targeted system.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can collect information related to a compromised host, including a list of drives.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can enumerate physical drives on a targeted host.[^3] [^4] [^2] [^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can collect information about a compromised computer's disk sizes.[^1]  |
| [S1026](https://attack.mitre.org/software/S1026) | Mongall | Mongall can identify drives on compromised hosts.[^1] <br> |
| [S1027](https://attack.mitre.org/software/S1027) | Heyoka Backdoor | Heyoka Backdoor can enumerate drives on a compromised host.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can enumerate all logical drives on a targeted machine.[^1]  |
| [S1048](https://attack.mitre.org/software/S1048) | macOS.OSAMiner | macOS.OSAMiner has checked to ensure there is enough disk space using the Unix utility `df`.[^1]  |
| [S1049](https://attack.mitre.org/software/S1049) | SUGARUSH | MoonWind can obtain the number of drives on the victim machine.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can enumerate all drives on a compromised host.[^1] [^2]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can retrieve information about storage drives from an infected machine.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can enumerate local drives.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can enumerate volumes.[^2] [^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal |  Royal can use `GetLogicalDrives` to enumerate logical drives.[^1] [^2]  |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK can discover logical drive information on compromised hosts.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to collect the C:\ drive serial number from a compromised machine.[^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can check the disk size through the values obtained with `DeviceInfo.`[^1]  |
| [S1089](https://attack.mitre.org/software/S1089) | SharpDisco | SharpDisco can use a plugin to enumerate system drives.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja can obtain information on physical drives from targeted hosts.[^1] [^2]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate uses the Delphi methods `Sysutils::DiskSize` and `GlobalMemoryStatusEx` to collect disk size and physical memory as part of the malware's anti-analysis checks for running in a virtualized environment.[^1]   |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can discover and mount hidden drives to encrypt them.[^1]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor can collect information about disk drives, their total and free space, and file system type.[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP can enumerate logical drives on targeted devices.[^1] [^2] <br> |
| [S1151](https://attack.mitre.org/software/S1151) | ZeroCleare | ZeroCleare can use the `IOCTL_DISK_GET_DRIVE_GEOMETRY_EX`, `IOCTL_DISK_GET_DRIVE_GEOMETRY`, and `IOCTL_DISK_GET_LENGTH_INFO` system calls to compute disk size.[^1]  |
| [S1168](https://attack.mitre.org/software/S1168) | SampleCheck5000 | SampleCheck5000 can create unique victim identifiers by using the compromised system’s volume ID.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can enumerate local drive configuration.[^2] [^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can enumerate local drive configuration.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has leveraged `wmic logicaldisk get` to map local network drives.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has retrieved the disk serial number of the device using WMI query `SELECT volumeserialnumber FROM win32_logicaldisk where Name =’C:` to identify the victim machine.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin has used `GetLogicalDrives()` and `EnumResourceW()` to locate mounted drives and shares.[^1] <br> |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has enumerated logical drives on infected hosts.[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | AshTag can use `volumeserialnumber` to enumerate volumes.[^1]   |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has used the Microsoft Windows native `GetLogicalDrives()` and `GetDriveType()` functions to enumerate all the drives visible to the system.[^1]  |

 [^1]: [Volexity](https://www.volexity.com/blog/2023/06/28/charming-kitten-updates-powerstar-with-an-interplanetary-twist/)
 [^2]: [AWS docs describe volumes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html)
 [^3]: [azure az disk](https://learn.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest)
 [^4]: [GCP gcloud compute disks list](https://cloud.google.com/sdk/gcloud/reference/compute/disks/list)
 [^5]: [TrendMicro ESXI Ransomware](https://www.trendmicro.com/en_us/research/22/a/analysis-and-Impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant.html)
 [^6]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^7]: [TrendMicro](https://www.trendmicro.com/en_us/research/21/e/darkside-linux-vms-targeted.html)
 [^8]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^9]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^10]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^11]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^12]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^13]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^14]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^15]: [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
 [^16]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
 [^17]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^18]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^19]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^20]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^21]: [Trend Micro KillDisk 1](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
 [^22]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^23]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^24]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
 [^25]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^26]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^27]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^28]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
 [^29]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^30]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^31]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^32]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^33]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^34]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^35]: [ATTACKIQ MUSTANG PANDA TONESHELL March 2023](https://www.attackiq.com/2023/03/23/emulating-the-politically-motivated-chinese-apt-mustang-panda/)
 [^36]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^37]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^38]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
 [^39]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^40]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^41]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^42]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^43]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
 [^44]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^45]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^46]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^47]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^48]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^49]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
 [^50]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^51]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^52]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^53]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^54]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^55]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
 [^56]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
 [^57]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^58]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^59]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^60]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
 [^61]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^62]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^63]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^64]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^65]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^66]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^67]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^68]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^69]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
 [^70]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^71]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^72]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
 [^73]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^74]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^75]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
 [^76]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^77]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^78]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^79]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^80]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^81]: [Group IB Ransomware May 2020](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)
 [^82]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^83]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)
 [^84]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^85]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^86]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^87]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
 [^88]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^89]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^90]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^91]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^92]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
 [^93]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^94]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^95]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^96]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)
 [^97]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
 [^98]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^99]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
 [^100]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^101]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
 [^102]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^103]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^104]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
 [^105]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^106]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
 [^107]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
 [^108]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^109]: [Trend Micro Royal Linux ESXi February 2023](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
 [^110]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^111]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^112]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^113]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^114]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^115]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^116]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^117]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^118]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^119]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
