---
parsed_by: focuslocust
source: mitre
type: generated
---
# Virtual Private Server

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1583.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Virtual Private Server](../../attack/techniques/T1583.003-virtual-private-server.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1583.003 |
| name | Virtual Private Server |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1583/003 |

## Preserved Source Material

```yaml
created: '2020-10-01T00:44:23.935Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may rent Virtual Private Servers (VPSs) that can be used during targeting. There exist a variety
  of cloud service providers that will sell virtual machines/containers as a service. By utilizing a VPS, adversaries can
  make it difficult to physically tie back operations to them. The use of cloud infrastructure can also make it easier for
  adversaries to rapidly provision, modify, and shut down their infrastructure.


  Acquiring a VPS for use in later stages of the adversary lifecycle, such as Command and Control, can allow adversaries to
  benefit from the ubiquity and trust associated with higher reputation cloud service providers. Adversaries may also acquire
  infrastructure from VPS service providers that are known for renting VPSs with minimal registration information, allowing
  for more anonymous acquisitions of infrastructure.(Citation: TrendmicroHideoutsLease)'
external_references:
- external_id: T1583.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1583/003
- description: Koczwara, M. (2021, September 7). Hunting Cobalt Strike C2 with Shodan. Retrieved October 12, 2021.
  source_name: Koczwara Beacon Hunting Sep 2021
  url: https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2
- description: 'Max Goncharov. (2015, July 15). Criminal Hideouts for Lease: Bulletproof Hosting Services. Retrieved March
    6, 2017.'
  source_name: TrendmicroHideoutsLease
  url: https://documents.trendmicro.com/assets/wp/wp-criminal-hideouts-for-lease.pdf
- description: Stephens, A. (2020, July 13). SCANdalous! (External Detection Using Network Scan Data and Automation). Retrieved
    November 17, 2024.
  source_name: Mandiant SCANdalous Jul 2020
  url: https://cloud.google.com/blog/topics/threat-intelligence/scandalous-external-detection-using-network-scan-data-and-automation/
- description: 'ThreatConnect. (2020, December 15). Infrastructure Research and Hunting: Boiling the Domain Ocean. Retrieved
    October 12, 2021.'
  source_name: ThreatConnect Infrastructure Dec 2020
  url: https://threatconnect.com/blog/infrastructure-research-hunting/
id: attack-pattern--79da0971-3147-4af6-a4f5-e8cd447cd795
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:48:59.607Z'
name: Virtual Private Server
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
- PRE
x_mitre_version: '1.1'
```
