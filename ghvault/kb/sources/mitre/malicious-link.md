---
parsed_by: focuslocust
source: mitre
type: generated
---
# Malicious Link

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1204.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Malicious Link](../../attack/techniques/T1204.001-malicious-link.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1204.001 |
| name | Malicious Link |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1204/001 |

## Preserved Source Material

```yaml
created: '2020-03-11T14:43:31.706Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected
  to social engineering to get them to click on a link that will lead to code execution. This user action will typically be
  observed as follow-on behavior from [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002). Clicking on a link
  may also lead to other execution techniques such as exploitation of a browser or application vulnerability via [Exploitation
  for Client Execution](https://attack.mitre.org/techniques/T1203). Links may also lead users to download files that require
  execution via [Malicious File](https://attack.mitre.org/techniques/T1204/002).
external_references:
- external_id: T1204.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1204/001
id: attack-pattern--ef67e13e-5598-4adc-bdb2-998225874fa9
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:49:35.144Z'
name: Malicious Link
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
x_mitre_remote_support: false
x_mitre_version: '1.2'
```
