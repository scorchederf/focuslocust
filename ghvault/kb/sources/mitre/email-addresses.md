---
parsed_by: focuslocust
source: mitre
type: generated
---
# Email Addresses

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1589.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Email Addresses](../../attack/techniques/T1589.002-email-addresses.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1589.002 |
| name | Email Addresses |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1589/002 |

## Preserved Source Material

```yaml
created: '2020-10-02T14:56:24.866Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather email addresses that can be used during targeting. Even if internal instances exist,
  organizations may have public-facing email infrastructure and addresses for employees.


  Adversaries may easily gather email addresses, since they may be readily available and exposed via online or other accessible
  data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation:
  HackersArise Email)(Citation: CNET Leaks) Email addresses could also be enumerated via more active means (i.e. [Active Scanning](https://attack.mitre.org/techniques/T1595)),
  such as probing and analyzing responses from authentication services that may reveal valid usernames in a system.(Citation:
  GrimBlog UsernameEnum) For example, adversaries may be able to enumerate email addresses in Office 365 environments by querying
  a variety of publicly available API endpoints, such as autodiscover and GetCredentialType.(Citation: GitHub Office 365 User
  Enumeration)(Citation: Azure Active Directory Reconnaisance)


  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)
  or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Email
  Accounts](https://attack.mitre.org/techniques/T1586/002)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)
  or [Brute Force](https://attack.mitre.org/techniques/T1110) via [External Remote Services](https://attack.mitre.org/techniques/T1133)).'
external_references:
- external_id: T1589.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1589/002
- description: 'Dr. Nestori Syynimaa. (2020, June 13). Just looking: Azure Active Directory reconnaissance as an outsider.
    Retrieved May 27, 2022.'
  source_name: Azure Active Directory Reconnaisance
  url: https://o365blog.com/post/just-looking/
- description: gremwell. (2020, March 24). Office 365 User Enumeration. Retrieved May 27, 2022.
  source_name: GitHub Office 365 User Enumeration
  url: https://github.com/gremwell/o365enum
- description: GrimHacker. (2017, July 24). Office365 ActiveSync Username Enumeration. Retrieved December 9, 2021.
  source_name: GrimBlog UsernameEnum
  url: https://grimhacker.com/2017/07/24/office365-activesync-username-enumeration/
- description: Hackers Arise. (n.d.). Email Scraping and Maltego. Retrieved October 20, 2020.
  source_name: HackersArise Email
  url: https://www.hackers-arise.com/email-scraping-and-maltego
- description: Ng, A. (2019, January 17). Massive breach leaks 773 million email addresses, 21 million passwords. Retrieved
    October 20, 2020.
  source_name: CNET Leaks
  url: https://www.cnet.com/news/massive-breach-leaks-773-million-emails-21-million-passwords/
id: attack-pattern--69f897fd-12a9-4c89-ad6a-46d2f3c38262
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:54.336Z'
name: Email Addresses
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.3'
```
