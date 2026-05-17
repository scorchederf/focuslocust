---
parsed_by: focuslocust
source: mitre
type: generated
---
# Unix Shell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Unix Shell](../../attack/techniques/T1059.004-unix-shell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1059.004 |
| name | Unix Shell |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1059/004 |

## Preserved Source Material

```yaml
created: '2020-03-09T14:15:05.330Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Unix shell commands and scripts for execution. Unix shells are the primary command prompt
  on Linux, macOS, and ESXi systems, though many variations of the Unix shell exist (e.g. sh, ash, bash, zsh, etc.) depending
  on the specific OS or distribution.(Citation: DieNet Bash)(Citation: Apple ZShell) Unix shells can control every aspect
  of a system, with certain commands requiring elevated privileges.


  Unix shells also support scripts that enable sequential execution of commands as well as other typical programming operations
  such as conditionals and loops. Common uses of shell scripts include long or repetitive tasks, or the need to run the same
  set of commands on multiple systems.


  Adversaries may abuse Unix shells to execute various commands or payloads. Interactive shells may be accessed through command
  and control channels or during lateral movement such as with [SSH](https://attack.mitre.org/techniques/T1021/004). Adversaries
  may also leverage shell scripts to deliver and execute multiple commands on victims or as part of payloads used for persistence.


  Some systems, such as embedded devices, lightweight Linux distributions, and ESXi servers, may leverage stripped-down Unix
  shells via Busybox, a small executable that contains a variety of tools, including a simple shell.'
external_references:
- external_id: T1059.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1059/004
- description: Apple. (2020, January 28). Use zsh as the default shell on your Mac. Retrieved June 12, 2020.
  source_name: Apple ZShell
  url: https://support.apple.com/HT208050
- description: die.net. (n.d.). bash(1) - Linux man page. Retrieved June 12, 2020.
  source_name: DieNet Bash
  url: https://linux.die.net/man/1/bash
id: attack-pattern--a9d4b653-6915-42af-98b2-5758c4ceee56
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:49:12.476Z'
name: Unix Shell
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
- ESXi
- Linux
- macOS
- Network Devices
x_mitre_remote_support: false
x_mitre_version: '1.4'
```
