---
parsed_by: focuslocust
source: mitre
type: generated
---
# Clear Windows Event Logs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1685.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Clear Windows Event Logs](../../attack/techniques/T1685.005-clear-windows-event-logs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1685.005 |
| name | Clear Windows Event Logs |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1685/005 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:03.796Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may clear Windows Event Logs to hide the activity of an intrusion. Windows Event Logs are a record
  of a computer''s alerts and notifications. There are three system-defined sources of events: System, Application, and Security,
  with five event types: Error, Warning, Information, Success Audit, and Failure Audit.


  With administrator privileges, the event logs can be cleared with the following utility commands:


  * `wevtutil cl system`

  * `wevtutil cl application`

  * `wevtutil cl security`


  These logs may also be cleared through other mechanisms, such as the event viewer GUI or [PowerShell](https://attack.mitre.org/techniques/T1059/001).
  For example, adversaries may use the PowerShell command `Remove-EventLog -LogName Security` to delete the Security EventLog
  and after reboot, disable future logging. Note: events may still be generated and logged in the .evtx file between the time
  the command is run and the reboot.(Citation: disable_win_evt_logging)


  Adversaries may also attempt to clear logs by directly deleting the stored log files within `C:\Windows\System32\winevt\logs\`.'
external_references:
- external_id: T1685.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1685/005
- description: 'Heiligenstein, L. (n.d.). REP-25: Disable Windows Event Logging. Retrieved April 7, 2022.'
  source_name: disable_win_evt_logging
  url: https://ptylu.github.io/content/report/report.html?report=25
id: attack-pattern--75b9a4d2-d4e2-4ca1-9aab-1badd9e05fd0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:41:59.512Z'
name: Clear Windows Event Logs
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Lucas Heiligenstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.0'
```
