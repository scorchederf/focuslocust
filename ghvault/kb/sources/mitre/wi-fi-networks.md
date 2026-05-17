---
parsed_by: focuslocust
source: mitre
type: generated
---
# Wi-Fi Networks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1669` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Wi-Fi Networks](../../attack/techniques/T1669-wi-fi-networks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1669 |
| name | Wi-Fi Networks |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1669 |

## Preserved Source Material

```yaml
created: '2025-02-25T15:49:33.963Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may gain initial access to target systems by connecting to wireless networks. They may accomplish\
  \ this by exploiting open Wi-Fi networks used by target devices or by accessing secured Wi-Fi networks — requiring [Valid\
  \ Accounts](https://attack.mitre.org/techniques/T1078) — belonging to a target organization.(Citation: DOJ GRU Charges 2018)(Citation:\
  \ Nearest Neighbor Volexity) Establishing a connection to a Wi-Fi access point requires a certain level of proximity to\
  \ both discover and maintain a stable network connection. \n\nAdversaries may establish a wireless connection through various\
  \ methods, such as by physically positioning themselves near a Wi-Fi network to conduct close access operations. To bypass\
  \ the need for physical proximity, adversaries may attempt to remotely compromise nearby third-party systems that have both\
  \ wired and wireless network connections available (i.e., dual-homed systems). These third-party compromised devices can\
  \ then serve as a bridge to connect to a target’s Wi-Fi network.(Citation: Nearest Neighbor Volexity)\n\nOnce an initial\
  \ wireless connection is achieved, adversaries may leverage this access for follow-on activities in the victim network or\
  \ further targeting of specific devices on the network. Adversaries may perform [Network Sniffing](https://attack.mitre.org/techniques/T1040)\
  \ or [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) activities for [Credential Access](https://attack.mitre.org/tactics/TA0006)\
  \ or [Discovery](https://attack.mitre.org/tactics/TA0007)."
external_references:
- external_id: T1669
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1669
- description: 'Koessel, Sean. Adair, Steven. Lancaster, Tom. (2024, November 22). The Nearest Neighbor Attack: How A Russian
    APT Weaponized Nearby Wi-Fi Networks for Covert Access. Retrieved February 25, 2025.'
  source_name: Nearest Neighbor Volexity
  url: https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/
- description: U.S. Department of Justice. (2018, October 4). U.S. Charges Russian GRU Officers with International Hacking
    and Related Influence and Disinformation Operations. Retrieved February 25, 2025.
  source_name: DOJ GRU Charges 2018
  url: https://www.justice.gov/archives/opa/pr/us-charges-russian-gru-officers-international-hacking-and-related-influence-and
id: attack-pattern--fde016f6-211a-41c8-a4ab-301f1e419c62
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: initial-access
modified: '2025-04-15T19:59:24.690Z'
name: Wi-Fi Networks
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Cian Heasley
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Network Devices
- Windows
- macOS
x_mitre_version: '1.0'
```
