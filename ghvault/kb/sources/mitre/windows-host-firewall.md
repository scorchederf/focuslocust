---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Host Firewall

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1686.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Host Firewall](../../attack/techniques/T1686.003-windows-host-firewall.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1686.003 |
| name | Windows Host Firewall |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1686/003 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:05.494Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may disable or modify the Windows host firewall to bypass controls limiting network usage. This
  can include disabling the Windows host firewall entirely, suppressing specific profiles (domain, private, public), or adding,
  deleting, and modifying firewall rules to allow or restrict traffic.(Citation: Nearest Neighbor Volexity)


  Adversaries may perform these modifications through multiple mechanisms depending on the Windows operating system and access
  level. For example, adversaries may use command-line utilities (e.g., `netsh advfirewall` or PowerShell cmdlets like `Set-NetFirewallProfile`,
  `New-NetFirewallRule`), Windows Registry modifications (e.g., altering firewall states and rule configurations via registry
  keys), or the Windows Control Panel to modify firewall settings through the Windows Security interface.


  By disabling or modifying Windows firewall services, adversaries may enable access to remote services, open ports for command
  and control traffic, or configure rules for further actions. '
external_references:
- external_id: T1686.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1686/003
- description: 'Koessel, Sean. Adair, Steven. Lancaster, Tom. (2024, November 22). The Nearest Neighbor Attack: How A Russian
    APT Weaponized Nearby Wi-Fi Networks for Covert Access. Retrieved February 25, 2025.'
  source_name: Nearest Neighbor Volexity
  url: https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/
id: attack-pattern--291ede6c-1473-454c-b614-5ac5ea63c987
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:39:19.227Z'
name: Windows Host Firewall
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.0'
```
