---
parsed_by: focuslocust
source: mitre
type: generated
---
# Audio-Visual Content

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1683.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Audio-Visual Content](../../attack/techniques/T1683.002-audio-visual-content.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1683.002 |
| name | Audio-Visual Content |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1683/002 |

## Preserved Source Material

```yaml
created: '2026-03-25T14:28:15.331Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may create or manipulate audio, image, and video content to support targeting and malicious operations.\
  \ Adversaries may also use synthetic voice recordings, real-time altered audio or video during live interactions, fabricated\
  \ profile photos and identity documents, or video content depicting fabricated or impersonated individuals.(Citation: Nov\
  \ AI Threat Tracker)\n\nContent may be produced manually through editing tools, generated using AI-assisted tools, or produced\
  \ using third-party synthetic services.(Citation: FBI 2025 AI Generate Content)(Citation: Europol Deepfakes) AI-assisted\
  \ tools have enabled adversaries to produce synthetic media at scale and generate content that is more difficult to identify\
  \ as inauthentic. \n\nAudio-visual content produced through these methods may be used in support of other techniques, such\
  \ as [Phishing](https://attack.mitre.org/techniques/T1660), [Spearphishing via Service](https://attack.mitre.org/techniques/T1566/003),\
  \ [Phishing for Information](https://attack.mitre.org/techniques/T1598), [Internal Spearphishing](https://attack.mitre.org/techniques/T1534),\
  \ [Social Engineering](https://attack.mitre.org/techniques/T1684), [Financial Theft](https://attack.mitre.org/techniques/T1657),\
  \ or [Establish Accounts](https://attack.mitre.org/techniques/T1585)."
external_references:
- external_id: T1683.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1683/002
- description: Europol. (2022). FACING REALITY? LAW ENFORCEMENT AND THE CHALLENGE OF DEEPFAKES. Retrieved April 17, 2026.
  source_name: Europol Deepfakes
  url: https://www.europol.europa.eu/cms/sites/default/files/documents/Europol_Innovation_Lab_Facing_Reality_Law_Enforcement_And_The_Challenge_Of_Deepfakes.pdf
- description: 'Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage
    of AI Tools. Retrieved March 31, 2026.'
  source_name: Nov AI Threat Tracker
  url: https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- description: Internet Crime Complaint Center, FBI. (2025). Federal Bureau of Investigation Internet Crime Report, 2025.
    Retrieved April 17, 2026.
  source_name: FBI 2025 AI Generate Content
  url: https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf
id: attack-pattern--8f452cb4-cbf4-4522-8b11-448787be95c4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2026-04-20T15:34:51.855Z'
name: Audio-Visual Content
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Gilberto Pérez
- Alex Wong
- Patrick Mkhael (aka Pinguino)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.0'
```
