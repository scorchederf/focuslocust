---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1651 - Cloud Administration Command

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1651` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. 

If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a Trusted Relationship to execute commands in connected virtual machines.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AADInternals](../../tools/unknown/aadinternals.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can execute commands on Azure virtual machines using the VM agent.(Citation: AADInternals Root Access to Azure VMs) |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can run commands on EC2 instances using AWS Systems Manager Run Command.(Citation: GitHub Pacu) |

## Source Verification

[source record](../../sources/mitre/cloud-administration-command.md)

## Evidence Excerpt

```text
created: '2023-03-13T15:26:11.741Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such
as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging
installed virtual machine agents. (Citation: AWS Systems Manager Run Command)(Citation: Microsoft Run Command)
If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services
to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider
or delegated administrator account may similarly be able to leverage a [Trusted Relationship](https://attack.mitre.org/techniques/T1199)
```
