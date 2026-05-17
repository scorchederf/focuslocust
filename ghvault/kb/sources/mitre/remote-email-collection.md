---
parsed_by: focuslocust
source: mitre
type: generated
---
# Remote Email Collection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1114.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Remote Email Collection](../../attack/techniques/T1114.002-remote-email-collection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1114.002 |
| name | Remote Email Collection |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1114/002 |

## Preserved Source Material

```yaml
created: '2020-02-19T18:52:24.547Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may target an Exchange server, Office 365, or Google Workspace to collect sensitive information.
  Adversaries may leverage a user's credentials and interact directly with the Exchange server to acquire information from
  within a network. Adversaries may also access externally facing Exchange services, Office 365, or Google Workspace to access
  email using credentials or access tokens. Tools such as [MailSniper](https://attack.mitre.org/software/S0413) can be used
  to automate searches for specific keywords.
external_references:
- external_id: T1114.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1114/002
id: attack-pattern--b4694861-542c-48ea-9eb1-10d356e7140a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:49:15.355Z'
name: Remote Email Collection
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
x_mitre_version: '1.3'
```
