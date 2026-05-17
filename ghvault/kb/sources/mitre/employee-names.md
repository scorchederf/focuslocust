---
parsed_by: focuslocust
source: mitre
type: generated
---
# Employee Names

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1589.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Employee Names](../../attack/techniques/T1589.003-employee-names.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1589.003 |
| name | Employee Names |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1589/003 |

## Preserved Source Material

```yaml
created: '2020-10-02T14:57:15.906Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather employee names that can be used during targeting. Employee names be used to derive email
  addresses as well as to help guide other reconnaissance efforts and/or craft more-believable lures.


  Adversaries may easily gather employee names, since they may be readily available and exposed via online or other accessible
  data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation:
  OPM Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)
  or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Compromise
  Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)
  or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).'
external_references:
- external_id: T1589.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1589/003
- description: Cybersecurity Resource Center. (n.d.). CYBERSECURITY INCIDENTS. Retrieved September 16, 2024.
  source_name: OPM Leak
  url: https://web.archive.org/web/20230602111604/https://www.opm.gov/cybersecurity/cybersecurity-incidents/
id: attack-pattern--76551c52-b111-4884-bc47-ff3e728f0156
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:57.975Z'
name: Employee Names
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
