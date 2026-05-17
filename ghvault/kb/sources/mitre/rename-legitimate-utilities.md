---
parsed_by: focuslocust
source: mitre
type: generated
---
# Rename Legitimate Utilities

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1036.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Rename Legitimate Utilities](../../attack/techniques/T1036.003-rename-legitimate-utilities.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1036.003 |
| name | Rename Legitimate Utilities |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1036/003 |

## Preserved Source Material

```yaml
created: '2020-02-10T20:03:11.691Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may rename legitimate / system utilities to try to evade security mechanisms concerning the usage
  of those utilities. Security monitoring and control mechanisms may be in place for legitimate utilities adversaries are
  capable of abusing, including both built-in binaries and tools such as PSExec, AutoHotKey, and IronPython.(Citation: LOLBAS
  Main Site)(Citation: Huntress Python Malware 2025)(Citation: The DFIR Report AutoHotKey 2023)(Citation: Splunk Detect Renamed
  PSExec) It may be possible to bypass those security mechanisms by renaming the utility prior to utilization (ex: rename
  <code>rundll32.exe</code>).(Citation: Elastic Masquerade Ball) An alternative case occurs when a legitimate utility is copied
  or moved to a different directory and renamed to avoid detections based on these utilities executing from non-standard paths.(Citation:
  F-Secure CozyDuke)'
external_references:
- external_id: T1036.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1036/003
- description: 'Ewing, P. (2016, October 31). How to Hunt: The Masquerade Ball. Retrieved October 31, 2016.'
  source_name: Elastic Masquerade Ball
  url: https://www.elastic.co/blog/how-hunt-masquerade-ball
- description: 'F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis. Retrieved December 10, 2015.'
  source_name: F-Secure CozyDuke
  url: https://www.f-secure.com/documents/996508/1030745/CozyDuke
- description: LOLBAS. (n.d.). Living Off The Land Binaries and Scripts (and also Libraries). Retrieved February 10, 2020.
  source_name: LOLBAS Main Site
  url: https://lolbas-project.github.io/
- description: 'Matthew Brennan. (2024, July 5). Snakes on a Domain: An Analysis of a Python Malware Loader. Retrieved April
    3, 2025.'
  source_name: Huntress Python Malware 2025
  url: https://www.huntress.com/blog/snakes-on-a-domain-an-analysis-of-a-python-malware-loader
- description: 'Splunk. (2025, February 24). Detection: Detect Renamed PSExec. Retrieved April 3, 2025.'
  source_name: Splunk Detect Renamed PSExec
  url: https://research.splunk.com/endpoint/683e6196-b8e8-11eb-9a79-acde48001122/
- description: The DFIR Report. (2023, February 6). Collect, Exfiltrate, Sleep, Repeat. Retrieved April 3, 2025.
  source_name: The DFIR Report AutoHotKey 2023
  url: https://thedfirreport.com/2023/02/06/collect-exfiltrate-sleep-repeat/
id: attack-pattern--bd5b58a4-a52d-4a29-bc0d-3f1d3968eb6b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:40:54.471Z'
name: Rename Legitimate Utilities
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Matt Anderson, @‌nosecurething, Huntress
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '3.0'
```
