---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1489
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1489-service-stop
tactic:
    - Impact
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

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.[^4] [^6]  <br><br>Adversaries may accomplish this by disabling individual services of high importance to an organization, such as `MSExchangeIS`, which will make Exchange content inaccessible.[^6]  In some cases, adversaries may stop or disable many or all services to render systems unusable.[^4]  Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct [[kb/mitre/attack/techniques/T1485-data-destruction|Data Destruction]] or [[kb/mitre/attack/techniques/T1486-data-encrypted-for-impact|Data Encrypted for Impact]] on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure.[^2] [^5] <br><br>Threat actors may also disable or stop service in cloud environments. For example, by leveraging the `DisableAPIServiceAccess` API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization.[^3] [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer uses the API call `ChangeServiceConfigW` to disable all services on the affected system.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry attempts to kill processes associated with Exchange, Microsoft SQL Server, and MySQL to make it possible to encrypt their data stores.[^1] [^2]  |
| [S0400](https://attack.mitre.org/software/S0400) | RobbinHood | RobbinHood stops 181 Windows services on the system before beginning the encryption process.[^1]   |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to stop services on the infected host.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has called `kill.bat` for stopping services, disabling services and killing processes.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has stopped SQL services to ensure it can encrypt any database.[^1]   |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can terminate system processes and services, some of which relate to backup software.[^1]  |
| [S0481](https://attack.mitre.org/software/S0481) | Ragnar Locker | Ragnar Locker has attempted to stop services associated with business applications and databases to release the lock on files used by these applications so they may be encrypted.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil has the capability to stop services and kill processes.[^1] [^2]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has the capability to stop processes and services.[^1]  |
| [S0556](https://attack.mitre.org/software/S0556) | Pay2Key | Pay2Key can stop the MS SQL service at the end of the encryption process to release files locked by the service.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can stop up to 146 Windows services related to security, backup, database, and email solutions through the use of `net stop`.[^1]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex can stop and disable services on the system.[^1]   |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack can kill processes and delete services.[^1]  |
| [S0583](https://attack.mitre.org/software/S0583) | Pysa | Pysa can stop services and processes.[^1]   |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer’s data wiper module writes zeros into the registry keys in `SYSTEM\CurrentControlSet\Services` to render a system inoperable.[^1]  |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS stops database, data backup solution, antivirus, and ICS-related processes.[^1] [^2] [^3]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk terminates various processes to get the user to reboot the victim machine.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop can kill several processes and services related to backups and security solutions.[^1] [^2]   |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba has a hardcoded list of services and processes to terminate.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk can stop specific services related to backups.[^1] [^2] [^3]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon looks for and attempts to stop database processes.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol will terminate services using the Service Control Manager (SCM) API.[^1]   |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor can disconnect all network adapters on a compromised host using `powershell -Command "Get-WmiObject -class Win32_NetworkAdapter \| ForEach { If ($.NetEnabled) { $.Disable() } }" > NUL`.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper has the ability to stop the Volume Shadow Copy service.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has terminated specific processes before encryption.[^1]  |
| [S1058](https://attack.mitre.org/software/S1058) | Prestige | Prestige has attempted to stop the MSSQL Windows service to ensure successful encryption using `C:\Windows\System32\net.exe stop MSSQLSERVER`.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat has the ability to stop VM services on compromised networks.[^2] [^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can use `RmShutDown` to kill  applications and services using the resources that are targeted for encryption.[^1]  |
| [S1096](https://attack.mitre.org/software/S1096) | Cheerscrypt | Cheerscrypt has the ability to terminate VM processes on compromised hosts through execution of `esxcli vm process kill`.[^1] <br> |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can issue a command to kill a process on compromised hosts.[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP can disable critical services and processes.[^1]  |
| [S1181](https://attack.mitre.org/software/S1181) | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware can terminate running services.[^1]  |
| [S1191](https://attack.mitre.org/software/S1191) | Megazord | Megazord has the ability to terminate a list of services and processes.[^1]  |
| [S1194](https://attack.mitre.org/software/S1194) | Akira _v2 | Akira _v2 can stop running virtual machines.[^1] [^2] [^3]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can automatically terminate processes that may interfere with the encryption or file extraction processes.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can terminate targeted processes and services related to security, backup, database management, and other applications that could stop or interfere with encryption.[^1] [^4] [^2] [^3]  |
| [S1211](https://attack.mitre.org/software/S1211) | Hannotog | Hannotog can stop Windows services.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub has the ability to terminate specified services.[^1]  |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA can start and stop the `vmsyslogd` service.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can terminate specific services on compromised hosts.[^3] [^1] [^2] [^4]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has the capability to terminate services related to backups, security, databases, communication, filesharing and websites.[^1] [^2] [^3]  Medusa Ransomware has also utilized the `taskkill /F /IM <process> /T` command to stop targeted processes and `net stop <process>` command to stop designated services.[^2] [^3]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has terminated Chrome and Brave browsers using the `taskkill` command on Windows and the `killall` command on other systems such as Linux and macOS.[^1]  InvisibleFerret has also utilized it’s `ssh_kill` command to terminate Chrome and Brave browser processes.[^2]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has terminated active processes and services based on a hardcoded list using the `CloseServiceHandle()` function.[^1]  Embargo has also leveraged MS4Killer to terminate processes contained in an embedded list of security software process names that were XOR-encrypted.[^2]  |
| [S9013](https://attack.mitre.org/software/S9013) | DRYHOOK | DRYHOOK has terminated all instances of the `cgi-server` process before activating the modified DSAuth.pm file.[^1]  |
| [S9014](https://attack.mitre.org/software/S9014) | PHASEJAM | PHASEJAM has disabled the `cgi-server` process on Ivanti Connect Secure appliances.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has terminated an existing process to ensure that its own new process can execute.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[kb/mitre/attack/mitigations/M1024-restrict-registry-permissions\|M1024]] | Restrict Registry Permissions | Ensure proper registry permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Operate intrusion detection, analysis, and response systems on a separate network from the production environment to lessen the chances that an adversary can see and interfere with critical response functions. |
| [[kb/mitre/attack/mitigations/M1060-out-of-band-communications-channel\|M1060]] | Out-of-Band Communications Channel | Develop and enforce security policies that include the use of out-of-band communication channels for critical communications during a security incident.[^1]  |

 [^1]: [AWS DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)
 [^2]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)
 [^3]: [Datadog Security Labs Cloud Persistence 2025](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/)
 [^4]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^5]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
 [^6]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
 [^7]: [Unit42 Clop April 2021](https://unit42.paloaltonetworks.com/clop-ransomware/)
 [^8]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^9]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^10]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^11]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
 [^12]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^13]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
 [^14]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
 [^15]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^16]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^17]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^18]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^19]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
 [^20]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
 [^21]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
 [^22]: [Sophos BlackCat Jul 2022](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)
 [^23]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^24]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^25]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
 [^26]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^27]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^28]: [CarbonBlack RobbinHood May 2019](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
 [^29]: [SentinelOne LockBit 2.0](https://www.sentinelone.com/anthology/lockbit-2-0/)
 [^30]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
 [^31]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^32]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^33]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
 [^34]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^35]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^36]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^37]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^38]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^39]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
 [^40]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
 [^41]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^42]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^43]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
 [^44]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)
 [^45]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
 [^46]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^47]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^48]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
 [^49]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^50]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^51]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^52]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
 [^53]: [FireEye Ransomware Feb 2020](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
 [^54]: [Palo Alto Unit 42 EKANS](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)
 [^55]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^56]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)
 [^57]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
 [^58]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^59]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
 [^60]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
 [^61]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^62]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
 [^63]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^64]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
 [^65]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^66]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^67]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^68]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^69]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
 [^70]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
