---
parsed_by: focuslocust
source: mitre
type: generated
---
# Archive via Custom Method

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1560.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Archive via Custom Method](../../attack/techniques/T1560.003-archive-via-custom-method.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1560.003 |
| name | Archive via Custom Method |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1560/003 |

## Preserved Source Material

```yaml
created: '2020-02-20T21:09:55.995Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method. Adversaries
  may choose to use custom archival methods, such as encryption with XOR or stream ciphers implemented with no external library
  or utility references. Custom implementations of well-known compression algorithms have also been used.(Citation: ESET Sednit
  Part 2)'
external_references:
- external_id: T1560.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1560/003
- description: 'ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November
    21, 2016.'
  source_name: ESET Sednit Part 2
  url: http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf
id: attack-pattern--143c0cbb-a297-4142-9624-87ffc778980b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:26.190Z'
name: Archive via Custom Method
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
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
