---
parsed_by: focuslocust
source: mitre
type: generated
---
# Multi-Factor Authentication Request Generation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1621` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Multi-Factor Authentication Request Generation](../../attack/techniques/T1621-multi-factor-authentication-request-generation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1621 |
| name | Multi-Factor Authentication Request Generation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1621 |

## Preserved Source Material

```yaml
created: '2022-04-01T02:15:49.754Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by
  generating MFA requests sent to users.


  Adversaries in possession of credentials to [Valid Accounts](https://attack.mitre.org/techniques/T1078) may be unable to
  complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security
  control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as
  Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account. If adversaries
  lack credentials to victim accounts, they may also abuse automatic push notification generation when this option is configured
  for self-service password reset (SSPR).(Citation: Obsidian SSPR Abuse 2023)


  In some cases, adversaries may continuously repeat login attempts in order to bombard users with MFA push notifications,
  SMS messages, and phone calls, potentially resulting in the user finally accepting the authentication request in response
  to “MFA fatigue.”(Citation: Russian 2FA Push Annoyance - Cimpanu)(Citation: MFA Fatigue Attacks - PortSwigger)(Citation:
  Suspected Russian Activity Targeting Government and Business Entities Around the Globe)'
external_references:
- external_id: T1621
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1621
- description: Catalin Cimpanu. (2021, December 9). Russian hackers bypass 2FA by annoying victims with repeated push notifications.
    Retrieved March 31, 2022.
  source_name: Russian 2FA Push Annoyance - Cimpanu
  url: https://therecord.media/russian-hackers-bypass-2fa-by-annoying-victims-with-repeated-push-notifications/
- description: 'Jessica Haworth. (2022, February 16). MFA fatigue attacks: Users tricked into allowing device access due to
    overload of push notifications. Retrieved March 31, 2022.'
  source_name: MFA Fatigue Attacks - PortSwigger
  url: https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications
- description: Luke Jenkins, Sarah Hawley, Parnian Najafi, Doug Bienstock. (2021, December 6). Suspected Russian Activity
    Targeting Government and Business Entities Around the Globe. Retrieved April 15, 2022.
  source_name: Suspected Russian Activity Targeting Government and Business Entities Around the Globe
  url: https://www.mandiant.com/resources/russian-targeting-gov-business
- description: 'Noah Corradin and Shuyang Wang. (2023, August 1). Behind The Breach: Self-Service Password Reset (SSPR) Abuse
    in Azure AD. Retrieved March 28, 2024.'
  source_name: Obsidian SSPR Abuse 2023
  url: https://www.obsidiansecurity.com/blog/behind-the-breach-self-service-password-reset-azure-ad/
id: attack-pattern--954a1639-f2d6-407d-aef3-4917622ca493
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:07.399Z'
name: Multi-Factor Authentication Request Generation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jon Sternstein, Stern Security
- Pawel Partyka, Microsoft 365 Defender
- Shanief Webb
- Obsidian Security
- Arun Seelagan, CISA
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- Linux
- macOS
- IaaS
- SaaS
- Office Suite
- Identity Provider
x_mitre_version: '1.2'
```
