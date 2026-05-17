---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Service Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1007` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Service Discovery](../../attack/techniques/T1007-system-service-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1007 |
| name | System Service Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1007 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:21.315Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may try to gather information about registered local system services. Adversaries may obtain information
  about services using tools as well as OS utility commands such as <code>sc query</code>, <code>tasklist /svc</code>, <code>systemctl
  --type=service</code>, and <code>net start</code>. Adversaries may also gather information about schedule tasks via commands
  such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation:
  SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)


  Adversaries may use the information from [System Service Discovery](https://attack.mitre.org/techniques/T1007) during automated
  discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts
  specific actions.'
external_references:
- external_id: T1007
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1007
- description: 'Gal Singer. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved
    May 22, 2025.'
  source_name: Aquasec Kinsing 2020
  url: https://www.aquasec.com/blog/threat-alert-kinsing-malware-container-vulnerability/
- description: 'Jia Yu Chan, Salim Bitam, Daniel Stepanic, and Seth Goodwin. (2024, December 12). Under the SADBRIDGE with
    GOSAR: QUASAR Gets a Golang Rewrite. Retrieved May 22, 2025.'
  source_name: Elastic Security Labs GOSAR 2024
  url: https://www.elastic.co/security-labs/under-the-sadbridge-with-gosar
- description: Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved
    May 22, 2025.
  source_name: SentinelLabs macOS Malware 2021
  url: https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/
- description: 'Splunk Threat Research Team , Teoderick Contreras. (2024, July 15). Breaking Down Linux.Gomir: Understanding
    this Backdoor’s TTPs. Retrieved May 22, 2025.'
  source_name: Splunk Linux Gormir 2024
  url: https://www.splunk.com/en_us/blog/security/breaking-down-linux-gomir-understanding-this-backdoors-ttps.html
id: attack-pattern--322bad5a-1c49-4d23-ab79-76d641794afa
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:36.812Z'
name: System Service Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Harshal Tupsamudre, Qualys
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.6'
```
