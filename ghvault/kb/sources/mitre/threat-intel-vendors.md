---
parsed_by: focuslocust
source: mitre
type: generated
---
# Threat Intel Vendors

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1597.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Threat Intel Vendors](../../attack/techniques/T1597.001-threat-intel-vendors.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1597.001 |
| name | Threat Intel Vendors |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1597/001 |

## Preserved Source Material

```yaml
created: '2020-10-02T17:03:45.918Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search private data from threat intelligence vendors for information that can be used during
  targeting. Threat intelligence vendors may offer paid feeds or portals that offer more data than what is publicly reported.
  Although sensitive details (such as customer names and other identifiers) may be redacted, this information may contain
  trends regarding breaches such as target industries, attribution claims, and successful TTPs/countermeasures.(Citation:
  D3Secutrity CTI Feeds)


  Adversaries may search in private threat intelligence vendor data to gather actionable information. If a threat actor is
  searching for information on their own activities, that falls under [Search Threat Vendor Data](https://attack.mitre.org/techniques/T1681).
  Information reported by vendors may also reveal opportunities other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)),
  establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)),
  and/or initial access (ex: [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190) or [External Remote
  Services](https://attack.mitre.org/techniques/T1133)).'
external_references:
- external_id: T1597.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1597/001
- description: Banerd, W. (2019, April 30). 10 of the Best Open Source Threat Intelligence Feeds. Retrieved October 20, 2020.
  source_name: D3Secutrity CTI Feeds
  url: https://d3security.com/blog/10-of-the-best-open-source-threat-intelligence-feeds/
id: attack-pattern--51e54974-a541-4fb6-a61b-0518e4c6de41
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:46.954Z'
name: Threat Intel Vendors
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '2.0'
```
