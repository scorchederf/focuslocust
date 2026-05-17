---
parsed_by: focuslocust
source: mitre
type: generated
---
# Software Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1518` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Software Discovery](../../attack/techniques/T1518-software-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1518 |
| name | Software Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1518 |

## Preserved Source Material

```yaml
created: '2019-09-16T17:52:44.147Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get a listing of software and software versions that are installed on a system or
  in a cloud environment. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1518)
  during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target
  and/or attempts specific actions.


  Such software may be deployed widely across the environment for configuration management or security reasons, such as [Software
  Deployment Tools](https://attack.mitre.org/techniques/T1072), and may allow adversaries broad access to infect devices or
  move laterally.


  Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are
  present or if the compromised system has a version of software that is vulnerable to [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).'
external_references:
- external_id: T1518
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1518
id: attack-pattern--e3b6daca-e963-4a69-aee6-ed4fd653ad58
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:31.671Z'
name: Software Discovery
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
- IaaS
- Linux
- macOS
- Windows
x_mitre_version: '1.5'
```
