---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Share Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1135` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Share Discovery](../../attack/techniques/T1135-network-share-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1135 |
| name | Network Share Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1135 |

## Preserved Source Material

```yaml
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information\
  \ to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often\
  \ contain shared network drives and folders that enable users to access file directories on various systems across a network.\
  \ \n\nFile sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation:\
  \ TechNet Shared Folder) [Net](https://attack.mitre.org/software/S0039) can be used to query a remote system for available\
  \ shared drives using the <code>net view \\\\\\\\remotesystem</code> command. It can also be used to query shared drives\
  \ on the local system using <code>net share</code>. For macOS, the <code>sharing -l</code> command lists all shared points\
  \ used for smb services."
external_references:
- external_id: T1135
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1135
- description: Microsoft. (n.d.). Share a Folder or Drive. Retrieved June 30, 2017.
  source_name: TechNet Shared Folder
  url: https://technet.microsoft.com/library/cc770880.aspx
- description: Wikipedia. (2017, April 15). Shared resource. Retrieved June 30, 2017.
  source_name: Wikipedia Shared Resource
  url: https://en.wikipedia.org/wiki/Shared_resource
id: attack-pattern--3489cfc5-640f-4bb3-a103-9137b97de79f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:37.475Z'
name: Network Share Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '3.2'
```
