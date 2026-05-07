---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1485
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1485-data-destruction
tactic:
    - Impact
platforms:
    - Containers
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.[^8] [^4] [^3] [^5] [^2] [^6]  Common operating system file deletion commands such as `del` and `rm` often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from [[kb/mitre/attack/techniques/T1561.001-disk-content-wipe|Disk Content Wipe]] and [[kb/mitre/attack/techniques/T1561.002-disk-structure-wipe|Disk Structure Wipe]] because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.<br><br>Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.[^5] [^2]  In some cases politically oriented image files have been used to overwrite data.[^4] [^3] [^5] <br><br>To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]], [[kb/mitre/attack/techniques/T1003-os-credential-dumping|OS Credential Dumping]], and [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares|SMB/Windows Admin Shares]].[^8] [^4] [^3] [^5] [^6] .<br><br>In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers.[^7] [^1]  Similarly, they may delete virtual machines from on-prem virtualized environments.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy 2 contains a "Destroy" plug-in that destroys data stored on victim hard drives by overwriting file contents.[^1] [^2]  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has a command to write random data across a file and delete it.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon attempts to overwrite operating system files and disk structures with image files.[^5] [^3] [^2]  In a later variant, randomly generated data was used for data overwrites.[^1] [^4]  |
| [[kb/mitre/attack/software/S0195-sdelete\|S0195]] | SDelete | [[kb/mitre/attack/software/S0195-sdelete\|SDelete]] deletes data in a way that makes it unrecoverable.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc can overwrite files indicated by the attacker before deleting them.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar can overwrite files with random data before deleting them.[^1]  |
| [S0341](https://attack.mitre.org/software/S0341) | Xbash | Xbash has destroyed Linux-based databases as part of its ransomware capabilities.[^1] 	 |
| [[kb/mitre/attack/software/S0364-rawdisk\|S0364]] | RawDisk | [[kb/mitre/attack/software/S0364-rawdisk\|RawDisk]] was used in Shamoon to write to protected system locations such as the MBR and disk partitions in an effort to destroy data.[^1] [^2]  |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer overwrites files locally and on remote shares.[^1] [^2]   |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill has a disk wiper module that targets files other than those in the Windows directory.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil has the capability to destroy files and folders.[^1] [^2] [^3] [^3] [^4] [^5] [^6]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer’s data wiper module clears registry keys and overwrites both ICS configuration and Windows files.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk deletes system files to make the OS unbootable. KillDisk also targets and deletes files with 35 different file extensions.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can delete specified files from a targeted system.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor can fill a victim's files and directories with zero-bytes in replacement of real content before deleting them.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can corrupt files by overwriting the first 1 MB with `0xcc` and appending random extensions.[^5] [^2] [^3] [^4] [^1] [^6]  |
| [S0693](https://attack.mitre.org/software/S0693) | CaddyWiper | CaddyWiper can work alphabetically through drives on a compromised system to take ownership of and overwrite all files.[^1] [^2]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can recursively wipe folders and files in `Windows`, `Program Files`, `Program Files(x86)`, `PerfLogs`, `Boot, System`, `Volume Information`, and `AppData` folders using `FSCTL_MOVE_FILE`. HermeticWiper can also overwrite symbolic links and big files in `My Documents` and on the Desktop with random bytes.[^1]  |
| [S1125](https://attack.mitre.org/software/S1125) | AcidRain | AcidRain performs an in-depth wipe of the target filesystem and various attached storage devices through either a data overwrite or calling various IOCTLS to erase it.[^1]  |
| [S1133](https://attack.mitre.org/software/S1133) | Apostle | Apostle initially masqueraded as ransomware but actual functionality is a data destruction tool, supported by an internal name linked to an early version, `wiper-action`. Apostle writes random data to original files after an encrypted copy is created, along with resizing the original file to zero and changing time property metadata before finally deleting the original file.[^1]  |
| [S1134](https://attack.mitre.org/software/S1134) | DEADWOOD | DEADWOOD overwrites files on victim systems with random data to effectively destroy them.[^1]  |
| [S1135](https://attack.mitre.org/software/S1135) | MultiLayer Wiper | MultiLayer Wiper deletes files on network drives, but corrupts and overwrites with random data files stored locally.[^1]  |
| [S1167](https://attack.mitre.org/software/S1167) | AcidPour | AcidPour can perform an in-depth wipe of victim filesystems and attached storage devices through either data overwrite or calling various IOCTLS to erase them, similar to AcidRain.[^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker can initiate a destructive payload depending on the operating system check through resizing and reformatting portions of the victim machine's disk, leading to system instability and potential data corruption.[^1]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has destroyed the victim’s home directory by overwriting and deleting every writable file within the user's home folder.[^1] [^3]  Shai-Hulud has also utilized the `shred` command on Linux devices.[^2]  |
| [S9030](https://attack.mitre.org/software/S9030) | SameCoin | SameCoin can overwrite designated files on targeted systems with random bytes.[^1]  |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has overwritten files with 16-byte sequences of random data generated by the Mersenne Twister algorithm using the Microsoft Windows native `CreateFileW()` function to open the file and the `SetFilePointerEx()` and `WriteFile()` functions to overwrite the file.[^1]  Additionally, versions of DynoWiper can also delete files using the `DeleteFileW` API.[^2] <br> |
| [S9039](https://attack.mitre.org/software/S9039) | LazyWiper | LazyWiper has overwritten files with pseudorandom 32‑byte sequences written at 16‑byte intervals making the file unrecoverable.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | In cloud environments, limit permissions to modify cloud bucket lifecycle policies (e.g., `PutLifecycleConfiguration` in AWS) to only those accounts that require it. In AWS environments, consider using Service Control policies to limit the use of the `PutBucketLifecycle` API call.  |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Implement multi-factor authentication (MFA) delete for cloud storage resources, such as AWS S3 buckets, to prevent unauthorized deletion of critical data and infrastructure. MFA delete requires additional authentication steps, making it significantly more difficult for adversaries to destroy data without proper credentials. This additional security layer helps protect against the impact of data destruction in cloud environments by ensuring that only authenticated actions can irreversibly delete storage or machine images. |
| [[kb/mitre/attack/mitigations/M1053-data-backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1485.001-lifecycle-triggered-deletion\|T1485.001]] | Lifecycle-Triggered Deletion |

 [^1]: [DOJ  - Cisco Insider](https://www.justice.gov/usao-ndca/pr/san-jose-man-pleads-guilty-damaging-cisco-s-network)
 [^2]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
 [^3]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^4]: [FireEye Shamoon Nov 2016](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
 [^5]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^6]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^7]: [Data Destruction - Threat Post](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/)
 [^8]: [Symantec Shamoon 2012](https://www.symantec.com/connect/blogs/shamoon-attacks)
 [^9]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^10]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^11]: [Crowdstrike WhisperGate January 2022](https://www.crowdstrike.com/blog/technical-analysis-of-whispergate-malware)
 [^12]: [Cybereason WhisperGate February 2022](https://www.cybereason.com/blog/cybereason-vs.-whispergate-wiper)
 [^13]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
 [^14]: [Microsoft WhisperGate January 2022](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
 [^15]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
 [^16]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)
 [^17]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
 [^18]: [AcidRain JAGS 2022](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)
 [^19]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
 [^20]: [Microsoft Shai-Hulud December 2025](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
 [^21]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)
 [^22]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)
 [^23]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^24]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^25]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^26]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
 [^27]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^28]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^29]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^30]: [ESET DynoWiper Update JAN 2026](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
 [^31]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^32]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^33]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^34]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)
 [^35]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^36]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)
 [^37]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
 [^38]: [ESET CaddyWiper March 2022](https://www.welivesecurity.com/2022/03/15/caddywiper-new-wiper-malware-discovered-ukraine)
 [^39]: [Cisco CaddyWiper March 2022](https://blog.talosintelligence.com/2022/03/threat-advisory-caddywiper.html)
 [^40]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)
 [^41]: [Microsoft SDelete July 2016](https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete)
 [^42]: [Securelist BlackEnergy Feb 2015](https://securelist.com/be2-extraordinary-plugins-siemens-targeting-dev-fails/68838/)
 [^43]: [ESET BlackEnergy Jan 2016](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)
 [^44]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^45]: [ESEST Black Energy Jan 2016](http://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)
 [^46]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^47]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^48]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
