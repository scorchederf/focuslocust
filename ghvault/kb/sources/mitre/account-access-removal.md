---
parsed_by: focuslocust
source: mitre
type: generated
---
# Account Access Removal

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1531` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Account Access Removal](../../attack/techniques/T1531-account-access-removal.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1531 |
| name | Account Access Removal |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1531 |

## Preserved Source Material

```yaml
created: '2019-10-09T18:48:31.906Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized
  by legitimate users. Accounts may be deleted, locked, or manipulated (ex: changed credentials, revoked permissions for SaaS
  platforms such as Sharepoint) to remove access to accounts.(Citation: Obsidian Security SaaS Ransomware June 2023) Adversaries
  may also subsequently log off and/or perform a [System Shutdown/Reboot](https://attack.mitre.org/techniques/T1529) to set
  malicious changes into place.(Citation: CarbonBlack LockerGoga 2019)(Citation: Unit42 LockerGoga 2019)


  In Windows, [Net](https://attack.mitre.org/software/S0039) utility, <code>Set-LocalUser</code> and <code>Set-ADAccountPassword</code>
  [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlets may be used by adversaries to modify user accounts.
  Accounts could also be disabled by Group Policy. In Linux, the <code>passwd</code> utility may be used to change passwords.
  On ESXi servers, accounts can be removed or modified via esxcli (`system account set`, `system account remove`).


  Adversaries who use ransomware or similar attacks may first perform this and other Impact behaviors, such as [Data Destruction](https://attack.mitre.org/techniques/T1485)
  and [Defacement](https://attack.mitre.org/techniques/T1491), in order to impede incident response/recovery before completing
  the [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) objective. '
external_references:
- external_id: T1531
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1531
- description: CarbonBlack Threat Analysis Unit. (2019, March 22). TAU Threat Intelligence Notification – LockerGoga Ransomware.
    Retrieved April 16, 2019.
  source_name: CarbonBlack LockerGoga 2019
  url: https://www.carbonblack.com/2019/03/22/tau-threat-intelligence-notification-lockergoga-ransomware/
- description: Harbison, M. (2019, March 26). Born This Way? Origins of LockerGoga. Retrieved April 16, 2019.
  source_name: Unit42 LockerGoga 2019
  url: https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/
- description: Obsidian Threat Research Team. (2023, June 6). SaaS Ransomware Observed in the Wild for Sharepoint in Microsoft
    365. Retrieved October 5, 2025.
  source_name: Obsidian Security SaaS Ransomware June 2023
  url: https://web.archive.org/web/20230608061141/https://www.obsidiansecurity.com/blog/saas-ransomware-observed-sharepoint-microsoft-365/
id: attack-pattern--b24e2a20-3b3d-4bf0-823b-1ed765398fb0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-10-24T17:49:14.836Z'
name: Account Access Removal
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Hubert Mank
- Arun Seelagan, CISA
- Liran Ravich, CardinalOps
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- SaaS
- IaaS
- Office Suite
- ESXi
x_mitre_version: '1.5'
```
