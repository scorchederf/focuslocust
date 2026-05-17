---
parsed_by: focuslocust
source: mitre
type: generated
---
# TCC Manipulation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1548.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [TCC Manipulation](../../attack/techniques/T1548.006-tcc-manipulation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1548.006 |
| name | TCC Manipulation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1548/006 |

## Preserved Source Material

```yaml
created: '2024-03-21T21:10:57.322Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries can manipulate or abuse the Transparency, Consent, & Control (TCC) service or database to grant
  malicious executables elevated permissions. TCC is a Privacy & Security macOS control mechanism used to determine if the
  running process has permission to access the data or services protected by TCC, such as screen sharing, camera, microphone,
  or Full Disk Access (FDA).


  When an application requests to access data or a service protected by TCC, the TCC daemon (`tccd`) checks the TCC database,
  located at `/Library/Application Support/com.apple.TCC/TCC.db` (and `~/` equivalent), and an overwrites file (if connected
  to an MDM) for existing permissions. If permissions do not exist, then the user is prompted to grant permission. Once permissions
  are granted, the database stores the application''s permissions and will not prompt the user again unless reset. For example,
  when a web browser requests permissions to the user''s webcam, once granted the web browser may not explicitly prompt the
  user again.(Citation: welivesecurity TCC)


  Adversaries may access restricted data or services protected by TCC through abusing applications previously granted permissions
  through [Process Injection](https://attack.mitre.org/techniques/T1055) or executing a malicious binary using another application.
  For example, adversaries can use Finder, a macOS native app with FDA permissions, to execute a malicious [AppleScript](https://attack.mitre.org/techniques/T1059/002).
  When executing under the Finder App, the malicious [AppleScript](https://attack.mitre.org/techniques/T1059/002) inherits
  access to all files on the system without requiring a user prompt. When System Integrity Protection (SIP) is disabled, TCC
  protections are also disabled. For a system without SIP enabled, adversaries can manipulate the TCC database to add permissions
  to their malicious executable through loading an adversary controlled TCC database using environment variables and [Launchctl](https://attack.mitre.org/techniques/T1569/001).(Citation:
  TCC macOS bypass)(Citation: TCC Database)


  '
external_references:
- external_id: T1548.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1548/006
- description: 'Marc-Etienne M.Léveillé. (2022, July 19). I see what you did there: A look at the CloudMensis macOS spyware.
    Retrieved March 21, 2024.'
  source_name: welivesecurity TCC
  url: https://www.welivesecurity.com/2022/07/19/i-see-what-you-did-there-look-cloudmensis-macos-spyware/
- description: 'Marina Liang. (2024, April 23). Return of the mac(OS): Transparency, Consent, and Control (TCC) Database Manipulation.
    Retrieved March 28, 2024.'
  source_name: TCC Database
  url: https://web.archive.org/web/20240411112413/https://interpressecurity.com/resources/return-of-the-macos-tcc/
- description: Phil Stokes. (2021, July 1). Bypassing macOS TCC User Privacy Protections By Accident and Design. Retrieved
    March 21, 2024.
  source_name: TCC macOS bypass
  url: https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/
id: attack-pattern--e8a0a025-3601-4755-abfb-8d08283329fb
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:52:55.058Z'
name: TCC Manipulation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Marina Liang
- Wojciech Reguła @_r3ggi
- Csaba Fitzl @theevilbit of Kandji
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
x_mitre_version: '2.0'
```
