---
parsed_by: focuslocust
source: mitre
type: generated
---
# Empire

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0363` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Empire](../../tools/unknown/empire.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | S0363 |
| name | Empire |
| type | tool |
| source | mitre |
| url | https://attack.mitre.org/software/S0363 |

## Preserved Source Material

```yaml
created: '2019-03-11T14:13:40.648Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and
  post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python,
  the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows
  and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint
  report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github
  PowerShell Empire)(Citation: GitHub ATTACK Empire)'
external_references:
- external_id: S0363
  source_name: mitre-attack
  url: https://attack.mitre.org/software/S0363
- description: '(Citation: Github PowerShell Empire)'
  source_name: EmPyre
- description: '(Citation: Github PowerShell Empire)'
  source_name: PowerShell Empire
- description: Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.
  source_name: Github PowerShell Empire
  url: https://github.com/PowerShellEmpire/Empire
- description: 'Stepanic, D. (2018, September 2). attck_empire: Generate ATT&CK Navigator layer file from PowerShell Empire
    agent logs. Retrieved March 11, 2019.'
  source_name: GitHub ATTACK Empire
  url: https://github.com/dstepanic/attck_empire
- description: The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand
    National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US
    National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available
    hacking tools. Retrieved March 11, 2019.
  source_name: NCSC Joint Report Public Tools
  url: https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools
id: tool--3433a9e8-1c47-4320-b9bf-ed449061d1c3
modified: '2025-10-24T03:33:19.777Z'
name: Empire
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: tool
x_mitre_aliases:
- Empire
- EmPyre
- PowerShell Empire
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.8'
```
