---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1029
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1029-scheduled-transfer
tactic:
    - Exfiltration
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.<br><br>When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel|Exfiltration Over C2 Channel]] or [[kb/mitre/attack/techniques/T1048-exfiltration-over-alternative-protocol|Exfiltration Over Alternative Protocol]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL collects, compresses, encrypts, and exfiltrates data to the C2 server every 10 minutes.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT has been programmed to sleep outside local business hours (9 to 5, Monday to Friday).[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can set its Beacon payload to reach out to the C2 server on an arbitrary and random interval.[^1]  |
| [S0200](https://attack.mitre.org/software/S0200) | Dipsind | Dipsind can be configured to only run during normal working hours, which would make its communications harder to distinguish from normal traffic.[^1]  |
| [S0211](https://attack.mitre.org/software/S0211) | Linfo | Linfo creates a backdoor through which remote attackers can change the frequency at which compromised hosts contact remote C2 infrastructure.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can sleep for a given number of seconds.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar can sleep for a specific time and be set to communicate at specific intervals.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can be configured to reconnect at certain intervals.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron can be configured to exfiltrate data during nighttime or working hours.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete sends stolen data to the C2 server every 10 minutes.[^1]   |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat can sleep when instructed to do so by the C2.[^1] 	 |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has sent data back to C2 every 8 hours.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can set itself to sleep before requesting a new command from C2.[^1]  |
| [S0668](https://attack.mitre.org/software/S0668) | TinyTurla | TinyTurla contacts its C2 based on a scheduled timing set in its configuration.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has the ability to wait for a specified time interval between communicating with and executing commands from C2.[^1]  |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark can pause C2 communications for a specified time.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja can configure its agent to work only in specific time frames.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [^1]  |

 [^1]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^2]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^3]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^4]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^5]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^6]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^7]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
 [^8]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^9]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
 [^10]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^11]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^12]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^13]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^14]: [Securelist ShadowPad Aug 2017](https://securelist.com/shadowpad-in-corporate-networks/81432/)
 [^15]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^16]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)
 [^17]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^18]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
