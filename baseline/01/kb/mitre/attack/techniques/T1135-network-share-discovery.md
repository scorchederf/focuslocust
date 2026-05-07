---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1135
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1135-network-share-discovery
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

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. <br><br>File sharing over a Windows network occurs over the SMB protocol. [^2]  [^1]  [[kb/mitre/attack/software/S0039-net|Net]] can be used to query a remote system for available shared drives using the `net view \\\\remotesystem` command. It can also be used to query shared drives on the local system using `net share`. For macOS, the `sharing -l` command lists all shared points used for smb services.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has a module to enumerate network shares.[^1] [^2]  |
| [[kb/mitre/attack/software/S0039-net\|S0039]] | Net | The `net view \\remotesystem` and `net share` commands in [[kb/mitre/attack/software/S0039-net\|Net]] can be used to find shared drives and directories on remote and local systems respectively.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can query shared drives on the local system.[^1]  |
| [S0165](https://attack.mitre.org/software/S0165) | OSInfo | OSInfo discovers shares on the network[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can list local and remote shared drives and folders over SMB.[^1]  |
| [S0233](https://attack.mitre.org/software/S0233) | MURKYTOP | MURKYTOP has the capability to retrieve information about shares on remote hosts.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects a list of network shares with the command `net share`.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can scan local network for open SMB.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy identifies network drives when they are added to victim systems.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can gather network share information.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot module shareDll/mshareDll discovers network shares via the WNetOpenEnumA API.[^1] [^2]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can find shared drives on the local system.[^1]  |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer will attempt to enumerate mapped network shares to later attempt to wipe all files on those shares.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has enumerated non-hidden network shares using `WNetEnumResourceW`. [^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat can enumerate connected drives for infected host machines.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can scan for network drives which may contain documents for collection.[^1] [^2] 	 |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has used the `net view /all` command to show available shares.[^1]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can enumerate the shared folders and associated permissions for a targeted network.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can enumerate shared drives on the domain.[^1]  |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer can search for network shares on the domain or workgroup using `net view <host>`.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can enumerate remote open SMB network shares using `NetShareEnum()`.[^1] [^2]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet enumerates the directories of a network resource.[^1]  |
| [S0606](https://attack.mitre.org/software/S0606) | Bad Rabbit | Bad Rabbit enumerates open SMB shares on internal victim networks.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop can enumerate network shares.[^1]  |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker can identify network adjacent and accessible drives.[^1]  |
| [S0616](https://attack.mitre.org/software/S0616) | DEATHRANSOM | DEATHRANSOM has the ability to use loop operations to enumerate network resources.[^1]  |
| [S0617](https://attack.mitre.org/software/S0617) | HELLOKITTY | HELLOKITTY has the ability to enumerate network resources.[^1]  |
| [S0618](https://attack.mitre.org/software/S0618) | FIVEHANDS | FIVEHANDS can enumerate network shares and mounted drives on a network.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can discover shared resources using the `NetShareEnum` API call.[^1]   |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk has the ability to enumerate network shares.[^1]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon has enumerated shared folders and mapped volumes.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can use `net share` to identify network shares for use in lateral movement.[^1] [^2]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol has a `ENMDSKS` command to enumerates available network shares.[^1]   |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling has the ability to enumerate network shares.[^1]  |
| [S0686](https://attack.mitre.org/software/S0686) | QuietSieve | QuietSieve can identify and search networked drives for specific file name extensions.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can enumerate connected remote logical drives.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate shares on a compromised host.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has been used to execute `net view` to discover mapped network shares.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has enumerated shared drives on a compromised network.[^2] [^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat has the ability to discover network shares on compromised networks.[^2] [^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can enumerate the shared resources of a given IP addresses using the API call `NetShareEnum`.[^1]  |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK can use [[kb/mitre/attack/software/S0104-netstat\|netstat]] and [[kb/mitre/attack/software/S0039-net\|Net]] to discover network shares.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can check a user's access to the C$ share on a compromised machine.[^1]   |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to execute the `net view` command.[^1]  |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira can identify remote file shares for encryption.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware has the ability to check for shared network drives to encrypt.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can identify shared resources in compromised environments.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can identify and enumerate victim system network shares.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | <br>Latrodectus can run `C:\Windows\System32\cmd.exe /c net view /all` to discover network shares.[^2] [^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware can identify network shares connected to the victim machine.[^1]  |
| [S1181](https://attack.mitre.org/software/S1181) | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware can identify network shares connected to the victim machine.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can discover remote shares.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can identify network shares on compromised systems.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub has the ability to target specific network shares for encryption.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin has the ability to list network drives.[^2] [^1]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has identified networked drives.[^1] [^2] [^3]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has searched for folders, subfolders and other networked or mounted drives for follow-on encryption actions.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Enable Windows Group Policy “Do Not Allow Anonymous Enumeration of SAM Accounts and Shares” security setting to limit users who can enumerate network shares.[^1]  |

 [^1]: [TechNet Shared Folder](https://technet.microsoft.com/library/cc770880.aspx)
 [^2]: [Wikipedia Shared Resource](https://en.wikipedia.org/wiki/Shared_resource)
 [^3]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^4]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^5]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^6]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^7]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^8]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
 [^9]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^10]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
 [^11]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^12]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^13]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^14]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^15]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^16]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^17]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^18]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
 [^19]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^20]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^21]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^22]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
 [^23]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^24]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
 [^25]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^26]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^27]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^28]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^29]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^30]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^31]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^32]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^33]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^34]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^35]: [ESET Bad Rabbit](https://www.welivesecurity.com/2017/10/24/bad-rabbit-not-petya-back/)
 [^36]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^37]: [ESET Trickbot Oct 2020](https://www.welivesecurity.com/2020/10/12/eset-takes-part-global-operation-disrupt-trickbot/)
 [^38]: [Bitdefender Trickbot March 2020](https://www.bitdefender.com/files/News/CaseStudies/study/316/Bitdefender-Whitepaper-TrickBot-en-EN-interactive.pdf)
 [^39]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^40]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^41]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
 [^42]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^43]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^44]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^45]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^46]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^47]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^48]: [Sophos BlackCat Jul 2022](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)
 [^49]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^50]: [Cobalt Strike TTPs Dec 2017](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)
 [^51]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^52]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^53]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)
 [^54]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^55]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
 [^56]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^57]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^58]: [Sentinel Labs WastedLocker July 2020](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
 [^59]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^60]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^61]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
 [^62]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^63]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^64]: [Joint CSA AvosLocker Mar 2022](https://www.ic3.gov/Media/News/2022/220318.pdf)
 [^65]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^66]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^67]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)
 [^68]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^69]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^70]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
