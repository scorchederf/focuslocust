---
parsed_by: focuslocust
source: mitre
type: generated
---
# Software Deployment Tools

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1072` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Software Deployment Tools](../../attack/techniques/T1072-software-deployment-tools.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1072 |
| name | Software Deployment Tools |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1072 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:57.201Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may gain access to and use centralized software suites installed within an enterprise to execute\
  \ commands and move laterally through the network. Configuration management and software deployment applications may be\
  \ used in an enterprise network or cloud environment for routine administration purposes. These systems may also be integrated\
  \ into CI/CD pipelines. Examples of such solutions include: SCCM, HBSS, Altiris, AWS Systems Manager, Microsoft Intune,\
  \ Azure Arc, and GCP Deployment Manager.  \n\nAccess to network-wide or enterprise-wide endpoint management software may\
  \ enable an adversary to achieve remote code execution on all connected systems. The access may be used to laterally move\
  \ to other systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.\n\n\
  SaaS-based configuration management services may allow for broad [Cloud Administration Command](https://attack.mitre.org/techniques/T1651)\
  \ on cloud-hosted instances, as well as the execution of arbitrary commands on on-premises endpoints. For example, Microsoft\
  \ Configuration Manager allows Global or Intune Administrators to run scripts as SYSTEM on on-premises devices joined to\
  \ Entra ID.(Citation: SpecterOps Lateral Movement from Azure to On-Prem AD 2020) Such services may also utilize [Web Protocols](https://attack.mitre.org/techniques/T1071/001)\
  \ to communicate back to adversary owned infrastructure.(Citation: Mitiga Security Advisory: SSM Agent as Remote Access\
  \ Trojan)\n\nNetwork infrastructure devices may also have configuration management tools that can be similarly abused by\
  \ adversaries.(Citation: Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation)\n\n\
  The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access\
  \ to the third-party system, or specific domain credentials may be required. However, the system may require an administrative\
  \ account to log in or to access specific functionality."
external_references:
- external_id: T1072
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1072
- description: ALEXANDER MARVI, BRAD SLAYBAUGH, DAN EBREO, TUFAIL AHMED, MUHAMMAD UMAIR, TINA JOHNSON. (2023, March 16). Fortinet
    Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved May 15, 2023.
  source_name: Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation
  url: https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem
- description: 'Andy Robbins. (2020, August 17). Death from Above: Lateral Movement from Azure to On-Prem AD. Retrieved March
    13, 2023.'
  source_name: SpecterOps Lateral Movement from Azure to On-Prem AD 2020
  url: https://posts.specterops.io/death-from-above-lateral-movement-from-azure-to-on-prem-ad-d18cb3959d4d
- description: 'Ariel Szarf, Or Aspir. (n.d.). Mitiga Security Advisory: Abusing the SSM Agent as a Remote Access Trojan.
    Retrieved January 31, 2024.'
  source_name: 'Mitiga Security Advisory: SSM Agent as Remote Access Trojan'
  url: https://www.mitiga.io/blog/mitiga-security-advisory-abusing-the-ssm-agent-as-a-remote-access-trojan
id: attack-pattern--92a78814-b191-47ca-909c-1ccfe3777414
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2025-10-24T17:49:06.595Z'
name: Software Deployment Tools
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Shane Tully, @securitygypsy
- Joe Gumke, U.S. Bank
- Tamir Yehuda
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- SaaS
- Windows
x_mitre_remote_support: false
x_mitre_version: '3.2'
```
