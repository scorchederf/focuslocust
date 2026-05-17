---
parsed_by: focuslocust
source: mitre
type: generated
---
# Compile After Delivery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Compile After Delivery](../../attack/techniques/T1027.004-compile-after-delivery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.004 |
| name | Compile After Delivery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/004 |

## Preserved Source Material

```yaml
created: '2020-03-16T15:30:57.711Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to make payloads difficult to discover and analyze by delivering files to victims as
  uncompiled code. Text-based source code files may subvert analysis and scrutiny from protections targeting executables/binaries.
  These payloads will need to be compiled before execution; typically via native utilities such as ilasm.exe(Citation: ATTACK
  IQ), csc.exe, or GCC/MinGW.(Citation: ClearSky MuddyWater Nov 2018)


  Source code payloads may also be encrypted, encoded, and/or embedded within other files, such as those delivered as a [Phishing](https://attack.mitre.org/techniques/T1566).
  Payloads may also be delivered in formats unrecognizable and inherently benign to the native OS (ex: EXEs on macOS/Linux)
  before later being (re)compiled into a proper executable binary with a bundled compiler and execution framework.(Citation:
  TrendMicro WindowsAppMac)'
external_references:
- external_id: T1027.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/004
- description: 'ClearSky Cyber Security. (2018, November). MuddyWater Operations in Lebanon and Oman: Using an Israeli compromised
    domain for a two-stage campaign. Retrieved November 29, 2018.'
  source_name: ClearSky MuddyWater Nov 2018
  url: https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf
- description: 'Federico Quattrin, Nick Desler, Tin Tam, & Matthew Rutkoske. (2023, March 16). Hiding in Plain Sight: Monitoring
    and Testing for Living-Off-the-Land Binaries. Retrieved July 15, 2024.'
  source_name: ATTACK IQ
  url: https://www.attackiq.com/2023/03/16/hiding-in-plain-sight/
- description: Trend Micro. (2019, February 11). Windows App Runs on Mac, Downloads Info Stealer and Adware. Retrieved April
    25, 2019.
  source_name: TrendMicro WindowsAppMac
  url: https://blog.trendmicro.com/trendlabs-security-intelligence/windows-app-runs-on-mac-downloads-info-stealer-and-adware/
id: attack-pattern--c726e0a2-a57a-4b7b-a973-d0f013246617
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:16:52.765Z'
name: Compile After Delivery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Liran Ravich, CardinalOps
- Praetorian
- Ye Yint Min Thu Htut, Offensive Security Team, DBS Bank
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
