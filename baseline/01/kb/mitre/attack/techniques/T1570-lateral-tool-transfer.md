---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1570
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1570-lateral-tool-transfer
tactic:
    - Lateral Movement
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer|Ingress Tool Transfer]]) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.<br><br>Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares|SMB/Windows Admin Shares]] to connected network shares or with authenticated connections via [[kb/mitre/attack/techniques/T1021.001-remote-desktop-protocol|Remote Desktop Protocol]].[^2] <br><br>Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [[kb/mitre/attack/software/S0095-ftp|ftp]]. In some cases, adversaries may be able to leverage [[kb/mitre/attack/techniques/T1102-web-service|Web Service]]s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0029-psexec\|S0029]] | PsExec | [[kb/mitre/attack/software/S0029-psexec\|PsExec]] can be used to download or upload a file over a network share.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky searches for network drives and removable media and duplicates itself onto them.[^1]  |
| [[kb/mitre/attack/software/S0095-ftp\|S0095]] | ftp | [[kb/mitre/attack/software/S0095-ftp\|ftp]] may be abused by adversaries to transfer tools or files between systems within a compromised environment.[^1] [^2]  |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to copy files to/from a remotely connected internal system.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon attempts to copy itself to remote machines on the network.[^1]  |
| [[kb/mitre/attack/software/S0190-bitsadmin\|S0190]] | BITSAdmin | [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-bits-jobs\|BITS Jobs]] to upload and/or download files from SMB file servers.[^1]  |
| [[kb/mitre/attack/software/S0357-impacket\|S0357]] | Impacket | [[kb/mitre/attack/software/S0357-impacket\|Impacket]] has used its `wmiexec` command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks.[^1]  |
| [[kb/mitre/attack/software/S0361-expand\|S0361]] | Expand | [[kb/mitre/attack/software/S0361-expand\|Expand]] can be used to download or upload a file over a network share.[^1]  |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer attempts to copy itself to remote machines on the network.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry attempts to copy itself to remote computers after gaining access via an SMB exploit.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has copied itself to remote systems using the `service.exe` filename.[^1]  |
| [S0372](https://attack.mitre.org/software/S0372) | LockerGoga | LockerGoga has been observed moving around the victim network via SMB, indicating the actors behind this ransomware are manually copying files form computer to computer instead of self-propagating.[^1]  |
| [[kb/mitre/attack/software/S0404-esentutl\|S0404]] | esentutl | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to copy files to/from a remote share.[^1]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Operators deploying Netwalker have used psexec to copy the Netwalker payload across accessible systems.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can use [[kb/mitre/attack/software/S0160-certutil\|certutil]] for propagation on Windows hosts within intranets.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet uses an RPC server that contains a file dropping routine and support for payload version updates for P2P communications within a victim network.[^1]  |
| [S0698](https://attack.mitre.org/software/S0698) | HermeticWizard | HermeticWizard can copy files to other machines on a compromised network.[^1]  |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can download the Saint Bot malware for follow-on execution.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can replicate itself across connected servers via `psexec`.[^1]  |
| [S1132](https://attack.mitre.org/software/S1132) | IPsec Helper | IPsec Helper can download additional payloads from command and control nodes and execute them.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | <br>INC Ransomware can push its encryption executable to multiple endpoints within compromised infrastructure.[^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware spreads itself laterally by writing the JavaScript launcher file to mapped shared folders.[^1]  |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA is capable of file transfer and arbitrary command execution.[^1]  |
| [S1218](https://attack.mitre.org/software/S1218) | VIRTUALPIE | VIRTUALPIE has file transfer capabilities.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc has the ability to copy files from one location to another.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin has used [[kb/mitre/attack/software/S0029-psexec\|PsExec]] to distribute a second encryptor, named encryptor_1.exe, across the targeted environment.[^1]  |
| [S9030](https://attack.mitre.org/software/S9030) | SameCoin | SameCoin can copy its wiper executable to remote machines within the same Active Directory.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known tools and protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. [^1]  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Consider using the host firewall to restrict file sharing communications such as SMB. [^1]  |

 [^1]: [Dropbox Malware Sync](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)
 [^2]: [Unit42 LockerGoga 2019](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)
 [^3]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^4]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
 [^5]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^6]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^7]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
 [^8]: [Microsoft About BITS](https://docs.microsoft.com/en-us/windows/win32/bits/about-bits)
 [^9]: [Microsoft FTP](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)
 [^10]: [Linux FTP](https://linux.die.net/man/1/ftp)
 [^11]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)
 [^12]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^13]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^14]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)
 [^15]: [LOLBAS Expand](https://lolbas-project.github.io/lolbas/Binaries/Expand/)
 [^16]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^17]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^18]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^19]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^20]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^21]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^22]: [PsExec Russinovich](http://windowsitpro.com/systems-management/psexec)
 [^23]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^24]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^25]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
 [^26]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
 [^27]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^28]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^29]: [TechNet Copy](https://technet.microsoft.com/en-us/library/bb490886.aspx)
 [^30]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
