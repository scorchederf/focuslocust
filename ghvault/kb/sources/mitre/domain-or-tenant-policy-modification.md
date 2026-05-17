---
parsed_by: focuslocust
source: mitre
type: generated
---
# Domain or Tenant Policy Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1484` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Domain or Tenant Policy Modification](../../attack/techniques/T1484-domain-or-tenant-policy-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1484 |
| name | Domain or Tenant Policy Modification |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1484 |

## Preserved Source Material

```yaml
created: '2019-03-07T14:10:32.650Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may modify the configuration settings of a domain or identity tenant to evade defenses and/or escalate\
  \ privileges in centrally managed environments. Such services provide a centralized means of managing identity resources\
  \ such as devices and accounts, and often include configuration settings that may apply between domains or tenants such\
  \ as trust relationships, identity syncing, or identity federation.\n\nModifications to domain or tenant settings may include\
  \ altering domain Group Policy Objects (GPOs) in Microsoft Active Directory (AD) or changing trust settings for domains,\
  \ including federation trusts relationships between domains or tenants.\n\nWith sufficient permissions, adversaries can\
  \ modify domain or tenant policy settings. Since configuration settings for these services apply to a large number of identity\
  \ resources, there are a great number of potential attacks malicious outcomes that can stem from this abuse. Examples of\
  \ such abuse include:  \n\n* modifying GPOs to push a malicious [Scheduled Task](https://attack.mitre.org/techniques/T1053/005)\
  \ to computers throughout the domain environment(Citation: ADSecurity GPO Persistence 2016)(Citation: Wald0 Guide to GPOs)(Citation:\
  \ Harmj0y Abusing GPO Permissions)\n* modifying domain trusts to include an adversary-controlled domain, allowing adversaries\
  \ to  forge access tokens that will subsequently be accepted by victim domain resources(Citation: Microsoft - Customer Guidance\
  \ on Recent Nation-State Cyber Attacks)\n* changing configuration settings within the AD environment to implement a [Rogue\
  \ Domain Controller](https://attack.mitre.org/techniques/T1207).\n* adding new, adversary-controlled federated identity\
  \ providers to identity tenants, allowing adversaries to authenticate as any user managed by the victim tenant (Citation:\
  \ Okta Cross-Tenant Impersonation 2023)\n\nAdversaries may temporarily modify domain or tenant policy, carry out a malicious\
  \ action(s), and then revert the change to remove suspicious indicators."
external_references:
- external_id: T1484
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1484
- description: 'Metcalf, S. (2016, March 14). Sneaky Active Directory Persistence #17: Group Policy. Retrieved March 5, 2019.'
  source_name: ADSecurity GPO Persistence 2016
  url: https://adsecurity.org/?p=2716
- description: MSRC. (2020, December 13). Customer Guidance on Recent Nation-State Cyber Attacks. Retrieved December 30, 2020.
  source_name: Microsoft - Customer Guidance on Recent Nation-State Cyber Attacks
  url: https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/
- description: 'Okta Defensive Cyber Operations. (2023, August 31). Cross-Tenant Impersonation: Prevention and Detection.
    Retrieved February 15, 2024.'
  source_name: Okta Cross-Tenant Impersonation 2023
  url: https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection
- description: Robbins, A. (2018, April 2). A Red Teamer’s Guide to GPOs and OUs. Retrieved March 5, 2019.
  source_name: Wald0 Guide to GPOs
  url: https://wald0.com/?p=179
- description: Schroeder, W. (2016, March 17). Abusing GPO Permissions. Retrieved September 23, 2024.
  source_name: Harmj0y Abusing GPO Permissions
  url: https://blog.harmj0y.net/redteaming/abusing-gpo-permissions/
id: attack-pattern--ebb42bbe-62d7-47d7-a55f-3b08b61d792d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-16T20:07:53.114Z'
name: Domain or Tenant Policy Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Obsidian Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- Identity Provider
x_mitre_version: '4.0'
```
