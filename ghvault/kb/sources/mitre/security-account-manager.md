---
parsed_by: focuslocust
source: mitre
type: generated
---
# Security Account Manager

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1003.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1003.002 |
| name | Security Account Manager |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1003/002 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:42:07.281Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either\
  \ through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file\
  \ that contains local accounts for the host, typically those found with the <code>net user</code> command. Enumerating the\
  \ SAM database requires SYSTEM level access.\n\nA number of tools can be used to retrieve the SAM file through in-memory\
  \ techniques:\n\n* pwdumpx.exe\n* [gsecdump](https://attack.mitre.org/software/S0008)\n* [Mimikatz](https://attack.mitre.org/software/S0002)\n\
  * secretsdump.py\n\nAlternatively, the SAM can be extracted from the Registry with Reg:\n\n* <code>reg save HKLM\\sam sam</code>\n\
  * <code>reg save HKLM\\system system</code>\n\nCreddump7 can then be used to process the SAM database locally to retrieve\
  \ hashes.(Citation: GitHub Creddump7)\n\nNotes: \n\n* RID 500 account is the local, built-in administrator.\n* RID 501 is\
  \ the guest account.\n* User accounts start with a RID of 1,000+.\n"
external_references:
- external_id: T1003.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1003/002
- description: Flathers, R. (2018, February 19). creddump7. Retrieved April 11, 2018.
  source_name: GitHub Creddump7
  url: https://github.com/Neohapsis/creddump7
id: attack-pattern--1644e709-12d2-41e5-a60f-3470991f5011
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:26.545Z'
name: Security Account Manager
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Ed Williams, Trustwave, SpiderLabs
- Olaf Hartong, Falcon Force
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.1'
```
