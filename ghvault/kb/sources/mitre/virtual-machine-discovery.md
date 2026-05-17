---
parsed_by: focuslocust
source: mitre
type: generated
---
# Virtual Machine Discovery

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

## Generated Concept Page

- [Virtual Machine Discovery](../../attack/techniques/T1673-virtual-machine-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1673 |
| name | Virtual Machine Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1673 |

## Preserved Source Material

```yaml
created: '2025-03-27T15:32:17.400Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor.\
  \ For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a [Hypervisor CLI](https://attack.mitre.org/techniques/T1059/012)\
  \ such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`).(Citation: Crowdstrike Hypervisor\
  \ Jackpotting Pt 2 2021)(Citation: TrendMicro Play) Adversaries may also directly leverage a graphical user interface, such\
  \ as VMware vCenter, in order to view virtual machines on a host. \n\nAdversaries may use the information from [Virtual\
  \ Machine Discovery](https://attack.mitre.org/techniques/T1673) during discovery to shape follow-on behaviors. Subsequently\
  \ discovered VMs may be leveraged for follow-on activities such as [Service Stop](https://attack.mitre.org/techniques/T1489)\
  \ or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486).(Citation: Crowdstrike Hypervisor Jackpotting\
  \ Pt 2 2021)"
external_references:
- external_id: T1673
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1673
- description: Cj Arsley Mateo, Darrel Tristan Virtusio, Sarah Pearl Camiling, Andrei Alimboyao, Nathaniel Morales, Jacob
    Santos, Earl John Bareng. (2024, July 19). Play Ransomware Group’s New Linux Variant Targets ESXi, Shows Ties With Prolific
    Puma. Retrieved March 26, 2025.
  source_name: TrendMicro Play
  url: https://www.trendmicro.com/en_us/research/24/g/new-play-ransomware-linux-variant-targets-esxi-shows-ties-with-p.html
- description: 'Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi
    Servers with Ransomware. Retrieved March 26, 2025.'
  source_name: Crowdstrike Hypervisor Jackpotting Pt 2 2021
  url: https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/
id: attack-pattern--6bc7f9aa-b91f-4b23-84b8-5e756eba68eb
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-04-15T21:24:32.155Z'
name: Virtual Machine Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Janantha Marasinghe
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
