---
parsed_by: focuslocust
source: mitre
type: generated
---
# Junk Code Insertion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.016` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Junk Code Insertion](../../attack/techniques/T1027.016-junk-code-insertion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.016 |
| name | Junk Code Insertion |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/016 |

## Preserved Source Material

```yaml
created: '2025-03-04T21:38:49.913Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use junk code / dead code to obfuscate a malware’s functionality. Junk code is code that either
  does not execute, or if it does execute, does not change the functionality of the code. Junk code makes analysis more difficult
  and time-consuming, as the analyst steps through non-functional code instead of analyzing the main code. It also may hinder
  detections that rely on static code analysis due to the use of benign functionality, especially when combined with [Compression](https://attack.mitre.org/techniques/T1027/015)
  or [Software Packing](https://attack.mitre.org/techniques/T1027/002).(Citation: ReasonLabs)(Citation: ReasonLabs Cyberpedia
  Junk Code)


  No-Operation (NOP) instructions are an example of dead code commonly used in x86 assembly language. They are commonly used
  as the 0x90 opcode. When NOPs are added to malware, the disassembler may show the NOP instructions, leading to the analyst
  needing to step through them.(Citation: ReasonLabs)


  The use of junk / dead code insertion is distinct from [Binary Padding](https://attack.mitre.org/techniques/T1027/001) because
  the purpose is to obfuscate the functionality of the code, rather than simply to change the malware’s signature.   '
external_references:
- external_id: T1027.016
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/016
- description: ReasonLabs. (n.d.). What is Dead code insertion?. Retrieved March 4, 2025.
  source_name: ReasonLabs
  url: https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html
- description: What is Junk Code?. (n.d.). ReasonLabs. Retrieved April 4, 2025.
  source_name: ReasonLabs Cyberpedia Junk Code
  url: https://cyberpedia.reasonlabs.com/EN/junk%20code.html
id: attack-pattern--671cd17f-a765-48fd-adc4-dad1941b1ae3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:19:48.489Z'
name: Junk Code Insertion
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Joas Antonio dos Santos, @C0d3Cr4zy
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
