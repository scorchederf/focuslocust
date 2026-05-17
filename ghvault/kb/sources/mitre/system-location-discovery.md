---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Location Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1614` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Location Discovery](../../attack/techniques/T1614-system-location-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1614 |
| name | System Location Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1614 |

## Preserved Source Material

```yaml
created: '2021-04-01T16:42:08.735Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '

  Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may
  use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery
  to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.


  Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout,
  and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer
  RAT malware 2020) Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of
  the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance''s availability zone may also be discovered
  by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft
  Azure Instance Metadata 2021)


  Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation
  IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)'
external_references:
- external_id: T1614
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1614
- description: Abrams, L. (2020, October 23). New RAT malware gets commands via Discord, has ransomware feature. Retrieved
    April 1, 2021.
  source_name: Bleepingcomputer RAT malware 2020
  url: https://www.bleepingcomputer.com/news/security/new-rat-malware-gets-commands-via-discord-has-ransomware-feature/
- description: Amazon. (n.d.). Instance identity documents. Retrieved April 2, 2021.
  source_name: AWS Instance Identity Documents
  url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html
- description: 'Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved April 1, 2021.'
  source_name: Securelist Trasparent Tribe 2020
  url: https://securelist.com/transparent-tribe-part-1/98127/
- description: FBI. (2020, November 19). Indicators of Compromise Associated with Ragnar Locker Ransomware. Retrieved September
    12, 2024.
  source_name: FBI Ragnar Locker 2020
  url: https://s3.documentcloud.org/documents/20413525/fbi-flash-indicators-of-compromise-ragnar-locker-ransomware-11192020-bc.pdf
- description: Microsoft. (2021, February 21). Azure Instance Metadata Service (Windows). Retrieved April 2, 2021.
  source_name: Microsoft Azure Instance Metadata 2021
  url: https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=windows
- description: 'Wisniewski, C. (2016, May 3). Location-based threats: How cybercriminals target you based on where you live.
    Retrieved April 1, 2021.'
  source_name: Sophos Geolocation 2016
  url: https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/
id: attack-pattern--c877e33f-1df6-40d6-b1e7-ce70f16f4979
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:22.536Z'
name: System Location Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Pooja Natarajan, NEC Corporation India
- Hiroki Nagahama, NEC Corporation
- Manikantan Srinivasan, NEC Corporation India
- Wes Hurd
- Katie Nickels, Red Canary
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Linux
- macOS
- Windows
x_mitre_version: '1.1'
```
