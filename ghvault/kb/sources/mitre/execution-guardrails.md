---
parsed_by: focuslocust
source: mitre
type: generated
---
# Execution Guardrails

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1480` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Execution Guardrails](../../attack/techniques/T1480-execution-guardrails.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1480 |
| name | Execution Guardrails |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1480 |

## Preserved Source Material

```yaml
created: '2019-01-31T02:10:08.261Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment
  specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against
  an intended target and reduces collateral damage from an adversary’s campaign.(Citation: FireEye Kevin Mandia Guardrails)
  Values an adversary can provide about a target system or environment to use as guardrails may include specific network share
  names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.(Citation:
  FireEye Outlook Dec 2019)


  Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated
  within. This use of guardrails is distinct from typical [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497).
  While use of [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) may involve checking for known
  sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for
  an expected target-specific value and only continuing with execution if there is such a match.


  Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims
  and platforms on which it will be most effective. A user-agent self-identifies data such as a user''s software application,
  operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only
  serve malware for the exploitable software while ignoring all other operating systems.(Citation: Trellix-Qakbot)'
external_references:
- external_id: T1480
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1480
- description: 'McWhirt, M., Carr, N., Bienstock, D. (2019, December 4). Breaking the Rules: A Tough Outlook for Home Page
    Attacks (CVE-2017-11774). Retrieved June 23, 2020.'
  source_name: FireEye Outlook Dec 2019
  url: https://www.fireeye.com/blog/threat-research/2019/12/breaking-the-rules-tough-outlook-for-home-page-attacks.html
- description: Pham Duy Phuc, John Fokker J.E., Alejandro Houspanossian and Mathanraj Thangaraju. (2023, March 7). Qakbot
    Evolves to OneNote Malware Distribution. Retrieved June 7, 2024.
  source_name: Trellix-Qakbot
  url: https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/
- description: Shoorbajee, Z. (2018, June 1). Playing nice? FireEye CEO says U.S. malware is more restrained than adversaries'.
    Retrieved January 17, 2019.
  source_name: FireEye Kevin Mandia Guardrails
  url: https://www.cyberscoop.com/kevin-mandia-fireeye-u-s-malware-nice/
id: attack-pattern--853c4192-4311-43e1-bfbb-b11b14911852
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:03:40.312Z'
name: Execution Guardrails
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Nick Carr, Mandiant
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
