---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0052 - Social Media

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

## Summary

Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations, social engineering, or other cyber threats.

*Data Collection Measures:*

- API Monitoring	
    - Social media APIs (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts.
- Web Scraping
    - Extracts public profile data, friend lists, or interactions to identify impersonation attempts.
- Threat Intelligence Feeds	
    - External feeds track malicious personas linked to disinformation campaigns or phishing.
- OSINT Tools
    - Maltego, SpiderFoot, and OpenCTI can map social media persona relationships.
- Endpoint Detection	
    - EDR logs user behavior and alerts on suspicious social media interactions.
- SIEM Logging
    - Detects access to known phishing pages or social media abuse via proxy logs.
- Dark Web Monitoring	
    - Identifies compromised social media credentials being sold.

## Source Verification

[source record](../../sources/mitre/social-media.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations,\
\ social engineering, or other cyber threats.\n\n*Data Collection Measures:*\n\n- API Monitoring\t\n    - Social media APIs\
\ (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts.\n- Web Scraping\n    - Extracts public\
\ profile data, friend lists, or interactions to identify impersonation attempts.\n- Threat Intelligence Feeds\t\n    -\
\ External feeds track malicious personas linked to disinformation campaigns or phishing.\n- OSINT Tools\n    - Maltego,\
\ SpiderFoot, and OpenCTI can map social media persona relationships.\n- Endpoint Detection\t\n    - EDR logs user behavior\
```
