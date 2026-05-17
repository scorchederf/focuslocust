---
parsed_by: focuslocust
source: mitre
type: generated
---
# Process Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1055` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Injection](../../attack/techniques/T1055-process-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1055 |
| name | Process Injection |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1055 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:47.843Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate\
  \ privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process.\
  \ Running code in the context of another process may allow access to the process's memory, system/network resources, and\
  \ possibly elevated privileges. Execution via process injection may also evade detection from security products since the\
  \ execution is masked under a legitimate process. \n\nThere are many different ways to inject code into a process, many\
  \ of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific.\
  \ \n\nMore sophisticated samples may perform multiple process injections to segment modules and further evade detection,\
  \ utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. "
external_references:
- external_id: T1055
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1055
id: attack-pattern--43e7dc91-05b2-474c-b9ac-2ed4fe101f4d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T22:26:41.663Z'
name: Process Injection
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Anastasios Pingios
- Christiaan Beek, @ChristiaanBeek
- Ryan Becwar
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
