---
parsed_by: focuslocust
source: mitre
type: generated
---
# Compression

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.015` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Compression](../../attack/techniques/T1027.015-compression.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.015 |
| name | Compression |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/015 |

## Preserved Source Material

```yaml
created: '2025-03-04T18:29:33.850Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use compression to obfuscate their payloads or files. Compressed file formats such as ZIP, gzip,
  7z, and RAR can compress and archive multiple files together to make it easier and faster to transfer files. In addition
  to compressing files, adversaries may also compress shellcode directly - for example, in order to store it in a Windows
  Registry key (i.e., [Fileless Storage](https://attack.mitre.org/techniques/T1027/011)).(Citation: Trustwave Pillowmint June
  2020)


  In order to further evade detection, adversaries may combine multiple ZIP files into one archive. This process of concatenation
  creates an archive that appears to be a single archive but in fact contains the central directories of the embedded archives.
  Some ZIP readers, such as 7zip, may not be able to identify concatenated ZIP files and miss the presence of the malicious
  payload.(Citation: Perception Point)


  File archives may be sent as one [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) through email.
  Adversaries have sent malicious payloads as archived files to encourage the user to interact with and extract the malicious
  payload onto their system (i.e., [Malicious File](https://attack.mitre.org/techniques/T1204/002)).(Citation: NTT Security
  Flagpro new December 2021) However, some file compression tools, such as 7zip, can be used to produce self-extracting archives.
  Adversaries may send self-extracting archives to hide the functionality of their payload and launch it without requiring
  multiple actions from the user.(Citation: The Hacker News)


  [Compression](https://attack.mitre.org/techniques/T1027/015) may be used in combination with [Encrypted/Encoded File](https://attack.mitre.org/techniques/T1027/013)
  where compressed files are encrypted and password-protected.'
external_references:
- external_id: T1027.015
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/015
- description: 'Arthur Vaiselbuh, Peleg Cabra. (2024, November 7). Evasive ZIP Concatenation: Trojan Targets Windows Users.
    Retrieved March 3, 2025.'
  source_name: Perception Point
  url: https://perception-point.io/blog/evasive-concatenated-zip-trojan-targets-windows-users/
- description: Hada, H. (2021, December 28).  Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.
  source_name: NTT Security Flagpro new December 2021
  url: https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech
- description: Ravie Lakshmanan. (2023, April 5). Hackers Using Self-Extracting Archives Exploit for Stealthy Backdoor Attacks.
    Retrieved March 3, 2025.
  source_name: The Hacker News
  url: https://thehackernews.com/2023/04/hackers-using-self-extracting-archives.html
- description: 'Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.'
  source_name: Trustwave Pillowmint June 2020
  url: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/
id: attack-pattern--fbd91bfc-75c2-4f0c-8116-3b4e722906b3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:16:53.338Z'
name: Compression
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Fernando Bacchin
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
