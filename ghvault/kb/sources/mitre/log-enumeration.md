---
parsed_by: focuslocust
source: mitre
type: generated
---
# Log Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1654` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Log Enumeration](../../attack/techniques/T1654-log-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1654 |
| name | Log Enumeration |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1654 |

## Preserved Source Material

```yaml
created: '2023-07-10T16:50:57.587Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types
  of valuable insights for an adversary, such as user authentication records ([Account Discovery](https://attack.mitre.org/techniques/T1087)),
  security or vulnerable software ([Software Discovery](https://attack.mitre.org/techniques/T1518)), or hosts within a compromised
  network ([Remote System Discovery](https://attack.mitre.org/techniques/T1018)).


  Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or [PowerShell](https://attack.mitre.org/techniques/T1059/001)
  on Windows to access and/or export security event information.(Citation: WithSecure Lazarus-NoPineapple Threat Intel Report
  2023)(Citation: Cadet Blizzard emerges as novel threat actor) In cloud environments, adversaries may leverage utilities
  such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure.(Citation:
  SIM Swapping and Abuse of the Microsoft Azure Serial Console)


  Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to
  adversary-controlled infrastructure for offline analysis.


  In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track
  incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.(Citation:
  Permiso GUI-Vil 2023)'
external_references:
- external_id: T1654
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1654
- description: 'Ian Ahl. (2023, May 22). Unmasking GUI-Vil: Financially Motivated Cloud Threat Actor. Retrieved August 30,
    2024.'
  source_name: Permiso GUI-Vil 2023
  url: https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor/
- description: 'Mandiant Intelligence. (2023, May 16). SIM Swapping and Abuse of the Microsoft Azure Serial Console: Serial
    Is Part of a Well Balanced Attack. Retrieved June 2, 2023.'
  source_name: SIM Swapping and Abuse of the Microsoft Azure Serial Console
  url: https://www.mandiant.com/resources/blog/sim-swapping-abuse-azure-serial
- description: Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat
    actor. Retrieved July 10, 2023.
  source_name: Cadet Blizzard emerges as novel threat actor
  url: https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/
- description: Ruohonen, S. & Robinson, S. (2023, February 2). No Pineapple! -DPRK Targeting of Medical Research and Technology
    Sector. Retrieved July 10, 2023.
  source_name: WithSecure Lazarus-NoPineapple Threat Intel Report 2023
  url: https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf
id: attack-pattern--866d0d6d-02c6-42bd-aa2f-02907fdc0969
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-04-15T19:58:48.705Z'
name: Log Enumeration
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Bilal Bahadır Yenici
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- IaaS
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
