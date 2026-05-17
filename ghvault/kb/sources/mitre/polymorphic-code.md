---
parsed_by: focuslocust
source: mitre
type: generated
---
# Polymorphic Code

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.014` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Polymorphic Code](../../attack/techniques/T1027.014-polymorphic-code.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.014 |
| name | Polymorphic Code |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/014 |

## Preserved Source Material

```yaml
created: '2024-09-27T12:28:03.938Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may utilize polymorphic code (also known as metamorphic or mutating code) to evade detection. Polymorphic\
  \ code is a type of software capable of changing its runtime footprint during code execution.(Citation: polymorphic-blackberry)\
  \ With each execution of the software, the code is mutated into a different version of itself that achieves the same purpose\
  \ or objective as the original. This functionality enables the malware to evade traditional signature-based defenses, such\
  \ as antivirus and antimalware tools.(Citation: polymorphic-sentinelone) \nOther obfuscation techniques can be used in conjunction\
  \ with polymorphic code to accomplish the intended effects, including using mutation engines to conduct actions such as\
  \ [Software Packing](https://attack.mitre.org/techniques/T1027/002), [Command Obfuscation](https://attack.mitre.org/techniques/T1027/010),\
  \ or [Encrypted/Encoded File](https://attack.mitre.org/techniques/T1027/013).(Citation: polymorphic-linkedin)(Citation:\
  \ polymorphic-medium)\n"
external_references:
- external_id: T1027.014
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/014
- description: Blackberry. (n.d.). What is Polymorphic Malware?. Retrieved September 27, 2024.
  source_name: polymorphic-blackberry
  url: https://www.blackberry.com/us/en/solutions/endpoint-security/ransomware-protection/polymorphic-malware
- description: SentinelOne. (2023, March 18). What is Polymorphic Malware? Examples and Challenges. Retrieved September 27,
    2024.
  source_name: polymorphic-sentinelone
  url: https://www.sentinelone.com/cybersecurity-101/threat-intelligence/what-is-polymorphic-malware
- description: 'Shellseekercyber. (2024, January 7). Explainer: Packed Malware. Retrieved September 27, 2024.'
  source_name: polymorphic-medium
  url: https://medium.com/@shellseekerscyber/explainer-packed-malware-16f09cc75035
- description: 'Sherwin Akshay. (2024, May 28). Techniques for concealing malware and hindering analysis: Packing up and unpacking
    stuff. Retrieved September 27, 2024.'
  source_name: polymorphic-linkedin
  url: https://www.linkedin.com/pulse/techniques-concealing-malware-hindering-analysis-packing-akshay-unijc
id: attack-pattern--b577dfc1-0177-4522-8d5a-782127c8592b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:20:58.199Z'
name: Polymorphic Code
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- TruKno
- Ye Yint Min Thu Htut, Active Defense Team, DBS Bank
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
