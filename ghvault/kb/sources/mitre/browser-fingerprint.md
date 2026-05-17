---
parsed_by: focuslocust
source: mitre
type: generated
---
# Browser Fingerprint

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1036.012` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Browser Fingerprint](../../attack/techniques/T1036.012-browser-fingerprint.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1036.012 |
| name | Browser Fingerprint |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1036/012 |

## Preserved Source Material

```yaml
created: '2025-09-22T20:13:45.616Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to blend in with legitimate traffic by spoofing browser and system attributes like operating
  system, system language, platform, user-agent string, resolution, time zone, etc.  The HTTP User-Agent request header is
  a string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user
  agent.(Citation: Mozilla User Agent)


  Adversaries may gather this information through [System Information Discovery](https://attack.mitre.org/techniques/T1082)
  or by users navigating to adversary-controlled websites, and then use that information to craft their web traffic to evade
  defenses.(Citation: Gummy Browsers Targeted Browser Spoofing against State-of-the-Art Fingerprinting Techniques)'
external_references:
- external_id: T1036.012
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1036/012
- description: MDN contributors. (2025, July 4). User-Agent header. Retrieved October 19, 2025.
  source_name: Mozilla User Agent
  url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent
- description: Zengrui Liu, Prakash Shrestha, and Nitesh Saxena. (2021, October 19). Retrieved April 15, 2026.
  source_name: Gummy Browsers Targeted Browser Spoofing against State-of-the-Art Fingerprinting Techniques
  url: https://arxiv.org/pdf/2110.10129
id: attack-pattern--afac5dbc-4383-4fb6-9ba6-45b25d49e530
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:37:12.322Z'
name: Browser Fingerprint
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
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
