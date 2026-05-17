---
parsed_by: focuslocust
source: mitre
type: generated
---
# Video Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1125` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Video Capture](../../attack/techniques/T1125-video-capture.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1125 |
| name | Video Capture |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1125 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:37.917Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary can leverage a computer''s peripheral devices (e.g., integrated cameras or webcams) or applications
  (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured
  from devices or applications, potentially in specified intervals, in lieu of video files.


  Malware or scripts may be used to interact with the devices through an available API provided by the operating system or
  an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique
  differs from [Screen Capture](https://attack.mitre.org/techniques/T1113) due to use of specific devices or applications
  for video recording rather than capturing the victim''s screen.


  In macOS, there are a few different malware samples that record the user''s webcam such as FruitFly and Proton. (Citation:
  objective-see 2017 review)'
external_references:
- external_id: T1125
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1125
- description: Patrick Wardle. (n.d.). Retrieved March 20, 2018.
  source_name: objective-see 2017 review
  url: https://objective-see.com/blog/blog_0x25.html
id: attack-pattern--6faf650d-bf31-4eb4-802d-1000cf38efaf
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:56.077Z'
name: Video Capture
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
x_mitre_version: '1.2'
```
