---
parsed_by: focuslocust
source: mitre
type: generated
---
# Pre-compromise

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1056` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pre-compromise](../../attack/mitigations/M1056-pre-compromise.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1056 |
| name | Pre-compromise |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1056 |

## Preserved Source Material

```yaml
created: '2020-10-19T14:57:58.771Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully
  identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities
  focus on reducing an organization''s attack surface, identify adversarial preparation efforts, and increase the difficulty
  for attackers to conduct successful operations. This mitigation can be implemented through the following measures:


  Limit Information Exposure:


  - Regularly audit and sanitize publicly available data, including job posts, websites, and social media.

  - Use tools like OSINT monitoring platforms (e.g., SpiderFoot, Recon-ng) to identify leaked information.


  Protect Domain and DNS Infrastructure:


  - Enable DNSSEC and use WHOIS privacy protection.

  - Monitor for domain hijacking or lookalike domains using services like RiskIQ or DomainTools.


  External Monitoring:


  - Use tools like Shodan, Censys to monitor your external attack surface.

  - Deploy external vulnerability scanners to proactively address weaknesses.


  Threat Intelligence:


  - Leverage platforms like MISP, Recorded Future, or Anomali to track adversarial infrastructure, tools, and activity.


  Content and Email Protections:


  - Use email security solutions like Proofpoint, Microsoft Defender for Office 365, or Mimecast.

  - Enforce SPF/DKIM/DMARC policies to protect against email spoofing.


  Training and Awareness:


  - Educate employees on identifying phishing attempts, securing their social media, and avoiding information leaks.'
external_references:
- external_id: M1056
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1056
id: course-of-action--78bb71be-92b4-46de-acd6-5f998fedf1cc
modified: '2024-12-18T18:24:37.835Z'
name: Pre-compromise
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.1'
```
