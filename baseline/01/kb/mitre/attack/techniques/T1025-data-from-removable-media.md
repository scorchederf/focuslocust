---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1025
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1025-data-from-removable-media
tactic:
    - Collection
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[kb/mitre/attack/software/S0106-cmd|cmd]] may be used to gather information. <br><br>Some adversaries may also use [[kb/mitre/attack/techniques/T1119-automated-collection|Automated Collection]] on removable media.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0036](https://attack.mitre.org/software/S0036) | FLASHFLOOD | FLASHFLOOD searches for interesting files (either a default or customized set of file extensions) on removable media and copies them to a staging area. The default file types copied would include data copied to the drive by SPACESHIP.[^1]  |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke steals user files from removable media with file extensions and keywords that match a predefined list.[^1]  |
| [S0090](https://attack.mitre.org/software/S0090) | Rover | Rover searches for files on attached removable drives based on a predefined list of file extensions every five seconds.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | Prikormka contains a module that collects documents with certain extensions from removable media or fixed drives connected via USB.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains a module to collect data from removable drives.[^1] [^2]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec has a package that collects documents from any inserted USB sticks.[^1]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | BADNEWS copies files with certain extensions from USB devices to<br>a predefined directory.[^1]  |
| [S0136](https://attack.mitre.org/software/S0136) | USBStealer | Once a removable media device is inserted back into the first victim, USBStealer collects data from it that was exfiltrated from a second victim.[^1] [^2]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT steals files based on an extension list if a USB drive is connected to the system.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can collect jpeg files from connected MTP devices.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete can find, encrypt, and upload files from fixed and removable drives.[^1] [^2]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to collect data from USB devices.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can collect data from removable media and stage it for exfiltration.[^1] 	 |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to steal written CD images and files of interest from previously connected removable drives when they become available again.[^1]  |
| [S0538](https://attack.mitre.org/software/S0538) | Crutch | Crutch can monitor removable drives and exfiltrate files matching a given extension list.[^1]  |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive | Explosive can scan all .exe files located in the USB drive.[^1]   |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can find and collect data from removable media devices.[^1] [^2]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT has the ability to extract data from removable devices connected to the endpoint.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | The FunnyDream FilePakMonitor component has the ability to collect files from removable devices.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules capable of gathering information from USB thumb drives and CD-ROMs on the victim machine given a list of provided criteria.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1057-data-loss-prevention\|M1057]] | Data Loss Prevention | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |

 [^1]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
 [^2]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)
 [^3]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^4]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^5]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^6]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^7]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
 [^8]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
 [^9]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^10]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^11]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^12]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
 [^13]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^14]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^15]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
 [^16]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^17]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^18]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^19]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^20]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^21]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
 [^22]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^23]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^24]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
