---
parsed_by: focuslocust
source: mitre
type: generated
---
# Bootkit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1542.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bootkit](../../attack/techniques/T1542.003-bootkit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1542.003 |
| name | Bootkit |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1542/003 |

## Preserved Source Material

```yaml
created: '2019-12-19T21:05:38.123Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use bootkits to persist on systems. A bootkit is a malware variant that modifies the boot sectors
  of a hard drive, allowing malicious code to execute before a computer''s operating system has loaded. Bootkits reside at
  a layer below the operating system and may make it difficult to perform full remediation unless an organization suspects
  one was used and can act accordingly.


  In BIOS systems, a bootkit may modify the Master Boot Record (MBR) and/or Volume Boot Record (VBR).(Citation: Mandiant M
  Trends 2016) The MBR is the section of disk that is first loaded after completing hardware initialization by the BIOS. It
  is the location of the boot loader. An adversary who has raw access to the boot drive may overwrite this area, diverting
  execution during startup from the normal boot loader to adversary code.(Citation: Lau 2011)


  The MBR passes control of the boot process to the VBR. Similar to the case of MBR, an adversary who has raw access to the
  boot drive may overwrite the VBR to divert execution during startup to adversary code.


  In UEFI (Unified Extensible Firmware Interface) systems, a bootkit may instead create or modify files in the EFI system
  partition (ESP). The ESP is a partition on data storage used by devices containing UEFI that allows the system to boot the
  OS and other utilities used by the system. An adversary can use the newly created or patched files in the ESP to run malicious
  kernel code.(Citation: Microsoft Security)(Citation: welivesecurity)'
external_references:
- external_id: T1542.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1542/003
- description: Lau, H. (2011, August 8). Are MBR Infections Back in Fashion? (Infographic). Retrieved November 13, 2014.
  source_name: Lau 2011
  url: http://www.symantec.com/connect/blogs/are-mbr-infections-back-fashion
- description: Mandiant. (2016, February 25). Mandiant M-Trends 2016. Retrieved November 17, 2024.
  source_name: Mandiant M Trends 2016
  url: https://web.archive.org/web/20211024160454/https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/rpt-mtrends-2016.pdf
- description: 'Martin Smolár. (2023, March 1). BlackLotus UEFI bootkit: Myth confirmed. Retrieved February 11, 2025.'
  source_name: welivesecurity
  url: https://www.welivesecurity.com/2023/03/01/blacklotus-uefi-bootkit-myth-confirmed/
- description: 'Microsoft Incident Response. (2023, April 11). Guidance for investigating attacks using CVE-2022-21894: The
    BlackLotus campaign. Retrieved February 12, 2025.'
  source_name: Microsoft Security
  url: https://www.microsoft.com/en-us/security/blog/2023/04/11/guidance-for-investigating-attacks-using-cve-2022-21894-the-blacklotus-campaign/
id: attack-pattern--1b7b1806-7746-41a1-a35d-e48dae25ddba
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2026-04-17T18:38:49.558Z'
name: Bootkit
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
- Windows
x_mitre_version: '2.0'
```
