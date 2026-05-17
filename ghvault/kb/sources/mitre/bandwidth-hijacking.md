---
parsed_by: focuslocust
source: mitre
type: generated
---
# Bandwidth Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1496.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bandwidth Hijacking](../../attack/techniques/T1496.002-bandwidth-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1496.002 |
| name | Bandwidth Hijacking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1496/002 |

## Preserved Source Material

```yaml
created: '2024-09-25T13:44:35.412Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may leverage the network bandwidth resources of co-opted systems to complete resource-intensive\
  \ tasks, which may impact system and/or hosted service availability. \n\nAdversaries may also use malware that leverages\
  \ a system's network bandwidth as part of a botnet in order to facilitate [Network Denial of Service](https://attack.mitre.org/techniques/T1498)\
  \ campaigns and/or to seed malicious torrents.(Citation: GoBotKR) Alternatively, they may engage in proxyjacking by selling\
  \ use of the victims' network bandwidth and IP address to proxyware services.(Citation: Sysdig Proxyjacking) Finally, they\
  \ may engage in internet-wide scanning in order to identify additional targets for compromise.(Citation: Unit 42 Leaked\
  \ Environment Variables 2024)\n\nIn addition to incurring potential financial costs or availability disruptions, this technique\
  \ may cause reputational damage if a victim’s bandwidth is used for illegal activities.(Citation: Sysdig Proxyjacking)"
external_references:
- external_id: T1496.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1496/002
- description: Crystal Morin. (2023, April 4). Proxyjacking has Entered the Chat. Retrieved July 6, 2023.
  source_name: Sysdig Proxyjacking
  url: https://sysdig.com/blog/proxyjacking-attackers-log4j-exploited/
- description: Margaret Kelley, Sean Johnstone, William Gamazo, and Nathaniel Quist. (2024, August 15). Leaked Environment
    Variables Allow Large-Scale Extortion Operation in Cloud Environments. Retrieved September 25, 2024.
  source_name: Unit 42 Leaked Environment Variables 2024
  url: https://unit42.paloaltonetworks.com/large-scale-cloud-extortion-operation/
- description: Zuzana Hromcová. (2019, July 8). Malicious campaign targets South Korean users with backdoor‑laced torrents.
    Retrieved March 31, 2022.
  source_name: GoBotKR
  url: https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/
id: attack-pattern--718cb208-6446-4572-a2f0-9c799c60091e
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-04-15T21:52:31.979Z'
name: Bandwidth Hijacking
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Windows
- macOS
- IaaS
- Containers
x_mitre_version: '1.0'
```
