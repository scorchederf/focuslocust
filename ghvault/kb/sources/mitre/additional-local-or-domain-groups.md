---
parsed_by: focuslocust
source: mitre
type: generated
---
# Additional Local or Domain Groups

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1098.007` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Additional Local or Domain Groups](../../attack/techniques/T1098.007-additional-local-or-domain-groups.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1098.007 |
| name | Additional Local or Domain Groups |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1098/007 |

## Preserved Source Material

```yaml
created: '2024-08-05T20:49:49.809Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "An adversary may add additional local or domain groups to an adversary-controlled account to maintain persistent\
  \ access to a system or domain.\n\nOn Windows, accounts may use the `net localgroup` and `net group` commands to add existing\
  \ users to local and domain groups.(Citation: Microsoft Net Localgroup)(Citation: Microsoft Net Group) On Linux, adversaries\
  \ may use the `usermod` command for the same purpose.(Citation: Linux Usermod)\n\nFor example, accounts may be added to\
  \ the local administrators group on Windows devices to maintain elevated privileges. They may also be added to the Remote\
  \ Desktop Users group, which allows them to leverage [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001)\
  \ to log into the endpoints in the future.(Citation: Microsoft RDP Logons) Adversaries may also add accounts to VPN user\
  \ groups to gain future persistence on the network.(Citation: Cyber Security News) On Linux, accounts may be added to the\
  \ sudoers group, allowing them to persistently leverage [Sudo and Sudo Caching](https://attack.mitre.org/techniques/T1548/003)\
  \ for elevated privileges. \n\nIn Windows environments, machine accounts may also be added to domain groups. This allows\
  \ the local SYSTEM account to gain privileges on the domain.(Citation: RootDSE AD Detection 2022)"
external_references:
- external_id: T1098.007
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1098/007
- description: Kaaviya. (n.d.). SuperBlack Actors Exploiting Two Fortinet Vulnerabilities to Deploy Ransomware. Retrieved
    September 22, 2025.
  source_name: Cyber Security News
  url: https://cybersecuritynews.com/superblack-actors-exploiting-two-fortinet-vulnerabilities/
- description: Man7. (n.d.). Usermod. Retrieved August 5, 2024.
  source_name: Linux Usermod
  url: https://www.man7.org/linux/man-pages/man8/usermod.8.html
- description: Microsoft. (2016, August 31). Net group. Retrieved August 5, 2024.
  source_name: Microsoft Net Group
  url: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc754051(v=ws.11)
- description: Microsoft. (2016, August 31). Net Localgroup. Retrieved August 5, 2024.
  source_name: Microsoft Net Localgroup
  url: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc725622(v=ws.11)
- description: Microsoft. (2017, April 9). Allow log on through Remote Desktop Services. Retrieved August 5, 2024.
  source_name: Microsoft RDP Logons
  url: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services
- description: Scarred Monk. (2022, May 6). Real-time detection scenarios in Active Directory environments. Retrieved August
    5, 2024.
  source_name: RootDSE AD Detection 2022
  url: https://rootdse.org/posts/monitoring-realtime-activedirectory-domain-scenarios
id: attack-pattern--3e6831b2-bf4c-4ae6-b328-2e7c6633b291
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-09-26T18:25:02.290Z'
name: Additional Local or Domain Groups
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Madhukar Raina (Senior Security Researcher - Hack The Box, UK)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- macOS
- Linux
x_mitre_version: '1.1'
```
