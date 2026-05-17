---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Remote Management

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1021.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Remote Management](../../attack/techniques/T1021.006-windows-remote-management.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1021.006 |
| name | Windows Remote Management |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1021/006 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:29:47.757Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with remote systems
  using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.


  WinRM is the name of both a Windows service and a protocol that allows a user to interact with a remote system (e.g., run
  an executable, modify the Registry, modify services).(Citation: Microsoft WinRM) It may be called with the `winrm` command
  or by any number of programs such as PowerShell.(Citation: Jacobsen 2014) WinRM  can be used as a method of remotely interacting
  with [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047).(Citation: MSDN WMI)'
external_references:
- external_id: T1021.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1021/006
- description: French, D. (2018, September 30). Detecting Lateral Movement Using Sysmon and Splunk. Retrieved October 11,
    2019.
  source_name: Medium Detecting Lateral Movement
  url: https://medium.com/threatpunter/detecting-lateral-movement-using-sysmon-and-splunk-318d3be141bc
- description: Jacobsen, K. (2014, May 16). Lateral Movement with PowerShell&#91;slides&#93;. Retrieved November 12, 2014.
  source_name: Jacobsen 2014
  url: https://www.slideshare.net/kieranjacobsen/lateral-movement-with-power-shell-2
- description: Microsoft. (n.d.). Windows Management Instrumentation. Retrieved April 27, 2016.
  source_name: MSDN WMI
  url: https://msdn.microsoft.com/en-us/library/aa394582.aspx
- description: Microsoft. (n.d.). Windows Remote Management. Retrieved September 12, 2024.
  source_name: Microsoft WinRM
  url: https://learn.microsoft.com/en-us/windows/win32/winrm/portal
id: attack-pattern--60d0c01d-e2bf-49dd-a453-f8a9c9fa6f65
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2025-10-24T17:48:51.000Z'
name: Windows Remote Management
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
- Windows
x_mitre_version: '1.2'
```
