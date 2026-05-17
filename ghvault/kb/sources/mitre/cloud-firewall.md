---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Firewall

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1686.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Firewall](../../attack/techniques/T1686.001-cloud-firewall.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1686.001 |
| name | Cloud Firewall |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1686/001 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:04.618Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access
  to cloud resources.


  Cloud environments typically utilize restrictive security groups and firewall rules that only allow network activity from
  trusted IP addresses via expected ports and protocols. An adversary with appropriate permissions may introduce new firewall
  rules or policies to allow access into a victim cloud environment and/or move laterally from the cloud control plane to
  the data plane.


  For example, an adversary may use a script or utility that creates new ingress rules in existing security groups (or creates
  new security groups entirely) to allow any TCP/IP connectivity to a cloud-hosted instance. They may also remove networking
  limitations to support traffic associated with malicious activity (such as cryptomining).(Citation: Palo Alto Unit 42 Compromised
  Cloud Compute Credentials 2022)(Citation: Expel AWS)'
external_references:
- external_id: T1686.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1686/001
- description: Anthony Randazzo, Britton Manahan, Sam Lipton. (2020, April 28). Managed Detection & Response for AWS. Retrieved
    April 15, 2026.
  source_name: Expel AWS
  url: https://expel.com/blog/finding-evil-in-aws/
- description: 'Dror Alon. (2022, December 8). Compromised Cloud Compute Credentials: Case Studies From the Wild. Retrieved
    March 9, 2023.'
  source_name: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022
  url: https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/
id: attack-pattern--ee474564-64be-4b83-a958-53f238f49b01
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:38:27.348Z'
name: Cloud Firewall
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Arun Seelagan, CISA
- Expel
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '1.0'
```
