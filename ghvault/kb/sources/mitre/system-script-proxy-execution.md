---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Script Proxy Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1216` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1216 |
| name | System Script Proxy Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1216 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files.
  Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be
  used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute
  malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker
  Bypass List)'
external_references:
- external_id: T1216
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1216
- description: Moe, O. (2018, March 1). Ultimate AppLocker Bypass List. Retrieved April 10, 2018.
  source_name: GitHub Ultimate AppLocker Bypass List
  url: https://github.com/api0cradle/UltimateAppLockerByPassList
- description: Oddvar Moe et al. (2022, February).  Living Off The Land Binaries, Scripts and Libraries. Retrieved March 7,
    2022.
  source_name: LOLBAS Project
  url: https://github.com/LOLBAS-Project/LOLBAS#criteria
id: attack-pattern--f6fe9070-7a65-49ea-ae72-76292f42cebe
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:42:22.297Z'
name: System Script Proxy Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Praetorian
- Wes Hurd
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
