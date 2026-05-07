---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1070
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1070-indicator-removal
tactic:
    - Stealth
platforms:
    - Containers
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Office Suite
    - Windows
permissions required:
    - none
---

## Description

Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal system behavior.<br><br>Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific, allowing adversaries to tailor modifications that minimize suspicion.<br><br>These actions may not prevent detection entirely but can delay recognition of malicious activity or reduce the fidelity of alerts by making events appear benign or consistent with routine operations. Additionally, selectively removed or modified artifacts may still be recoverable through deeper forensic analysis, though their absence or alteration can complicate timeline reconstruction and attribution.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy has removed the watermark associated with enabling the `TESTSIGNING` boot configuration option by removing the relevant strings in the `user32.dll.mui` of the system.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can overwrite Registry settings to reduce its visibility on the victim.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot deletes all artifacts associated with the malware from the infected machine.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can clean saved cookies and logins from the web browser.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can clear a memory blog in the process by overwriting it with junk bytes.[^1] 	 |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has used the “Wow64RevertWow64FsRedirection” function following attempts to delete the shadow volumes, in order to leave the system in the same state as it was prior to redirection.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has a command to delete a Registry key it uses, `\Software\Microsoft\Internet Explorer\notes`.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to clean up and remove data structures from a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0527-cspy-downloader\|S0527]] | CSPY Downloader | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] has the ability to remove values it writes to the Registry.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST removed HTTP proxy registry values to clean up traces of execution.[^1]  |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM has a function called "DeleteLeftovers" to remove certain artifacts of the attack.[^1]  |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot will delete an associated registry key if a certain server response is received.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has deleted arbitrary Registry values.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet can delete OLE Automation and SQL stored procedures used to store malicious payloads.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can uninstall malicious components from the Registry, stop processes, and clear the browser history.[^1]  |
| [S0691](https://attack.mitre.org/software/S0691) | Neoichor | Neoichor can clear the browser history on a compromised host by changing the `ClearBrowsingHistoryOnExit` value to 1 in the `HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Privacy` Registry key.[^1] <br><br> |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can remove artifacts from the compromised host, including created Registry keys.[^1]  |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] can erase file references to payloads in-memory after being reflectively loaded and executed.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro can close specific Windows Security and Internet Explorer dialog boxes to mask external connections.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can disable pop-up information about folders and desktop items and delete Registry keys to hide malicious services.[^2] [^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream has the ability to clean traces of malware deployment.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to delete created WMI objects to evade detections.[^1]  |
| [S1132](https://attack.mitre.org/software/S1132) | IPsec Helper | IPsec Helper can delete various registry keys related to its execution and use.[^1]  |
| [S1135](https://attack.mitre.org/software/S1135) | MultiLayer Wiper | MultiLayer Wiper uses a batch script to clear file system cache memory via the `ProcessIdleTasks` export in `advapi32.dll` as an anti-analysis and anti-forensics technique.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP restores the `.text` section of compromised DLLs after malicious code is loaded into memory and before the file is closed.[^1]  |
| [S1161](https://attack.mitre.org/software/S1161) | BPFDoor | BPFDoor clears the file location `/proc/<PID>/environ` removing all environment variables for the process.[^1]   |
| [S9029](https://attack.mitre.org/software/S9029) | IronWind | IronWind has used a .NET DLL named "exit-DN4-core.dll" to terminate malicious processes running on victim's systems.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |
| [[kb/mitre/attack/mitigations/M1029-remote-data-storage\|M1029]] | Remote Data Storage | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system.  |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1070.007-clear-network-connection-history-and-configurations\|T1070.007]] | Clear Network Connection History and Configurations |
| [[kb/mitre/attack/techniques/T1070.003-clear-command-history\|T1070.003]] | Clear Command History |
| [[kb/mitre/attack/techniques/T1070.008-clear-mailbox-data\|T1070.008]] | Clear Mailbox Data |
| [[kb/mitre/attack/techniques/T1070.006-timestomp\|T1070.006]] | Timestomp |
| [[kb/mitre/attack/techniques/T1070.005-network-share-connection-removal\|T1070.005]] | Network Share Connection Removal |
| [[kb/mitre/attack/techniques/T1070.010-relocate-malware\|T1070.010]] | Relocate Malware |
| [[kb/mitre/attack/techniques/T1070.009-clear-persistence\|T1070.009]] | Clear Persistence |
| [[kb/mitre/attack/techniques/T1070.004-file-deletion\|T1070.004]] | File Deletion |

 [^1]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^2]: [Donut Github](https://github.com/TheWover/donut)
 [^3]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^4]: [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
 [^5]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^6]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
 [^7]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^8]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^9]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
 [^10]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^11]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^12]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^13]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^14]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^15]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^16]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^17]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^18]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^19]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^20]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^21]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^22]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^23]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^24]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^25]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^26]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^27]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
 [^28]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
