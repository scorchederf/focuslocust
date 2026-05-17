---
parsed_by: focuslocust
source: mitre
type: generated
---
# Local Email Collection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1114.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Local Email Collection](../../attack/techniques/T1114.001-local-email-collection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1114.001 |
| name | Local Email Collection |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1114/001 |

## Preserved Source Material

```yaml
created: '2020-02-19T18:46:06.098Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may target user email on local systems to collect sensitive information. Files containing email
  data can be acquired from a user’s local system, such as Outlook storage or cache files.


  Outlook stores data locally in offline data files with an extension of .ost. Outlook 2010 and later supports .ost file sizes
  up to 50GB, while earlier versions of Outlook support up to 20GB.(Citation: Outlook File Sizes) IMAP accounts in Outlook
  2013 (and earlier) and POP accounts use Outlook Data Files (.pst) as opposed to .ost, whereas IMAP accounts in Outlook 2016
  (and later) use .ost files. Both types of Outlook data files are typically stored in `C:\Users\<username>\Documents\Outlook
  Files` or `C:\Users\<username>\AppData\Local\Microsoft\Outlook`.(Citation: Microsoft Outlook Files)'
external_references:
- external_id: T1114.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1114/001
- description: Microsoft. (n.d.). Introduction to Outlook Data Files (.pst and .ost). Retrieved February 19, 2020.
  source_name: Microsoft Outlook Files
  url: https://support.office.com/en-us/article/introduction-to-outlook-data-files-pst-and-ost-222eaf92-a995-45d9-bde2-f331f60e2790
- description: N. O'Bryan. (2018, May 30). Managing Outlook Cached Mode and OST File Sizes. Retrieved February 19, 2020.
  source_name: Outlook File Sizes
  url: https://practical365.com/clients/office-365-proplus/outlook-cached-mode-ost-file-sizes/
id: attack-pattern--1e9eb839-294b-48cc-b0d3-c45555a2a004
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:29.669Z'
name: Local Email Collection
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.1'
```
