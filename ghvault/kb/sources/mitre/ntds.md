---
parsed_by: focuslocust
source: mitre
type: generated
---
# NTDS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1003.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [NTDS](../../attack/techniques/T1003.003-ntds.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1003.003 |
| name | NTDS |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1003/003 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:42:35.572Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal
  credential information, as well as obtain other information about domain members such as devices, users, and access rights.
  By default, the NTDS file (NTDS.dit) is located in <code>%SystemRoot%\NTDS\Ntds.dit</code> of a domain controller.(Citation:
  Wikipedia Active Directory)


  In addition to looking for NTDS files on active Domain Controllers, adversaries may search for backups that contain the
  same or similar information.(Citation: Metcalf 2015)


  The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory
  hashes.


  * Volume Shadow Copy

  * secretsdump.py

  * Using the in-built Windows tool, ntdsutil.exe

  * Invoke-NinjaCopy

  '
external_references:
- external_id: T1003.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1003/003
- description: Metcalf, S. (2015, January 19). Attackers Can Now Use Mimikatz to Implant Skeleton Key on Domain Controllers
    & BackDoor Your Active Directory Forest. Retrieved February 3, 2015.
  source_name: Metcalf 2015
  url: http://adsecurity.org/?p=1275
- description: Wikipedia. (2018, March 10). Active Directory. Retrieved April 11, 2018.
  source_name: Wikipedia Active Directory
  url: https://en.wikipedia.org/wiki/Active_Directory
id: attack-pattern--edf91964-b26e-4b4a-9600-ccacd7d7df24
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:34.852Z'
name: NTDS
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Ed Williams, Trustwave, SpiderLabs
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.3'
```
