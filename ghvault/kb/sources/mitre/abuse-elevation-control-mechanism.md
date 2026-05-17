---
parsed_by: focuslocust
source: mitre
type: generated
---
# Abuse Elevation Control Mechanism

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1548` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Abuse Elevation Control Mechanism](../../attack/techniques/T1548-abuse-elevation-control-mechanism.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1548 |
| name | Abuse Elevation Control Mechanism |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1548 |

## Preserved Source Material

```yaml
created: '2020-01-30T13:58:14.373Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may circumvent mechanisms designed to control privilege elevation to gain higher-level permissions.
  Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform
  on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher
  risk.(Citation: TechNet How UAC Works)(Citation: sudo man page 2018) An adversary can perform several methods to take advantage
  of built-in control mechanisms in order to escalate privileges on a system.(Citation: OSX Keydnap malware)(Citation: Fortinet
  Fareit)'
external_references:
- external_id: T1548
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1548
- description: Lich, B. (2016, May 31). How User Account Control Works. Retrieved June 3, 2016.
  source_name: TechNet How UAC Works
  url: https://technet.microsoft.com/en-us/itpro/windows/keep-secure/how-user-account-control-works
- description: Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July
    3, 2017.
  source_name: OSX Keydnap malware
  url: https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/
- description: Salvio, J., Joven, R. (2016, December 16). Malicious Macro Bypasses UAC to Elevate Privilege for Fareit Malware.
    Retrieved December 27, 2016.
  source_name: Fortinet Fareit
  url: https://blog.fortinet.com/2016/12/16/malicious-macro-bypasses-uac-to-elevate-privilege-for-fareit-malware
- description: Todd C. Miller. (2018). Sudo Man Page. Retrieved March 19, 2018.
  source_name: sudo man page 2018
  url: https://www.sudo.ws/
id: attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-21T18:05:00.504Z'
name: Abuse Elevation Control Mechanism
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- IaaS
- Office Suite
- Identity Provider
x_mitre_version: '2.0'
```
