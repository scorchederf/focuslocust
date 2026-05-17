---
parsed_by: focuslocust
source: mitre
type: generated
---
# Spearphishing Voice

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1566.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Spearphishing Voice](../../attack/techniques/T1566.004-spearphishing-voice.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1566.004 |
| name | Spearphishing Voice |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1566/004 |

## Preserved Source Material

```yaml
created: '2023-09-07T21:50:08.827Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use voice communications to ultimately gain access to victim systems. Spearphishing voice is
  a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of manipulating
  a user into providing access to systems through a phone call or other forms of voice communications. Spearphishing frequently
  involves social engineering techniques, such as posing as a trusted source (ex: [Impersonation](https://attack.mitre.org/techniques/T1684/001))
  and/or creating a sense of urgency or alarm for the recipient.


  All forms of phishing are electronically delivered social engineering. In this scenario, adversaries are not directly sending
  malware to a victim vice relying on [User Execution](https://attack.mitre.org/techniques/T1204) for delivery and execution.
  For example, victims may receive phishing messages that instruct them to call a phone number where they are directed to
  visit a malicious URL, download malware,(Citation: sygnia Luna Month)(Citation: CISA Remote Monitoring and Management Software)
  or install adversary-accessible remote management tools ([Remote Access Tools](https://attack.mitre.org/techniques/T1219))
  onto their computer.(Citation: Unit42 Luna Moth)


  Adversaries may also combine voice phishing with [Multi-Factor Authentication Request Generation](https://attack.mitre.org/techniques/T1621)
  in order to trick users into divulging MFA credentials or accepting authentication prompts.(Citation: Proofpoint Vishing)'
external_references:
- external_id: T1566.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1566/004
- description: CISA. (n.d.). Protecting Against Malicious Use of Remote Monitoring and Management Software. Retrieved February
    2, 2023.
  source_name: CISA Remote Monitoring and Management Software
  url: https://www.cisa.gov/uscert/ncas/alerts/aa23-025a
- description: Kristopher Russo. (n.d.). Luna Moth Callback Phishing Campaign. Retrieved February 2, 2023.
  source_name: Unit42 Luna Moth
  url: https://unit42.paloaltonetworks.com/luna-moth-callback-phishing/
- description: 'Oren Biderman, Tomer Lahiyani, Noam Lifshitz, Ori Porag. (n.d.). LUNA MOTH: THE THREAT ACTORS BEHIND RECENT
    FALSE SUBSCRIPTION SCAMS. Retrieved February 2, 2023.'
  source_name: sygnia Luna Month
  url: https://blog.sygnia.co/luna-moth-false-subscription-scams
- description: Proofpoint. (n.d.). What Is Vishing?. Retrieved September 8, 2023.
  source_name: Proofpoint Vishing
  url: https://www.proofpoint.com/us/threat-reference/vishing
id: attack-pattern--bb5e59c4-abe7-40c7-8196-e373cb1e5974
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: initial-access
modified: '2026-04-17T16:04:48.737Z'
name: Spearphishing Voice
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- Identity Provider
x_mitre_version: '1.2'
```
