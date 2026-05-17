---
parsed_by: focuslocust
source: mitre
type: generated
---
# Device Registration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1098.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Device Registration](../../attack/techniques/T1098.005-device-registration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1098.005 |
| name | Device Registration |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1098/005 |

## Preserved Source Material

```yaml
created: '2022-03-04T18:30:38.989Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may register a device to an adversary-controlled account. Devices may be registered in a multifactor
  authentication (MFA) system, which handles authentication to the network, or in a device management system, which handles
  device access and compliance.


  MFA systems, such as Duo or Okta, allow users to associate devices with their accounts in order to complete MFA requirements.
  An adversary that compromises a user’s credentials may enroll a new device in order to bypass initial MFA requirements and
  gain persistent access to a network.(Citation: CISA MFA PrintNightmare)(Citation: DarkReading FireEye SolarWinds) In some
  cases, the MFA self-enrollment process may require only a username and password to enroll the account''s first device or
  to enroll a device to an inactive account. (Citation: Mandiant APT29 Microsoft 365 2022)


  Similarly, an adversary with existing access to a network may register a device or a virtual machine to Entra ID and/or
  its device management system, Microsoft Intune, in order to access sensitive data or resources while bypassing conditional
  access policies.(Citation: AADInternals - Device Registration)(Citation: AADInternals - Conditional Access Bypass)(Citation:
  Microsoft DEV-0537)(Citation: Expel Atlas Lion 2025)


  Devices registered in Entra ID may be able to conduct [Internal Spearphishing](https://attack.mitre.org/techniques/T1534)
  campaigns via intra-organizational emails, which are less likely to be treated as suspicious by the email client.(Citation:
  Microsoft - Device Registration) Additionally, an adversary may be able to perform a [Service Exhaustion Flood](https://attack.mitre.org/techniques/T1499/002)
  on an Entra ID tenant by registering a large number of devices.(Citation: AADInternals - BPRT)'
external_references:
- external_id: T1098.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1098/005
- description: 'Ben Nahorney and Jennifer Maynard. (2025, April 10). Observing Atlas Lion (part one): Why take control when
    you can enroll?. Retrieved May 22, 2025.'
  source_name: Expel Atlas Lion 2025
  url: https://expel.com/blog/observing-atlas-lion-part-one/
- description: Cybersecurity and Infrastructure Security Agency. (2022, March 15). Russian State-Sponsored Cyber Actors Gain
    Network Access by Exploiting Default Multifactor Authentication Protocols and “PrintNightmare” Vulnerability. Retrieved
    March 16, 2022.
  source_name: CISA MFA PrintNightmare
  url: https://www.cisa.gov/uscert/ncas/alerts/aa22-074a
- description: 'Douglas Bienstock. (2022, August 18). You Can’t Audit Me: APT29 Continues Targeting Microsoft 365. Retrieved
    February 23, 2023.'
  source_name: Mandiant APT29 Microsoft 365 2022
  url: https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft
- description: Dr. Nestori Syynimaa. (2020, September 6). Bypassing conditional access by faking device compliance. Retrieved
    March 4, 2022.
  source_name: AADInternals - Conditional Access Bypass
  url: https://o365blog.com/post/mdm
- description: 'Dr. Nestori Syynimaa. (2021, January 31). BPRT unleashed: Joining multiple devices to Azure AD and Intune.
    Retrieved March 4, 2022.'
  source_name: AADInternals - BPRT
  url: https://o365blog.com/post/bprt/
- description: Dr. Nestori Syynimaa. (2021, March 3). Deep-dive to Azure AD device join. Retrieved March 9, 2022.
  source_name: AADInternals - Device Registration
  url: https://o365blog.com/post/devices/
- description: 'Kelly Jackson Higgins. (2021, January 7). FireEye''s Mandia: ''Severity-Zero Alert'' Led to Discovery of SolarWinds
    Attack. Retrieved April 18, 2022.'
  source_name: DarkReading FireEye SolarWinds
  url: https://www.darkreading.com/threat-intelligence/fireeye-s-mandia-severity-zero-alert-led-to-discovery-of-solarwinds-attack
- description: 'Microsoft 365 Defender Threat Intelligence Team. (2022, January 26). Evolved phishing: Device registration
    trick adds to phishers’ toolbox for victims without MFA. Retrieved March 4, 2022.'
  source_name: Microsoft - Device Registration
  url: https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa
- description: Microsoft. (2022, March 22). DEV-0537 criminal actor targeting organizations for data exfiltration and destruction.
    Retrieved March 23, 2022.
  source_name: Microsoft DEV-0537
  url: https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/
id: attack-pattern--7decb26c-715c-40cf-b7e0-026f7d7cc215
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-05-22T21:02:06.575Z'
name: Device Registration
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Pawel Partyka, Microsoft 365 Defender
- Mike Moran
- Joe Gumke, U.S. Bank
- Arad Inbar, Fidelis Security
- Arun Seelagan, CISA
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- Identity Provider
x_mitre_version: '1.4'
```
