---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1132
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
mitre-attack: kb/mitre/attack/techniques/T1132-data-encoding
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

Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems.[^2]  [^3]  Some data encoding systems may also result in data compression, such as gzip.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | After encrypting C2 data, BADNEWS converts it into a hexadecimal representation and then encodes it into base64.[^1]  |
| [S0132](https://attack.mitre.org/software/S0132) | H1N1 | H1N1 obfuscates C2 traffic with an altered version of base64.[^1]  |
| [S0362](https://attack.mitre.org/software/S0362) | Linux Rabbit | Linux Rabbit sends the payload from the C2 server as an encoded URL parameter. [^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used encoded data in HTTP URLs for C2.[^1] 	 |
| [[kb/mitre/attack/software/S0699-mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] provides various transform functions to encode and/or randomize C2 data.[^1] 	 |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can randomly generate and Base64 encode parameters in phishing links to defeat static detection.[^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can encode queries sent to LLMs.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1132.001-standard-encoding\|T1132.001]] | Standard Encoding |
| [[kb/mitre/attack/techniques/T1132.002-non-standard-encoding\|T1132.002]] | Non-Standard Encoding |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [Wikipedia Binary-to-text Encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding)
 [^3]: [Wikipedia Character Encoding](https://en.wikipedia.org/wiki/Character_encoding)
 [^4]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^5]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^6]: [Mythc Documentation](https://docs.mythic-c2.net/)
 [^7]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
 [^8]: [Breakdev Evilginx 2.4 SEP 2020](https://breakdev.org/evilginx-2-4-gone-phishing/)
 [^9]: [Anomali Linux Rabbit 2018](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
 [^10]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
