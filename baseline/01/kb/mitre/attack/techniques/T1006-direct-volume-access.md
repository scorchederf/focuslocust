---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1006
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1006-direct-volume-access
tactic:
    - Stealth
platforms:
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. [^2] <br><br>Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell.[^1]  Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and [[kb/mitre/attack/software/S0404-esentutl|esentutl]]) to create shadow copies or backups of data from system volumes.[^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0404-esentutl\|S0404]] | esentutl | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can use the Volume Shadow Copy service to copy locked files such as `ntds.dit`.[^2] [^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Ensure only accounts required to configure and manage backups have the privileges to do so. Monitor these accounts for unauthorized backup activity. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of behaviors related to efforts by an adversary to create backups, such as command execution or preventing API calls to backup related services. |

 [^1]: [Github PowerSploit Ninjacopy](https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Invoke-NinjaCopy.ps1)
 [^2]: [Hakobyan 2009](http://www.codeproject.com/Articles/32169/FDump-Dumping-File-Sectors-Directly-from-Disk-usin)
 [^3]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)
 [^4]: [Cary Esentutl](https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/)
