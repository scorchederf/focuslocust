---
parsed_by: focuslocust
source: mitre
type: generated
---
# Malicious File

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1204.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Malicious File](../../attack/techniques/T1204.002-malicious-file.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1204.002 |
| name | Malicious File |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1204/002 |

## Preserved Source Material

```yaml
created: '2020-03-11T14:49:36.954Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected\
  \ to social engineering to get them to open a file that will lead to code execution. This user action will typically be\
  \ observed as follow-on behavior from [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001). Adversaries\
  \ may use several types of files that require a user to execute them, including .doc, .pdf, .xls, .rtf, .scr, .exe, .lnk,\
  \ .pif, .cpl, .reg, and .iso.(Citation: Mandiant Trojanized Windows 10)\n\nAdversaries may employ various forms of [Masquerading](https://attack.mitre.org/techniques/T1036)\
  \ and [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027) to increase the likelihood that a user\
  \ will open and successfully execute a malicious file. These methods may include using a familiar naming convention and/or\
  \ password protecting the file and supplying instructions to a user on how to open it.(Citation: Password Protected Word\
  \ Docs) \n\nWhile [Malicious File](https://attack.mitre.org/techniques/T1204/002) frequently occurs shortly after Initial\
  \ Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or\
  \ on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534)."
external_references:
- external_id: T1204.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1204/002
- description: 'Lawrence Abrams. (2017, July 12). PSA: Don''t Open SPAM Containing Password Protected Word Docs. Retrieved
    January 5, 2022.'
  source_name: Password Protected Word Docs
  url: https://www.bleepingcomputer.com/news/security/psa-dont-open-spam-containing-password-protected-word-docs/
- description: Mandiant Intelligence. (2022, December 15). Trojanized Windows 10 Operating System Installers Targeted Ukrainian
    Government. Retrieved September 26, 2025.
  source_name: Mandiant Trojanized Windows 10
  url: https://www.mandiant.com/resources/blog/trojanized-windows-installers-ukrainian-government
id: attack-pattern--232b7f21-adf9-4b42-b936-b9d6f7df856e
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:48:31.674Z'
name: Malicious File
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- TruKno
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_remote_support: false
x_mitre_version: '1.6'
```
