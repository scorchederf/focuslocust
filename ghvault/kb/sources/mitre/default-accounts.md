---
parsed_by: focuslocust
source: mitre
type: generated
---
# Default Accounts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1078.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Default Accounts](../../attack/techniques/T1078.001-default-accounts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1078.001 |
| name | Default Accounts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1078/001 |

## Preserved Source Material

```yaml
created: '2020-03-13T20:15:31.974Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may obtain and abuse credentials of a default account as a means of gaining Initial Access, Persistence,
  Privilege Escalation, or Defense Evasion. Default accounts are those that are built-into an OS, such as the Guest or Administrator
  accounts on Windows systems. Default accounts also include default factory/provider set accounts on other types of systems,
  software, or devices, including the root user account in AWS, the root user account in ESXi, and the default service account
  in Kubernetes.(Citation: Microsoft Local Accounts Feb 2019)(Citation: AWS Root User)(Citation: Threat Matrix for Kubernetes)


  Default accounts are not limited to client machines; rather, they also include accounts that are preset for equipment such
  as network devices and computer applications, whether they are internal, open source, or commercial. Appliances that come
  preset with a username and password combination pose a serious threat to organizations that do not change it post installation,
  as they are easy targets for an adversary. Similarly, adversaries may also utilize publicly disclosed or stolen [Private
  Keys](https://attack.mitre.org/techniques/T1552/004) or credential materials to legitimately connect to remote environments
  via [Remote Services](https://attack.mitre.org/techniques/T1021).(Citation: Metasploit SSH Module)


  Default accounts may be created on a system after initial setup by connecting or integrating it with another application.
  For example, when an ESXi server is connected to a vCenter server, a default privileged account called `vpxuser` is created
  on the ESXi server. If a threat actor is able to compromise this account’s credentials (for example, via [Exploitation for
  Credential Access](https://attack.mitre.org/techniques/T1212) on the vCenter host), they will then have access to the ESXi
  server.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Pentera vCenter Information Disclosure)'
external_references:
- external_id: T1078.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1078/001
- description: Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by
    Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.
  source_name: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023
  url: https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/
- description: Amazon. (n.d.). AWS Account Root User. Retrieved April 5, 2021.
  source_name: AWS Root User
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html
- description: Microsoft. (2018, December 9). Local Accounts. Retrieved February 11, 2019.
  source_name: Microsoft Local Accounts Feb 2019
  url: https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts
- description: undefined. (n.d.). Retrieved April 12, 2019.
  source_name: Metasploit SSH Module
  url: https://github.com/rapid7/metasploit-framework/tree/master/modules/exploits/linux/ssh
- description: Weizman, Y. (2020, April 2). Threat Matrix for Kubernetes. Retrieved March 30, 2021.
  source_name: Threat Matrix for Kubernetes
  url: https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/
- description: Yuval Lazar. (2022, March 29). Mitigating VMware vCenter Information Disclosure. Retrieved March 26, 2025.
  source_name: Pentera vCenter Information Disclosure
  url: https://pentera.io/blog/information-disclosure-in-vmware-vcenter/
id: attack-pattern--6151cbea-819b-455a-9fa6-99a1cc58797d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
- kill_chain_name: mitre-attack
  phase_name: initial-access
modified: '2026-04-15T22:50:51.753Z'
name: Default Accounts
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Janantha Marasinghe
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Network Devices
- Office Suite
- SaaS
- Windows
x_mitre_version: '2.0'
```
