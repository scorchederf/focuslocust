---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Devices

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1584.008` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Devices](../../attack/techniques/T1584.008-network-devices.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1584.008 |
| name | Network Devices |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1584/008 |

## Preserved Source Material

```yaml
created: '2024-03-28T03:29:35.616Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may compromise third-party network devices that can be used during targeting. Network devices, such
  as small office/home office (SOHO) routers, may be compromised where the adversary''s ultimate goal is not [Initial Access](https://attack.mitre.org/tactics/TA0001)
  to that environment, but rather to leverage these devices to support additional targeting.


  Once an adversary has control, compromised network devices can be used to launch additional operations, such as hosting
  payloads for [Phishing](https://attack.mitre.org/techniques/T1566) campaigns (i.e., [Link Target](https://attack.mitre.org/techniques/T1608/005))
  or enabling the required access to execute [Content Injection](https://attack.mitre.org/techniques/T1659) operations. Adversaries
  may also be able to harvest reusable credentials (i.e., [Valid Accounts](https://attack.mitre.org/techniques/T1078)) from
  compromised network devices.


  Adversaries often target Internet-facing edge devices and related network appliances that specifically do not support robust
  host-based defenses.(Citation: Mandiant Fortinet Zero Day)(Citation: Wired Russia Cyberwar)


  Compromised network devices may be used to support subsequent [Command and Control](https://attack.mitre.org/tactics/TA0011)
  activity, such as [Hide Infrastructure](https://attack.mitre.org/techniques/T1665) through an established [Proxy](https://attack.mitre.org/techniques/T1090)
  and/or [Botnet](https://attack.mitre.org/techniques/T1584/005) network.(Citation: Justice GRU 2024)'
external_references:
- external_id: T1584.008
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1584/008
- description: Greenberg, A. (2022, November 10). Russia’s New Cyberwarfare in Ukraine Is Fast, Dirty, and Relentless. Retrieved
    March 22, 2023.
  source_name: Wired Russia Cyberwar
  url: https://www.wired.com/story/russia-ukraine-cyberattacks-mandiant/
- description: Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in
    Espionage Operation. Retrieved March 22, 2023.
  source_name: Mandiant Fortinet Zero Day
  url: https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem
- description: Office of Public Affairs. (2024, February 15). Justice Department Conducts Court-Authorized Disruption of Botnet
    Controlled by the Russian Federation’s Main Intelligence Directorate of the General Staff (GRU). Retrieved March 28, 2024.
  source_name: Justice GRU 2024
  url: https://www.justice.gov/opa/pr/justice-department-conducts-court-authorized-disruption-botnet-controlled-russian
id: attack-pattern--149b477f-f364-4824-b1b5-aa1d56115869
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-22T03:56:34.319Z'
name: Network Devices
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Gavin Knapp
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.1'
```
