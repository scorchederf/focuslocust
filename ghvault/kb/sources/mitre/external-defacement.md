---
parsed_by: focuslocust
source: mitre
type: generated
---
# External Defacement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1491.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [External Defacement](../../attack/techniques/T1491.002-external-defacement.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1491.002 |
| name | External Defacement |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1491/002 |

## Preserved Source Material

```yaml
created: '2020-02-20T14:34:08.496Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may deface systems external to an organization in an attempt to deliver messaging, intimidate,
  or otherwise mislead an organization or users. [External Defacement](https://attack.mitre.org/techniques/T1491/002) may
  ultimately cause users to distrust the systems and to question/discredit the system’s integrity. Externally-facing websites
  are a common victim of defacement; often targeted by adversary and hacktivist groups in order to push a political message
  or spread propaganda.(Citation: FireEye Cyber Threats to Media Industries)(Citation: Kevin Mandia Statement to US Senate
  Committee on Intelligence)(Citation: Anonymous Hackers Deface Russian Govt Site) [External Defacement](https://attack.mitre.org/techniques/T1491/002)
  may be used as a catalyst to trigger events, or as a response to actions taken by an organization or government. Similarly,
  website defacement may also be used as setup, or a precursor, for future attacks such as [Drive-by Compromise](https://attack.mitre.org/techniques/T1189).(Citation:
  Trend Micro Deep Dive Into Defacement)'
external_references:
- external_id: T1491.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1491/002
- description: Andy. (2018, May 12). ‘Anonymous’ Hackers Deface Russian Govt. Site to Protest Web-Blocking (NSFW). Retrieved
    April 19, 2019.
  source_name: Anonymous Hackers Deface Russian Govt Site
  url: https://torrentfreak.com/anonymous-hackers-deface-russian-govt-site-to-protest-web-blocking-nsfw-180512/
- description: FireEye. (n.d.). Retrieved November 17, 2024.
  source_name: FireEye Cyber Threats to Media Industries
  url: https://web.archive.org/web/20210719110553/https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/ib-entertainment.pdf
- description: Kevin Mandia. (2017, March 30). Prepared Statement of Kevin Mandia, CEO of FireEye, Inc. before the United
    States Senate Select Committee on Intelligence. Retrieved April 19, 2019.
  source_name: Kevin Mandia Statement to US Senate Committee on Intelligence
  url: https://www.intelligence.senate.gov/sites/default/files/documents/os-kmandia-033017.pdf
- description: 'Marco Balduzzi, Ryan Flores, Lion Gu, Federico Maggi, Vincenzo Ciancaglini, Roel Reyes, Akira Urano. (n.d.).
    A Deep Dive into Defacement: How Geopolitical Events Trigger Web Attacks. Retrieved April 19, 2019.'
  source_name: Trend Micro Deep Dive Into Defacement
  url: https://documents.trendmicro.com/assets/white_papers/wp-a-deep-dive-into-defacement.pdf
id: attack-pattern--0cfe31a7-81fc-472c-bc45-e2808d1066a3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-10-24T17:48:23.460Z'
name: External Defacement
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Integrity
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- IaaS
- Linux
- macOS
x_mitre_version: '1.2'
```
