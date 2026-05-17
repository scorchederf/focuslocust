---
parsed_by: focuslocust
source: mitre
type: generated
---
# Trap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1546.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Trap](../../attack/techniques/T1546.005-trap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1546.005 |
| name | Trap |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1546/005 |

## Preserved Source Material

```yaml
created: '2020-01-24T14:17:43.906Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may establish persistence by executing malicious content triggered by an interrupt signal. The <code>trap</code>
  command allows programs and shells to specify commands that will be executed upon receiving interrupt signals. A common
  situation is a script allowing for graceful termination and handling of common keyboard interrupts like <code>ctrl+c</code>
  and <code>ctrl+d</code>.


  Adversaries can use this to register code to be executed when the shell encounters specific interrupts as a persistence
  mechanism. Trap commands are of the following format <code>trap ''command list'' signals</code> where "command list" will
  be executed when "signals" are received.(Citation: Trap Manual)(Citation: Cyberciti Trap Statements)'
external_references:
- external_id: T1546.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1546/005
- description: ss64. (n.d.). trap. Retrieved May 21, 2019.
  source_name: Trap Manual
  url: https://ss64.com/bash/trap.html
- description: Cyberciti. (2016, March 29). Trap statement. Retrieved May 21, 2019.
  source_name: Cyberciti Trap Statements
  url: https://bash.cyberciti.biz/guide/Trap_statement
id: attack-pattern--63220765-d418-44de-8fae-694b3912317d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:48:51.725Z'
name: Trap
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
- Linux
x_mitre_version: '1.1'
```
