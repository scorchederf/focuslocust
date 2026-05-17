---
parsed_by: focuslocust
source: mitre
type: generated
---
# Mutual Exclusion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1480.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mutual Exclusion](../../attack/techniques/T1480.002-mutual-exclusion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1480.002 |
| name | Mutual Exclusion |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1480/002 |

## Preserved Source Material

```yaml
created: '2024-09-19T14:00:03.401Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may constrain execution or actions based on the presence of a mutex associated with malware. A mutex
  is a locking mechanism used to synchronize access to a resource. Only one thread or process can acquire a mutex at a given
  time.(Citation: Microsoft Mutexes)


  While local mutexes only exist within a given process, allowing multiple threads to synchronize access to a resource, system
  mutexes can be used to synchronize the activities of multiple processes.(Citation: Microsoft Mutexes) By creating a unique
  system mutex associated with a particular malware, adversaries can verify whether or not a system has already been compromised.(Citation:
  Sans Mutexes 2012)


  In Linux environments, malware may instead attempt to acquire a lock on a mutex file. If the malware is able to acquire
  the lock, it continues to execute; if it fails, it exits to avoid creating a second instance of itself.(Citation: Intezer
  RedXOR 2021)(Citation: Deep Instinct BPFDoor 2023)


  Mutex names may be hard-coded or dynamically generated using a predictable algorithm.(Citation: ICS Mutexes 2015)'
external_references:
- external_id: T1480.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1480/002
- description: Joakim Kennedy and Avigayil Mechtinger. (2021, March 10). New Linux Backdoor RedXOR Likely Operated by Chinese
    Nation-State Actor. Retrieved September 19, 2024.
  source_name: Intezer RedXOR 2021
  url: https://intezer.com/blog/malware-analysis/new-linux-backdoor-redxor-likely-operated-by-chinese-nation-state-actor/
- description: Lenny Zeltser. (2012, July 24). Looking at Mutex Objects for Malware Discovery & Indicators of Compromise.
    Retrieved September 19, 2024.
  source_name: Sans Mutexes 2012
  url: https://www.sans.org/blog/looking-at-mutex-objects-for-malware-discovery-indicators-of-compromise/
- description: Lenny Zeltser. (2015, March 9). How Malware Generates Mutex Names to Evade Detection. Retrieved September 19,
    2024.
  source_name: ICS Mutexes 2015
  url: https://isc.sans.edu/diary/How+Malware+Generates+Mutex+Names+to+Evade+Detection/19429/
- description: Microsoft. (2022, March 11). Mutexes. Retrieved September 19, 2024.
  source_name: Microsoft Mutexes
  url: https://learn.microsoft.com/en-us/dotnet/standard/threading/mutexes
- description: Shaul Vilkomir-Preisman and Eliran Nissan. (2023, May 10). BPFDoor Malware Evolves – Stealthy Sniffing Backdoor
    Ups Its Game. Retrieved September 19, 2024.
  source_name: Deep Instinct BPFDoor 2023
  url: https://www.deepinstinct.com/blog/bpfdoor-malware-evolves-stealthy-sniffing-backdoor-ups-its-game
id: attack-pattern--49fca0d2-685d-41eb-8bd4-05451cc3a742
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:07:21.724Z'
name: Mutual Exclusion
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Manikantan Srinivasan, NEC Corporation India
- Pooja Natarajan, NEC Corporation India
- Nagahama Hiroki – NEC Corporation Japan
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
