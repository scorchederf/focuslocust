---
parsed_by: focuslocust
source: mitre
type: generated
---
# Hijack Execution Flow

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hijack Execution Flow](../../attack/techniques/T1574-hijack-execution-flow.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574 |
| name | Hijack Execution Flow |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574 |

## Preserved Source Material

```yaml
created: '2020-03-12T20:38:12.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking
  execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries
  may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions
  on execution.


  There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates
  programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations
  where the operating system looks for programs/resources, such as file directories and in the case of Windows the Registry,
  could also be poisoned to include malicious payloads.'
external_references:
- external_id: T1574
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574
id: attack-pattern--aedfca76-3b30-4866-b2aa-0f1d7fd1e4b6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-20T21:18:17.156Z'
name: Hijack Execution Flow
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
