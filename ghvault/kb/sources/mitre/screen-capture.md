---
parsed_by: focuslocust
source: mitre
type: generated
---
# Screen Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1113` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Screen Capture](../../attack/techniques/T1113-screen-capture.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1113 |
| name | Screen Capture |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1113 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:25.060Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation.
  Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations.
  Taking a screenshot is also typically possible through native utilities or API calls, such as <code>CopyFromScreen</code>,
  <code>xwd</code>, or <code>screencapture</code>.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)

  '
external_references:
- external_id: T1113
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1113
- description: Microsoft. (n.d.). Graphics.CopyFromScreen Method. Retrieved March 24, 2020.
  source_name: CopyFromScreen .NET
  url: https://docs.microsoft.com/en-us/dotnet/api/system.drawing.graphics.copyfromscreen?view=netframework-4.8
- description: Thomas Reed. (2017, January 18). New Mac backdoor using antiquated code. Retrieved July 5, 2017.
  source_name: Antiquated Mac Malware
  url: https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/
id: attack-pattern--0259baeb-9f63-4c69-bf10-eb038c390688
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:19.886Z'
name: Screen Capture
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.1'
```
