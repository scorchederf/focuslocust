---
parsed_by: focuslocust
source: mitre
type: generated
---
# Non-Standard Port

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1571` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Non-Standard Port](../../attack/techniques/T1571-non-standard-port.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1571 |
| name | Non-Standard Port |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1571 |

## Preserved Source Material

```yaml
created: '2020-03-14T18:18:32.443Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may communicate using a protocol and port pairing that are typically not associated. For example,
  HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed
  to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or
  muddle analysis/parsing of network data.


  Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration
  settings can be used to modify protocol and port pairings.(Citation: change_rdp_port_conti)'
external_references:
- external_id: T1571
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1571
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: 'Security Response attack Investigation Team. (2019, March 27). Elfin: Relentless Espionage Group Targets Multiple
    Organizations in Saudi Arabia and U.S.. Retrieved April 10, 2019.'
  source_name: Symantec Elfin Mar 2019
  url: https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage
- description: 'The DFIR Report. (2022, March 1). "Change RDP port" #ContiLeaks. Retrieved September 12, 2024.'
  source_name: change_rdp_port_conti
  url: https://x.com/TheDFIRReport/status/1498657772254240768
- description: Zhang, X. (2018, April 05). Analysis of New Agent Tesla Spyware Variant. Retrieved November 5, 2018.
  source_name: Fortinet Agent Tesla April 2018
  url: https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html
id: attack-pattern--b18eae87-b469-4e14-b454-b171b416bc18
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:14.187Z'
name: Non-Standard Port
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '1.3'
```
