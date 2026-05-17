---
parsed_by: focuslocust
source: mitre
type: generated
---
# Linux and Mac Permissions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1222.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Linux and Mac Permissions](../../attack/techniques/T1222.002-linux-and-mac-permissions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1222.002 |
| name | Linux and Mac Permissions |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1222/002 |

## Preserved Source Material

```yaml
created: '2020-02-04T19:24:27.774Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access
  protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory
  permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions.
  File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform
  which actions (read, write, execute, etc.).


  Most Linux and Linux-based platforms provide a standard set of permission groups (user, group, and other) and a standard
  set of permissions (read, write, and execute) that are applied to each group. While nuances of each platform’s permissions
  implementation may vary, most of the platforms provide two primary commands used to manipulate file and directory ACLs:
  <code>chown</code> (short for change owner), and <code>chmod</code> (short for change mode).


  Adversarial may use these commands to make themselves the owner of files and directories or change the mode if current permissions
  allow it. They could subsequently lock others out of the file. Specific file and directory modifications may be a required
  step for many techniques, such as establishing Persistence via [Unix Shell Configuration Modification](https://attack.mitre.org/techniques/T1546/004)
  or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).(Citation:
  20 macOS Common Tools and Techniques) '
external_references:
- external_id: T1222.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1222/002
- description: Hybrid Analysis. (2018, June 12). c9b65b764985dfd7a11d3faf599c56b8.exe. Retrieved August 19, 2018.
  source_name: Hybrid Analysis Icacls1 June 2018
  url: https://www.hybrid-analysis.com/sample/ef0d2628823e8e0a0de3b08b8eacaf41cf284c086a948bdfd67f4e4373c14e4d?environmentId=100
- description: Hybrid Analysis. (2018, May 30). 2a8efbfadd798f6111340f7c1c956bee.dll. Retrieved August 19, 2018.
  source_name: Hybrid Analysis Icacls2 May 2018
  url: https://www.hybrid-analysis.com/sample/22dab012c3e20e3d9291bce14a2bfc448036d3b966c6e78167f4626f5f9e38d6?environmentId=110
- description: Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved
    August 23, 2021.
  source_name: 20 macOS Common Tools and Techniques
  url: https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/
id: attack-pattern--09b130a2-a77e-4af0-a361-f46f9aad1345
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:51:53.173Z'
name: Linux and Mac Permissions
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
x_mitre_version: '2.0'
```
