---
parsed_by: focuslocust
source: mitre
type: generated
---
# Social Engineering

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1684` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Social Engineering](../../attack/techniques/T1684-social-engineering.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1684 |
| name | Social Engineering |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1684 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:53:26.607Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use social engineering techniques to influence users to take actions that result in unauthorized\
  \ access, approval of changes, disclosure of sensitive information, or execution of adversary-supplied instructions (i.e.,\
  \ introduction of malicious payloads or software), while minimizing technical indicators. \n\nAdversaries may leverage trust-building\
  \ methods across multiple channels (e.g., executive, vendor, or help desk scenarios, including AI-enabled voice interactions)\
  \ to prompt user-authorized actions such as password resets, MFA changes, financial approvals, or the disclosure of sensitive\
  \ information. Adversaries may also leverage common business communications and workflows such as email, collaboration platforms,\
  \ voice communications, recruiting processes, help desk interactions, and SaaS consent mechanisms to make malicious requests\
  \ appear routine and legitimate.(Citation: Proofpoint TA427 April 2024)(Citation: SE SentinelOne 2)(Citation: SE - Hackers\
  \ Target Workday)\n\nAdditionally, adversaries have persuaded victims to take actions through references of current events,\
  \ harnessing relevant themes to the work role or the organizations mission. For example, adversaries may use scare tactics\
  \ (i.e., threaten repercussions for non-compliance) or otherwise incite victims’ emotions in order to generate a sense of\
  \ urgency to take action.(Citation: SE Proofpoint)(Citation: SE SentinelOne)\n\nThis technique may include common social\
  \ engineering patterns such as [Phishing](https://attack.mitre.org/techniques/T1566) and [Spearphishing Voice](https://attack.mitre.org/techniques/T1566/004),\
  \ often supported by convincing and targeted narratives.(Citation: SE SentinelOne 2)(Citation: Fortinet Trends 25-26)"
external_references:
- external_id: T1684
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1684
- description: David Jones. (2025, August 19). Hackers target Workday in social engineering attack. Retrieved April 15, 2026.
  source_name: SE - Hackers Target Workday
  url: https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.
- description: Fortinet. (n.d.). Recent Cyber Attacks & Emerging Cybersecurity Trends. Retrieved April 15, 2026.
  source_name: Fortinet Trends 25-26
  url: https://www.fortinet.com/uk/resources/cyberglossary/recent-cyber-attacks
- description: 'Lesnewich, G. et al. (2024, April 16). From Social Engineering to DMARC Abuse: TA427’s Art of Information
    Gathering. Retrieved May 3, 2024.'
  source_name: Proofpoint TA427 April 2024
  url: https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering
- description: Proofpoint. (n.d.). What Is Social Engineering?. Retrieved April 15, 2026.
  source_name: SE Proofpoint
  url: https://www.proofpoint.com/us/threat-reference/social-engineering
- description: SentinelOne. (2023, October 19). Social Engineering Attacks | How to Recognize and Resist The Bait. Retrieved
    April 15, 2026.
  source_name: SE SentinelOne
  url: https://www.sentinelone.com/blog/social-engineering-attacks-how-to-recognize-and-resist-the-bait/
- description: SentinelOne. (2025, August 19). 15 Types of Social Engineering Attacks. Retrieved April 15, 2026.
  source_name: SE SentinelOne 2
  url: https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/
id: attack-pattern--41e4d77a-6275-4976-9e35-785985598519
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T15:39:55.218Z'
name: Social Engineering
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Office Suite
- SaaS
- Windows
x_mitre_version: '1.0'
```
