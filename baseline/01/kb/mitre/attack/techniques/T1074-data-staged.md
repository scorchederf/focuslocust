---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1074
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/collection
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1074-data-staged
tactic:
    - Collection
platforms:
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[kb/mitre/attack/techniques/T1560-archive-collected-data|Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[kb/mitre/attack/software/S0106-cmd|cmd]] and bash may be used to copy data into a staging location.[^2] <br><br>In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [[kb/mitre/attack/techniques/T1578.002-create-cloud-instance|Create Cloud Instance]] and stage data in that instance.[^1] <br><br>Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos can write captured SSH connection credentials to a file under the `/var/run` directory with a `.pid` extension for exfiltration.[^1]   |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark has stored information in folders named `U1` and `U2` prior to exfiltration.[^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can create directories to store logs and other collected data.[^1]  |
| [S1076](https://attack.mitre.org/software/S1076) | QUIETCANARY | QUIETCANARY has the ability to stage data prior to exfiltration.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1074.001-local-data-staging\|T1074.001]] | Local Data Staging |
| [[kb/mitre/attack/techniques/T1074.002-remote-data-staging\|T1074.002]] | Remote Data Staging |

 [^1]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
 [^2]: [PWC Cloud Hopper April 2017](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)
 [^3]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^4]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^5]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^6]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
