---
parsed_by: focuslocust
source: mitre
type: generated
---
# Group Policy Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1615` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Group Policy Discovery](../../attack/techniques/T1615-group-policy-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1615 |
| name | Group Policy Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1615 |

## Preserved Source Material

```yaml
created: '2021-08-06T13:10:12.916Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security
  measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in
  the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD).
  Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network
  path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence
  2016)


  Adversaries may use commands such as <code>gpresult</code> or various publicly available PowerShell functions, such as <code>Get-DomainGPO</code>
  and <code>Get-DomainGPOLocalGroup</code>, to gather information on Group Policy settings.(Citation: Microsoft gpresult)(Citation:
  Github PowerShell Empire) Adversaries may use this information to shape follow-on behaviors, including determining potential
  attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [Domain or Tenant
  Policy Modification](https://attack.mitre.org/techniques/T1484)) for their benefit.'
external_references:
- external_id: T1615
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1615
- description: 'Metcalf, S. (2016, March 14). Sneaky Active Directory Persistence #17: Group Policy. Retrieved March 5, 2019.'
  source_name: ADSecurity GPO Persistence 2016
  url: https://adsecurity.org/?p=2716
- description: Microsoft. (2017, October 16). gpresult. Retrieved August 6, 2021.
  source_name: Microsoft gpresult
  url: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult
- description: Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.
  source_name: Github PowerShell Empire
  url: https://github.com/PowerShellEmpire/Empire
- description: 'srachui. (2012, February 13). Group Policy Basics – Part 1: Understanding the Structure of a Group Policy
    Object. Retrieved March 5, 2019.'
  source_name: TechNet Group Policy Basics
  url: https://blogs.technet.microsoft.com/musings_of_a_technical_tam/2012/02/13/group-policy-basics-part-1-understanding-the-structure-of-a-group-policy-object/
id: attack-pattern--1b20efbf-8063-4fc3-a07d-b575318a301b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:28.148Z'
name: Group Policy Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Ted Samuels, Rapid7
- Jonhnathan Ribeiro, 3CORESec, @_w0rk3r
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.1'
```
