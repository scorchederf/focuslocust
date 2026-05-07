---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1216
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1216-system-script-proxy-execution
tactic:
    - Stealth
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files.[^2]  This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.[^1] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1216.001-pubprn\|T1216.001]] | PubPrn |
| [[kb/mitre/attack/techniques/T1216.002-syncappvpublishingserver\|T1216.002]] | SyncAppvPublishingServer |

 [^1]: [GitHub Ultimate AppLocker Bypass List](https://github.com/api0cradle/UltimateAppLockerByPassList)
 [^2]: [LOLBAS Project](https://github.com/LOLBAS-Project/LOLBAS#criteria)
