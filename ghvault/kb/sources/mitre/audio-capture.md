---
parsed_by: focuslocust
source: mitre
type: generated
---
# Audio Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1123` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Audio Capture](../../attack/techniques/T1123-audio-capture.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1123 |
| name | Audio Capture |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1123 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:34.528Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary can leverage a computer''s peripheral devices (e.g., microphones and webcams) or applications (e.g.,
  voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to
  gather information.(Citation: ESET Attor Oct 2019)


  Malware or scripts may be used to interact with the devices through an available API provided by the operating system or
  an application to capture audio. Audio files may be written to disk and exfiltrated later.'
external_references:
- external_id: T1123
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1123
- description: 'Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO
    A SPY PLATFORM. Retrieved May 6, 2020.'
  source_name: ESET Attor Oct 2019
  url: https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf
id: attack-pattern--1035cdf2-3e5f-446f-a7a7-e8f6d7925967
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:24.702Z'
name: Audio Capture
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
x_mitre_version: '1.0'
```
