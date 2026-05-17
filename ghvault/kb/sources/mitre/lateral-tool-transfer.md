---
parsed_by: focuslocust
source: mitre
type: generated
---
# Lateral Tool Transfer

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1570` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1570 |
| name | Lateral Tool Transfer |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1570 |

## Preserved Source Material

```yaml
created: '2020-03-11T21:01:00.959Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into
  the victim environment (i.e., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) files may then be copied
  from one system to another to stage adversary tools or other files over the course of an operation.


  Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols
  such as file sharing over [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) to connected network
  shares or with authenticated connections via [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001).(Citation:
  Unit42 LockerGoga 2019)


  Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp,
  and [ftp](https://attack.mitre.org/software/S0095). In some cases, adversaries may be able to leverage [Web Service](https://attack.mitre.org/techniques/T1102)s
  such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.(Citation:
  Dropbox Malware Sync)'
external_references:
- external_id: T1570
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1570
- description: David Talbot. (2013, August 21). Dropbox and Similar Services Can Sync Malware. Retrieved May 31, 2023.
  source_name: Dropbox Malware Sync
  url: https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/
- description: Harbison, M. (2019, March 26). Born This Way? Origins of LockerGoga. Retrieved April 16, 2019.
  source_name: Unit42 LockerGoga 2019
  url: https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/
id: attack-pattern--bf90d72c-c00b-45e3-b3aa-68560560d4c5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2025-10-24T17:49:19.137Z'
name: Lateral Tool Transfer
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Shailesh Tiwary (Indian Army)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '1.4'
```
