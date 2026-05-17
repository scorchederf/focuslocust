---
parsed_by: focuslocust
source: mitre
type: generated
---
# Remote Desktop Software

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1219.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Remote Desktop Software](../../attack/techniques/T1219.002-remote-desktop-software.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1219.002 |
| name | Remote Desktop Software |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1219/002 |

## Preserved Source Material

```yaml
created: '2025-03-24T22:24:47.684Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "An adversary may use legitimate desktop support software to establish an interactive command and control channel\
  \ to target systems within networks. Desktop support software provides a graphical interface for remotely controlling another\
  \ computer, transmitting the display output, keyboard input, and mouse control between devices using various protocols.\
  \ Desktop support software, such as `VNC`, `Team Viewer`, `AnyDesk`, `ScreenConnect`, `LogMein`, `AmmyyAdmin`, and other\
  \ remote monitoring and management (RMM) tools, are commonly used as legitimate technical support software and may be allowed\
  \ by application control within a target environment.(Citation: Symantec Living off the Land)(Citation: CrowdStrike 2015\
  \ Global Threat Report)(Citation: CrySyS Blog TeamSpy) \n \nRemote access modules/features may also exist as part of otherwise\
  \ existing software such as Zoom or Google Chrome’s Remote Desktop.(Citation: Google Chrome Remote Desktop)(Citation: Chrome\
  \ Remote Desktop) "
external_references:
- external_id: T1219.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1219/002
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
id: attack-pattern--d4287702-e2f7-4946-bdfa-2c7f5aaa5032
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-04-16T16:42:15.226Z'
name: Remote Desktop Software
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
