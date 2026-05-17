---
parsed_by: focuslocust
source: mitre
type: generated
---
# Socket Filters

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1205.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Socket Filters](../../attack/techniques/T1205.002-socket-filters.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1205.002 |
| name | Socket Filters |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1205/002 |

## Preserved Source Material

```yaml
created: '2022-09-30T21:18:41.930Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attach filters to a network socket to monitor then activate backdoors used for persistence or
  command and control. With elevated permissions, adversaries can use features such as the `libpcap` library to open sockets
  and install filters to allow or disallow certain types of data to come through the socket. The filter may apply to all traffic
  passing through the specified network interface (or every interface if not specified). When the network interface receives
  a packet matching the filter criteria, additional actions can be triggered on the host, such as activation of a reverse
  shell.


  To establish a connection, an adversary sends a crafted packet to the targeted host that matches the installed filter criteria.(Citation:
  haking9 libpcap network sniffing) Adversaries have used these socket filters to trigger the installation of implants, conduct
  ping backs, and to invoke command shells. Communication with these socket filters may also be used in conjunction with [Protocol
  Tunneling](https://attack.mitre.org/techniques/T1572).(Citation: exatrack bpf filters passive backdoors)(Citation: Leonardo
  Turla Penquin May 2020)


  Filters can be installed on any Unix-like platform with `libpcap` installed or on Windows hosts using `Winpcap`.  Adversaries
  may use either `libpcap` with `pcap_setfilter` or the standard library function `setsockopt` with `SO_ATTACH_FILTER` options.
  Since the socket connection is not active until the packet is received, this behavior may be difficult to detect due to
  the lack of activity on a host, low CPU overhead, and limited visibility into raw socket usage.'
external_references:
- external_id: T1205.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1205/002
- description: 'ExaTrack. (2022, May 11). Tricephalic Hellkeeper: a tale of a passive backdoor. Retrieved October 18, 2022.'
  source_name: exatrack bpf filters passive backdoors
  url: https://exatrack.com/public/Tricephalic_Hellkeeper.pdf
- description: Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.
  source_name: Leonardo Turla Penquin May 2020
  url: https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf
- description: 'Luis Martin Garcia. (2008, February 1). Hakin9 Issue 2/2008 Vol 3 No.2 VoIP Abuse: Storming SIP Security.
    Retrieved October 18, 2022.'
  source_name: haking9 libpcap network sniffing
  url: http://recursos.aldabaknocking.com/libpcapHakin9LuisMartinGarcia.pdf
id: attack-pattern--005cc321-08ce-4d17-b1ea-cb5275926520
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2026-04-15T22:45:22.463Z'
name: Socket Filters
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- CrowdStrike
- Tim (Wadhwa-)Brown
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
