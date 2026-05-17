---
parsed_by: focuslocust
source: mitre
type: generated
---
# Email Accounts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1585.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Email Accounts](../../attack/techniques/T1585.002-email-accounts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1585.002 |
| name | Email Accounts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1585/002 |

## Preserved Source Material

```yaml
created: '2020-10-01T01:09:53.217Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create email accounts that can be used during targeting. Adversaries can use accounts created
  with email providers to further their operations, such as leveraging them to conduct [Phishing for Information](https://attack.mitre.org/techniques/T1598)
  or [Phishing](https://attack.mitre.org/techniques/T1566).(Citation: Mandiant APT1) Establishing email accounts may also
  allow adversaries to abuse free services – such as trial periods – to [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)
  for follow-on purposes.(Citation: Free Trial PurpleUrchin)


  Adversaries may also take steps to cultivate a persona around the email account, such as through use of [Social Media Accounts](https://attack.mitre.org/techniques/T1585/001),
  to increase the chance of success of follow-on behaviors. Created email accounts can also be used in the acquisition of
  infrastructure (ex: [Domains](https://attack.mitre.org/techniques/T1583/001)).(Citation: Mandiant APT1)


  To decrease the chance of physically tying back operations to themselves, adversaries may make use of disposable email services.(Citation:
  Trend Micro R980 2016) '
external_references:
- external_id: T1585.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1585/002
- description: Antazo, F. and Yambao, M. (2016, August 10). R980 Ransomware Found Abusing Disposable Email Address Service.
    Retrieved October 13, 2020.
  source_name: Trend Micro R980 2016
  url: https://blog.trendmicro.com/trendlabs-security-intelligence/r980-ransomware-disposable-email-service/
- description: Gamazo, William. Quist, Nathaniel.. (2023, January 5). PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform
    Resources. Retrieved February 28, 2024.
  source_name: Free Trial PurpleUrchin
  url: https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/
- description: Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.
  source_name: Mandiant APT1
  url: https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf
id: attack-pattern--65013dd2-bc61-43e3-afb5-a14c4fa7437a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:48:52.378Z'
name: Email Accounts
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
x_mitre_version: '1.1'
```
