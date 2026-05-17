---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Share Connection Removal

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1070.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Share Connection Removal](../../attack/techniques/T1070.005-network-share-connection-removal.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1070.005 |
| name | Network Share Connection Removal |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1070/005 |

## Preserved Source Material

```yaml
created: '2020-01-31T12:39:18.816Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation.
  Windows shared drive and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) connections can be removed
  when no longer needed. [Net](https://attack.mitre.org/software/S0039) is an example utility that can be used to remove network
  share connections with the <code>net use \\system\share /delete</code> command. (Citation: Technet Net Use)'
external_references:
- external_id: T1070.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1070/005
- description: Microsoft. (n.d.). Net Use. Retrieved November 25, 2016.
  source_name: Technet Net Use
  url: https://technet.microsoft.com/bb490717.aspx
id: attack-pattern--a750a9f6-0bde-4bb3-9aae-1e2786e9780c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:29:50.512Z'
name: Network Share Connection Removal
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
- Windows
x_mitre_version: '2.0'
```
