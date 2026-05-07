---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S9002
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S9002-diskpart
---

## Description

[[kb/mitre/attack/software/S9002-diskpart|Diskpart]] is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.[^1]   <br><br>Adversaries may abuse [[kb/mitre/attack/software/S9002-diskpart|Diskpart]] to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using [[kb/mitre/attack/software/S9002-diskpart|Diskpart]] to conduct [[kb/mitre/attack/tactics/TA0007-discovery|Discovery]] techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.[^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can execute a disk partition script file, which attempts to mount a virtual hard disk.[^1]  [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can also assign and mount virtual disks.[^1]     |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can show information about the selected disk, partition, volume, or virtual hard disk (VHD).[^1]   |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | If executed with elevated privileges, [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can list all volumes, including virtual disks.[^1]     |
| [[kb/mitre/attack/techniques/T1222.001-windows-permissions\|T1222.001]] | Windows Permissions | [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can be used to display, set, or clear attributes of a disk or volume.[^1]    |
| [[kb/mitre/attack/techniques/T1561.002-disk-structure-wipe\|T1561.002]] | Disk Structure Wipe | [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can be used to delete a partition or a volume.[^1]  [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can also be used to remove all partitions or volume formatting from the selected disk.[^2]     |

 [^1]: [Microsoft_diskpart_Feb2023](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)
 [^2]: [Trendmicro_RansomHub_Dec2024](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-ransomhub)
 [^3]: [Halcyon_CloakRansomware_Dec2024](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)
