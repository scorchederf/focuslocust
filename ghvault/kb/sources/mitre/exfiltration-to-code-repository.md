---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration to Code Repository

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1567.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration to Code Repository](../../attack/techniques/T1567.001-exfiltration-to-code-repository.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1567.001 |
| name | Exfiltration to Code Repository |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1567/001 |

## Preserved Source Material

```yaml
created: '2020-03-09T14:51:11.772Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may exfiltrate data to a code repository rather than over their primary command and control channel.
  Code repositories are often accessible via an API (ex: https://api.github.com). Access to these APIs are often over HTTPS,
  which gives the adversary an additional level of protection.


  Exfiltration to a code repository can also provide a significant amount of cover to the adversary if it is a popular service
  already used by hosts within the network. '
external_references:
- external_id: T1567.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1567/001
id: attack-pattern--86a96bf6-cf8b-411c-aaeb-8959944d64f7
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:04.207Z'
name: Exfiltration to Code Repository
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
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
