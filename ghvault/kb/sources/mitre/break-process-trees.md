---
parsed_by: focuslocust
source: mitre
type: generated
---
# Break Process Trees

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1036.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Break Process Trees](../../attack/techniques/T1036.009-break-process-trees.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1036.009 |
| name | Break Process Trees |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1036/009 |

## Preserved Source Material

```yaml
created: '2023-09-27T19:49:40.815Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "An adversary may attempt to evade process tree-based analysis by modifying executed malware's parent process\
  \ ID (PPID). If endpoint protection software leverages the “parent-child\" relationship for detection, breaking this relationship\
  \ could result in the adversary’s behavior not being associated with previous process tree activity. On Unix-based systems\
  \ breaking this process tree is common practice for administrators to execute software using scripts and programs.(Citation:\
  \ 3OHA double-fork 2022) \n\nOn Linux systems, adversaries may execute a series of [Native API](https://attack.mitre.org/techniques/T1106)\
  \ calls to alter malware's process tree. For example, adversaries can execute their payload without any arguments, call\
  \ the `fork()` API call twice, then have the parent process exit. This creates a grandchild process with no parent process\
  \ that is immediately adopted by the `init` system process (PID 1), which successfully disconnects the execution of the\
  \ adversary's payload from its previous process tree.\n\nAnother example is using the “daemon” syscall to detach from the\
  \ current parent process and run in the background.(Citation: Sandfly BPFDoor 2022)(Citation: Microsoft XorDdos Linux Stealth\
  \ 2022) "
external_references:
- external_id: T1036.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1036/009
- description: Juan Tapiador. (2022, April 11). UNIX daemonization and the double fork. Retrieved September 29, 2023.
  source_name: 3OHA double-fork 2022
  url: https://0xjet.github.io/3OHA/2022/04/11/post.html
- description: 'Microsoft Threat Intelligence. (2022, May 19). Rise in XorDdos: A deeper look at the stealthy DDoS malware
    targeting Linux devices. Retrieved September 27, 2023.'
  source_name: Microsoft XorDdos Linux Stealth 2022
  url: https://www.microsoft.com/en-us/security/blog/2022/05/19/rise-in-xorddos-a-deeper-look-at-the-stealthy-ddos-malware-targeting-linux-devices/
- description: The Sandfly Security Team. (2022, May 11). BPFDoor - An Evasive Linux Backdoor Technical Analysis. Retrieved
    September 29, 2023.
  source_name: Sandfly BPFDoor 2022
  url: https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/
id: attack-pattern--34a80bc4-80f2-46e6-94ff-f3265a4b657c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:32:49.027Z'
name: Break Process Trees
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Tim (Wadhwa-)Brown
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
