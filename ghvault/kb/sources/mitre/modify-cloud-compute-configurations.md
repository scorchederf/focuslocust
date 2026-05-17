---
parsed_by: focuslocust
source: mitre
type: generated
---
# Modify Cloud Compute Configurations

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1578.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Modify Cloud Compute Configurations](../../attack/techniques/T1578.005-modify-cloud-compute-configurations.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1578.005 |
| name | Modify Cloud Compute Configurations |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1578/005 |

## Preserved Source Material

```yaml
created: '2023-09-05T14:19:17.486Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify settings that directly affect the size, locations, and resources available to cloud compute
  infrastructure in order to evade defenses. These settings may include service quotas, subscription associations, tenant-wide
  policies, or other configurations that impact available compute. Such modifications may allow adversaries to abuse the victim’s
  compute resources to achieve their goals, potentially without affecting the execution of running instances and/or revealing
  their activities to the victim.


  For example, cloud providers often limit customer usage of compute resources via quotas. Customers may request adjustments
  to these quotas to support increased computing needs, though these adjustments may require approval from the cloud provider.
  Adversaries who compromise a cloud environment may similarly request quota adjustments in order to support their activities,
  such as enabling additional [Resource Hijacking](https://attack.mitre.org/techniques/T1496) without raising suspicion by
  using up a victim’s entire quota.(Citation: Microsoft Cryptojacking 2023) Adversaries may also increase allowed resource
  usage by modifying any tenant-wide policies that limit the sizes of deployed virtual machines.(Citation: Microsoft Azure
  Policy)


  Adversaries may also modify settings that affect where cloud resources can be deployed, such as enabling [Unused/Unsupported
  Cloud Regions](https://attack.mitre.org/techniques/T1535). '
external_references:
- external_id: T1578.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1578/005
- description: 'Microsoft Threat Intelligence. (2023, July 25). Cryptojacking: Understanding and defending against cloud compute
    resource abuse. Retrieved September 5, 2023.'
  source_name: Microsoft Cryptojacking 2023
  url: https://www.microsoft.com/en-us/security/blog/2023/07/25/cryptojacking-understanding-and-defending-against-cloud-compute-resource-abuse/
- description: Microsoft. (2023, August 30). Azure Policy built-in policy definitions. Retrieved September 5, 2023.
  source_name: Microsoft Azure Policy
  url: https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies#compute
id: attack-pattern--ca00366b-83a1-4c7b-a0ce-8ff950a7c87f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.098Z'
name: Modify Cloud Compute Configurations
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Amir Gharib, Microsoft Threat Intelligence
- Blake Strom, Microsoft Threat Intelligence
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '3.0'
```
