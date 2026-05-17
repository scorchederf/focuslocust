---
parsed_by: focuslocust
source: mitre
type: generated
---
# Keychain

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1555.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Keychain](../../attack/techniques/T1555.001-keychain.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1555.001 |
| name | Keychain |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1555/001 |

## Preserved Source Material

```yaml
created: '2020-02-12T18:55:24.728Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management\
  \ system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and\
  \ secure notes. There are three types of Keychains: Login Keychain, System Keychain, and Local Items (iCloud) Keychain.\
  \ The default Keychain is the Login Keychain, which stores user passwords and information. The System Keychain stores items\
  \ accessed by the operating system, such as items shared among users on a host. The Local Items (iCloud) Keychain is used\
  \ for items synced with Apple’s iCloud service. \n\nKeychains can be viewed and edited through the Keychain Access application\
  \ or using the command-line utility <code>security</code>. Keychain files are located in <code>~/Library/Keychains/</code>,\
  \ <code>/Library/Keychains/</code>, and <code>/Network/Library/Keychains/</code>.(Citation: Keychain Services Apple)(Citation:\
  \ Keychain Decryption Passware)(Citation: OSX Keychain Schaumann)\n\nAdversaries may gather user credentials from Keychain\
  \ storage/memory. For example, the command <code>security dump-keychain –d</code> will dump all Login Keychain credentials\
  \ from <code>~/Library/Keychains/login.keychain-db</code>. Adversaries may also directly read Login Keychain credentials\
  \ from the <code>~/Library/Keychains/login.keychain</code> file. Both methods require a password, where the default password\
  \ for the Login Keychain is the current user’s password to login to the macOS host.(Citation: External to DA, the OS X Way)(Citation:\
  \ Empire Keychain Decrypt)  "
external_references:
- external_id: T1555.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1555/001
- description: Alex Rymdeko-Harvey, Steve Borosh. (2016, May 14). External to DA, the OS X Way. Retrieved September 12, 2024.
  source_name: External to DA, the OS X Way
  url: https://www.slideshare.net/slideshow/external-to-da-the-os-x-way/62021418
- description: Apple. (n.d.). Keychain Services. Retrieved April 11, 2022.
  source_name: Keychain Services Apple
  url: https://developer.apple.com/documentation/security/keychain_services
- description: Empire. (2018, March 8). Empire keychaindump_decrypt Module. Retrieved April 14, 2022.
  source_name: Empire Keychain Decrypt
  url: https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/lib/modules/python/collection/osx/keychaindump_decrypt.py
- description: Jan Schaumann. (2015, November 5). Using the OS X Keychain to store and retrieve passwords. Retrieved March
    31, 2022.
  source_name: OSX Keychain Schaumann
  url: https://www.netmeister.org/blog/keychain-passwords.html
- description: Yana Gourenko. (n.d.). A Deep Dive into Apple Keychain Decryption. Retrieved April 13, 2022.
  source_name: Keychain Decryption Passware
  url: https://support.passware.com/hc/en-us/articles/4573379868567-A-Deep-Dive-into-Apple-Keychain-Decryption
id: attack-pattern--1eaebf46-e361-4437-bc23-d5d65a3b92e3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:29.756Z'
name: Keychain
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
- macOS
x_mitre_version: '1.1'
```
