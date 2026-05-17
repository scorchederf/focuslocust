---
parsed_by: focuslocust
source: mitre
type: generated
---
# Establish Accounts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1585` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Establish Accounts](../../attack/techniques/T1585-establish-accounts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1585 |
| name | Establish Accounts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1585 |

## Preserved Source Material

```yaml
created: '2020-10-01T01:05:42.216Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create and cultivate accounts with services that can be used during targeting. Adversaries can
  create accounts that can be used to build a persona to further operations. Persona development consists of the development
  of public information, presence, history and appropriate affiliations. This development could be applied to social media,
  website, or other publicly available information that could be referenced and scrutinized for legitimacy over the course
  of an operation using that persona or identity.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage)


  For operations incorporating social engineering, the utilization of an online persona may be important. These personas may
  be fictitious or impersonate real people. The persona may exist on a single site or across multiple sites (ex: Facebook,
  LinkedIn, Twitter, Google, GitHub, Docker Hub, etc.). Establishing a persona may require development of additional documentation
  to make them seem real. This could include filling out profile information, developing social networks, or incorporating
  photos.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage)


  Establishing accounts can also include the creation of accounts with email providers, which may be directly leveraged for
  [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Phishing](https://attack.mitre.org/techniques/T1566).(Citation:
  Mandiant APT1) In addition, establishing accounts may allow adversaries to abuse free services, such as registering for
  trial periods to [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) for malicious purposes.(Citation: Free
  Trial PurpleUrchin)

  '
external_references:
- external_id: T1585
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1585
- description: Gamazo, William. Quist, Nathaniel.. (2023, January 5). PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform
    Resources. Retrieved February 28, 2024.
  source_name: Free Trial PurpleUrchin
  url: https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/
- description: Lennon, M. (2014, May 29). Iranian Hackers Targeted US Officials in Elaborate Social Media Attack Operation.
    Retrieved March 1, 2017.
  source_name: NEWSCASTER2014
  url: https://www.securityweek.com/iranian-hackers-targeted-us-officials-elaborate-social-media-attack-operation
- description: Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.
  source_name: Mandiant APT1
  url: https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf
- description: Ryan, T. (2010). “Getting In Bed with Robin Sage.”. Retrieved March 6, 2017.
  source_name: BlackHatRobinSage
  url: http://media.blackhat.com/bh-us-10/whitepapers/Ryan/BlackHat-USA-2010-Ryan-Getting-In-Bed-With-Robin-Sage-v1.0.pdf
id: attack-pattern--cdfc5f0a-9bb9-4352-b896-553cfa2d8fd8
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:49:24.456Z'
name: Establish Accounts
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
x_mitre_version: '1.3'
```
