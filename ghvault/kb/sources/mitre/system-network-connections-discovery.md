---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Network Connections Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1049` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1049 |
| name | System Network Connections Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1049 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:45.139Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently\
  \ accessing or from remote systems by querying for information over the network. \n\nAn adversary who gains access to a\
  \ system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine\
  \ what systems and services are connected. The actions performed are likely the same types of discovery techniques depending\
  \ on the operating system, but the resulting information may include details about the networked cloud environment relevant\
  \ to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.(Citation: Amazon\
  \ AWS VPC Guide)(Citation: Microsoft Azure Virtual Network Overview)(Citation: Google VPC Overview) Similarly, adversaries\
  \ who gain access to network devices may also perform similar discovery activities to gather information about connected\
  \ systems and services.\n\nUtilities and commands that acquire this information include [netstat](https://attack.mitre.org/software/S0104),\
  \ \"net use,\" and \"net session\" with [Net](https://attack.mitre.org/software/S0039). In Mac and Linux, [netstat](https://attack.mitre.org/software/S0104)\
  \ and <code>lsof</code> can be used to list current connections. <code>who -a</code> and <code>w</code> can be used to show\
  \ which users are currently logged in, similar to \"net session\". Additionally, built-in features native to network devices\
  \ and [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) may be used (e.g. <code>show ip sockets</code>,\
  \ <code>show tcp brief</code>).(Citation: US-CERT-TA18-106A) On ESXi servers, the command `esxi network ip connection list`\
  \ can be used to list active network connections.(Citation: Sygnia ESXi Ransomware 2025)"
external_references:
- external_id: T1049
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1049
- description: Amazon. (n.d.). What Is Amazon VPC?. Retrieved October 6, 2019.
  source_name: Amazon AWS VPC Guide
  url: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- description: Annamalai, N., Casey, C., Almeida, M., et. al.. (2019, June 18). What is Azure Virtual Network?. Retrieved
    October 6, 2019.
  source_name: Microsoft Azure Virtual Network Overview
  url: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
- description: Google. (2019, September 23). Virtual Private Cloud (VPC) network overview. Retrieved October 6, 2019.
  source_name: Google VPC Overview
  url: https://cloud.google.com/vpc/docs/vpc
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
- description: 'Zhongyuan Hau (Aaron), Ren Jie Yow, and Yoav Mazor. (2025, January 21). ESXi Ransomware Attacks: Stealthy
    Persistence through. Retrieved March 27, 2025.'
  source_name: Sygnia ESXi Ransomware 2025
  url: https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/
id: attack-pattern--7e150503-88e7-4861-866b-ff1ac82c4475
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:01.094Z'
name: System Network Connections Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
- Austin Clark, @c2defense
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '2.5'
```
