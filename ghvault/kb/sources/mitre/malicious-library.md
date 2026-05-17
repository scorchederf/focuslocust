---
parsed_by: focuslocust
source: mitre
type: generated
---
# Malicious Library

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1204.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Malicious Library](../../attack/techniques/T1204.005-malicious-library.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1204.005 |
| name | Malicious Library |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1204/005 |

## Preserved Source Material

```yaml
created: '2025-05-22T19:50:18.472Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may rely on a user installing a malicious library to facilitate execution. Threat actors may [Upload
  Malware](https://attack.mitre.org/techniques/T1608/001) to package managers such as NPM and PyPi, as well as to public code
  repositories such as GitHub. User may install libraries without realizing they are malicious, thus bypassing techniques
  that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that establishes
  persistence, steals data, or mines cryptocurrency.(Citation: Datadog Security Labs Malicious PyPi Packages 2024)(Citation:
  Fortinet Malicious NPM Packages 2023)


  In some cases, threat actors may compromise and backdoor existing popular libraries (i.e., [Compromise Software Dependencies
  and Development Tools](https://attack.mitre.org/techniques/T1195/001)). Alternatively, they may create entirely new packages
  and leverage behaviors such as typosquatting to encourage users to install them.'
external_references:
- external_id: T1204.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1204/005
- description: ' Sebastian Obregoso  and Christophe Tafani-Dereeper. (2024, May 23). Malicious PyPI packages targeting highly
    specific MacOS machines. Retrieved May 22, 2025.'
  source_name: Datadog Security Labs Malicious PyPi Packages 2024
  url: https://securitylabs.datadoghq.com/articles/malicious-pypi-package-targeting-highly-specific-macos-machines/
- description: Jin Lee and Jenna Wang. (2023, October 2). Malicious Packages Hidden in NPM. Retrieved May 22, 2025.
  source_name: Fortinet Malicious NPM Packages 2023
  url: https://www.fortinet.com/blog/threat-research/malicious-packages-hiddin-in-npm
id: attack-pattern--73b24a10-6bf4-4af1-a81e-67b8bcb6c4e6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-05-22T21:22:40.822Z'
name: Malicious Library
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
- Linux
- macOS
- Windows
x_mitre_remote_support: false
x_mitre_version: '1.0'
```
