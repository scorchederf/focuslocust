---
parsed_by: focuslocust
source: mitre
type: generated
---
# Query Registry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1012` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Query Registry](../../attack/techniques/T1012-query-registry.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1012 |
| name | Query Registry |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1012 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:25.584Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may interact with the Windows Registry to gather information about the system, configuration, and
  installed software.


  The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation:
  Wikipedia Windows Registry) Information can easily be queried using the [Reg](https://attack.mitre.org/software/S0075) utility,
  though other means to access the Registry exist. Some of the information may help adversaries to further their operation
  within a network. Adversaries may use the information from [Query Registry](https://attack.mitre.org/techniques/T1012) during
  automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or
  attempts specific actions.'
external_references:
- external_id: T1012
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1012
- description: Wikipedia. (n.d.). Windows Registry. Retrieved February 2, 2015.
  source_name: Wikipedia Windows Registry
  url: https://en.wikipedia.org/wiki/Windows_Registry
id: attack-pattern--c32f7008-9fea-41f7-8366-5eb9b74bd896
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:20.660Z'
name: Query Registry
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
- Windows
x_mitre_version: '1.3'
```
