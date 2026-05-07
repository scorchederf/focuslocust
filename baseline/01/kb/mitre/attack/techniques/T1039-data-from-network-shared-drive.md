---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1039
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1039-data-from-network-shared-drive
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

Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[kb/mitre/attack/software/S0106-cmd|cmd]] may be used to gather information.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke steals user files from network shared drives with file extensions and keywords that match a predefined list.[^1]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | When it first starts, BADNEWS crawls the victim's mapped drives and collects documents with the following extensions: .doc, .docx, .pdf, .ppt, .pptx, and .txt.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can collect data from network drives and stage it for exfiltration.[^1] 	 |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor can collect any files found in the enumerated drivers before sending it to its C2 channel.[^1]   |

 [^1]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
 [^2]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
 [^3]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^4]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
