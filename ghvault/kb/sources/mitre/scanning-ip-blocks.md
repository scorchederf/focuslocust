---
parsed_by: focuslocust
source: mitre
type: generated
---
# Scanning IP Blocks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1595.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Scanning IP Blocks](../../attack/techniques/T1595.001-scanning-ip-blocks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1595.001 |
| name | Scanning IP Blocks |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1595/001 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:54:23.193Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may scan victim IP blocks to gather information that can be used during targeting. Public IP addresses
  may be allocated to organizations by block, or a range of sequential addresses.


  Adversaries may scan IP blocks in order to [Gather Victim Network Information](https://attack.mitre.org/techniques/T1590),
  such as which IP addresses are actively in use as well as more detailed information about hosts assigned these addresses.
  Scans may range from simple pings (ICMP requests and responses) to more nuanced scans that may reveal host software/versions
  via server banners or other network artifacts.(Citation: Botnet Scan) Information from these scans may reveal opportunities
  for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search
  Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop
  Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)),
  and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).'
external_references:
- external_id: T1595.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1595/001
- description: Dainotti, A. et al. (2012). Analysis of a “/0” Stealth Scan from a Botnet. Retrieved October 20, 2020.
  source_name: Botnet Scan
  url: https://www.caida.org/publications/papers/2012/analysis_slash_zero/analysis_slash_zero.pdf
id: attack-pattern--db8f5003-3b20-48f0-9b76-123e44208120
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:49:28.603Z'
name: Scanning IP Blocks
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Diego Sappa, Securonix
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.1'
```
