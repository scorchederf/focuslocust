---
parsed_by: focuslocust
source: mitre
type: generated
---
# Hypervisor CLI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059.012` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hypervisor CLI](../../attack/techniques/T1059.012-hypervisor-cli.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1059.012 |
| name | Hypervisor CLI |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1059/012 |

## Preserved Source Material

```yaml
created: '2025-03-26T20:01:13.412Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse hypervisor command line interpreters (CLIs) to execute malicious commands. Hypervisor\
  \ CLIs typically enable a wide variety of functionality for managing both the hypervisor itself and the guest virtual machines\
  \ it hosts. \n\nFor example, on ESXi systems, tools such as `esxcli` and `vim-cmd` allow administrators to configure firewall\
  \ rules and log forwarding on the hypervisor, list virtual machines, start and stop virtual machines, and more.(Citation:\
  \ Broadcom ESXCLI Reference)(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: LOLESXi) Adversaries may\
  \ be able to leverage these tools in order to support further actions, such as [File and Directory Discovery](https://attack.mitre.org/techniques/T1083)\
  \ or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486)."
external_references:
- external_id: T1059.012
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1059/012
- description: Broadcom. (n.d.). ESXCLI Reference. Retrieved March 27, 2025.
  source_name: Broadcom ESXCLI Reference
  url: https://developer.broadcom.com/xapis/esxcli-command-reference/latest/
- description: Janantha Marasinghe. (n.d.). Living Off The Land ESXi. Retrieved April 14, 2025.
  source_name: LOLESXi
  url: https://lolesxi-project.github.io/LOLESXi/
- description: 'Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi
    Servers with Ransomware. Retrieved March 26, 2025.'
  source_name: Crowdstrike Hypervisor Jackpotting Pt 2 2021
  url: https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/
id: attack-pattern--d2d642da-61ff-4211-b4df-7923c9ca220c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-04-15T21:24:59.280Z'
name: Hypervisor CLI
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Liran Ravich, CardinalOps
- Janantha Marasinghe
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
x_mitre_remote_support: false
x_mitre_version: '1.0'
```
