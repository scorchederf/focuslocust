---
parsed_by: focuslocust
source: mitre
type: generated
---
# Scheduled Task／Job

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1053` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Scheduled Task／Job](../../attack/techniques/T1053-scheduled-task-job.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1053 |
| name | Scheduled Task／Job |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1053 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:46.977Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious
  code. Utilities exist within all major operating systems to schedule programs or scripts to be executed at a specified date
  and time. A task can also be scheduled on a remote system, provided the proper authentication is met (ex: RPC and file and
  printer sharing in Windows environments). Scheduling a task on a remote system typically may require being a member of an
  admin or otherwise privileged group on the remote system.(Citation: TechNet Task Scheduler Security)


  Adversaries may use task scheduling to execute programs at system startup or on a scheduled basis for persistence. These
  mechanisms can also be abused to run a process under the context of a specified account (such as one with elevated permissions/privileges).
  Similar to [System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218), adversaries have also abused task
  scheduling to potentially mask one-time execution under a trusted system process.(Citation: ProofPoint Serpent)'
external_references:
- external_id: T1053
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1053
- description: Campbell, B. et al. (2022, March 21). Serpent, No Swiping! New Backdoor Targets French Entities with Unique
    Attack Chain. Retrieved April 11, 2022.
  source_name: ProofPoint Serpent
  url: https://www.proofpoint.com/us/blog/threat-insight/serpent-no-swiping-new-backdoor-targets-french-entities-unique-attack-chain
- description: Microsoft. (2005, January 21). Task Scheduler and security. Retrieved June 8, 2016.
  source_name: TechNet Task Scheduler Security
  url: https://technet.microsoft.com/en-us/library/cc785125.aspx
id: attack-pattern--35dd844a-b219-4e2b-a6bb-efa9a75995a9
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-06T13:58:22.807Z'
name: Scheduled Task/Job
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Prashant Verma, Paladion
- Leo Loobeek, @leoloobeek
- Travis Smith, Tripwire
- Alain Homewood, Insomnia Security
- Andrew Northern, @ex_raritas
- Bryan Campbell, @bry_campbell
- Zachary Abzug, @ZackDoesML
- Selena Larson, @selenalarson
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.5'
```
