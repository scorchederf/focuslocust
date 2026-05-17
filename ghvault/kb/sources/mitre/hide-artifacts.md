---
parsed_by: focuslocust
source: mitre
type: generated
---
# Hide Artifacts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hide Artifacts](../../attack/techniques/T1564-hide-artifacts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564 |
| name | Hide Artifacts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564 |

## Preserved Source Material

```yaml
created: '2020-02-26T17:41:25.933Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems
  may have features to hide various artifacts, such as important system files and administrative task execution, to avoid
  disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse
  these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.(Citation:
  Sofacy Komplex Trojan)(Citation: Cybereason OSX Pirrit)(Citation: MalwareBytes ADS July 2015)


  Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are
  isolated from common security instrumentation, such as through the use of virtualization technology.(Citation: Sophos Ragnar
  May 2020)'
external_references:
- external_id: T1564
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564
- description: Amit Serper. (2016). Cybereason Lab Analysis OSX.Pirrit. Retrieved December 10, 2021.
  source_name: Cybereason OSX Pirrit
  url: https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf
- description: Arntz, P. (2015, July 22). Introduction to Alternate Data Streams. Retrieved March 21, 2018.
  source_name: MalwareBytes ADS July 2015
  url: https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/
- description: Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved
    July 8, 2017.
  source_name: Sofacy Komplex Trojan
  url: https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/
- description: SophosLabs. (2020, May 21). Ragnar Locker ransomware deploys virtual machine to dodge security. Retrieved June
    29, 2020.
  source_name: Sophos Ragnar May 2020
  url: https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/
id: attack-pattern--22905430-4901-4c2a-84f6-98243cb173f8
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:17:25.231Z'
name: Hide Artifacts
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Office Suite
- Windows
x_mitre_version: '2.0'
```
