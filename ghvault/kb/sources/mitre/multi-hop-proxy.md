---
parsed_by: focuslocust
source: mitre
type: generated
---
# Multi-hop Proxy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1090.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Multi-hop Proxy](../../attack/techniques/T1090.003-multi-hop-proxy.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1090.003 |
| name | Multi-hop Proxy |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1090/003 |

## Preserved Source Material

```yaml
created: '2020-03-14T23:23:41.770Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may chain together multiple proxies to disguise the source of malicious traffic. Typically, a defender\
  \ will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not\
  \ be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source\
  \ of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies\
  \ to identify its source.\n\nFor example, adversaries may construct or use onion routing networks – such as the publicly\
  \ available [Tor](https://attack.mitre.org/software/S0183) network – to transport encrypted C2 traffic through a compromised\
  \ population, allowing communication with any device within the network.(Citation: Onion Routing) Adversaries may also use\
  \ operational relay box (ORB) networks composed of virtual private servers (VPS), Internet of Things (IoT) devices, smart\
  \ devices, and end-of-life routers to obfuscate their operations.(Citation: ORB Mandiant) \n\nIn the case of network infrastructure,\
  \ it is possible for an adversary to leverage multiple compromised devices to create a multi-hop proxy chain (i.e., [Network\
  \ Devices](https://attack.mitre.org/techniques/T1584/008)). By leveraging [Patch System Image](https://attack.mitre.org/techniques/T1601/001)\
  \ on routers, adversaries can add custom code to the affected network devices that will implement onion routing between\
  \ those nodes. This method is dependent upon the [Network Boundary Bridging](https://attack.mitre.org/techniques/T1599)\
  \ method allowing the adversaries to cross the protected network boundary of the Internet perimeter and into the organization’s\
  \ Wide-Area Network (WAN).  Protocols such as ICMP may be used as a transport.  \n\nSimilarly, adversaries may abuse peer-to-peer\
  \ (P2P) and blockchain-oriented infrastructure to implement routing between a decentralized network of peers.(Citation:\
  \ NGLite Trojan)"
external_references:
- external_id: T1090.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1090/003
- description: Raggi, Michael. (2024, May 22). IOC Extinction? China-Nexus Cyber Espionage Actors Use ORB Networks to Raise
    Cost on Defenders. Retrieved July 8, 2024.
  source_name: ORB Mandiant
  url: https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-orb-networks
- description: Robert Falcone, Jeff White, and Peter Renals. (2021, November 7). Targeted Attack Campaign Against ManageEngine
    ADSelfService Plus Delivers Godzilla Webshells, NGLite Trojan and KdcSponge Stealer. Retrieved February 8, 2024.
  source_name: NGLite Trojan
  url: https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/
- description: Wikipedia. (n.d.). Onion Routing. Retrieved October 20, 2020.
  source_name: Onion Routing
  url: https://en.wikipedia.org/wiki/Onion_routing
id: attack-pattern--a782ebe2-daba-42c7-bc82-e8e9d923162d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:11.774Z'
name: Multi-hop Proxy
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Eduardo Chavarro Ovalle
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '2.4'
```
