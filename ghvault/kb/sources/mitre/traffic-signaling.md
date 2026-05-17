---
parsed_by: focuslocust
source: mitre
type: generated
---
# Traffic Signaling

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1205` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Traffic Signaling](../../attack/techniques/T1205-traffic-signaling.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1205 |
| name | Traffic Signaling |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1205 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use traffic signaling to hide open ports or other malicious functionality used for persistence
  or command and control. Traffic signaling involves the use of a magic value or sequence that must be sent to a system to
  trigger a special response, such as opening a closed port or executing a malicious task. This may take the form of sending
  a series of packets with certain characteristics before a port will be opened that the adversary can use for command and
  control. Usually this series of packets consists of attempted connections to a predefined sequence of closed ports (i.e.
  [Port Knocking](https://attack.mitre.org/techniques/T1205/001)), but can involve unusual flags, specific strings, or other
  unique characteristics. After the sequence is completed, opening a port may be accomplished by the host-based firewall,
  but could also be implemented by custom software.


  Adversaries may also communicate with an already open port, but the service listening on that port will only respond to
  commands or trigger other malicious functionality if passed the appropriate magic value(s).


  The observation of the signal packets to trigger the communication can be conducted through different methods. One means,
  originally implemented by Cd00r (Citation: Hartrell cd00r 2002), is to use the libpcap libraries to sniff for the packets
  in question. Another method leverages raw sockets, which enables the malware to use ports that are already open for use
  by other programs.


  On network devices, adversaries may use crafted packets to enable [Network Device Authentication](https://attack.mitre.org/techniques/T1556/004)
  for standard services offered by the device such as telnet.  Such signaling may also be used to open a closed service port
  such as telnet, or to trigger module modification of malware implants on the device, adding, removing, or changing malicious
  capabilities.  Adversaries may use crafted packets to attempt to connect to one or more (open or closed) ports, but may
  also attempt to connect to a router interface, broadcast, and network address IP on the same port in order to achieve their
  goals and objectives.(Citation: Cisco Synful Knock Evolution)(Citation: Mandiant - Synful Knock)(Citation: Cisco Blog Legacy
  Device Attacks)  To enable this traffic signaling on embedded devices, adversaries must first achieve and leverage [Patch
  System Image](https://attack.mitre.org/techniques/T1601/001) due to the monolithic nature of the architecture.


  Adversaries may also use the Wake-on-LAN feature to turn on powered off systems. Wake-on-LAN is a hardware feature that
  allows a powered down system to be powered on, or woken up, by sending a magic packet to it. Once the system is powered
  on, it may become a target for lateral movement.(Citation: Bleeping Computer - Ryuk WoL)(Citation: AMD Magic Packet)'
external_references:
- external_id: T1205
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1205
- description: Abrams, L. (2021, January 14). Ryuk Ransomware Uses Wake-on-Lan To Encrypt Offline Devices. Retrieved February
    11, 2021.
  source_name: Bleeping Computer - Ryuk WoL
  url: https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/
- description: AMD. (1995, November 1). Magic Packet Technical White Paper. Retrieved February 17, 2021.
  source_name: AMD Magic Packet
  url: https://www.amd.com/system/files/TechDocs/20213.pdf
- description: Bill Hau, Tony Lee, Josh Homan. (2015, September 15). SYNful Knock - A Cisco router implant - Part I. Retrieved
    November 17, 2024.
  source_name: Mandiant - Synful Knock
  url: https://cloud.google.com/blog/topics/threat-intelligence/synful-knock-acis/
- description: Graham Holmes. (2015, October 8). Evolution of attacks on Cisco IOS devices. Retrieved October 19, 2020.
  source_name: Cisco Synful Knock Evolution
  url: https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices
- description: 'Hartrell, Greg. (2002, August). Get a handle on cd00r: The invisible backdoor. Retrieved October 13, 2018.'
  source_name: Hartrell cd00r 2002
  url: https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
id: attack-pattern--451a9977-d255-43c9-b431-66de80130c8c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2026-04-15T22:44:32.591Z'
name: Traffic Signaling
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Josh Day, Gigamon
- Tony Lee
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '3.0'
```
