---
parsed_by: focuslocust
source: mitre
type: generated
---
# Python

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Python](../../attack/techniques/T1059.006-python.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1059.006 |
| name | Python |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1059/006 |

## Preserved Source Material

```yaml
created: '2020-03-09T14:38:24.334Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Python commands and scripts for execution. Python is a very popular scripting/programming
  language, with capabilities to perform many functions. Python can be executed interactively from the command-line (via the
  <code>python.exe</code> interpreter) or via scripts (.py) that can be written and distributed to different systems. Python
  code can also be compiled into binary executables.(Citation: Zscaler APT31 Covid-19 October 2020)


  Python comes with many built-in packages to interact with the underlying system, such as file operations and device I/O.
  Adversaries can use these libraries to download and execute commands or other scripts as well as perform various malicious
  behaviors.'
external_references:
- external_id: T1059.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1059/006
- description: Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online
    Services. Retrieved March 24, 2021.
  source_name: Zscaler APT31 Covid-19 October 2020
  url: https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online
id: attack-pattern--cc3502b5-30cc-4473-ad48-42d51a6ef6d1
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:49:23.660Z'
name: Python
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
x_mitre_remote_support: false
x_mitre_version: '1.1'
```
