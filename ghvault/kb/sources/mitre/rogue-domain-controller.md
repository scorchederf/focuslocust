---
parsed_by: focuslocust
source: mitre
type: generated
---
# Rogue Domain Controller

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1207` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Rogue Domain Controller](../../attack/techniques/T1207-rogue-domain-controller.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1207 |
| name | Rogue Domain Controller |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1207 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data. DCShadow
  may be used to create a rogue Domain Controller (DC). DCShadow is a method of manipulating Active Directory (AD) data, including
  objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a DC. (Citation:
  DCShadow Blog) Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain
  object, including credentials and keys.


  Registering a rogue DC involves creating a new server and nTDSDSA objects in the Configuration partition of the AD schema,
  which requires Administrator privileges (either Domain or local to the DC) or the KRBTGT hash. (Citation: Adsecurity Mimikatz
  Guide)


  This technique may bypass system logging and security monitors such as security information and event management (SIEM)
  products (since actions taken on a rogue DC may not be reported to these sensors). (Citation: DCShadow Blog) The technique
  may also be used to alter and delete replication and other associated metadata to obstruct forensic analysis. Adversaries
  may also utilize this technique to perform [SID-History Injection](https://attack.mitre.org/techniques/T1134/005) and/or
  manipulate AD objects (such as accounts, access control lists, schemas) to establish backdoors for Persistence. (Citation:
  DCShadow Blog)'
external_references:
- external_id: T1207
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1207
- description: Delpy, B. & LE TOUX, V. (n.d.). DCShadow. Retrieved March 20, 2018.
  source_name: DCShadow Blog
  url: https://www.dcshadow.com/
- description: Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.
  source_name: Adsecurity Mimikatz Guide
  url: https://adsecurity.org/?page_id=1821
id: attack-pattern--564998d8-ab3e-4123-93fb-eccaa6b9714a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:52.911Z'
name: Rogue Domain Controller
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Vincent Le Toux
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
