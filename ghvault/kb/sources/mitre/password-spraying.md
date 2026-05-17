---
parsed_by: focuslocust
source: mitre
type: generated
---
# Password Spraying

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1110.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password Spraying](../../attack/techniques/T1110.003-password-spraying.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1110.003 |
| name | Password Spraying |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1110/003 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:39:25.122Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use a single or small list of commonly used passwords against many different accounts to attempt
  to acquire valid account credentials. Password spraying uses one password (e.g. ''Password01''), or a small list of commonly
  used passwords, that may match the complexity policy of the domain. Logins are attempted with that password against many
  different accounts on a network to avoid account lockouts that would normally occur when brute forcing a single account
  with many passwords. (Citation: BlackHillsInfosec Password Spraying)


  Typically, management services over commonly used ports are used when password spraying. Commonly targeted services include
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


  In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing
  federated authentication protocols," as well as externally facing email applications, such as Office 365.(Citation: US-CERT
  TA18-068A 2018)


  In order to avoid detection thresholds, adversaries may deliberately throttle password spraying attempts to avoid triggering
  security alerting. Additionally, adversaries may leverage LDAP and Kerberos authentication attempts, which are less likely
  to trigger high-visibility events such as Windows "logon failure" event ID 4625 that is commonly triggered by failed SMB
  connection attempts.(Citation: Microsoft Storm-0940)  '
external_references:
- external_id: T1110.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1110/003
- description: 'Metcalf, S. (2018, May 6). Trimarc Research: Detecting Password Spraying with Security Event Auditing. Retrieved
    January 16, 2019.'
  source_name: Trimarc Detecting Password Spraying
  url: https://www.trimarcsecurity.com/single-post/2018/05/06/Trimarc-Research-Detecting-Password-Spraying-with-Security-Event-Auditing
- description: Microsoft Threat Intelligence. (2024, October 31). Chinese threat actor Storm-0940 uses credentials from password
    spray attacks from a covert network. Retrieved June 4, 2025.
  source_name: Microsoft Storm-0940
  url: https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/
- description: Thyer, J. (2015, October 30). Password Spraying & Other Fun with RPCCLIENT. Retrieved April 25, 2017.
  source_name: BlackHillsInfosec Password Spraying
  url: http://www.blackhillsinfosec.com/?p=4645
- description: US-CERT. (2018, March 27). TA18-068A Brute Force Attacks Conducted by Cyber Actors. Retrieved October 2, 2019.
  source_name: US-CERT TA18-068A 2018
  url: https://www.us-cert.gov/ncas/alerts/TA18-086A
id: attack-pattern--692074ae-bb62-4a5e-a735-02cb6bde458c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:53.996Z'
name: Password Spraying
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Microsoft Threat Intelligence Center (MSTIC)
- John Strand
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
- Network Devices
- Office Suite
- SaaS
- Windows
- macOS
x_mitre_version: '1.8'
```
