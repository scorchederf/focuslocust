---
parsed_by: focuslocust
source: mitre
type: generated
---
# Downgrade Attack

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1689` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Downgrade Attack](../../attack/techniques/T1689-downgrade-attack.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1689 |
| name | Downgrade Attack |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1689 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:53:28.276Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does
  not support updated security controls. Downgrade attacks typically take advantage of a system’s backward compatibility to
  force it into less secure modes of operation.


  Adversaries may downgrade and use various less-secure versions of features of a system, such as [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)
  or even network protocols that can be abused to enable [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)
  or [Network Sniffing](https://attack.mitre.org/techniques/T1040).(Citation: Praetorian TLS Downgrade Attack 2014) For example,
  [PowerShell](https://attack.mitre.org/techniques/T1059/001) versions 5+ includes Script Block Logging (SBL), which can record
  executed script content. However, adversaries may attempt to execute a previous version of PowerShell that does not support
  SBL with the intent to impair defenses while running malicious scripts that may have otherwise been detected.(Citation:
  CrowdStrike downgrade attack)(Citation: Google Cloud downgrade attack)(Citation: att_def_ps_logging)


  Adversaries may similarly target network traffic to downgrade from an encrypted HTTPS connection to an unsecured HTTP connection
  that exposes network data in clear text.(Citation: Targeted SSL Stripping Attacks Are Real)(Citation: CrowdStrike Downgrade
  attack 2) On Windows systems, adversaries may downgrade the boot manager to a vulnerable version that bypasses Secure Boot,
  granting the ability to disable various operating system security mechanisms.(Citation: SafeBreach)'
external_references:
- external_id: T1689
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1689
- description: 'Alon Leviev. (2024, August 7). Windows Downdate: Downgrade Attacks Using Windows Updates. Retrieved January
    8, 2025.'
  source_name: SafeBreach
  url: https://www.safebreach.com/blog/downgrade-attacks-using-windows-updates/
- description: Bart Lenaerts-Bergmans. (2023, March 13). What are Downgrade Attacks?. Retrieved April 15, 2026.
  source_name: CrowdStrike Downgrade attack 2
  url: https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/downgrade-attack/
- description: Check Point. (n.d.). Targeted SSL Stripping Attacks Are Real. Retrieved May 24, 2023.
  source_name: Targeted SSL Stripping Attacks Are Real
  url: https://blog.checkpoint.com/research/targeted-ssl-stripping-attacks-are-real/amp/
- description: 'Falcon Complete Team. (2021, May 11). Response When Minutes Matter: Rising Up Against Ransomware. Retrieved
    April 15, 2026.'
  source_name: CrowdStrike downgrade attack
  url: https://www.crowdstrike.com/en-us/blog/how-falcon-complete-stopped-a-big-game-hunting-ransomware-attack/
- description: Hao, M. (2019, February 27). Attack and Defense Around PowerShell Event Logging. Retrieved November 24, 2021.
  source_name: att_def_ps_logging
  url: https://nsfocusglobal.com/attack-and-defense-around-powershell-event-logging/
- description: Nathan Kirk. (2018, June 18). Bring Your Own Land (BYOL) — A Novel Red Teaming Technique. Retrieved April 15,
    2026.
  source_name: Google Cloud downgrade attack
  url: https://cloud.google.com/blog/topics/threat-intelligence/bring-your-own-land-novel-red-teaming-technique/
- description: Praetorian. (2014, August 19). Man-in-the-Middle TLS Protocol Downgrade Attack. Retrieved October 8, 2021.
  source_name: Praetorian TLS Downgrade Attack 2014
  url: https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack/
id: attack-pattern--30904c16-39f9-41c6-b01a-500eb8878442
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:44:42.756Z'
name: Downgrade Attack
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Arad Inbar, Fidelis Security
- Daniel Feichter, @VirtualAllocEx, Infosec Tirol
- Mayuresh Dani, Qualys
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
- Windows
- Linux
x_mitre_version: '1.0'
```
