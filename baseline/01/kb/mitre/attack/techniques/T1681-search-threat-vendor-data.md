---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1681
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1681-search-threat-vendor-data
tactic:
    - Reconnaissance
platforms:
    - PRE
permissions required:
    - none
---

## Description

Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives, or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their behavior when planning their future operations. <br><br>Adversaries have been observed replacing atomic indicators mentioned in blog posts in under a week.[^2]  Adversaries have also been seen searching for their own domain names in threat vendor data and then taking them down, likely to avoid seizure or further investigation.[^1] <br><br>This technique is distinct from [[kb/mitre/attack/techniques/T1597.001-threat-intel-vendors|Threat Intel Vendors]] in that it describes threat actors performing reconnaissance on their own activity, not in search of victim information. 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on designing defenses that are not reliant on atomic indicators. |

 [^1]: [Sentinel One Contagious Interview ClickFix September 2025](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)
 [^2]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
