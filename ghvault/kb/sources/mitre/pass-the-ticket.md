---
parsed_by: focuslocust
source: mitre
type: generated
---
# Pass the Ticket

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1550.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pass the Ticket](../../attack/techniques/T1550.003-pass-the-ticket.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1550.003 |
| name | Pass the Ticket |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1550/003 |

## Preserved Source Material

```yaml
created: '2020-01-30T17:03:43.072Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may “pass the ticket” using stolen Kerberos tickets to move laterally within an environment, bypassing
  normal system access controls. Pass the ticket (PtT) is a method of authenticating to a system using Kerberos tickets without
  having access to an account''s password. Kerberos authentication can be used as the first step to lateral movement to a
  remote system.


  When preforming PtT, valid Kerberos tickets for [Valid Accounts](https://attack.mitre.org/techniques/T1078) are captured
  by [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). A user''s service tickets or ticket granting ticket
  (TGT) may be obtained, depending on the level of access. A service ticket allows for access to a particular resource, whereas
  a TGT can be used to request service tickets from the Ticket Granting Service (TGS) to access any resource the user has
  privileges to access.(Citation: ADSecurity AD Kerberos Attacks)(Citation: GentilKiwi Pass the Ticket)


  A [Silver Ticket](https://attack.mitre.org/techniques/T1558/002) can be obtained for services that use Kerberos as an authentication
  mechanism and are used to generate tickets to access that particular resource and the system that hosts the resource (e.g.,
  SharePoint).(Citation: ADSecurity AD Kerberos Attacks)


  A [Golden Ticket](https://attack.mitre.org/techniques/T1558/001) can be obtained for the domain using the Key Distribution
  Service account KRBTGT account NTLM hash, which enables generation of TGTs for any account in Active Directory.(Citation:
  Campbell 2014)


  Adversaries may also create a valid Kerberos ticket using other user information, such as stolen password hashes or AES
  keys. For example, "overpassing the hash" involves using a NTLM password hash to authenticate as a user (i.e. [Pass the
  Hash](https://attack.mitre.org/techniques/T1550/002)) while also using the password hash to create a valid Kerberos ticket.(Citation:
  Stealthbits Overpass-the-Hash)'
external_references:
- external_id: T1550.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1550/003
- description: Campbell, C. (2014). The Secret Life of Krbtgt. Retrieved November 17, 2024.
  source_name: Campbell 2014
  url: https://defcon.org/images/defcon-22/dc-22-presentations/Campbell/DEFCON-22-Christopher-Campbell-The-Secret-Life-of-Krbtgt.pdf
- description: Deply, B. (2014, January 13). Pass the ticket. Retrieved September 12, 2024.
  source_name: GentilKiwi Pass the Ticket
  url: https://web.archive.org/web/20210515214027/https://blog.gentilkiwi.com/securite/mimikatz/pass-the-ticket-kerberos
- description: Metcalf, S. (2014, November 22). Mimikatz and Active Directory Kerberos Attacks. Retrieved June 2, 2016.
  source_name: ADSecurity AD Kerberos Attacks
  url: https://adsecurity.org/?p=556
- description: Warren, J. (2019, February 26). How to Detect Overpass-the-Hash Attacks. Retrieved February 4, 2021.
  source_name: Stealthbits Overpass-the-Hash
  url: https://stealthbits.com/blog/how-to-detect-overpass-the-hash-attacks/
id: attack-pattern--7b211ac6-c815-4189-93a9-ab415deca926
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2026-04-15T22:47:57.805Z'
name: Pass the Ticket
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Ryan Becwar
- Vincent Le Toux
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
