---
parsed_by: focuslocust
source: mitre
type: generated
---
# Brute Force

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1110` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Brute Force](../../attack/techniques/T1110-brute-force.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1110 |
| name | Brute Force |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1110 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:22.767Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password\
  \ hashes are obtained.(Citation: TrendMicro Pawn Storm Dec 2020) Without knowledge of the password for an account or set\
  \ of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism.(Citation: Dragos\
  \ Crashoverride 2018) Brute forcing passwords can take place via interaction with a service that will check the validity\
  \ of those credentials or offline against previously acquired credential data, such as password hashes.\n\nBrute forcing\
  \ credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access\
  \ to [Valid Accounts](https://attack.mitre.org/techniques/T1078) within a victim environment leveraging knowledge gathered\
  \ from other post-compromise behaviors such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), [Account\
  \ Discovery](https://attack.mitre.org/techniques/T1087), or [Password Policy Discovery](https://attack.mitre.org/techniques/T1201).\
  \ Adversaries may also combine brute forcing activity with behaviors such as [External Remote Services](https://attack.mitre.org/techniques/T1133)\
  \ as part of Initial Access. \n\nIf an adversary guesses the correct password but fails to login to a compromised account\
  \ due to location-based conditional access policies, they may change their infrastructure until they match the victim’s\
  \ location and therefore bypass those policies.(Citation: ReliaQuest Health Care Social Engineering Campaign 2024)"
external_references:
- external_id: T1110
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1110
- description: Hacquebord, F., Remorin, L. (2020, December 17). Pawn Storm’s Lack of Sophistication as a Strategy. Retrieved
    January 13, 2021.
  source_name: TrendMicro Pawn Storm Dec 2020
  url: https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html
- description: Hayden Evans. (2024, April 4). Health Care Social Engineering Campaign. Retrieved May 22, 2025.
  source_name: ReliaQuest Health Care Social Engineering Campaign 2024
  url: https://www.reliaquest.com/blog/health-care-social-engineering-campaign/
- description: 'Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December
    18, 2020.'
  source_name: Dragos Crashoverride 2018
  url: https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf
id: attack-pattern--a93494bb-4b80-4ea1-8695-3236a49916fd
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:12.218Z'
name: Brute Force
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- David Fiser, @anu4is, Trend Micro
- Alfredo Oliveira, Trend Micro
- Magno Logan, @magnologan, Trend Micro
- Yossi Weizman, Azure Defender Research Team
- Ed Williams, Trustwave, SpiderLabs
- Mohamed Kmal
- ReliaQuest
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
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
x_mitre_version: '2.8'
```
