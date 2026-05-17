---
parsed_by: focuslocust
source: mitre
type: generated
---
# Purchase Technical Data

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1597.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Purchase Technical Data](../../attack/techniques/T1597.002-purchase-technical-data.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1597.002 |
| name | Purchase Technical Data |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1597/002 |

## Preserved Source Material

```yaml
created: '2020-10-02T17:05:43.562Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may purchase technical information about victims that can be used during targeting. Information
  about victims may be available for purchase within reputable private sources and databases, such as paid subscriptions to
  feeds of scan databases or other data aggregation services. Adversaries may also purchase information from less-reputable
  sources such as dark web or cybercrime blackmarkets.


  Adversaries may purchase information about their already identified targets, or use purchased data to discover opportunities
  for successful breaches. Threat actors may gather various technical details from purchased data, including but not limited
  to employee contact information, credentials, or specifics regarding a victim’s infrastructure.(Citation: ZDNET Selling
  Data) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598)
  or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop
  Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)),
  and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).'
external_references:
- external_id: T1597.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1597/002
- description: Cimpanu, C. (2020, May 9). A hacker group is selling more than 73 million user records on the dark web. Retrieved
    October 20, 2020.
  source_name: ZDNET Selling Data
  url: https://www.zdnet.com/article/a-hacker-group-is-selling-more-than-73-million-user-records-on-the-dark-web/
id: attack-pattern--0a241b6c-7bb2-48f9-98f7-128145b4d27f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:22.109Z'
name: Purchase Technical Data
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
