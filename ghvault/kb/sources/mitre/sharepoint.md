---
parsed_by: focuslocust
source: mitre
type: generated
---
# Sharepoint

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1213.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Sharepoint](../../attack/techniques/T1213.002-sharepoint.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1213.002 |
| name | Sharepoint |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1213/002 |

## Preserved Source Material

```yaml
created: '2020-02-14T13:35:32.938Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may leverage the SharePoint repository as a source to mine valuable information. SharePoint will
  often contain useful information for an adversary to learn about the structure and functionality of the internal network
  and systems. For example, the following is a list of example information that may hold potential value to an adversary and
  may also be found on SharePoint:


  * Policies, procedures, and standards

  * Physical / logical network diagrams

  * System architecture diagrams

  * Technical system documentation

  * Testing / development credentials (i.e., [Unsecured Credentials](https://attack.mitre.org/techniques/T1552))

  * Work / project schedules

  * Source code snippets

  * Links to network shares and other internal resources

  '
external_references:
- external_id: T1213.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1213/002
- description: Microsoft. (2017, July 19). Configure audit settings for a site collection. Retrieved April 4, 2018.
  source_name: Microsoft SharePoint Logging
  url: https://support.office.com/en-us/article/configure-audit-settings-for-a-site-collection-a9920c97-38c0-44f2-8bcb-4cf1e2ae22d2
id: attack-pattern--0c4b4fda-9062-47da-98b9-ceae2dcf052a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:22.832Z'
name: Sharepoint
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Arun Seelagan, CISA
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Office Suite
- Windows
x_mitre_version: '1.1'
```
