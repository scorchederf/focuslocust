---
parsed_by: focuslocust
source: mitre
type: generated
---
# Masquerading

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1036` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Masquerading](../../attack/techniques/T1036-masquerading.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1036 |
| name | Masquerading |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1036 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:38.511Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to
  users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated
  or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users
  into misidentifying the file type, and giving legitimate task or service names.


  Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1036).(Citation:
  LOLBAS Main Site)'
external_references:
- external_id: T1036
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1036
- description: LOLBAS. (n.d.). Living Off The Land Binaries and Scripts (and also Libraries). Retrieved February 10, 2020.
  source_name: LOLBAS Main Site
  url: https://lolbas-project.github.io/
id: attack-pattern--42e8de7b-37b2-4258-905a-6897815e58e0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:32:00.311Z'
name: Masquerading
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Bartosz Jerzman
- David Lu, Tripwire
- Elastic
- Felipe Espósito, @Pr0teus
- Menachem Goldstein
- Nick Carr, Mandiant
- Oleg Kolesnikov, Securonix
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
