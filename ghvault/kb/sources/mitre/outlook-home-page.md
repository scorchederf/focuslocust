---
parsed_by: focuslocust
source: mitre
type: generated
---
# Outlook Home Page

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1137.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Outlook Home Page](../../attack/techniques/T1137.004-outlook-home-page.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1137.004 |
| name | Outlook Home Page |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1137/004 |

## Preserved Source Material

```yaml
created: '2019-11-07T20:09:56.536Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Microsoft Outlook''s Home Page feature to obtain persistence on a compromised system.
  Outlook Home Page is a legacy feature used to customize the presentation of Outlook folders. This feature allows for an
  internal or external URL to be loaded and presented whenever a folder is opened. A malicious HTML page can be crafted that
  will execute code when loaded by Outlook Home Page.(Citation: SensePost Outlook Home Page)


  Once malicious home pages have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious
  Home Pages will execute when the right Outlook folder is loaded/reloaded.(Citation: SensePost Outlook Home Page)

  '
external_references:
- external_id: T1137.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1137/004
- description: Fox, C., Vangel, D. (2018, April 22). Detect and Remediate Outlook Rules and Custom Forms Injections Attacks
    in Office 365. Retrieved February 4, 2019.
  source_name: Microsoft Detect Outlook Forms
  url: https://docs.microsoft.com/en-us/office365/securitycompliance/detect-and-remediate-outlook-rules-forms-attack
- description: SensePost. (2017, September 21). NotRuler - The opposite of Ruler, provides blue teams with the ability to
    detect Ruler usage against Exchange. Retrieved February 4, 2019.
  source_name: SensePost NotRuler
  url: https://github.com/sensepost/notruler
- description: Stalmans, E. (2017, October 11). Outlook Home Page – Another Ruler Vector. Retrieved February 4, 2019.
  source_name: SensePost Outlook Home Page
  url: https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/
id: attack-pattern--bf147104-abf9-4221-95d1-e81585859441
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:18.872Z'
name: Outlook Home Page
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
