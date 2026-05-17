---
parsed_by: focuslocust
source: mitre
type: generated
---
# Security Software Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1518.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Security Software Discovery](../../attack/techniques/T1518.001-security-software-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1518.001 |
| name | Security Software Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1518/001 |

## Preserved Source Material

```yaml
created: '2020-02-21T21:16:18.066Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors
  that are installed on a system or in a cloud environment. This may include things such as cloud monitoring agents and anti-virus.
  Adversaries may use the information from [Security Software Discovery](https://attack.mitre.org/techniques/T1518/001) during
  automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or
  attempts specific actions.


  Example commands that can be used to obtain security software information are [netsh](https://attack.mitre.org/software/S0108),
  <code>reg query</code> with [Reg](https://attack.mitre.org/software/S0075), <code>dir</code> with [cmd](https://attack.mitre.org/software/S0106),
  and [Tasklist](https://attack.mitre.org/software/S0057), but other indicators of discovery behavior may be more specific
  to the type of software or security system the adversary is looking for. It is becoming more common to see macOS malware
  perform checks for LittleSnitch and KnockKnock software.


  Adversaries may also utilize the [Cloud API](https://attack.mitre.org/techniques/T1059/009) to discover cloud-native security
  software installed on compute infrastructure, such as the AWS CloudWatch agent, Azure VM Agent, and Google Cloud Monitor
  agent. These agents  may collect  metrics and logs from the VM, which may be centrally aggregated in a cloud-based monitoring
  platform.'
external_references:
- external_id: T1518.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1518/001
id: attack-pattern--cba37adb-d6fb-4610-b069-dd04c0643384
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:23.401Z'
name: Security Software Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Isif Ibrahima, Mandiant
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Linux
- macOS
- Windows
x_mitre_version: '1.5'
```
