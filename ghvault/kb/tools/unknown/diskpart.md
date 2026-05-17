---
parsed_by: focuslocust
source: mitre
type: generated
---
# Diskpart

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S9002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Diskpart is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.  

Adversaries may abuse Diskpart to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using Diskpart to conduct Discovery techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/diskpart.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [Diskpart](https://attack.mitre.org/software/S9002) can execute a disk partition script file, which attempts to mount a virtual hard disk.(Citation: Halcyon_CloakRansomware_Dec2024) [Diskpart](https://attack.mitre.org/software/S9002) can also assign and mount virtual disks.(Citation: Halcyon_CloakRansomware_Dec2024)    |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [Diskpart](https://attack.mitre.org/software/S9002) can show information about the selected disk, partition, volume, or virtual hard disk (VHD).(Citation: Microsoft_diskpart_Feb2023)  |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | If executed with elevated privileges, [Diskpart](https://attack.mitre.org/software/S9002) can list all volumes, including virtual disks.(Citation: Halcyon_CloakRansomware_Dec2024)    |
| [T1222.001 - Windows Permissions](../../attack/techniques/T1222.001-windows-permissions.md) | explicit | source | [Diskpart](https://attack.mitre.org/software/S9002) can be used to display, set, or clear attributes of a disk or volume.(Citation: Microsoft_diskpart_Feb2023)   |
| [T1561.002 - Disk Structure Wipe](../../attack/techniques/T1561.002-disk-structure-wipe.md) | explicit | source | [Diskpart](https://attack.mitre.org/software/S9002) can be used to delete a partition or a volume.(Citation: Microsoft_diskpart_Feb2023) [Diskpart](https://attack.mitre.org/software/S9002) can also be used to remove all partitions or volume formatting from the selected disk.(Citation: Trendmicro_RansomHub_Dec2024)    |

## Source Verification

[source record](../../sources/mitre/diskpart.md)

## Evidence Excerpt

```text
created: '2026-01-26T18:36:33.410Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "[Diskpart](https://attack.mitre.org/software/S9002) is a Windows command-line utility that is used to manage\
\ the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.(Citation: Microsoft_diskpart_Feb2023)\
\  \n\nAdversaries may abuse [Diskpart](https://attack.mitre.org/software/S9002) to perform discovery and destructive actions\
\ on a system’s storage. For example, adversaries have been observed using [Diskpart](https://attack.mitre.org/software/S9002)\
\ to conduct [Discovery](https://attack.mitre.org/tactics/TA0007) techniques to enumerate disks and volumes to gather information\
\ about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite\
```
