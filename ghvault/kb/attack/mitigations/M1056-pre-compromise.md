---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1056 - Pre-compromise

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

## Summary

Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures:

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

- Educate employees on identifying phishing attempts, securing their social media, and avoiding information leaks.

## Source Verification

[source record](../../sources/mitre/pre-compromise.md)

## Evidence Excerpt

```text
created: '2020-10-19T14:57:58.771Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully
identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities
focus on reducing an organization''s attack surface, identify adversarial preparation efforts, and increase the difficulty
for attackers to conduct successful operations. This mitigation can be implemented through the following measures:
Limit Information Exposure:
- Regularly audit and sanitize publicly available data, including job posts, websites, and social media.
```
