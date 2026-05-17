---
parsed_by: focuslocust
source: mitre
type: generated
---
# Shortcut Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shortcut Modification](../../attack/techniques/T1547.009-shortcut-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.009 |
| name | Shortcut Modification |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/009 |

## Preserved Source Material

```yaml
created: '2020-01-24T19:00:32.917Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create or modify shortcuts that can execute a program during system boot or user login. Shortcuts
  or symbolic links are used to reference other files or programs that will be opened or executed when the shortcut is clicked
  or executed by a system startup process.


  Adversaries may abuse shortcuts in the startup folder to execute their tools and achieve persistence.(Citation: Shortcut
  for Persistence ) Although often used as payloads in an infection chain (e.g. [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)),
  adversaries may also create a new shortcut as a means of indirection, while also abusing [Masquerading](https://attack.mitre.org/techniques/T1036)
  to make the malicious shortcut appear as a legitimate program. Adversaries can also edit the target path or entirely replace
  an existing shortcut so their malware will be executed instead of the intended legitimate program.


  Shortcuts can also be abused to establish persistence by implementing other methods. For example, LNK browser extensions
  may be modified (e.g. [Browser Extensions](https://attack.mitre.org/techniques/T1176/001)) to persistently launch malware.'
external_references:
- external_id: T1547.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/009
- description: Elastic. (n.d.). Shortcut File Written or Modified for Persistence. Retrieved June 1, 2022.
  source_name: 'Shortcut for Persistence '
  url: https://www.elastic.co/guide/en/security/7.17/shortcut-file-written-or-modified-for-persistence.html#shortcut-file-written-or-modified-for-persistence
- description: French, D., Filar, B.. (2020, March 21). A Chain Is No Stronger Than Its Weakest LNK. Retrieved November 30,
    2020.
  source_name: BSidesSLC 2020 - LNK Elastic
  url: https://www.youtube.com/watch?v=nJ0UsyiUEqQ
id: attack-pattern--4ab929c6-ee2d-4fb5-aab4-b14be2ed7179
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:48:44.403Z'
name: Shortcut Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- David French, Elastic
- Bobby, Filar, Elastic
- Travis Smith, Tripwire
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.3'
```
