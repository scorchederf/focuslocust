---
parsed_by: focuslocust
source: mitre
type: generated
---
# Non-Application Layer Protocol

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1095` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Non-Application Layer Protocol](../../attack/techniques/T1095-non-application-layer-protocol.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1095 |
| name | Non-Application Layer Protocol |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1095 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:10.728Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among
  infected hosts within a network. The list of possible protocols is extensive.(Citation: Wikipedia OSI) Specific examples
  include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols,
  such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled
  protocols, such as Serial over LAN (SOL).


  ICMP communication between hosts is one example.(Citation: Cisco Synful Knock Evolution) Because ICMP is part of the Internet
  Protocol Suite, it is required to be implemented by all IP-compatible hosts.(Citation: Microsoft ICMP) However, it is not
  as commonly monitored as other Internet Protocols such as TCP or UDP and may be used by adversaries to hide communications.


  In ESXi environments, adversaries may leverage the Virtual Machine Communication Interface (VMCI) for communication between
  guest virtual machines and the ESXi host. This traffic is similar to client-server communications on traditional network
  sockets but is localized to the physical machine running the ESXi host, meaning it does not traverse external networks (routers,
  switches). This results in communications that are invisible to external monitoring and standard networking tools like tcpdump,
  netstat, nmap, and Wireshark. By adding a VMCI backdoor to a compromised ESXi host, adversaries may persistently regain
  access from any guest VM to the compromised ESXi host’s backdoor, regardless of network segmentation or firewall rules in
  place.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)'
external_references:
- external_id: T1095
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1095
- description: Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by
    Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.
  source_name: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023
  url: https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: Graham Holmes. (2015, October 8). Evolution of attacks on Cisco IOS devices. Retrieved October 19, 2020.
  source_name: Cisco Synful Knock Evolution
  url: https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices
- description: Microsoft. (n.d.). Internet Control Message Protocol (ICMP) Basics. Retrieved December 1, 2014.
  source_name: Microsoft ICMP
  url: http://support.microsoft.com/KB/170292
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
- description: Wikipedia. (n.d.). List of network protocols (OSI model). Retrieved December 4, 2014.
  source_name: Wikipedia OSI
  url: http://en.wikipedia.org/wiki/List_of_network_protocols_%28OSI_model%29
id: attack-pattern--c21d5a77-d422-4a69-acd7-2c53c1faa34b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:20.136Z'
name: Non-Application Layer Protocol
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Ryan Becwar
- Duane Michael
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
x_mitre_version: '2.4'
```
