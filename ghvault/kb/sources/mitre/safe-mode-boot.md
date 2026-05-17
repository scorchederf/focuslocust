---
parsed_by: focuslocust
source: mitre
type: generated
---
# Safe Mode Boot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1688` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Safe Mode Boot](../../attack/techniques/T1688-safe-mode-boot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1688 |
| name | Safe Mode Boot |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1688 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:53:27.979Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Windows safe mode to disable endpoint defenses. Safe mode starts up the Windows operating
  system with a limited set of drivers and services. Third-party security software such as endpoint detection and response
  (EDR) tools may not start after booting Windows in safe mode. There are two versions of safe mode: Safe Mode and Safe Mode
  with Networking. It is possible to start additional services after a safe mode boot.(Citation: Microsoft Windows Startup
  Settings)(Citation: Sophos Safe Mode Boot)


  Adversaries may abuse safe mode to disable endpoint defenses that may not start with a limited boot. Hosts can be forced
  into safe mode after the next reboot via modifications to Boot Configuration Data (BCD) stores, which are files that manage
  boot application settings.(Citation: Microsoft bcdedit)


  Adversaries may also add their malicious applications to the list of minimal services that start in safe mode by modifying
  relevant Registry values (i.e. [Modify Registry](https://attack.mitre.org/techniques/T1112)). Malicious [Component Object
  Model](https://attack.mitre.org/techniques/T1559/001) (COM) objects may also be registered and loaded in safe mode.(Citation:
  CyberArk Labs Safe Mode 2016)(Citation: Cybereason safe mode boot)(Citation: BleepingComputer REvil 2021)'
external_references:
- external_id: T1688
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1688
- description: Abrams, L. (2021, March 19). REvil ransomware has a new ‘Windows Safe Mode’ encryption mode. Retrieved June
    23, 2021.
  source_name: BleepingComputer REvil 2021
  url: https://www.bleepingcomputer.com/news/security/revil-ransomware-has-a-new-windows-safe-mode-encryption-mode/
- description: Andrew Brandt. (2019, December 9). Snatch ransomware reboots PCs into Safe Mode to bypass protection. Retrieved
    April 15, 2026.
  source_name: Sophos Safe Mode Boot
  url: https://www.sophos.com/en-us/blog/snatch-ransomware-reboots-pcs-into-safe-mode-to-bypass-protection
- description: Cybereason Nocturnus. (n.d.). Cybereason vs. MedusaLocker Ransomware. Retrieved April 15, 2026.
  source_name: Cybereason safe mode boot
  url: https://www.cybereason.com/blog/research/medusalocker-ransomware
- description: Microsoft. (n.d.). Retrieved April 15, 2026.
  source_name: Microsoft Windows Startup Settings
  url: https://support.microsoft.com/en-us/windows/windows-startup-settings-1af6ec8c-4d4a-4b23-adb7-e76eef0b847f
- description: Microsoft. (n.d.). Retrieved April 15, 2026.
  source_name: Microsoft bcdedit
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit
- description: 'Naim, D.. (2016, September 15). CyberArk Labs: From Safe Mode to Domain Compromise. Retrieved June 23, 2021.'
  source_name: CyberArk Labs Safe Mode 2016
  url: https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise
id: attack-pattern--c7660f19-f8c5-4ae3-a5e5-24381c270376
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:48:52.409Z'
name: Safe Mode Boot
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Jorell Magtibay, National Australia Bank Limited
- Kiyohito Yamamoto, RedLark, NTT Communications
- Yusuke Kubo, RedLark, NTT Communications
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.0'
```
