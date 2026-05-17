---
parsed_by: focuslocust
source: mitre
type: generated
---
# Browser Information Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1217` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Browser Information Discovery](../../attack/techniques/T1217-browser-information-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1217 |
| name | Browser Information Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1217 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved
  by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users
  (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such
  as servers, tools/dashboards, or other related infrastructure.(Citation: Kaspersky Autofill)


  Browser information may also highlight additional targets after an adversary has access to valid credentials, especially
  [Credentials In Files](https://attack.mitre.org/techniques/T1552/001) associated with logins cached by a browser.


  Specific storage locations vary based on platform and/or application, but browser information is typically stored in local
  files and databases (e.g., `%APPDATA%/Google/Chrome`).(Citation: Chrome Roaming Profiles)'
external_references:
- external_id: T1217
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1217
- description: Chrome Enterprise and Education Help. (n.d.). Use Chrome Browser with Roaming User Profiles. Retrieved March
    28, 2023.
  source_name: Chrome Roaming Profiles
  url: https://support.google.com/chrome/a/answer/7349337
- description: Golubev, S. (n.d.). How malware steals autofill data from browsers. Retrieved March 28, 2023.
  source_name: Kaspersky Autofill
  url: https://www.kaspersky.com/blog/browser-data-theft/27871/
id: attack-pattern--5e4a2073-9643-44cb-a0b5-e7f4048446c7
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:50.561Z'
name: Browser Information Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Mike Kemmerer
- Manikantan Srinivasan, NEC Corporation India
- Yinon Engelsman, Talon Cyber Security
- Yonatan Gotlib, Talon Cyber Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
