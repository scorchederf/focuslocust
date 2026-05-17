---
parsed_by: focuslocust
source: mitre
type: generated
---
# Code Repositories

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1213.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Code Repositories](../../attack/techniques/T1213.003-code-repositories.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1213.003 |
| name | Code Repositories |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1213/003 |

## Preserved Source Material

```yaml
created: '2021-05-11T18:51:16.343Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may leverage code repositories to collect valuable information. Code repositories are tools/services
  that store source code and automate software builds. They may be hosted internally or privately on third party sites such
  as Github, GitLab, SourceForge, and BitBucket. Users typically interact with code repositories through a web application
  or command-line utilities such as git.


  Once adversaries gain access to a victim network or a private code repository, they may collect sensitive information such
  as proprietary source code or [Unsecured Credentials](https://attack.mitre.org/techniques/T1552) contained within software''s
  source code.  Having access to software''s source code may allow adversaries to develop [Exploits](https://attack.mitre.org/techniques/T1587/004),
  while credentials may provide access to additional resources using [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation:
  Wired Uber Breach)(Citation: Krebs Adobe)


  **Note:** This is distinct from [Code Repositories](https://attack.mitre.org/techniques/T1593/003), which focuses on conducting
  [Reconnaissance](https://attack.mitre.org/tactics/TA0043) via public code repositories.'
external_references:
- external_id: T1213.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1213/003
- description: 'Andy Greenberg. (2017, January 21). Hack Brief: Uber Paid Off Hackers to Hide a 57-Million User Data Breach.
    Retrieved May 14, 2021.'
  source_name: Wired Uber Breach
  url: https://www.wired.com/story/uber-paid-off-hackers-to-hide-a-57-million-user-data-breach/
- description: Brian Krebs. (2013, October 3). Adobe To Announce Source Code, Customer Data Breach. Retrieved May 17, 2021.
  source_name: Krebs Adobe
  url: https://krebsonsecurity.com/2013/10/adobe-to-announce-source-code-customer-data-breach/
id: attack-pattern--cff94884-3b1c-4987-a70b-6d5643c621c3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:49:25.081Z'
name: Code Repositories
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Itamar Mizrahi, Cymptom
- Toby Kohlenberg
- Josh Liburdi, @jshlbrd
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- SaaS
x_mitre_version: '1.2'
```
