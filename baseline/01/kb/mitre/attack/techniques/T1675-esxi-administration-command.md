---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1675
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/esxi
mitre-attack: kb/mitre/attack/techniques/T1675-esxi-administration-command
tactic:
    - Execution
platforms:
    - ESXi
permissions required:
    - none
---

## Description

Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow for remote management from the ESXi server. The tools daemon service runs as `vmtoolsd.exe` on Windows guest operating systems, `vmware-tools-daemon` on macOS, and `vmtoolsd ` on Linux.[^3]  <br><br>Adversaries may leverage a variety of tools to execute commands on ESXi-hosted VMs – for example, by using the vSphere Web Services SDK to programmatically execute commands and scripts via APIs such as `StartProgramInGuest`, `ListProcessesInGuest`,  `ListFileInGuest`, and `InitiateFileTransferFromGuest`.[^1] [^2]  This may enable follow-on behaviors on the guest VMs, such as [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery|File and Directory Discovery]], [[kb/mitre/attack/techniques/T1005-data-from-local-system|Data from Local System]], or [[kb/mitre/attack/techniques/T1003-os-credential-dumping|OS Credential Dumping]]. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA can execute commands on guest virtual machines from compromised ESXi hypervisors.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | If not required, restrict the permissions of users to perform Guest Operations on ESXi-hosted VMs.[^1]  |

 [^1]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
 [^2]: [Broadcom Running Guest OS Operations](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/web-services-sdk-programming-guide/virtual-machine-guest-operations/running-guest-os-operations.html)
 [^3]: [Broadcom VMware Tools Services](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-4-0/vmware-tools-administration-12-4-0/introduction-to-vmware-tools/vmware-tools-service.html)
 [^4]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
 [^5]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)
