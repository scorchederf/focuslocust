---
parsed_by: focuslocust
source: mitre
type: generated
---
# Mark-of-the-Web Bypass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1553.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mark-of-the-Web Bypass](../../attack/techniques/T1553.005-mark-of-the-web-bypass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1553.005 |
| name | Mark-of-the-Web Bypass |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1553/005 |

## Preserved Source Material

```yaml
created: '2021-02-22T14:20:31.650Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse specific file formats to subvert Mark-of-the-Web (MOTW) controls. In Windows, when files
  are downloaded from the Internet, they are tagged with a hidden NTFS Alternate Data Stream (ADS) named <code>Zone.Identifier</code>
  with a specific value known as the MOTW.(Citation: Microsoft Zone.Identifier 2020) Files that are tagged with MOTW are protected
  and cannot perform certain actions. For example, starting in MS Office 10, if a MS Office file has the MOTW, it will open
  in Protected View. Executables tagged with the MOTW will be processed by Windows Defender SmartScreen that compares files
  with an allowlist of well-known executables. If the file is not known/trusted, SmartScreen will prevent the execution and
  warn the user not to run it.(Citation: Beek Use of VHD Dec 2020)(Citation: Outflank MotW 2020)(Citation: Intezer Russian
  APT Dec 2020)


  Adversaries may abuse container files such as compressed/archive (.arj, .gzip) and/or disk image (.iso, .vhd) file formats
  to deliver malicious payloads that may not be tagged with MOTW. Container files downloaded from the Internet will be marked
  with MOTW but the files within may not inherit the MOTW after the container files are extracted and/or mounted. MOTW is
  a NTFS feature and many container files do not support NTFS alternative data streams. After a container file is extracted
  and/or mounted, the files contained within them may be treated as local files on disk and run without protections.(Citation:
  Beek Use of VHD Dec 2020)(Citation: Outflank MotW 2020)'
external_references:
- external_id: T1553.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1553/005
- description: Beek, C. (2020, December 3). Investigating the Use of VHD Files By Cybercriminals. Retrieved November 17, 2024.
  source_name: Beek Use of VHD Dec 2020
  url: https://web.archive.org/web/20201203131725/https://christiaanbeek.medium.com/investigating-the-use-of-vhd-files-by-cybercriminals-3f1f08304316
- description: Hegt, S. (2020, March 30). Mark-of-the-Web from a red team’s perspective. Retrieved February 22, 2021.
  source_name: Outflank MotW 2020
  url: https://outflank.nl/blog/2020/03/30/mark-of-the-web-from-a-red-teams-perspective/
- description: 'Kennedy, J. (2020, December 9). A Zebra in Gopher''s Clothing: Russian APT Uses COVID-19 Lures to Deliver
    Zebrocy. Retrieved February 22, 2021.'
  source_name: Intezer Russian APT Dec 2020
  url: https://www.intezer.com/blog/research/russian-apt-uses-covid-19-lures-to-deliver-zebrocy/
- description: Microsoft. (2020, August 31). Zone.Identifier Stream Name. Retrieved February 22, 2021.
  source_name: Microsoft Zone.Identifier 2020
  url: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/6e3f7352-d11c-4d76-8c39-2516a9df36e8
id: attack-pattern--7e7c2fba-7cca-486c-9582-4c1bb2851961
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.040Z'
name: Mark-of-the-Web Bypass
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Christiaan Beek, @ChristiaanBeek
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
