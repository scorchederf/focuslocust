---
parsed_by: focuslocust
source: mitre
type: generated
---
# Services File Permissions Weakness

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574.010` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Services File Permissions Weakness](../../attack/techniques/T1574.010-services-file-permissions-weakness.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574.010 |
| name | Services File Permissions Weakness |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574/010 |

## Preserved Source Material

```yaml
created: '2020-03-12T20:43:53.998Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute their own malicious payloads by hijacking the binaries used by services. Adversaries
  may use flaws in the permissions of Windows services to replace the binary that is executed upon service start. These service
  processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the
  permissions on the file system directory containing a target binary, or permissions on the binary itself are improperly
  set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original
  process. If the original process and thread are running under a higher permissions level, then the replaced binary will
  also execute under higher-level permissions, which could include SYSTEM.


  Adversaries may use this technique to replace legitimate binaries with malicious ones as a means of executing code at a
  higher permissions level. If the executing process is set to run at a specific time or during a certain event (e.g., system
  bootup) then this technique can also be used for persistence.'
external_references:
- external_id: T1574.010
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574/010
id: attack-pattern--9e8b28c9-35fe-48ac-a14d-e6cc032dcbcd
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T23:02:37.539Z'
name: Services File Permissions Weakness
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Stefan Kanthak
- Travis Smith, Tripwire
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
