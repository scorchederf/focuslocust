---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Sniffing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1040` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Sniffing](../../attack/techniques/T1040-network-sniffing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1040 |
| name | Network Sniffing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1040 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:41.399Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may passively sniff network traffic to capture information about an environment, including authentication
  material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture
  information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to
  passively access data in transit over the network, or use span ports to capture a larger amount of data.


  Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol.
  Techniques for name service resolution poisoning, such as [Name Resolution Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001),
  can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.


  Network sniffing may reveal configuration details, such as running services, version numbers, and other network characteristics
  (e.g. IP addresses, hostnames, VLAN IDs) necessary for subsequent [Lateral Movement](https://attack.mitre.org/tactics/TA0008)
  and/or [Stealth](https://attack.mitre.org/tactics/TA0005) activities. Adversaries may likely also utilize network sniffing
  during [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) (AiTM) to passively gain additional knowledge
  about the environment.


  In cloud-based environments, adversaries may still be able to use traffic mirroring services to sniff network traffic from
  virtual machines. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified
  instances to collect traffic from and specified targets to send collected traffic to.(Citation: AWS Traffic Mirroring)(Citation:
  GCP Packet Mirroring)(Citation: Azure Virtual Network TAP) Often, much of this traffic will be in cleartext due to the use
  of TLS termination at the load balancer level to reduce the strain of encrypting and decrypting traffic.(Citation: Rhino
  Security Labs AWS VPC Traffic Mirroring)(Citation: SpecterOps AWS Traffic Mirroring) The adversary can then use exfiltration
  techniques such as Transfer Data to Cloud Account in order to access the sniffed traffic.(Citation: Rhino Security Labs
  AWS VPC Traffic Mirroring)


  On network devices, adversaries may perform network captures using [Network Device CLI](https://attack.mitre.org/techniques/T1059/008)
  commands such as `monitor capture`.(Citation: US-CERT-TA18-106A)(Citation: capture_embedded_packet_on_software)'
external_references:
- external_id: T1040
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1040
- description: Amazon Web Services. (n.d.). How Traffic Mirroring works. Retrieved March 17, 2022.
  source_name: AWS Traffic Mirroring
  url: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html
- description: Cisco. (2022, August 17). Configure and Capture Embedded Packet on Software. Retrieved July 13, 2022.
  source_name: capture_embedded_packet_on_software
  url: https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-embedded-packet-capture/116045-productconfig-epc-00.html
- description: Google Cloud. (n.d.). Packet Mirroring overview. Retrieved March 17, 2022.
  source_name: GCP Packet Mirroring
  url: https://cloud.google.com/vpc/docs/packet-mirroring
- description: Luke Paine. (2020, March 11). Through the Looking Glass — Part 1. Retrieved March 17, 2022.
  source_name: SpecterOps AWS Traffic Mirroring
  url: https://posts.specterops.io/through-the-looking-glass-part-1-f539ae308512
- description: Microsoft. (2022, February 9). Virtual network TAP. Retrieved March 17, 2022.
  source_name: Azure Virtual Network TAP
  url: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview
- description: Spencer Gietzen. (2019, September 17). Abusing VPC Traffic Mirroring in AWS. Retrieved March 17, 2022.
  source_name: Rhino Security Labs AWS VPC Traffic Mirroring
  url: https://rhinosecuritylabs.com/aws/abusing-vpc-traffic-mirroring-in-aws/
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
id: attack-pattern--3257eb21-f9a7-4430-8de1-d8b6e288f529
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:36.910Z'
name: Network Sniffing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Oleg Kolesnikov, Securonix
- Tiago Faria, 3CORESec
- Austin Clark, @c2defense
- Itamar Mizrahi, Cymptom
- Eliraz Levi, Hunters
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.7'
```
