---
parsed_by: focuslocust
source: mitre
type: generated
---
# Disable or Modify Tools

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1685` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Disable or Modify Tools](../../attack/techniques/T1685-disable-or-modify-tools.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1685 |
| name | Disable or Modify Tools |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1685 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:53:26.949Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and\
  \ response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce\
  \ visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting\
  \ tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses\
  \ more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments.(Citation:\
  \ SCADAfence_ransomware) \n\nIn addition to directly targeting tools, adversaries may block or manipulate indicators and\
  \ telemetry used for detection. This includes maliciously disabling or redirecting sensors such as Event Tracing for Windows\
  \ (ETW), modifying event log configurations (e.g., redirecting Security logs), or interfering with logging pipelines and\
  \ forwarding mechanisms (e.g., SIEM ingestion).(Citation: Microsoft Lamin Sept 2017)(Citation: ETW Palantir)\n\nMore advanced\
  \ techniques include leveraging legitimate drivers or debugging mechanisms to render tools non-functional, bypassing anti-tampering\
  \ protections, and targeting specific defenses such as Sysmon or cloud monitoring agents. Adversaries may also disrupt broader\
  \ defensive operations, including update mechanisms, logging infrastructure (e.g., syslog), or event aggregation, further\
  \ degrading an organization’s ability to detect and respond to malicious activity.(Citation: Cocomazzi FIN7 Reboot)"
external_references:
- external_id: T1685
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1685
- description: Cocomazzi, Antonio. (2024, July 17). FIN7 Reboot | Cybercrime Gang Enhances Ops with New EDR Bypasses and Automated
    Attacks. Retrieved September 24, 2025.
  source_name: Cocomazzi FIN7 Reboot
  url: https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/
- description: Microsoft. (2009, May 17). Backdoor:Win32/Lamin.A. Retrieved September 6, 2018.
  source_name: Microsoft Lamin Sept 2017
  url: https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=Backdoor:Win32/Lamin.A
- description: 'Palantir. (2018, December 24). Tampering with Windows Event Tracing: Background, Offense, and Defense. Retrieved
    April 15, 2026.'
  source_name: ETW Palantir
  url: https://blog.palantir.com/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63
- description: Shaked, O. (2020, January 20). Anatomy of a Targeted Ransomware Attack. Retrieved June 18, 2022.
  source_name: SCADAfence_ransomware
  url: https://cdn.logic-control.com/docs/scadafence/Anatomy-Of-A-Targeted-Ransomware-Attack-WP.pdf
id: attack-pattern--bbde9781-60aa-4b8a-a911-895b0c1b3872
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:39:46.202Z'
name: Disable or Modify Tools
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Alex Soler, AttackIQ
- Cian Heasley
- Daniel Feichter, @VirtualAllocEx, Infosec Tirol
- Gal Singer, @galsinger29, Team Nautilus Aqua Security
- Gordon Long, LegioX/Zoom, asaurusrex
- Lucas Heiligenstein
- Menachem Goldstein
- Nathaniel Quist, Palo Alto Networks
- Nay Myo Hlaing (Ethan), DBS Bank
- Rob Smith
- Sarathkumar Rajendran, Microsoft Defender365
- Ziv Karliner, @ziv_kr, Team Nautilus Aqua Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.0'
```
