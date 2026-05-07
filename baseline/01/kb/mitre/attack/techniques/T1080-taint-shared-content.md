---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1080
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1080-taint-shared-content
tactic:
    - Lateral Movement
platforms:
    - Windows
    - SaaS
    - Linux
    - macOS
    - Office Suite
permissions required:
    - none
---

## Description

<br>Adversaries may deliver payloads to remote systems by adding content to shared storage locations, such as network drives or internal code repositories. Content stored on network drives or in other shared locations may be tainted by adding malicious programs, scripts, or exploit code to otherwise valid files. Once a user opens the shared tainted content, the malicious portion can be executed to run the adversary's code on a remote system. Adversaries may use tainted shared content to move laterally.<br><br>A directory share pivot is a variation on this technique that uses several other techniques to propagate malware when users access a shared network directory. It uses [[kb/mitre/attack/techniques/T1547.009-shortcut-modification|Shortcut Modification]] of directory .LNK files that use [[kb/mitre/attack/techniques/T1036-masquerading|Masquerading]] to look like the real directories, which are hidden through [[kb/mitre/attack/techniques/T1564.001-hidden-files-and-directories|Hidden Files and Directories]]. The malicious .LNK-based directories have an embedded command that executes the hidden malware file in the directory and then opens the real intended directory so that the user's expected action still occurs. When used with frequently used network directories, the technique may result in frequent reinfections and broad access to systems and potentially to new and higher privileged accounts. [^1] <br><br>Adversaries may also compromise shared network directories through binary infections by appending or prepending its code to the healthy binary on the shared network directory. The malware may modify the original entry point (OEP) of the healthy binary to ensure that it is executed before the legitimate code. The infection could continue to spread via the newly infected file when it is executed by a remote system. These infections may target both binary and non-binary formats that end with extensions including, but not limited to, .EXE, .DLL, .SCR, .BAT, and/or .VBS.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0132](https://attack.mitre.org/software/S0132) | H1N1 | H1N1 has functionality to copy itself to network shares.[^1]  |
| [S0133](https://attack.mitre.org/software/S0133) | Miner-C | Miner-C copies itself into the public folder of Network Attached Storage (NAS) devices and infects new victims who open the file.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can replace legitimate software or documents in the compromised network with their trojanized versions, in an attempt to propagate itself within the network.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has copied itself to and infected files in network drives for propagation.[^2] [^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can spread itself by infecting other portable executable files on networks shared drives.[^1] 	 |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can spread itself by infecting other remote machines via network shared drives.[^1] [^2]   |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet infects remote servers via network shares and by infecting WinCC database views with malicious code.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Protect shared folders by minimizing users who have write access. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Identify potentially malicious software that may be used to taint content or may result from it and audit and/or block the unknown programs by using application control [^1]  tools, like AppLocker, [^5]  [^4]  or Software Restriction Policies [^2]  where appropriate. [^3]  |
| [[kb/mitre/attack/mitigations/M1049-antivirus-antimalware\|M1049]] | Antivirus/Antimalware | Anti-virus can be used to automatically quarantine suspicious files.[^1]  |
| [[kb/mitre/attack/mitigations/M1050-exploit-protection\|M1050]] | Exploit Protection | Use utilities that detect or mitigate common features used in exploitation, such as the Microsoft Enhanced Mitigation Experience Toolkit (EMET). |

 [^1]: [Retwin Directory Share Pivot](https://rewtin.blogspot.ch/2017/11/abusing-user-shares-for-efficient.html)
 [^2]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
 [^3]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^4]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)
 [^5]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)
 [^6]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))
 [^7]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)
 [^8]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
 [^9]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)
 [^10]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^11]: [Cybereason Conti Jan 2021](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
 [^12]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^13]: [Softpedia MinerC](https://news.softpedia.com/news/cryptocurrency-mining-malware-discovered-targeting-seagate-nas-hard-drives-508119.shtml)
 [^14]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^15]: [TrendMicro Ursnif File Dec 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/info-stealing-file-infector-hits-us-uk/)
 [^16]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
