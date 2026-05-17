---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1675 - ESXi Administration Command

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

## Summary

Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow for remote management from the ESXi server. The tools daemon service runs as `vmtoolsd.exe` on Windows guest operating systems, `vmware-tools-daemon` on macOS, and `vmtoolsd ` on Linux. 

Adversaries may leverage a variety of tools to execute commands on ESXi-hosted VMs – for example, by using the vSphere Web Services SDK to programmatically execute commands and scripts via APIs such as `StartProgramInGuest`, `ListProcessesInGuest`,  `ListFileInGuest`, and `InitiateFileTransferFromGuest`. This may enable follow-on behaviors on the guest VMs, such as File and Directory Discovery, Data from Local System, or OS Credential Dumping.

## Source Verification

[source record](../../sources/mitre/esxi-administration-command.md)

## Evidence Excerpt

```text
created: '2025-03-28T14:01:52.810Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi\
\ virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow\
\ for remote management from the ESXi server. The tools daemon service runs as `vmtoolsd.exe` on Windows guest operating\
\ systems, `vmware-tools-daemon` on macOS, and `vmtoolsd ` on Linux.(Citation: Broadcom VMware Tools Services) \n\nAdversaries\
\ may leverage a variety of tools to execute commands on ESXi-hosted VMs – for example, by using the vSphere Web Services\
\ SDK to programmatically execute commands and scripts via APIs such as `StartProgramInGuest`, `ListProcessesInGuest`, \
```
