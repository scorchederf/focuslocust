---
parsed_by: focuslocust
source: mitre
type: generated
---
# Add-ins

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1137.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Add-ins](../../attack/techniques/T1137.006-add-ins.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1137.006 |
| name | Add-ins |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1137/006 |

## Preserved Source Material

```yaml
created: '2019-11-07T19:52:52.801Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system. Office add-ins
  can be used to add functionality to Office programs. (Citation: Microsoft Office Add-ins) There are different types of add-ins
  that can be used by the various Office products; including Word/Excel add-in Libraries (WLL/XLL), VBA add-ins, Office Component
  Object Model (COM) add-ins, automation add-ins, VBA Editor (VBE), Visual Studio Tools for Office (VSTO) add-ins, and Outlook
  add-ins. (Citation: MRWLabs Office Persistence Add-ins)(Citation: FireEye Mail CDS 2018)


  Add-ins can be used to obtain persistence because they can be set to execute code when an Office application starts. '
external_references:
- external_id: T1137.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1137/006
- description: Caban, D. and Hirani, M. (2018, October 3). You’ve Got Mail! Enterprise Email Compromise. Retrieved November
    17, 2024.
  source_name: FireEye Mail CDS 2018
  url: https://web.archive.org/web/20190508170121/https://summit.fireeye.com/content/dam/fireeye-www/summit/cds-2018/presentations/cds18-technical-s03-youve-got-mail.pdf
- description: Knowles, W. (2017, April 21). Add-In Opportunities for Office Persistence. Retrieved November 17, 2024.
  source_name: MRWLabs Office Persistence Add-ins
  url: https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/
- description: Microsoft. (n.d.). Add or remove add-ins. Retrieved July 3, 2017.
  source_name: Microsoft Office Add-ins
  url: https://support.office.com/article/Add-or-remove-add-ins-0af570c4-5cf3-4fa9-9b88-403625a0b460
- description: Shukrun, S. (2019, June 2). Office Templates and GlobalDotName - A Stealthy Office Persistence Technique. Retrieved
    August 26, 2019.
  source_name: GlobalDotName Jun 2019
  url: https://www.221bluestreet.com/post/office-templates-and-globaldotname-a-stealthy-office-persistence-technique
id: attack-pattern--34f1d81d-fe88-4f97-bd3b-a3164536255d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:48:37.911Z'
name: Add-ins
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
- Office Suite
x_mitre_version: '1.2'
```
