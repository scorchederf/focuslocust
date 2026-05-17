---
parsed_by: focuslocust
source: mitre
type: generated
---
# Credential Stuffing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1110.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Credential Stuffing](../../attack/techniques/T1110.004-credential-stuffing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1110.004 |
| name | Credential Stuffing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1110/004 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:39:59.959Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use credentials obtained from breach dumps of unrelated accounts to gain access to target accounts
  through credential overlap. Occasionally, large numbers of username and password pairs are dumped online when a website
  or service is compromised and the user account credentials accessed. The information may be useful to an adversary attempting
  to compromise accounts by taking advantage of the tendency for users to use the same passwords across personal and business
  accounts.


  Credential stuffing is a risky option because it could cause numerous authentication failures and account lockouts, depending
  on the organization''s login failure policies.


  Typically, management services over commonly used ports are used when stuffing credentials. Commonly targeted services include
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
  TA18-068A 2018)'
external_references:
- external_id: T1110.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1110/004
- description: US-CERT. (2018, March 27). TA18-068A Brute Force Attacks Conducted by Cyber Actors. Retrieved October 2, 2019.
  source_name: US-CERT TA18-068A 2018
  url: https://www.us-cert.gov/ncas/alerts/TA18-086A
id: attack-pattern--b2d03cea-aec1-45ca-9744-9ee583c1e1cc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:14.923Z'
name: Credential Stuffing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Diogo Fernandes
- Anastasios Pingios
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
