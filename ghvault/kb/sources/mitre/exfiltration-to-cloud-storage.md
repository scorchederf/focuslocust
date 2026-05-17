---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration to Cloud Storage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1567.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration to Cloud Storage](../../attack/techniques/T1567.002-exfiltration-to-cloud-storage.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1567.002 |
| name | Exfiltration to Cloud Storage |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1567/002 |

## Preserved Source Material

```yaml
created: '2020-03-09T15:04:32.767Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control
  channel. Cloud storage services allow for the storage, edit, and retrieval of data from a remote cloud storage server over
  the Internet.


  Examples of cloud storage services include Dropbox and Google Docs. Exfiltration to these cloud storage services can provide
  a significant amount of cover to the adversary if hosts within the network are already communicating with the service. '
external_references:
- external_id: T1567.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1567/002
id: attack-pattern--bf1b6176-597c-4600-bfcd-ac989670f96b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:19.048Z'
name: Exfiltration to Cloud Storage
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
x_mitre_version: '1.3'
```
