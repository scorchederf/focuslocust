---
parsed_by: focuslocust
source: mitre
type: generated
---
# Stripped Payloads

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.008` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Stripped Payloads](../../attack/techniques/T1027.008-stripped-payloads.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.008 |
| name | Stripped Payloads |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/008 |

## Preserved Source Material

```yaml
created: '2022-09-29T18:30:12.244Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to make a payload difficult to analyze by removing symbols, strings, and other human
  readable information. Scripts and executables may contain variables names and other strings that help developers document
  code functionality. Symbols are often created by an operating system’s `linker` when executable payloads are compiled. Reverse
  engineers use these symbols and strings to analyze code and to identify functionality in payloads.(Citation: Mandiant golang
  stripped binaries explanation)(Citation: intezer stripped binaries elf files 2018)


  Adversaries may use stripped payloads in order to make malware analysis more difficult. For example, compilers and other
  tools may provide features to remove or obfuscate strings and symbols. Adversaries have also used stripped payload formats,
  such as run-only AppleScripts, a compiled and stripped version of [AppleScript](https://attack.mitre.org/techniques/T1059/002),
  to evade detection and analysis. The lack of human-readable information may directly hinder detection and analysis of payloads.(Citation:
  SentinelLabs reversing run-only applescripts 2021)'
external_references:
- external_id: T1027.008
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/008
- description: 'Ignacio Sanmillan. (2018, February 7). Executable and Linkable Format 101. Part 2: Symbols. Retrieved September
    29, 2022.'
  source_name: intezer stripped binaries elf files 2018
  url: https://www.intezer.com/blog/malware-analysis/executable-linkable-format-101-part-2-symbols/
- description: Phil Stokes. (2021, January 11). FADE DEAD | Adventures in Reversing Malicious Run-Only AppleScripts. Retrieved
    September 29, 2022.
  source_name: SentinelLabs reversing run-only applescripts 2021
  url: https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/
- description: STEPHEN ECKELS. (2022, February 28). Ready, Set, Go — Golang Internals and Symbol Recovery. Retrieved September
    29, 2022.
  source_name: Mandiant golang stripped binaries explanation
  url: https://www.mandiant.com/resources/blog/golang-internals-symbol-recovery
id: attack-pattern--2f41939b-54c3-41d6-8f8b-35f1ec18ed97
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:21:58.918Z'
name: Stripped Payloads
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
- Network Devices
- Windows
x_mitre_version: '2.0'
```
