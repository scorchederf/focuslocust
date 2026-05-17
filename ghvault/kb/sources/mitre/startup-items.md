---
parsed_by: focuslocust
source: mitre
type: generated
---
# Startup Items

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1037.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Startup Items](../../attack/techniques/T1037.005-startup-items.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1037.005 |
| name | Startup Items |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1037/005 |

## Preserved Source Material

```yaml
created: '2020-01-15T18:00:33.603Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use startup items automatically executed at boot initialization to establish persistence. Startup\
  \ items execute during the final phase of the boot process and contain shell scripts or other executable files along with\
  \ configuration information used by the system to determine the execution order for all startup items.(Citation: Startup\
  \ Items)\n\nThis is technically a deprecated technology (superseded by [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)),\
  \ and thus the appropriate folder, <code>/Library/StartupItems</code> isn’t guaranteed to exist on the system by default,\
  \ but does appear to exist by default on macOS Sierra. A startup item is a directory whose executable and configuration\
  \ property list (plist), <code>StartupParameters.plist</code>, reside in the top-level directory. \n\nAn adversary can create\
  \ the appropriate folders/files in the StartupItems directory to register their own persistence mechanism.(Citation: Methods\
  \ of Mac Malware Persistence) Additionally, since StartupItems run during the bootup phase of macOS, they will run as the\
  \ elevated root user."
external_references:
- external_id: T1037.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1037/005
- description: Apple. (2016, September 13). Startup Items. Retrieved July 11, 2017.
  source_name: Startup Items
  url: https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html
- description: Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.
  source_name: Methods of Mac Malware Persistence
  url: https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf
id: attack-pattern--c0dfe7b0-b873-4618-9ff8-53e31f70907f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:19.678Z'
name: Startup Items
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
x_mitre_version: '1.1'
```
