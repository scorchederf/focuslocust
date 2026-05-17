---
parsed_by: focuslocust
source: mitre
type: generated
---
# Path Interception by Unquoted Path

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Path Interception by Unquoted Path](../../attack/techniques/T1574.009-path-interception-by-unquoted-path.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574.009 |
| name | Path Interception by Unquoted Path |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574/009 |

## Preserved Source Material

```yaml
created: '2020-03-13T13:51:58.519Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute their own malicious payloads by hijacking vulnerable file path references. Adversaries
  can take advantage of paths that lack surrounding quotations by placing an executable in a higher level directory within
  the path, so that Windows will choose the adversary''s executable to launch.


  Service paths (Citation: Microsoft CurrentControlSet Services) and shortcut paths may also be vulnerable to path interception
  if the path has one or more spaces and is not surrounded by quotation marks (e.g., <code>C:\unsafe path with space\program.exe</code>
  vs. <code>"C:\safe path with space\program.exe"</code>). (Citation: Help eliminate unquoted path) (stored in Windows Registry
  keys) An adversary can place an executable in a higher level directory of the path, and Windows will resolve that executable
  instead of the intended executable. For example, if the path in a shortcut is <code>C:\program files\myapp.exe</code>, an
  adversary may create a program at <code>C:\program.exe</code> that will be run instead of the intended program. (Citation:
  Windows Unquoted Services) (Citation: Windows Privilege Escalation Guide)


  This technique can be used for persistence if executables are called on a regular basis, as well as privilege escalation
  if intercepted executables are started by a higher privileged process.'
external_references:
- external_id: T1574.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574/009
- description: absolomb. (2018, January 26). Windows Privilege Escalation Guide. Retrieved August 10, 2018.
  source_name: Windows Privilege Escalation Guide
  url: https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/
- description: HackHappy. (2018, April 23). Windows Privilege Escalation – Unquoted Services. Retrieved August 10, 2018.
  source_name: Windows Unquoted Services
  url: https://securityboulevard.com/2018/04/windows-privilege-escalation-unquoted-services/
- description: Mark Baggett. (2012, November 8). Help eliminate unquoted path vulnerabilities. Retrieved November 8, 2012.
  source_name: Help eliminate unquoted path
  url: https://isc.sans.edu/diary/Help+eliminate+unquoted+path+vulnerabilities/14464
- description: Microsoft. (2017, April 20). HKLM\SYSTEM\CurrentControlSet\Services Registry Tree. Retrieved March 16, 2020.
  source_name: Microsoft CurrentControlSet Services
  url: https://docs.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree
id: attack-pattern--bf96a5a3-3bce-43b7-8597-88545984c07b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T23:01:45.477Z'
name: Path Interception by Unquoted Path
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Stefan Kanthak
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
