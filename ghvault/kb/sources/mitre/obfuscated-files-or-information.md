---
parsed_by: focuslocust
source: mitre
type: generated
---
# Obfuscated Files or Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027 |
| name | Obfuscated Files or Information |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:32.662Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding,\
  \ or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different\
  \ platforms and the network to evade defenses. \n\nPayloads may be compressed, archived, or encrypted in order to avoid\
  \ detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action\
  \ may be required to open and [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) for [User\
  \ Execution](https://attack.mitre.org/techniques/T1204). The user may also be required to input a password to open a password\
  \ protected compressed/encrypted file that was provided by the adversary.(Citation: Volexity PowerDuke November 2016) Adversaries\
  \ may also use compressed or archived scripts, such as JavaScript. \n\nPortions of files can also be encoded to hide the\
  \ plain-text strings that would otherwise help defenders with discovery.(Citation: Linux/Cdorked.A We Live Security Analysis)\
  \ Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.(Citation:\
  \ Carbon Black Obfuscation Sept 2016)\n\nAdversaries may also abuse [Command Obfuscation](https://attack.mitre.org/techniques/T1027/010)\
  \ to obscure commands executed from payloads or directly via [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059).\
  \ Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature\
  \ based detections and application control mechanisms.(Citation: FireEye Obfuscation June 2017)(Citation: FireEye Revoke-Obfuscation\
  \ July 2017)(Citation: PaloAlto EncodedCommand March 2017) "
external_references:
- external_id: T1027
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027
- description: 'Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think
    Tanks and NGOs. Retrieved January 11, 2017.'
  source_name: Volexity PowerDuke November 2016
  url: https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/
- description: 'Bohannon, D. & Carr N. (2017, June 30). Obfuscation in the Wild: Targeted Attackers Lead the Way in Evasion
    Techniques. Retrieved February 12, 2018.'
  source_name: FireEye Obfuscation June 2017
  url: https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html
- description: 'Bohannon, D. & Holmes, L. (2017, July 27). Revoke-Obfuscation: PowerShell Obfuscation Detection Using Science.
    Retrieved November 17, 2024.'
  source_name: FireEye Revoke-Obfuscation July 2017
  url: https://www.blackhat.com/docs/us-17/thursday/us-17-Bohannon-Revoke-Obfuscation-PowerShell-Obfuscation-Detection-And%20Evasion-Using-Science-wp.pdf
- description: 'Pierre-Marc Bureau. (2013, April 26). Linux/Cdorked.A: New Apache backdoor being used in the wild to serve
    Blackhole. Retrieved September 10, 2017.'
  source_name: Linux/Cdorked.A We Live Security Analysis
  url: https://www.welivesecurity.com/2013/04/26/linuxcdorked-new-apache-backdoor-in-the-wild-serves-blackhole/
- description: Tedesco, B. (2016, September 23). Security Alert Summary. Retrieved February 12, 2018.
  source_name: Carbon Black Obfuscation Sept 2016
  url: https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/
- description: White, J. (2017, March 10). Pulling Back the Curtains on EncodedCommand PowerShell Attacks. Retrieved February
    12, 2018.
  source_name: PaloAlto EncodedCommand March 2017
  url: https://researchcenter.paloaltonetworks.com/2017/03/unit42-pulling-back-the-curtains-on-encodedcommand-powershell-attacks/
id: attack-pattern--b3d682b6-98f2-4fb0-aa3b-b4df007ca70a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:14:56.435Z'
name: Obfuscated Files or Information
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Christiaan Beek, @ChristiaanBeek
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
- Network Devices
- Windows
x_mitre_version: '2.0'
```
