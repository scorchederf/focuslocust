---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1561
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1561-disk-wipe
tactic:
    - Impact
platforms:
    - Linux
    - macOS
    - Windows
    - Network Devices
permissions required:
    - none
---

## Description

Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot record (MBR). A complete wipe of all disk sectors may be attempted.<br><br>To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]], [[kb/mitre/attack/techniques/T1003-os-credential-dumping|OS Credential Dumping]], and [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares|SMB/Windows Admin Shares]].[^2] <br><br>On network devices, adversaries may wipe configuration files and other data from the device using [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] commands such as `erase`.[^1] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1053-data-backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1561.002-disk-structure-wipe\|T1561.002]] | Disk Structure Wipe |
| [[kb/mitre/attack/techniques/T1561.001-disk-content-wipe\|T1561.001]] | Disk Content Wipe |

 [^1]: [erase_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/D_through_E.html#wp3557227463)
 [^2]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
 [^3]: [Microsoft Sysmon v6 May 2017](https://docs.microsoft.com/sysinternals/downloads/sysmon)
 [^4]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)
