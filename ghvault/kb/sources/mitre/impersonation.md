---
parsed_by: focuslocust
source: mitre
type: generated
---
# Impersonation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1684.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Impersonation](../../attack/techniques/T1684.001-impersonation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1684.001 |
| name | Impersonation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1684/001 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:01.082Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may impersonate a trusted person or organization in order to persuade and trick a target into performing
  some action on their behalf. For example, adversaries may communicate with victims (via [Phishing for Information](https://attack.mitre.org/techniques/T1598),
  [Phishing](https://attack.mitre.org/techniques/T1566), or [Internal Spearphishing](https://attack.mitre.org/techniques/T1534))
  while impersonating a known sender such as an executive, colleague, or third-party vendor. Established trust can then be
  leveraged to accomplish an adversary’s ultimate goals, possibly against multiple victims.


  In many cases of business email compromise or email fraud campaigns, adversaries use impersonation to defraud victims --
  deceiving them into sending money or divulging information that ultimately enables [Financial Theft](https://attack.mitre.org/techniques/T1657).


  Adversaries will often also use social engineering techniques such as manipulative and persuasive language in email subject
  lines and body text such as `payment`, `request`, or `urgent` to push the victim to act quickly before malicious activity
  is detected. These campaigns are often specifically targeted against people who, due to job roles and/or accesses, can carry
  out the adversary’s goal.  


  Impersonation is typically preceded by reconnaissance techniques such as [Gather Victim Identity Information](https://attack.mitre.org/techniques/T1589)
  and [Gather Victim Org Information](https://attack.mitre.org/techniques/T1591) as well as acquiring infrastructure such
  as email domains (i.e. [Domains](https://attack.mitre.org/techniques/T1583/001)) to substantiate their false identity.(Citation:
  Crowdstrike BEC)


  There is the potential for multiple victims in campaigns involving impersonation. For example, an adversary may Compromise
  Accounts targeting one organization which can then be used to support impersonation against other entities.(Citation: VEC)'
external_references:
- external_id: T1684.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1684/001
- description: Bart Lenaerts-Bergmans. (2023, August 8). What is Business Email Compromise?. Retrieved April 15, 2026.
  source_name: Crowdstrike BEC
  url: https://www.crowdstrike.com/en-us/cybersecurity-101/threat-intelligence/business-email-compromise-bec/
- description: CloudFlare. (n.d.). What is vendor email compromise (VEC)?. Retrieved September 12, 2023.
  source_name: VEC
  url: https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/#:~:text=Vendor%20email%20compromise%2C%20also%20referred,steal%20from%20that%20vendor%27s%20customers.
id: attack-pattern--cd92d2b8-ce43-4666-9472-f1b4b9f4f8be
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-22T15:50:04.400Z'
name: Impersonation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Blake Strom, Microsoft Threat Intelligence
- Pawel Partyka, Microsoft Threat Intelligence
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Office Suite
- SaaS
- Windows
x_mitre_version: '1.0'
```
