---
parsed_by: focuslocust
source: mitre
type: generated
---
# Remote Access Tools

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1219` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Remote Access Tools](../../attack/techniques/T1219-remote-access-tools.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1219 |
| name | Remote Access Tools |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1219 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may use legitimate remote access tools to establish an interactive command and control channel
  within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command
  line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard,
  Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically
  command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software
  permissions. This software is commonly used for troubleshooting, software installation, and system management.(Citation:
  Symantec Living off the Land)(Citation: CrowdStrike 2015 Global Threat Report)(Citation: CrySyS Blog TeamSpy) Adversaries
  may similarly abuse response features included in EDR and other defensive tools that enable remote access.


  Remote access tools may be installed and used post-compromise as an alternate communications channel for redundant access
  or to establish an interactive remote desktop session with the target system. It may also be used as a malware component
  to establish a reverse connection or back-connect to a service or adversary-controlled system.


  Installation of many remote access tools may also include persistence (e.g., the software''s installation routine creates
  a [Windows Service](https://attack.mitre.org/techniques/T1543/003)). Remote access modules/features may also exist as part
  of otherwise existing software (e.g., Google Chrome’s Remote Desktop).(Citation: Google Chrome Remote Desktop)(Citation:
  Chrome Remote Desktop)'
external_references:
- external_id: T1219
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1219
- description: CrowdStrike Intelligence. (2016). 2015 Global Threat Report. Retrieved April 11, 2018.
  source_name: CrowdStrike 2015 Global Threat Report
  url: https://go.crowdstrike.com/rs/281-OBQ-266/images/15GlobalThreatReport.pdf
- description: CrySyS Lab. (2013, March 20). TeamSpy – Obshie manevri. Ispolzovat’ tolko s razreshenija S-a. Retrieved April
    11, 2018.
  source_name: CrySyS Blog TeamSpy
  url: https://blog.crysys.hu/2013/03/teamspy/
- description: Google. (n.d.). Retrieved March 14, 2024.
  source_name: Google Chrome Remote Desktop
  url: https://support.google.com/chrome/answer/1649523
- description: Huntress. (n.d.). Retrieved March 14, 2024.
  source_name: Chrome Remote Desktop
  url: https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708
- description: Wueest, C., Anand, H. (2017, July). Living off the land and fileless attack techniques. Retrieved April 10,
    2018.
  source_name: Symantec Living off the Land
  url: https://www.symantec.com/content/dam/symantec/docs/security-center/white-papers/istr-living-off-the-land-and-fileless-attack-techniques-en.pdf
id: attack-pattern--4061e78c-1284-44b4-9116-73e4ac3912f7
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:48:42.154Z'
name: Remote Access Tools
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Matt Kelly, @breakersall
- Zachary Stanford, @svch0st
- Dray Agha, @Purp1eW0lf, Huntress Labs
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '3.0'
```
