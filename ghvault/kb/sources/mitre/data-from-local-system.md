---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data from Local System

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data from Local System](../../attack/techniques/T1005-data-from-local-system.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1005 |
| name | Data from Local System |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1005 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:20.537Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual
  machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.


  Adversaries may do this using a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), such as
  [cmd](https://attack.mitre.org/software/S0106) as well as a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008),
  which have functionality to interact with the file system to gather information.(Citation: show_run_config_cmd_cisco) Adversaries
  may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on the local system.

  '
external_references:
- external_id: T1005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1005
- description: Cisco. (2022, August 16). show running-config - Cisco IOS Configuration Fundamentals Command Reference . Retrieved
    July 13, 2022.
  source_name: show_run_config_cmd_cisco
  url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_protocols_through_showmon.html#wp2760878733
- description: 'Gyler, C.,Perez D.,Jones, S.,Miller, S.. (2021, February 25). This is Not a Test: APT41 Initiates Global Intrusion
    Campaign Using Multiple Exploits. Retrieved February 17, 2022.'
  source_name: 'Mandiant APT41 Global Intrusion '
  url: https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
id: attack-pattern--3c4a2599-71ee-4405-ba1e-0e28414b4bc5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:40.839Z'
name: Data from Local System
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- William Cain
- Austin Clark, @c2defense
- Liran Ravich, CardinalOps
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
x_mitre_version: '1.8'
```
