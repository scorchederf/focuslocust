---
parsed_by: focuslocust
source: mitre
type: generated
---
# Deobfuscate／Decode Files or Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1140` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1140 |
| name | Deobfuscate／Decode Files or Information |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1140 |

## Preserved Source Material

```yaml
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027) to hide artifacts
  of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending
  on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present
  on the system.


  One such example is the use of [certutil](https://attack.mitre.org/software/S0160) to decode a remote access tool portable
  executable file that has been hidden inside a certificate file.(Citation: Malwarebytes Targeted Attack against Saudi Arabia)
  Another example is using the Windows <code>copy /b</code> or <code>type</code> command to reassemble binary fragments into
  a malicious payload.(Citation: Carbon Black Obfuscation Sept 2016)(Citation: Sentinel One Tainted Love 2023)


  Sometimes a user''s action may be required to open it for deobfuscation or decryption as part of [User Execution](https://attack.mitre.org/techniques/T1204).
  The user may also be required to input a password to open a password protected compressed/encrypted file that was provided
  by the adversary.(Citation: Volexity PowerDuke November 2016)'
external_references:
- external_id: T1140
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1140
- description: 'Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think
    Tanks and NGOs. Retrieved January 11, 2017.'
  source_name: Volexity PowerDuke November 2016
  url: https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/
- description: Aleksandar Milenkoski, Juan Andres Guerrero-Saade, and Joey Chen. (2023, March 23). Operation Tainted Love
    | Chinese APTs Target Telcos in New Attacks. Retrieved March 18, 2025.
  source_name: Sentinel One Tainted Love 2023
  url: https://www.sentinelone.com/labs/operation-tainted-love-chinese-apts-target-telcos-in-new-attacks/
- description: Malwarebytes Labs. (2017, March 27). New targeted attack against Saudi Arabia Government. Retrieved July 3,
    2017.
  source_name: Malwarebytes Targeted Attack against Saudi Arabia
  url: https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/
- description: Tedesco, B. (2016, September 23). Security Alert Summary. Retrieved February 12, 2018.
  source_name: Carbon Black Obfuscation Sept 2016
  url: https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/
id: attack-pattern--3ccef7ae-cb5e-48f6-8302-897105fbf55c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T19:58:25.069Z'
name: Deobfuscate/Decode Files or Information
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Cristóbal Martínez Martín
- Matthew Demaske, Adaptforward
- Red Canary
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
