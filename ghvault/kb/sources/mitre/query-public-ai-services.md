---
parsed_by: focuslocust
source: mitre
type: generated
---
# Query Public AI Services

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1682` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Query Public AI Services](../../attack/techniques/T1682-query-public-ai-services.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1682 |
| name | Query Public AI Services |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1682 |

## Preserved Source Material

```yaml
created: '2026-03-25T14:21:30.680Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may query publicly accessible artificial intelligence (AI) services, such as large language models
  (LLMs), to support targeting and operations. In addition to searching websites or databases directly (i.e., [Search Open
  Websites/Domains](https://attack.mitre.org/techniques/T1593)), adversaries may use AI services to synthesize, aggregate,
  and analyze publicly available information at scale. This may include identifying individuals or organizations to target,
  researching organizational structures and personnel, identifying technologies used by target organizations, researching
  business relationships to develop plausible pretexts for [Social Engineering](https://attack.mitre.org/techniques/T1684)
  approaches, identifying contact information for use in [Phishing](https://attack.mitre.org/techniques/T1566) or [Phishing
  for Information](https://attack.mitre.org/techniques/T1598), or gathering derogatory or sensitive information about individuals
  that may be used for extortion or coercion.(Citation: MSFT-AI)(Citation: GTIG AI Threat Tracker)


  Information gathered through AI services may be leveraged for other behaviors, such as establishing operational resources
  (i.e., [Generate Content](https://attack.mitre.org/techniques/T1683) or [Establish Accounts](https://attack.mitre.org/techniques/T1585).
  For obtaining access to AI tools and services, see [Artificial Intelligence](https://attack.mitre.org/techniques/T1588/007).'
external_references:
- external_id: T1682
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1682
- description: 'Google Threat Intelligence Group . (2026, February 12). GTIG AI Threat Tracker: Distillation, Experimentation,
    and (Continued) Integration of AI for Adversarial Use. Retrieved March 25, 2026.'
  source_name: GTIG AI Threat Tracker
  url: https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use
- description: Microsoft Threat Intelligence. (2024, February 14). Staying ahead of threat actors in the age of AI. Retrieved
    March 11, 2024.
  source_name: MSFT-AI
  url: https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/
id: attack-pattern--143122a8-fcda-4dd7-aded-5b9387d9c2d6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2026-04-20T20:59:00.096Z'
name: Query Public AI Services
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.0'
```
