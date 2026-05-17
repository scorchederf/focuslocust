---
parsed_by: focuslocust
source: mitre
type: generated
---
# Boot or Logon Initialization Scripts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1037` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Boot or Logon Initialization Scripts](../../attack/techniques/T1037-boot-or-logon-initialization-scripts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1037 |
| name | Boot or Logon Initialization Scripts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1037 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:38.910Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation:\
  \ Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform\
  \ administrative functions, which may often execute other programs or send information to an internal logging server. These\
  \ scripts can vary based on operating system and whether applied locally or remotely.  \n\nAdversaries may use these scripts\
  \ to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials\
  \ or an administrator account may be necessary. \n\nAn adversary may also be able to escalate their privileges since some\
  \ boot or logon initialization scripts run with higher privileges."
external_references:
- external_id: T1037
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1037
- description: Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved
    April 24, 2019.
  source_name: Anomali Rocke March 2019
  url: https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang
- description: 'Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.'
  source_name: Mandiant APT29 Eye Spy Email Nov 22
  url: https://www.mandiant.com/resources/blog/unc3524-eye-spy-email
id: attack-pattern--03259939-0b57-482f-8eb5-87c0e0d54334
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:48:20.077Z'
name: Boot or Logon Initialization Scripts
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
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '2.4'
```
