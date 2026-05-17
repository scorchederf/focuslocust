---
parsed_by: focuslocust
source: mitre
type: generated
---
# Trusted Relationship

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1199` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Trusted Relationship](../../attack/techniques/T1199-trusted-relationship.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1199 |
| name | Trusted Relationship |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1199 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through
  trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than
  standard mechanisms of gaining access to a network.


  Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal
  systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed
  security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider''s access
  may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the
  enterprise. As such, [Valid Accounts](https://attack.mitre.org/techniques/T1078) used by the other party for access to internal
  network systems may be compromised and used.(Citation: CISA IT Service Providers)


  In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions.
  By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships
  or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant.(Citation:
  Office 365 Delegated Administration)'
external_references:
- external_id: T1199
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1199
- description: CISA. (n.d.). APTs Targeting IT Service Provider Customers. Retrieved November 16, 2020.
  source_name: CISA IT Service Providers
  url: https://us-cert.cisa.gov/APTs-Targeting-IT-Service-Provider-Customers
- description: 'Microsoft. (n.d.). Partners: Offer delegated administration. Retrieved May 27, 2022.'
  source_name: Office 365 Delegated Administration
  url: https://support.microsoft.com/en-us/topic/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e?ui=en-us&rs=en-us&ad=us
id: attack-pattern--9fa07bef-9c81-421e-a8e5-ad4366c5a925
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: initial-access
modified: '2025-11-12T15:42:52.705Z'
name: Trusted Relationship
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Praetorian
- ExtraHop
- Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows
x_mitre_version: '2.4'
```
