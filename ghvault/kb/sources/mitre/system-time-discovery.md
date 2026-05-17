---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Time Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1124` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Time Discovery](../../attack/techniques/T1124-system-time-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1124 |
| name | System Time Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1124 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:37.450Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may gather the system time and/or time zone settings from a local or remote system. The system
  time is set and stored by services, such as the Windows Time Service on Windows or <code>systemsetup</code> on macOS.(Citation:
  MSDN System Time)(Citation: Technet Windows Time Service)(Citation: systemsetup mac time) These time settings may also be
  synchronized between systems and services in an enterprise network, typically accomplished with a network time server within
  a domain.(Citation: Mac Time Sync)(Citation: linux system time)


  System time information may be gathered in a number of ways, such as with [Net](https://attack.mitre.org/software/S0039)
  on Windows by performing <code>net time \\hostname</code> to gather the system time on a remote system. The victim''s time
  zone may also be inferred from the current system time or gathered by using <code>w32tm /tz</code>.(Citation: Technet Windows
  Time Service) In addition, adversaries can discover device uptime through functions such as <code>GetTickCount()</code>
  to determine how long it has been since the system booted up.(Citation: Virtualization/Sandbox Evasion)


  On network devices, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `show clock detail`
  can be used to see the current time configuration.(Citation: show_clock_detail_cisco_cmd) On ESXi servers, `esxcli system
  clock get` can be used for the same purpose.


  In addition, system calls – such as <code>time()</code> – have been used to collect the current time on Linux devices.(Citation:
  MAGNET GOBLIN) On macOS systems, adversaries may use commands such as <code>systemsetup -gettimezone</code> or <code>timeIntervalSinceNow</code>
  to gather current time zone information or current date and time.(Citation: System Information Discovery Technique)(Citation:
  ESET DazzleSpy Jan 2022)


  This information could be useful for performing other techniques, such as executing a file with a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053)(Citation:
  RSA EU12 They''re Inside), or to discover locality information based on time zone to assist in victim targeting (i.e. [System
  Location Discovery](https://attack.mitre.org/techniques/T1614)). Adversaries may also use knowledge of system time as part
  of a time bomb, or delaying execution until a specified date/time.(Citation: AnyRun TimeBomb)'
external_references:
- external_id: T1124
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1124
- description: Apple Support. (n.d.). About systemsetup in Remote Desktop. Retrieved March 27, 2024.
  source_name: systemsetup mac time
  url: https://support.apple.com/en-gb/guide/remote-desktop/apd95406b8d/mac
- description: ArchLinux. (2024, February 1). System Time. Retrieved March 27, 2024.
  source_name: linux system time
  url: https://wiki.archlinux.org/title/System_time
- description: Check Point Research. (2024, March 8). MAGNET GOBLIN TARGETS PUBLICLY FACING SERVERS USING 1-DAY VULNERABILITIES.
    Retrieved March 27, 2024.
  source_name: MAGNET GOBLIN
  url: https://research.checkpoint.com/2024/magnet-goblin-targets-publicly-facing-servers-using-1-day-vulnerabilities/
- description: 'Cisco. (2023, March 6). show clock detail - Cisco IOS Security Command Reference: Commands S to Z . Retrieved
    July 13, 2022.'
  source_name: show_clock_detail_cisco_cmd
  url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s2.html#wp1896741674
- description: Cone, Matt. (2021, January 14). Synchronize your Mac's Clock with a Time Server. Retrieved March 27, 2024.
  source_name: Mac Time Sync
  url: https://www.macinstruct.com/tutorials/synchronize-your-macs-clock-with-a-time-server/
- description: M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in
    Asia. Retrieved May 6, 2022.
  source_name: ESET DazzleSpy Jan 2022
  url: https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/
- description: 'Malicious History. (2020, September 17). Time Bombs: Malware With Delayed Execution. Retrieved April 22, 2021.'
  source_name: AnyRun TimeBomb
  url: https://any.run/cybersecurity-blog/time-bombs-malware-with-delayed-execution/
- description: Mathers, B. (2016, September 30). Windows Time Service Tools and Settings. Retrieved November 25, 2016.
  source_name: Technet Windows Time Service
  url: https://technet.microsoft.com/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-time-service-tools-and-settings
- description: Microsoft. (n.d.). System Time. Retrieved November 25, 2016.
  source_name: MSDN System Time
  url: https://msdn.microsoft.com/ms724961.aspx
- description: Rivner, U., Schwartz, E. (2012). They’re Inside… Now What?. Retrieved November 25, 2016.
  source_name: RSA EU12 They're Inside
  url: https://www.rsaconference.com/writable/presentations/file_upload/ht-209_rivner_schwartz.pdf
- description: YUCEEL, Huseyin Can. Picus Labs. (2022, June 9). The System Information Discovery Technique Explained - MITRE
    ATT&CK T1082. Retrieved March 27, 2024.
  source_name: System Information Discovery Technique
  url: https://www.picussecurity.com/resource/the-system-information-discovery-technique-explained-mitre-attack-t1082
- description: YUCEEL, Huseyin Can. Picus Labs. (2022, June 9). Virtualization/Sandbox Evasion - How Attackers Avoid Malware
    Analysis. Retrieved December 26, 2023.
  source_name: Virtualization/Sandbox Evasion
  url: https://www.picussecurity.com/resource/virtualization/sandbox-evasion-how-attackers-avoid-malware-analysis
id: attack-pattern--f3c544dc-673c-4ef3-accb-53229f1ae077
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:36.399Z'
name: System Time Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- FIRST.ORG's Cyber Threat Intelligence SIG
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
x_mitre_version: '1.5'
```
