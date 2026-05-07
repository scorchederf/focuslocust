---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1001
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1001-data-obfuscation
tactic:
    - Command And Control
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may obfuscate command and control traffic to make it more difficult to detect.[^2]  Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, or impersonating legitimate protocols. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy may obfuscate portions of the initial C2 handshake.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum leverages the HTTP protocol for C2 communication, while hiding the actual messages in the Cookie and Set-Cookie headers of the HTTP requests.[^1]  |
| [S0495](https://attack.mitre.org/software/S0495) | RDAT | RDAT has used encoded data within subdomains as AES ciphertext to communicate from the host to the C2.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has hashed a string containing system information prior to exfiltration via POST requests.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist can embed C2 responses in the source code of a fake Flickr webpage.[^1]  |
| [S0682](https://attack.mitre.org/software/S0682) | TrailBlazer | TrailBlazer can masquerade its C2 traffic as legitimate Google Notifications HTTP requests.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can send compressed and obfuscated packets to C2.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja has the ability to modify headers and URL paths to hide malicious traffic in HTTP requests.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate will retrieved encrypted commands from its command and control server for follow-on actions such as cryptocurrency mining.[^1]  |
| [S1120](https://attack.mitre.org/software/S1120) | FRAMESTING | FRAMESTING can send and receive zlib compressed data within `POST` requests.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer encrypts the payload of HTTP POST communications using the same XOR key used for the malware's DLL payload.[^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has encoded with XOR and encrypted with RC4 its beacon.[^1]  |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate some obfuscation activity at the network level. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1001.003-protocol-or-service-impersonation\|T1001.003]] | Protocol or Service Impersonation |
| [[kb/mitre/attack/techniques/T1001.002-steganography\|T1001.002]] | Steganography |
| [[kb/mitre/attack/techniques/T1001.001-junk-data\|T1001.001]] | Junk Data |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^3]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
 [^4]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^5]: [Lumen_SystemBC_Sept2025](https://blog.lumen.com/systembc-bringing-the-noise/)
 [^6]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^7]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^8]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
 [^9]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^10]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
 [^11]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)
 [^12]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
 [^13]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
 [^14]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
