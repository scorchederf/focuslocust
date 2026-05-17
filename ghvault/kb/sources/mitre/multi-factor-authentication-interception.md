---
parsed_by: focuslocust
source: mitre
type: generated
---
# Multi-Factor Authentication Interception

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1111` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Multi-Factor Authentication Interception](../../attack/techniques/T1111-multi-factor-authentication-interception.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1111 |
| name | Multi-Factor Authentication Interception |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1111 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:23.195Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may target multi-factor authentication (MFA) mechanisms, (i.e., smart cards, token generators, etc.)\
  \ to gain access to credentials that can be used to access systems, services, and network resources. Use of MFA is recommended\
  \ and provides a higher level of security than usernames and passwords alone, but organizations should be aware of techniques\
  \ that could be used to intercept and bypass these security mechanisms. \n\nIf a smart card is used for multi-factor authentication,\
  \ then a keylogger will need to be used to obtain the password associated with a smart card during normal use. With both\
  \ an inserted card and access to the smart card password, an adversary can connect to a network resource using the infected\
  \ system to proxy the authentication with the inserted hardware token. (Citation: Mandiant M Trends 2011)\n\nAdversaries\
  \ may also employ a keylogger to similarly target other hardware tokens, such as RSA SecurID. Capturing token input (including\
  \ a user's personal identification code) may provide temporary access (i.e. replay the one-time passcode until the next\
  \ value rollover) as well as possibly enabling adversaries to reliably predict future authentication values (given access\
  \ to both the algorithm and any seed values used to generate appended temporary codes). (Citation: GCN RSA June 2011)\n\n\
  Other methods of MFA may be intercepted and used by an adversary to authenticate. It is common for one-time codes to be\
  \ sent via out-of-band communications (email, SMS). If the device and/or service is not secured, then it may be vulnerable\
  \ to interception. Service providers can also be targeted: for example, an adversary may compromise an SMS messaging service\
  \ in order to steal MFA codes sent to users’ phones.(Citation: Okta Scatter Swine 2022)"
external_references:
- external_id: T1111
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1111
- description: Jackson, William. (2011, June 7). RSA confirms its tokens used in Lockheed hack. Retrieved November 17, 2024.
  source_name: GCN RSA June 2011
  url: https://www.route-fifty.com/cybersecurity/2011/06/rsa-confirms-its-tokens-used-in-lockheed-hack/282818/
- description: Mandiant. (2011, January 27). Mandiant M-Trends 2011. Retrieved January 10, 2016.
  source_name: Mandiant M Trends 2011
  url: https://dl.mandiant.com/EE/assets/PDF_MTrends_2011.pdf
- description: 'Okta. (2022, August 25). Detecting Scatter Swine: Insights into a Relentless Phishing Campaign. Retrieved
    February 24, 2023.'
  source_name: Okta Scatter Swine 2022
  url: https://sec.okta.com/scatterswine
id: attack-pattern--dd43c543-bb85-4a6f-aa6e-160d90d06a49
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:29.231Z'
name: Multi-Factor Authentication Interception
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- John Lambert, Microsoft Threat Intelligence Center
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.1'
```
