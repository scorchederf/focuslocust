---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Network Configuration Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1016` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1016 |
| name | System Network Configuration Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1016 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:27.342Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses,
  of systems they access or through information discovery of remote systems. Several operating system administration utilities
  exist that can be used to gather this information. Examples include [Arp](https://attack.mitre.org/software/S0099), [ipconfig](https://attack.mitre.org/software/S0100)/[ifconfig](https://attack.mitre.org/software/S0101),
  [nbtstat](https://attack.mitre.org/software/S0102), and [route](https://attack.mitre.org/software/S0103).


  Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to
  gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes
  (e.g. <code>show ip route</code>, <code>show ip interface</code>).(Citation: US-CERT-TA18-106A)(Citation: Mandiant APT41
  Global Intrusion ) On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the
  command `esxcli network nic list` will retrieve the MAC address, while `esxcli network ip interface ipv4 get` will retrieve
  the local IPv4 address.(Citation: Trellix Rnasomhouse 2024)


  Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016)
  during automated discovery to shape follow-on behaviors, including determining certain access within the target network
  and what actions to do next. '
external_references:
- external_id: T1016
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1016
- description: 'Gyler, C.,Perez D.,Jones, S.,Miller, S.. (2021, February 25). This is Not a Test: APT41 Initiates Global Intrusion
    Campaign Using Multiple Exploits. Retrieved February 17, 2022.'
  source_name: 'Mandiant APT41 Global Intrusion '
  url: https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits
- description: Pham Duy Phuc, Max Kersten, Noël Keijzer, and Michaël Schrijver. (2024, February 14). RansomHouse am See. Retrieved
    March 26, 2025.
  source_name: Trellix Rnasomhouse 2024
  url: https://www.trellix.com/en-au/blogs/research/ransomhouse-am-see/
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
id: attack-pattern--707399d6-ab3e-4963-9315-d9d3818cd6a0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:56.618Z'
name: System Network Configuration Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Austin Clark, @c2defense
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.7'
```
