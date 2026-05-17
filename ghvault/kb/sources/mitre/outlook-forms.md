---
parsed_by: focuslocust
source: mitre
type: generated
---
# Outlook Forms

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1137.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Outlook Forms](../../attack/techniques/T1137.003-outlook-forms.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1137.003 |
| name | Outlook Forms |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1137/003 |

## Preserved Source Material

```yaml
created: '2019-11-07T20:06:02.624Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system. Outlook forms are
  used as templates for presentation and functionality in Outlook messages. Custom Outlook forms can be created that will
  execute code when a specifically crafted email is sent by an adversary utilizing the same custom Outlook form.(Citation:
  SensePost Outlook Forms)


  Once malicious forms have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious forms
  will execute when an adversary sends a specifically crafted email to the user.(Citation: SensePost Outlook Forms)'
external_references:
- external_id: T1137.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1137/003
- description: Fox, C., Vangel, D. (2018, April 22). Detect and Remediate Outlook Rules and Custom Forms Injections Attacks
    in Office 365. Retrieved February 4, 2019.
  source_name: Microsoft Detect Outlook Forms
  url: https://docs.microsoft.com/en-us/office365/securitycompliance/detect-and-remediate-outlook-rules-forms-attack
- description: SensePost. (2017, September 21). NotRuler - The opposite of Ruler, provides blue teams with the ability to
    detect Ruler usage against Exchange. Retrieved February 4, 2019.
  source_name: SensePost NotRuler
  url: https://github.com/sensepost/notruler
- description: Stalmans, E. (2017, April 28). Outlook Forms and Shells. Retrieved February 4, 2019.
  source_name: SensePost Outlook Forms
  url: https://sensepost.com/blog/2017/outlook-forms-and-shells/
id: attack-pattern--a9e2cea0-c805-4bf8-9e31-f5f0513a3634
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:12.562Z'
name: Outlook Forms
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
