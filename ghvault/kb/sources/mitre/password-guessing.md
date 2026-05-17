---
parsed_by: focuslocust
source: mitre
type: generated
---
# Password Guessing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1110.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password Guessing](../../attack/techniques/T1110.001-password-guessing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1110.001 |
| name | Password Guessing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1110/001 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:38:22.617Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries with no prior knowledge of legitimate credentials within the system or environment may guess passwords
  to attempt access to accounts. Without knowledge of the password for an account, an adversary may opt to systematically
  guess the password using a repetitive or iterative mechanism. An adversary may guess login credentials without prior knowledge
  of system or environment passwords during an operation by using a list of common passwords. Password guessing may or may
  not take into account the target''s policies on password complexity or use policies that may lock accounts out after a number
  of failed attempts.


  Guessing passwords can be a risky option because it could cause numerous authentication failures and account lockouts, depending
  on the organization''s login failure policies. (Citation: Cylance Cleaver)


  Typically, management services over commonly used ports are used when guessing passwords. Commonly targeted services include
  the following:


  * SSH (22/TCP)

  * Telnet (23/TCP)

  * FTP (21/TCP)

  * NetBIOS / SMB / Samba (139/TCP & 445/TCP)

  * LDAP (389/TCP)

  * Kerberos (88/TCP)

  * RDP / Terminal Services (3389/TCP)

  * HTTP/HTTP Management Services (80/TCP & 443/TCP)

  * MSSQL (1433/TCP)

  * Oracle (1521/TCP)

  * MySQL (3306/TCP)

  * VNC (5900/TCP)

  * SNMP (161/UDP and 162/TCP/UDP)


  In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing
  federated authentication protocols," as well as externally facing email applications, such as Office 365.(Citation: US-CERT
  TA18-068A 2018). Further, adversaries may abuse network device interfaces (such as `wlanAPI`) to brute force accessible
  wifi-router(s) via wireless authentication protocols.(Citation: Trend Micro Emotet 2020)


  In default environments, LDAP and Kerberos connection attempts are less likely to trigger events over SMB, which creates
  Windows "logon failure" event ID 4625.'
external_references:
- external_id: T1110.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1110/001
- description: Cybercrime & Digital Threat Team. (2020, February 13). Emotet Now Spreads via Wi-Fi. Retrieved February 16,
    2022.
  source_name: Trend Micro Emotet 2020
  url: https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/emotet-now-spreads-via-wi-fi
- description: Cylance. (2014, December). Operation Cleaver. Retrieved September 14, 2017.
  source_name: Cylance Cleaver
  url: https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf
- description: US-CERT. (2018, March 27). TA18-068A Brute Force Attacks Conducted by Cyber Actors. Retrieved October 2, 2019.
  source_name: US-CERT TA18-068A 2018
  url: https://www.us-cert.gov/ncas/alerts/TA18-086A
id: attack-pattern--09c4c11e-4fa1-4f8c-8dad-3cf8e69ad119
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:21.929Z'
name: Password Guessing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Microsoft Threat Intelligence Center (MSTIC)
- Mohamed Kmal
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Network Devices
- Office Suite
- SaaS
- Windows
x_mitre_version: '1.7'
```
