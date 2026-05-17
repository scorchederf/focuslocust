---
parsed_by: focuslocust
source: mitre
type: generated
---
# Email Collection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1114` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Email Collection](../../attack/techniques/T1114-email-collection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1114 |
| name | Email Collection |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1114 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:25.454Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may target user email to collect sensitive information. Emails may contain sensitive data, including
  trade secrets or personal information, that can prove valuable to adversaries. Emails may also contain details of ongoing
  incident response operations, which may allow adversaries to adjust their techniques in order to maintain persistence or
  evade defenses.(Citation: TrustedSec OOB Communications)(Citation: CISA AA20-352A 2021) Adversaries can collect or forward
  email from mail servers or clients. '
external_references:
- external_id: T1114
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1114
- description: CISA. (2021, April 15). Advanced Persistent Threat Compromise of Government Agencies, Critical Infrastructure,
    and Private Sector Organizations. Retrieved August 30, 2024.
  source_name: CISA AA20-352A 2021
  url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a
- description: McMichael, T.. (2015, June 8). Exchange and Office 365 Mail Forwarding. Retrieved October 8, 2019.
  source_name: Microsoft Tim McMichael Exchange Mail Forwarding 2
  url: https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/
- description: 'Tyler Hudak. (2022, December 29). To OOB, or Not to OOB?: Why Out-of-Band Communications are Essential for
    Incident Response. Retrieved August 30, 2024.'
  source_name: TrustedSec OOB Communications
  url: https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response
id: attack-pattern--1608f3e1-598a-42f4-a01a-2e252e81728f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:26.463Z'
name: Email Collection
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Swetha Prabakaran, Microsoft Threat Intelligence Center (MSTIC)
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- macOS
- Linux
- Office Suite
x_mitre_version: '2.6'
```
