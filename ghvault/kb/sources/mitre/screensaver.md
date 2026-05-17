---
parsed_by: focuslocust
source: mitre
type: generated
---
# Screensaver

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1546.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Screensaver](../../attack/techniques/T1546.002-screensaver.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1546.002 |
| name | Screensaver |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1546/002 |

## Preserved Source Material

```yaml
created: '2020-01-24T13:51:01.210Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may establish persistence by executing malicious content triggered by user inactivity. Screensavers
  are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with
  a .scr file extension.(Citation: Wikipedia Screensaver) The Windows screensaver application scrnsave.scr is located in <code>C:\Windows\System32\</code>,
  and <code>C:\Windows\sysWOW64\</code>  on 64-bit Windows systems, along with screensavers included with base Windows installations.


  The following screensaver settings are stored in the Registry (<code>HKCU\Control Panel\Desktop\</code>) and could be manipulated
  to achieve persistence:


  * <code>SCRNSAVE.exe</code> - set to malicious PE path

  * <code>ScreenSaveActive</code> - set to ''1'' to enable the screensaver

  * <code>ScreenSaverIsSecure</code> - set to ''0'' to not require a password to unlock

  * <code>ScreenSaveTimeout</code> - sets user inactivity timeout before screensaver is executed


  Adversaries can use screensaver settings to maintain persistence by setting the screensaver to run malware after a certain
  timeframe of user inactivity.(Citation: ESET Gazer Aug 2017)'
external_references:
- external_id: T1546.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1546/002
- description: 'ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.'
  source_name: ESET Gazer Aug 2017
  url: https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf
- description: Wikipedia. (2017, November 22). Screensaver. Retrieved December 5, 2017.
  source_name: Wikipedia Screensaver
  url: https://en.wikipedia.org/wiki/Screensaver
id: attack-pattern--ce4b7013-640e-48a9-b501-d0025a95f4bf
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:24.634Z'
name: Screensaver
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Bartosz Jerzman
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.3'
```
