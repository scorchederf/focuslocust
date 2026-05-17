---
parsed_by: focuslocust
source: mitre
type: generated
---
# File and Directory Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1083` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1083 |
| name | File and Directory Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1083 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:04.710Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate files and directories or may search in specific locations of a host or network share
  for certain information within a file system. Adversaries may use the information from [File and Directory Discovery](https://attack.mitre.org/techniques/T1083)
  during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target
  and/or attempts specific actions.


  Many command shell utilities can be used to obtain this information. Examples include <code>dir</code>, <code>tree</code>,
  <code>ls</code>, <code>find</code>, and <code>locate</code>.(Citation: Windows Commands JPCERT) Custom tools may also be
  used to gather file and directory information and interact with the [Native API](https://attack.mitre.org/techniques/T1106).
  Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to
  gather file and directory information (e.g. <code>dir</code>, <code>show flash</code>, and/or <code>nvram</code>).(Citation:
  US-CERT-TA18-106A)


  Some files and directories may require elevated or specific user permissions to access.'
external_references:
- external_id: T1083
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1083
- description: Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.
  source_name: Windows Commands JPCERT
  url: https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
id: attack-pattern--7bc57495-ea59-4380-be31-a64af124ef18
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:00.036Z'
name: File and Directory Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
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
x_mitre_version: '1.7'
```
