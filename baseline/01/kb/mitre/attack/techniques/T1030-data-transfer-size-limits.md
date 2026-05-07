---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1030
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1030-data-transfer-size-limits
tactic:
    - Exfiltration
platforms:
    - Linux
    - macOS
    - Windows
    - ESXi
permissions required:
    - none
---

## Description

An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0030](https://attack.mitre.org/software/S0030) | Carbanak | Carbanak exfiltrates data in compressed chunks if a message is larger than 4096 bytes .[^1]  |
| [S0150](https://attack.mitre.org/software/S0150) | POSHSPY | POSHSPY uploads data in 2048-byte chunks.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike will break large data sets into smaller chunks for exfiltration.[^1]  |
| [S0170](https://attack.mitre.org/software/S0170) | Helminth | Helminth splits data into chunks up to 23 bytes and sends the data in DNS queries to its C2 server.[^1]  |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE exfiltrates command output and collected files to its C2 server in 1500-byte blocks.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel can split the data to be exilftrated into chunks that will fit in subdomains of DNS queries.[^1]  |
| [S0495](https://attack.mitre.org/software/S0495) | RDAT | RDAT can upload a file via HTTP POST response to the C2 split into 102,400-byte portions. RDAT can also download data from the C2 which is split into 81,920-byte portions.[^1] 	 |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed has divided files if the size is 0x1000000 bytes or more.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT can break large files of interest into smaller chunks to prepare them for exfiltration.[^1]  |
| [[kb/mitre/attack/software/S0699-mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports custom chunk sizes used to upload/download files.[^1] 	 |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can exfiltrate data to the C2 server in 27-character chunks.[^1]  |
| [[kb/mitre/attack/software/S1040-rclone\|S1040]] | Rclone | The [[kb/mitre/attack/software/S1040-rclone\|Rclone]] "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.[^2] [^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can split exfiltrated data that exceeds 1.33 MB in size into multiple random sized parts between 384 and 512 KB.[^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can be configured to exfiltrate files at a specified rate to evade network detection mechanisms.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
 [^3]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
 [^4]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^5]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^6]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^7]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^8]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
 [^9]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^10]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
 [^11]: [Mythc Documentation](https://docs.mythic-c2.net/)
 [^12]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
 [^13]: [Rclone](https://rclone.org)
 [^14]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^15]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
 [^16]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
