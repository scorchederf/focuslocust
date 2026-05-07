---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1573
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
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1573-encrypted-channel
tactic:
    - Command And Control
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has encrypted TCP communications to evade detection.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can encrypt C2 communications.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has encrypted data before sending to the C2 server.[^1]  |
| [S0498](https://attack.mitre.org/software/S0498) | Cryptoistic | Cryptoistic can engage in encrypted communications with C2.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has used encryption for its C2 channel.[^1]   |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can use an encrypted beacon to check in with C2.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar can support encrypted communications between the client and server.[^3] [^1] [^2]  |
| [S1012](https://attack.mitre.org/software/S1012) | PowerLess | PowerLess can use an encrypted channel for C2 communications.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa has used TLS encryption to initialize a custom protocol for C2 communications.[^1]  |
| [S1046](https://attack.mitre.org/software/S1046) | PowGoop | PowGoop can receive encrypted commands from C2.[^1]  |
| [S1198](https://attack.mitre.org/software/S1198) | Gomir | Gomir uses a custom encryption algorithm for content sent to command and control infrastructure.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1020-ssl-tls-inspection\|M1020]] | SSL/TLS Inspection | SSL/TLS inspection can be used to see the contents of encrypted sessions to look for network-based indicators of malware communication protocols. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1573.001-symmetric-cryptography\|T1573.001]] | Symmetric Cryptography |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography |

 [^1]: [SANS Decrypting SSL](http://www.sans.org/reading-room/whitepapers/analyst/finding-hidden-threats-decrypting-ssl-34840)
 [^2]: [SEI SSL Inspection Risks](https://insights.sei.cmu.edu/cert/2015/03/the-risks-of-ssl-inspection.html)
 [^3]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^4]: [Secureworks BRONZE PRESIDENT December 2019](https://www.secureworks.com/research/bronze-president-targets-ngos)
 [^5]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
 [^6]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^7]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^8]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^9]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
 [^10]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^11]: [Cocomazzi FIN7 Reboot](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)
 [^12]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)
 [^13]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^14]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^15]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^16]: [Fortinet Emotet May 2017](https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-emotet-variant-part-1.html)
