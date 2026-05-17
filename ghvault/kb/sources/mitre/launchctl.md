---
parsed_by: focuslocust
source: mitre
type: generated
---
# Launchctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1569.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Launchctl](../../attack/techniques/T1569.001-launchctl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1569.001 |
| name | Launchctl |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1569/001 |

## Preserved Source Material

```yaml
created: '2020-03-10T18:26:56.187Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse launchctl to execute commands or programs. Launchctl interfaces with launchd, the service
  management framework for macOS. Launchctl supports taking subcommands on the command-line, interactively, or even redirected
  from standard input.(Citation: Launchctl Man)


  Adversaries use launchctl to execute commands and programs as [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s
  or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s. Common subcommands include: <code>launchctl load</code>,<code>launchctl
  unload</code>, and <code>launchctl start</code>. Adversaries can use scripts or manually run the commands <code>launchctl
  load -w "%s/Library/LaunchAgents/%s"</code> or <code>/bin/launchctl load</code> to execute [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s
  or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s.(Citation: Sofacy Komplex Trojan)(Citation: 20 macOS
  Common Tools and Techniques)

  '
external_references:
- external_id: T1569.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1569/001
- description: Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved
    July 8, 2017.
  source_name: Sofacy Komplex Trojan
  url: https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/
- description: Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved
    August 23, 2021.
  source_name: 20 macOS Common Tools and Techniques
  url: https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/
- description: SS64. (n.d.). launchctl. Retrieved March 28, 2020.
  source_name: Launchctl Man
  url: https://ss64.com/osx/launchctl.html
id: attack-pattern--810aa4ad-61c9-49cb-993f-daa06199421d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:49:02.098Z'
name: Launchctl
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
x_mitre_version: '1.3'
```
