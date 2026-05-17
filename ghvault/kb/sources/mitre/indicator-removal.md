---
parsed_by: focuslocust
source: mitre
type: generated
---
# Indicator Removal

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1070` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Indicator Removal](../../attack/techniques/T1070-indicator-removal.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1070 |
| name | Indicator Removal |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1070 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:55.892Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and
  blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that
  appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal
  system behavior.


  Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user
  or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific,
  allowing adversaries to tailor modifications that minimize suspicion.


  These actions may not prevent detection entirely but can delay recognition of malicious activity or reduce the fidelity
  of alerts by making events appear benign or consistent with routine operations. Additionally, selectively removed or modified
  artifacts may still be recoverable through deeper forensic analysis, though their absence or alteration can complicate timeline
  reconstruction and attribution.'
external_references:
- external_id: T1070
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1070
id: attack-pattern--799ace7f-e227-4411-baa0-8868704f2a69
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T15:10:02.929Z'
name: Indicator Removal
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Brad Geesaman, @bradgeesaman
- Ed Williams, Trustwave, SpiderLabs
- Blake Strom, Microsoft 365 Defender
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
- Network Devices
- Office Suite
- Windows
x_mitre_version: '3.0'
```
