---
parsed_by: focuslocust
source: mitre
type: generated
---
# Steal or Forge Authentication Certificates

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1649` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Steal or Forge Authentication Certificates](../../attack/techniques/T1649-steal-or-forge-authentication-certificates.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1649 |
| name | Steal or Forge Authentication Certificates |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1649 |

## Preserved Source Material

```yaml
created: '2022-08-03T03:20:58.955Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital
  certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material.
  For example, Entra ID device certificates and Active Directory Certificate Services (AD CS) certificates bind to an identity
  and can be used as credentials for domain accounts.(Citation: O365 Blog Azure AD Device IDs)(Citation: Microsoft AD CS Overview)


  Authentication certificates can be both stolen and forged. For example, AD CS certificates can be stolen from encrypted
  storage (in the Registry or files)(Citation: APT29 Deep Look at Credential Roaming), misplaced certificate files (i.e. [Unsecured
  Credentials](https://attack.mitre.org/techniques/T1552)), or directly from the Windows certificate store via various crypto
  APIs.(Citation: SpecterOps Certified Pre Owned)(Citation: GitHub CertStealer)(Citation: GitHub GhostPack Certificates) With
  appropriate enrollment rights, users and/or machines within a domain can also request and/or manually renew certificates
  from enterprise certificate authorities (CA). This enrollment process defines various settings and permissions associated
  with the certificate. Of note, the certificate’s extended key usage (EKU) values define signing, encryption, and authentication
  use cases, while the certificate’s subject alternative name (SAN) values define the certificate owner’s alternate names.(Citation:
  Medium Certified Pre Owned)


  Abusing certificates for authentication credentials may enable other behaviors such as [Lateral Movement](https://attack.mitre.org/tactics/TA0008).
  Certificate-related misconfigurations may also enable opportunities for [Privilege Escalation](https://attack.mitre.org/tactics/TA0004),
  by way of allowing users to impersonate or assume privileged accounts or permissions via the identities (SANs) associated
  with a certificate. These abuses may also enable [Persistence](https://attack.mitre.org/tactics/TA0003) via stealing or
  forging certificates that can be used as [Valid Accounts](https://attack.mitre.org/techniques/T1078) for the duration of
  the certificate''s validity, despite user password resets. Authentication certificates can also be stolen and forged for
  machine accounts.


  Adversaries who have access to root (or subordinate) CA certificate private keys (or mechanisms protecting/managing these
  keys) may also establish [Persistence](https://attack.mitre.org/tactics/TA0003) by forging arbitrary authentication certificates
  for the victim domain (known as “golden” certificates).(Citation: Medium Certified Pre Owned) Adversaries may also target
  certificates and related services in order to access other forms of credentials, such as [Golden Ticket](https://attack.mitre.org/techniques/T1558/001)
  ticket-granting tickets (TGT) or NTLM plaintext.(Citation: Medium Certified Pre Owned)'
external_references:
- external_id: T1649
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1649
- description: HarmJ0y. (2018, August 22). SharpDPAPI - Certificates. Retrieved August 2, 2022.
  source_name: GitHub GhostPack Certificates
  url: https://github.com/GhostPack/SharpDPAPI#certificates
- description: Microsoft. (2016, August 31). Active Directory Certificate Services Overview. Retrieved August 2, 2022.
  source_name: Microsoft AD CS Overview
  url: https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831740(v=ws.11)
- description: Schroeder, W. (2021, June 17). Certified Pre-Owned. Retrieved August 2, 2022.
  source_name: Medium Certified Pre Owned
  url: https://posts.specterops.io/certified-pre-owned-d95910965cd2
- description: Schroeder, W. & Christensen, L. (2021, June 22). Certified Pre-Owned - Abusing Active Directory Certificate
    Services. Retrieved August 2, 2022.
  source_name: SpecterOps Certified Pre Owned
  url: https://web.archive.org/web/20220818094600/https://specterops.io/assets/resources/Certified_Pre-Owned.pdf
- description: Syynimaa, N. (2022, February 15). Stealing and faking Azure AD device identities. Retrieved August 3, 2022.
  source_name: O365 Blog Azure AD Device IDs
  url: https://o365blog.com/post/deviceidentity/
- description: TheWover. (2021, April 21). CertStealer. Retrieved August 2, 2022.
  source_name: GitHub CertStealer
  url: https://github.com/TheWover/CertStealer
- description: 'Thibault Van Geluwe De Berlaere. (2022, November 8). They See Me Roaming: Following APT29 by Taking a Deeper
    Look at Windows Credential Roaming. Retrieved November 9, 2022.'
  source_name: APT29 Deep Look at Credential Roaming
  url: https://www.mandiant.com/resources/blog/apt29-windows-credential-roaming
id: attack-pattern--7de1f7ac-5d0c-4c9c-8873-627202205331
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-04-15T23:12:50.646Z'
name: Steal or Forge Authentication Certificates
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Tristan Bennett, Seamless Intelligence
- Lee Christensen, SpecterOps
- Thirumalai Natarajan, Mandiant
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- Linux
- macOS
- Identity Provider
x_mitre_version: '1.2'
```
