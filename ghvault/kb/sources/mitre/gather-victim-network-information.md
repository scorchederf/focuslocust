---
parsed_by: focuslocust
source: mitre
type: generated
---
# Gather Victim Network Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1590` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Gather Victim Network Information](../../attack/techniques/T1590-gather-victim-network-information.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1590 |
| name | Gather Victim Network Information |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1590 |

## Preserved Source Material

```yaml
created: '2020-10-02T15:45:17.628Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather information about the victim''s networks that can be used during targeting. Information
  about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well
  as specifics regarding its topology and operations.


  Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595)
  or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about networks may also be exposed
  to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation:
  WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other
  forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)),
  establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise
  Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).'
external_references:
- external_id: T1590
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1590
- description: CIRCL Computer Incident Response Center. (n.d.). Passive DNS. Retrieved October 20, 2020.
  source_name: Circl Passive DNS
  url: https://www.circl.lu/services/passive-dns/
- description: Hacker Target. (n.d.). DNS Dumpster. Retrieved October 20, 2020.
  source_name: DNS Dumpster
  url: https://dnsdumpster.com/
- description: NTT America. (n.d.). Whois Lookup. Retrieved November 17, 2024.
  source_name: WHOIS
  url: https://who.is/
id: attack-pattern--9d48cab2-7929-4812-ad22-f536665f0109
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:49:08.938Z'
name: Gather Victim Network Information
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
- PRE
x_mitre_version: '1.0'
```
