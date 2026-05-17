---
parsed_by: focuslocust
source: mitre
type: generated
---
# Indicator Removal from Tools

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Indicator Removal from Tools](../../attack/techniques/T1027.005-indicator-removal-from-tools.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.005 |
| name | Indicator Removal from Tools |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/005 |

## Preserved Source Material

```yaml
created: '2020-03-19T21:27:32.820Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may remove indicators from tools if they believe their malicious tool was detected, quarantined,
  or otherwise curtailed. They can modify the tool by removing the indicator and using the updated version that is no longer
  detected by the target''s defensive systems or subsequent targets that may use similar systems.


  A good example of this is when malware is detected with a file signature and quarantined by anti-virus software. An adversary
  who can determine that the malware was quarantined because of its file signature may modify the file to explicitly avoid
  that signature, and then re-use the malware.'
external_references:
- external_id: T1027.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/005
id: attack-pattern--b0533c6e-8fea-4788-874f-b799cacc4b92
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:19:28.558Z'
name: Indicator Removal from Tools
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
