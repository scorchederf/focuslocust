---
parsed_by: focuslocust
source: mitre
type: generated
---
# Search Open Websites／Domains

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1593` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Search Open Websites／Domains](../../attack/techniques/T1593-search-open-websites-domains.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1593 |
| name | Search Open Websites／Domains |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1593 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:48:04.509Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search freely available websites and/or domains for information about victims that can be used
  during targeting. Information about victims may be available in various online sites, such as social media, new sites, or
  those hosting information about business operations such as hiring or requested/rewarded contracts.(Citation: Cyware Social
  Media)(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)


  Adversaries may search in different online sites depending on what information they seek to gather. Information from these
  sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598)
  or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex:
  [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)),
  and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Phishing](https://attack.mitre.org/techniques/T1566)).'
external_references:
- external_id: T1593
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1593
- description: Borges, E. (2019, March 5). Exploring Google Hacking Techniques. Retrieved September 12, 2024.
  source_name: SecurityTrails Google Hacking
  url: https://www.recordedfuture.com/threat-intelligence-101/threat-analysis-techniques/google-dorks
- description: Cyware Hacker News. (2019, October 2). How Hackers Exploit Social Media To Break Into Your Company. Retrieved
    October 20, 2020.
  source_name: Cyware Social Media
  url: https://cyware.com/news/how-hackers-exploit-social-media-to-break-into-your-company-88e8da8e
- description: Offensive Security. (n.d.). Google Hacking Database. Retrieved October 23, 2020.
  source_name: ExploitDB GoogleHacking
  url: https://www.exploit-db.com/google-hacking-database
id: attack-pattern--a0e6614a-7740-4b24-bd65-f1bde09fc365
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:49:10.188Z'
name: Search Open Websites/Domains
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
x_mitre_version: '1.1'
```
