---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1491
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1491-defacement
tactic:
    - Impact
platforms:
    - Windows
    - IaaS
    - Linux
    - macOS
    - ESXi
permissions required:
    - none
---

## Description

Adversaries may modify visual content available internally or externally to an enterprise network, thus affecting the integrity of the original content. Reasons for [[kb/mitre/attack/techniques/T1491-defacement|Defacement]] include delivering messaging, intimidation, or claiming (possibly false) credit for an intrusion. Disturbing or offensive images may be used as a part of [[kb/mitre/attack/techniques/T1491-defacement|Defacement]] in order to cause user discomfort, or to pressure compliance with accompanying messages. <br>

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1053-data-backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.<br> |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1491.002-external-defacement\|T1491.002]] | External Defacement |
| [[kb/mitre/attack/techniques/T1491.001-internal-defacement\|T1491.001]] | Internal Defacement |

 [^1]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)
