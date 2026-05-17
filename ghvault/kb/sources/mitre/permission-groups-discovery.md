---
parsed_by: focuslocust
source: mitre
type: generated
---
# Permission Groups Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1069` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Permission Groups Discovery](../../attack/techniques/T1069-permission-groups-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1069 |
| name | Permission Groups Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1069 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:55.471Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to discover group and permission settings. This information can help adversaries determine
  which user accounts and groups are available, the membership of users in particular groups, and which users and groups have
  elevated permissions.


  Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary
  with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike
  BloodHound April 2018)'
external_references:
- external_id: T1069
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1069
- description: Kubernetes. (n.d.). Authorization Overview. Retrieved June 24, 2021.
  source_name: K8s Authorization Overview
  url: https://kubernetes.io/docs/reference/access-authn-authz/authorization/
- description: 'Red Team Labs. (2018, April 24). Hidden Administrative Accounts: BloodHound to the Rescue. Retrieved October
    28, 2020.'
  source_name: CrowdStrike BloodHound April 2018
  url: https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/
id: attack-pattern--15dbf668-795c-41e6-8219-f0447c0e64ce
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:26.378Z'
name: Permission Groups Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Daniel Prizmant, Palo Alto Networks
- Yuval Avrahami, Palo Alto Networks
- Microsoft Threat Intelligence Center (MSTIC)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows
x_mitre_version: '2.6'
```
