---
parsed_by: focuslocust
source: mitre
type: generated
---
# Software Packing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Software Packing](../../attack/techniques/T1027.002-software-packing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.002 |
| name | Software Packing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/002 |

## Preserved Source Material

```yaml
created: '2020-02-05T14:17:46.686Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may perform software packing or virtual machine software protection to conceal their code. Software\
  \ packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an\
  \ attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory. Virtual\
  \ machine software protection translates an executable's original code into a special format that only a special virtual\
  \ machine can run. A virtual machine is then called to run this code.(Citation: ESET FinFisher Jan 2018) \n\nUtilities used\
  \ to perform software packing are called packers. Example packers are MPRESS and UPX. A more comprehensive list of known\
  \ packers is available, but adversaries may create their own packing techniques that do not leave the same artifacts as\
  \ well-known packers to evade defenses.(Citation: Awesome Executable Packing)  "
external_references:
- external_id: T1027.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/002
- description: Alexandre D'Hondt. (n.d.). Awesome Executable Packing. Retrieved March 11, 2022.
  source_name: Awesome Executable Packing
  url: https://github.com/dhondta/awesome-executable-packing
- description: Kafka, F. (2018, January). ESET's Guide to Deobfuscating and Devirtualizing FinFisher. Retrieved August 12,
    2019.
  source_name: ESET FinFisher Jan 2018
  url: https://www.welivesecurity.com/wp-content/uploads/2018/01/WP-FinFisher.pdf
id: attack-pattern--deb98323-e13f-4b0c-8d94-175379069062
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:15:31.610Z'
name: Software Packing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Filip Kafka, ESET
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
