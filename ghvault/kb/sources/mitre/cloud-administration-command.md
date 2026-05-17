---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Administration Command

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

## Generated Concept Page

- [Cloud Administration Command](../../attack/techniques/T1651-cloud-administration-command.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1651 |
| name | Cloud Administration Command |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1651 |

## Preserved Source Material

```yaml
created: '2023-03-13T15:26:11.741Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such
  as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging
  installed virtual machine agents. (Citation: AWS Systems Manager Run Command)(Citation: Microsoft Run Command)


  If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services
  to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider
  or delegated administrator account may similarly be able to leverage a [Trusted Relationship](https://attack.mitre.org/techniques/T1199)
  to execute commands in connected virtual machines.(Citation: MSTIC Nobelium Oct 2021)'
external_references:
- external_id: T1651
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1651
- description: AWS. (n.d.). AWS Systems Manager Run Command. Retrieved March 13, 2023.
  source_name: AWS Systems Manager Run Command
  url: https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html
- description: Microsoft Threat Intelligence Center. (2021, October 25). NOBELIUM targeting delegated administrative privileges
    to facilitate broader attacks. Retrieved March 25, 2022.
  source_name: MSTIC Nobelium Oct 2021
  url: https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/
- description: Microsoft. (2023, March 10). Run scripts in your VM by using Run Command. Retrieved March 13, 2023.
  source_name: Microsoft Run Command
  url: https://learn.microsoft.com/en-us/azure/virtual-machines/run-command-overview
id: attack-pattern--d94b3ae9-8059-4989-8e9f-ea0f601f80a7
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-04-15T19:59:13.081Z'
name: Cloud Administration Command
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Cisco
- Nichols Jasper
- Jared Wilson
- Caio Silva
- Adrien Bataille
- Anders Vejlby
- Nader Zaveri
- Tamir Yehuda
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_remote_support: false
x_mitre_version: '2.1'
```
