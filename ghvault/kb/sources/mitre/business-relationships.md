---
parsed_by: focuslocust
source: mitre
type: generated
---
# Business Relationships

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1591.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Business Relationships](../../attack/techniques/T1591.002-business-relationships.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1591.002 |
| name | Business Relationships |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1591/002 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:27:55.713Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather information about the victim''s business relationships that can be used during targeting.
  Information about an organization’s business relationships may include a variety of details, including second or third-party
  organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated)
  network access. This information may also reveal supply chains and shipment paths for the victim’s hardware and software
  resources.


  Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598).
  Information about business relationships may also be exposed to adversaries via online or other accessible data sets (ex:
  [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation:
  ThreatPost Broadvoice Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Phishing
  for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)),
  establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)),
  and/or initial access (ex: [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195), [Drive-by Compromise](https://attack.mitre.org/techniques/T1189),
  or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).'
external_references:
- external_id: T1591.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1591/002
- description: Seals, T. (2020, October 15). Broadvoice Leak Exposes 350M Records, Personal Voicemail Transcripts. Retrieved
    October 20, 2020.
  source_name: ThreatPost Broadvoice Leak
  url: https://threatpost.com/broadvoice-leaks-350m-records-voicemail-transcripts/160158/
id: attack-pattern--6ee2dc99-91ad-4534-a7d8-a649358c331f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:55.897Z'
name: Business Relationships
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
