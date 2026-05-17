---
parsed_by: focuslocust
source: mitre
type: generated
---
# Social Media

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0052` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Social Media](../../attack/data-sources/DC0052-social-media.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0052 |
| name | Social Media |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0052 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations,\
  \ social engineering, or other cyber threats.\n\n*Data Collection Measures:*\n\n- API Monitoring\t\n    - Social media APIs\
  \ (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts.\n- Web Scraping\n    - Extracts public\
  \ profile data, friend lists, or interactions to identify impersonation attempts.\n- Threat Intelligence Feeds\t\n    -\
  \ External feeds track malicious personas linked to disinformation campaigns or phishing.\n- OSINT Tools\n    - Maltego,\
  \ SpiderFoot, and OpenCTI can map social media persona relationships.\n- Endpoint Detection\t\n    - EDR logs user behavior\
  \ and alerts on suspicious social media interactions.\n- SIEM Logging\n    - Detects access to known phishing pages or social\
  \ media abuse via proxy logs.\n- Dark Web Monitoring\t\n    - Identifies compromised social media credentials being sold."
external_references:
- external_id: DC0052
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0052
id: x-mitre-data-component--8fb2f315-1aca-4cef-ae0d-8105e1f95985
modified: '2025-10-21T15:10:28.402Z'
name: Social Media
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Persona
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
