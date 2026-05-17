---
parsed_by: focuslocust
source: mitre
type: generated
---
# Clear Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1070.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Clear Persistence](../../attack/techniques/T1070.009-clear-persistence.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1070.009 |
| name | Clear Persistence |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1070/009 |

## Preserved Source Material

```yaml
created: '2022-07-29T19:32:11.552Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may clear artifacts associated with previously established persistence on a host system to remove
  evidence of their activity. This may involve various actions, such as removing services, deleting executables, [Modify Registry](https://attack.mitre.org/techniques/T1112),
  [Plist File Modification](https://attack.mitre.org/techniques/T1647), or other methods of cleanup to prevent defenders from
  collecting evidence of their persistent presence.(Citation: Cylance Dust Storm) Adversaries may also delete accounts previously
  created to maintain persistence (i.e. [Create Account](https://attack.mitre.org/techniques/T1136)).(Citation: Talos - Cisco
  Attack 2022)


  In some instances, artifacts of persistence may also be removed once an adversary’s persistence is executed in order to
  prevent errors with the new instance of the malware.(Citation: NCC Group Team9 June 2020)'
external_references:
- external_id: T1070.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1070/009
- description: Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.
  source_name: Cylance Dust Storm
  url: https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf
- description: Nick Biasini. (2022, August 10). Cisco Talos shares insights related to recent cyber attack on Cisco. Retrieved
    March 9, 2023.
  source_name: Talos - Cisco Attack 2022
  url: https://blog.talosintelligence.com/recent-cyber-attack/
- description: Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1,
    2020.
  source_name: NCC Group Team9 June 2020
  url: https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/
id: attack-pattern--d2c4e5ea-dbdf-4113-805a-b1e2a337fb33
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:28:24.292Z'
name: Clear Persistence
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Gavin Knapp
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
x_mitre_version: '2.0'
```
