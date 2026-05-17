---
parsed_by: focuslocust
source: mitre
type: generated
---
# Active Scanning

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1595` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Scanning](../../attack/techniques/T1595-active-scanning.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1595 |
| name | Active Scanning |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1595 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:53:16.526Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute active reconnaissance scans to gather information that can be used during targeting.
  Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of
  reconnaissance that do not involve direct interaction.


  Adversaries may perform different forms of active scanning depending on what information they seek to gather. These scans
  can also be performed in various ways, including using native features of network protocols such as ICMP.(Citation: Botnet
  Scan)(Citation: OWASP Fingerprinting) Information from these scans may reveal opportunities for other forms of reconnaissance
  (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)),
  establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)),
  and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Exploit Public-Facing
  Application](https://attack.mitre.org/techniques/T1190)).'
external_references:
- external_id: T1595
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1595
- description: Dainotti, A. et al. (2012). Analysis of a “/0” Stealth Scan from a Botnet. Retrieved October 20, 2020.
  source_name: Botnet Scan
  url: https://www.caida.org/publications/papers/2012/analysis_slash_zero/analysis_slash_zero.pdf
- description: OWASP Wiki. (2018, February 16). OAT-004 Fingerprinting. Retrieved October 20, 2020.
  source_name: OWASP Fingerprinting
  url: https://wiki.owasp.org/index.php/OAT-004_Fingerprinting
id: attack-pattern--67073dde-d720-45ae-83da-b12d5e73ca3b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:53.018Z'
name: Active Scanning
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
- PRE
x_mitre_version: '1.0'
```
