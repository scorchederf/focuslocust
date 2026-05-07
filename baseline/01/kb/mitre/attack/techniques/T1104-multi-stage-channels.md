---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1104
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1104-multi-stage-channels
tactic:
    - Command And Control
platforms:
    - Linux
    - macOS
    - Windows
    - ESXi
permissions required:
    - none
---

## Description

Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.<br><br>Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.<br><br>The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or [[kb/mitre/attack/techniques/T1008-fallback-channels|Fallback Channels]] in case the original first-stage communication path is discovered and blocked.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Individual Uroburos implants can use multiple communication channels based on one of four available modes of operation.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | BACKSPACE attempts to avoid detection by checking a first stage command and control server to determine if it should connect to the second stage server, which performs "louder" interactions with the malware.[^1]  |
| [S0069](https://attack.mitre.org/software/S0069) | BLACKCOFFEE | BLACKCOFFEE uses Microsoft’s TechNet Web portal to obtain an encoded tag containing the IP address of a command and control server and then communicates separately with that IP address for C2. If the C2 server is discovered or shut down, the threat actors can update the encoded IP address on TechNet to maintain control of the victims’ machines.[^1]  |
| [S0220](https://attack.mitre.org/software/S0220) | Chaos | After initial compromise, Chaos will download a second stage to establish a more permanent presence on the affected system.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak can download additional modules and malware capable of using separate C2 channels.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | The Bazar loader is used to download and execute the Bazar backdoor.[^1] [^2]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 can download and execute additional payloads and modules over separate communication channels.[^2] [^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can use one C2 URL for first contact and to upload information about the host computer and two additional C2 URLs for getting commands.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | <br>Latrodectus has used a two-tiered C2 configuration with tier one nodes connecting to the victim and tier two nodes connecting to backend infrastructure.[^1]  |
| [S1206](https://attack.mitre.org/software/S1206) | JumbledPath | JumbledPath can communicate over a unique series of connections to send and retrieve data from exploited devices.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |

 [^1]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^2]: [FireEye APT17](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)
 [^3]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^4]: [Cisco Salt Typhoon FEB 2025](https://blog.talosintelligence.com/salt-typhoon-analysis/)
 [^5]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^6]: [Zscaler Bazar September 2020](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)
 [^7]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^8]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^9]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^10]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^11]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^12]: [Chaos Stolen Backdoor](http://gosecure.net/2018/02/14/chaos-stolen-backdoor-rising/)
