---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1673 - Virtual Machine Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1673` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a Hypervisor CLI such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`). Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. 

Adversaries may use the information from Virtual Machine Discovery during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as Service Stop or Data Encrypted for Impact.

## Source Verification

[source record](../../sources/mitre/virtual-machine-discovery.md)

## Evidence Excerpt

```text
created: '2025-03-27T15:32:17.400Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor.\
\ For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a [Hypervisor CLI](https://attack.mitre.org/techniques/T1059/012)\
\ such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`).(Citation: Crowdstrike Hypervisor\
\ Jackpotting Pt 2 2021)(Citation: TrendMicro Play) Adversaries may also directly leverage a graphical user interface, such\
\ as VMware vCenter, in order to view virtual machines on a host. \n\nAdversaries may use the information from [Virtual\
\ Machine Discovery](https://attack.mitre.org/techniques/T1673) during discovery to shape follow-on behaviors. Subsequently\
```
