---
parsed_by: focuslocust
source: mitre
type: generated
---
# Internet Connection Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1016.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Internet Connection Discovery](../../attack/techniques/T1016.001-internet-connection-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1016.001 |
| name | Internet Connection Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1016/001 |

## Preserved Source Material

```yaml
created: '2021-03-17T15:28:10.689Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated
  discovery and can be accomplished in numerous ways such as using [Ping](https://attack.mitre.org/software/S0097), <code>tracert</code>,
  and GET requests to websites, or performing initial speed testing to confirm bandwidth.


  Adversaries may use the results and responses from these requests to determine if the system is capable of communicating
  with their C2 servers before attempting to connect to them. The results may also be used to identify routes, redirectors,
  and proxy servers.'
external_references:
- external_id: T1016.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1016/001
id: attack-pattern--132d5b37-aac5-4378-a8dc-3127b18a73dc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:26.017Z'
name: Internet Connection Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Christopher Peacock
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- Linux
- macOS
- ESXi
x_mitre_version: '1.2'
```
