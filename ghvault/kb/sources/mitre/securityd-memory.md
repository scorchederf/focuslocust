---
parsed_by: focuslocust
source: mitre
type: generated
---
# Securityd Memory

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1555.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Securityd Memory](../../attack/techniques/T1555.002-securityd-memory.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1555.002 |
| name | Securityd Memory |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1555/002 |

## Preserved Source Material

```yaml
created: '2020-02-12T18:56:31.051Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary with root access may gather credentials by reading `securityd`’s memory. `securityd` is a service/daemon
  responsible for implementing security protocols such as encryption and authorization.(Citation: Apple Dev SecurityD) A privileged
  adversary may be able to scan through `securityd`''s memory to find the correct sequence of keys to decrypt the user’s logon
  keychain. This may provide the adversary with various plaintext passwords, such as those for users, WiFi, mail, browsers,
  certificates, secure notes, etc.(Citation: OS X Keychain)(Citation: OSX Keydnap malware)


  In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s
  keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords.(Citation:
  OS X Keychain)(Citation: External to DA, the OS X Way) Apple’s `securityd` utility takes the user’s logon password, encrypts
  it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s
  password, but once the master key is found, an adversary need only iterate over the other values to unlock the final password.(Citation:
  OS X Keychain)'
external_references:
- external_id: T1555.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1555/002
- description: Alex Rymdeko-Harvey, Steve Borosh. (2016, May 14). External to DA, the OS X Way. Retrieved September 12, 2024.
  source_name: External to DA, the OS X Way
  url: https://www.slideshare.net/slideshow/external-to-da-the-os-x-way/62021418
- description: Apple. (n.d.). Security Server and Security Agent. Retrieved March 29, 2024.
  source_name: Apple Dev SecurityD
  url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/Architecture/Architecture.html
- description: Juuso Salonen. (2012, September 5). Breaking into the OS X keychain. Retrieved November 17, 2024.
  source_name: OS X Keychain
  url: https://web.archive.org/web/20130106164109/https://juusosalonen.com/post/30923743427/breaking-into-the-os-x-keychain
- description: Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July
    3, 2017.
  source_name: OSX Keydnap malware
  url: https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/
id: attack-pattern--1a80d097-54df-41d8-9d33-34e755ec5e72
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:28.055Z'
name: Securityd Memory
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
x_mitre_version: '1.2'
```
