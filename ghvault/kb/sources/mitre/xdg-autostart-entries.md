---
parsed_by: focuslocust
source: mitre
type: generated
---
# XDG Autostart Entries

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.013` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [XDG Autostart Entries](../../attack/techniques/T1547.013-xdg-autostart-entries.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.013 |
| name | XDG Autostart Entries |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/013 |

## Preserved Source Material

```yaml
created: '2019-09-10T18:13:12.195Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may add or modify XDG Autostart Entries to execute malicious programs or commands when a user’s
  desktop environment is loaded at login. XDG Autostart entries are available for any XDG-compliant Linux system. XDG Autostart
  entries use Desktop Entry files (`.desktop`) to configure the user’s desktop environment upon user login. These configuration
  files determine what applications launch upon user login, define associated applications to open specific file types, and
  define applications used to open removable media.(Citation: Free Desktop Application Autostart Feb 2006)(Citation: Free
  Desktop Entry Keys)


  Adversaries may abuse this feature to establish persistence by adding a path to a malicious binary or command to the `Exec`
  directive in the `.desktop` configuration file. When the user’s desktop environment is loaded at user login, the `.desktop`
  files located in the XDG Autostart directories are automatically executed. System-wide Autostart entries are located in
  the `/etc/xdg/autostart` directory while the user entries are located in the `~/.config/autostart` directory.


  Adversaries may combine this technique with [Masquerading](https://attack.mitre.org/techniques/T1036) to blend malicious
  Autostart entries with legitimate programs.(Citation: Red Canary Netwire Linux 2022)'
external_references:
- external_id: T1547.013
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/013
- description: Free Desktop. (2006, February 13). Desktop Application Autostart Specification. Retrieved September 12, 2019.
  source_name: Free Desktop Application Autostart Feb 2006
  url: https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html
- description: Free Desktop. (2017, December 24). Recognized Desktop Entry Keys. Retrieved November 17, 2024.
  source_name: Free Desktop Entry Keys
  url: https://specifications.freedesktop.org/desktop-entry-spec/latest/recognized-keys.html
- description: TONY LAMBERT. (2022, June 7). Trapping the Netwire RAT on Linux. Retrieved September 28, 2023.
  source_name: Red Canary Netwire Linux 2022
  url: https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/
id: attack-pattern--e0232cb0-ded5-4c2e-9dc7-2893142a5c11
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:30.252Z'
name: XDG Autostart Entries
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Tony Lambert, Red Canary
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
x_mitre_version: '1.2'
```
