---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1659
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1659-content-injection
tactic:
    - Command And Control
    - Initial Access
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e., [[kb/mitre/attack/techniques/T1608.004-drive-by-target|Drive-by Target]] followed by [[kb/mitre/attack/techniques/T1189-drive-by-compromise|Drive-by Compromise]]), adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e., [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer|Ingress Tool Transfer]]) and other data to already compromised systems.[^2] <br><br>Adversaries may inject content to victim systems in various ways, including:<br><br>* From the middle, where the adversary is in-between legitimate online client-server communications (**Note:** this is similar but distinct from [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle|Adversary-in-the-Middle]], which describes AiTM activity solely within an enterprise environment) [^3] <br>* From the side, where malicious content is injected and races to the client as a fake response to requests of a legitimate online server [^4] <br><br>Content injection is often the result of compromised upstream communication channels, for example at the level of an internet service provider (ISP) as is the case with "lawful interception."[^4] [^2] [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1088](https://attack.mitre.org/software/S1088) | Disco | Disco has achieved initial access and execution through content injection into DNS,  HTTP, and SMB replies to targeted hosts that redirect them to download malicious files.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Where possible, ensure that online traffic is appropriately encrypted through services such as trusted VPNs. |

 [^1]: [EFF China GitHub Attack](https://www.eff.org/deeplinks/2015/04/china-uses-unencrypted-websites-to-hijack-browsers-in-github-attack)
 [^2]: [ESET MoustachedBouncer](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^3]: [Kaspersky Encyclopedia MiTM](https://encyclopedia.kaspersky.com/glossary/man-in-the-middle-attack/)
 [^4]: [Kaspersky ManOnTheSide](https://usa.kaspersky.com/blog/man-on-the-side/27854/)
 [^5]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
