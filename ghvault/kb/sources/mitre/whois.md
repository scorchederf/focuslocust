---
parsed_by: focuslocust
source: mitre
type: generated
---
# WHOIS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1596.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WHOIS](../../attack/techniques/T1596.002-whois.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1596.002 |
| name | WHOIS |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1596/002 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:56:49.744Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search public WHOIS data for information about victims that can be used during targeting. WHOIS
  data is stored by regional Internet registries (RIR) responsible for allocating and assigning Internet resources such as
  domain names. Anyone can query WHOIS servers for information about a registered domain, such as assigned IP blocks, contact
  information, and DNS nameservers.(Citation: WHOIS)


  Adversaries may search WHOIS data to gather actionable information. Threat actors can use online resources or command-line
  utilities to pillage through WHOIS data for information about potential victims. Information from these sources may reveal
  opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing
  for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)
  or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote
  Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).'
external_references:
- external_id: T1596.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1596/002
- description: NTT America. (n.d.). Whois Lookup. Retrieved November 17, 2024.
  source_name: WHOIS
  url: https://who.is/
id: attack-pattern--166de1c6-2814-4fe5-8438-4e80f76b169f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:26.629Z'
name: WHOIS
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.0'
```
