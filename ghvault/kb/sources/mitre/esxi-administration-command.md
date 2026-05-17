---
parsed_by: focuslocust
source: mitre
type: generated
---
# ESXi Administration Command

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1675` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ESXi Administration Command](../../attack/techniques/T1675-esxi-administration-command.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1675 |
| name | ESXi Administration Command |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1675 |

## Preserved Source Material

```yaml
created: '2025-03-28T14:01:52.810Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi\
  \ virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow\
  \ for remote management from the ESXi server. The tools daemon service runs as `vmtoolsd.exe` on Windows guest operating\
  \ systems, `vmware-tools-daemon` on macOS, and `vmtoolsd ` on Linux.(Citation: Broadcom VMware Tools Services) \n\nAdversaries\
  \ may leverage a variety of tools to execute commands on ESXi-hosted VMs – for example, by using the vSphere Web Services\
  \ SDK to programmatically execute commands and scripts via APIs such as `StartProgramInGuest`, `ListProcessesInGuest`, \
  \ `ListFileInGuest`, and `InitiateFileTransferFromGuest`.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day\
  \ 2023)(Citation: Broadcom Running Guest OS Operations) This may enable follow-on behaviors on the guest VMs, such as [File\
  \ and Directory Discovery](https://attack.mitre.org/techniques/T1083), [Data from Local System](https://attack.mitre.org/techniques/T1005),\
  \ or [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). "
external_references:
- external_id: T1675
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1675
- description: Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by
    Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.
  source_name: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023
  url: https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/
- description: Broadcom. (n.d.). Running Guest OS Operations. Retrieved March 28, 2025.
  source_name: Broadcom Running Guest OS Operations
  url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/web-services-sdk-programming-guide/virtual-machine-guest-operations/running-guest-os-operations.html
- description: Broadcom. (n.d.). VMware Tools Services. Retrieved March 28, 2025.
  source_name: Broadcom VMware Tools Services
  url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-4-0/vmware-tools-administration-12-4-0/introduction-to-vmware-tools/vmware-tools-service.html
id: attack-pattern--31e5011f-090e-45be-9bb6-17a1c5e8219b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-04-16T14:57:47.078Z'
name: ESXi Administration Command
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
x_mitre_remote_support: false
x_mitre_version: '1.0'
```
