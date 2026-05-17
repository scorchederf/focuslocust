---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1680 - Local Storage Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1680` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform Lateral Movement, or as a precursor to Direct Volume Access. 

On ESXi systems, adversaries may use Hypervisor CLI commands such as `esxcli` to list storage connected to the host as well as `.vmdk` files.

On Windows systems, adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive` in PowerShell to retrieve drives and may additionally use Windows API functions such as `GetDriveType`.

Linux has commands such as `parted`, `lsblk`, `fdisk`, `lshw`, and `df` that can list information about disk partitions such as size, type, file system types, and free space. The command `diskutil` on MacOS can be used to list disks while `system_profiler SPStorageDataType` can additionally show information such as a volume’s mount path, file system, and the type of drive in the system. 

Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as `describe volume` in AWS, `gcloud compute disks list` in GCP, and `az disk list` in Azure.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can check the disk size through the values obtained with `DeviceInfo.`(Citation: Telefonica Snip3 December 2021) |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the system drives and associated system name.(Citation: CME Github September 2018) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including a list of drives.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/local-storage-discovery.md)

## Evidence Excerpt

```text
created: '2025-09-25T21:09:38.677Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space\
\ and volume serial number. This can be done to prepare for ransomware-related encryption, to perform [Lateral Movement](https://attack.mitre.org/tactics/TA0109),\
\ or as a precursor to [Direct Volume Access](https://attack.mitre.org/techniques/T1006). \n\nOn ESXi systems, adversaries\
\ may use [Hypervisor CLI](https://attack.mitre.org/techniques/T1059/012) commands such as `esxcli` to list storage connected\
\ to the host as well as `.vmdk` files.(Citation: TrendMicro)(Citation: TrendMicro ESXI Ransomware)\n\nOn Windows systems,\
\ adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive`\
```
