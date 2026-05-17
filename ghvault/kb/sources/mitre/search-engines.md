---
parsed_by: focuslocust
source: mitre
type: generated
---
# Search Engines

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1593.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Search Engines](../../attack/techniques/T1593.002-search-engines.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1593.002 |
| name | Search Engines |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1593/002 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:50:12.809Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use search engines to collect information about victims that can be used during targeting. Search
  engine services typical crawl online sites to index context and may provide users with specialized syntax to search for
  specific keywords or specific types of content (i.e. filetypes).(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB
  GoogleHacking)


  Adversaries may craft various search engine queries depending on what information they seek to gather. Threat actors may
  use search engines to harvest general information about victims, as well as use specialized queries to look for spillages/leaks
  of sensitive information such as network details or credentials. Information from these sources may reveal opportunities
  for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search
  Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish
  Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)),
  and/or initial access (ex: [Valid Accounts](https://attack.mitre.org/techniques/T1078) or [Phishing](https://attack.mitre.org/techniques/T1566)).'
external_references:
- external_id: T1593.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1593/002
- description: Borges, E. (2019, March 5). Exploring Google Hacking Techniques. Retrieved September 12, 2024.
  source_name: SecurityTrails Google Hacking
  url: https://www.recordedfuture.com/threat-intelligence-101/threat-analysis-techniques/google-dorks
- description: Offensive Security. (n.d.). Google Hacking Database. Retrieved October 23, 2020.
  source_name: ExploitDB GoogleHacking
  url: https://www.exploit-db.com/google-hacking-database
id: attack-pattern--6e561441-8431-4773-a9b8-ccf28ef6a968
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:55.709Z'
name: Search Engines
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
