---
parsed_by: focuslocust
source: mitre
type: generated
---
# ARP Cache Poisoning

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1557.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ARP Cache Poisoning](../../attack/techniques/T1557.002-arp-cache-poisoning.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1557.002 |
| name | ARP Cache Poisoning |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1557/002 |

## Preserved Source Material

```yaml
created: '2020-10-15T12:05:58.755Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may poison Address Resolution Protocol (ARP) caches to position themselves between the communication
  of two or more networked devices. This activity may be used to enable follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040)
  or [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002).


  The ARP protocol is used to resolve IPv4 addresses to link layer addresses, such as a media access control (MAC) address.(Citation:
  RFC826 ARP) Devices in a local network segment communicate with each other by using link layer addresses. If a networked
  device does not have the link layer address of a particular networked device, it may send out a broadcast ARP request to
  the local network to translate the IP address to a MAC address. The device with the associated IP address directly replies
  with its MAC address. The networked device that made the ARP request will then use as well as store that information in
  its ARP cache.


  An adversary may passively wait for an ARP request to poison the ARP cache of the requesting device. The adversary may reply
  with their MAC address, thus deceiving the victim by making them believe that they are communicating with the intended networked
  device. For the adversary to poison the ARP cache, their reply must be faster than the one made by the legitimate IP address
  owner. Adversaries may also send a gratuitous ARP reply that maliciously announces the ownership of a particular IP address
  to all the devices in the local network segment.


  The ARP protocol is stateless and does not require authentication. Therefore, devices may wrongly add or update the MAC
  address of the IP address in their ARP cache.(Citation: Sans ARP Spoofing Aug 2003)(Citation: Cylance Cleaver)


  Adversaries may use ARP cache poisoning as a means to intercept network traffic. This activity may be used to collect and/or
  relay data such as credentials, especially those sent over an insecure, unencrypted protocol.(Citation: Sans ARP Spoofing
  Aug 2003)

  '
external_references:
- external_id: T1557.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1557/002
- description: Cylance. (2014, December). Operation Cleaver. Retrieved September 14, 2017.
  source_name: Cylance Cleaver
  url: https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf
- description: Plummer, D. (1982, November). An Ethernet Address Resolution Protocol. Retrieved October 15, 2020.
  source_name: RFC826 ARP
  url: https://tools.ietf.org/html/rfc826
- description: Siles, R. (2003, August). Real World ARP Spoofing. Retrieved October 15, 2020.
  source_name: Sans ARP Spoofing Aug 2003
  url: https://pen-testing.sans.org/resources/papers/gcih/real-world-arp-spoofing-105411
id: attack-pattern--cabe189c-a0e3-4965-a473-dcff00f17213
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:49:23.221Z'
name: ARP Cache Poisoning
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jon Sternstein, Stern Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Windows
- macOS
x_mitre_version: '1.1'
```
