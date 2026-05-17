---
parsed_by: focuslocust
source: mitre
type: generated
---
# Disable or Modify Windows Event Log

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1685.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Disable or Modify Windows Event Log](../../attack/techniques/T1685.001-disable-or-modify-windows-event-log.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1685.001 |
| name | Disable or Modify Windows Event Log |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1685/001 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:01.982Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may disable or modify the Windows Event Log to limit data that can be leveraged for detections and\
  \ audits. Windows Event Log records user and system activity such as login attempts and process creation.(Citation: EventLog_Core_Technologies)\
  \ This data is used by security tools and analysts to generate detections. \n\nThe EventLog service maintains event logs\
  \ from various system components and applications. By default, the service automatically starts when a system powers on.\
  \ An audit policy, maintained by the Local Security Policy (secpol.msc), defines which system events the EventLog service\
  \ logs. Security audit policy settings can be changed by running secpol.msc, then navigating to `Security Settings\\Local\
  \ Policies\\Audit Policy` for basic audit policy settings or `Security Settings\\Advanced Audit Policy Configuration` for\
  \ advanced audit policy settings.(Citation: Microsoft Audit Policy)(Citation: Microsoft Adv Security Settings) `auditpol.exe`\
  \ may also be used to set audit policies.(Citation: Microsoft auditpol)\n\nAdversaries may target system-wide logging or\
  \ just that of a particular application. For example, the Windows EventLog service may be disabled using the `Set-Service\
  \ -Name EventLog -Status Stopped` or `sc config eventlog start=disabled` commands (followed by manually stopping the service\
  \ using `Stop-Service -Name EventLog`). Additionally, the service may be disabled by modifying the \"Start\" value in `HKEY_LOCAL_MACHINE\\\
  SYSTEM\\CurrentControlSet\\Services\\EventLog` then restarting the system for the change to take effect.(Citation: Disable_Win_Event_Logging)(Citation:\
  \ disable_win_evt_logging)\n\nThere are several ways to disable the EventLog service via registry key modification. Without\
  \ Administrator privileges, adversaries may modify the \"Start\" value in the key `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\\
  Control\\WMI\\Autologger\\EventLog-Security`, then reboot the system to disable the Security EventLog.(Citation: winser19_file_overwrite_bug_twitter)\
  \ With Administrator privilege, adversaries may modify the same values in `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\\
  Control\\WMI\\Autologger\\EventLog-System` and `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Autologger\\\
  EventLog-Application` to disable the entire EventLog.\n\nAdditionally, adversaries may use `auditpol` and its sub-commands\
  \ in a command prompt to disable auditing or clear the audit policy. To enable or disable a specified setting or audit category,\
  \ adversaries may use the `/success` or `/failure` parameters. For example, `auditpol /set /category:\"Account Logon\" /success:disable\
  \ /failure:disable` turns off auditing for the Account Logon category.(Citation: auditpol.exe_STRONTIC) To clear the audit\
  \ policy, adversaries may run the following lines: `auditpol /clear /y` or `auditpol /remove /allusers`.(Citation: T1562.002_redcanaryco)"
external_references:
- external_id: T1685.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1685/001
- description: ' dmcxblue. (n.d.). Disable Windows Event Logging. Retrieved September 10, 2021.'
  source_name: Disable_Win_Event_Logging
  url: https://dmcxblue.gitbook.io/red-team-notes-2-0/red-team-techniques/defense-evasion/t1562-impair-defenses/disable-windows-event-logging
- description: 'Core Technologies. (2021, May 24). Essential Windows Services: EventLog / Windows Event Log. Retrieved September
    14, 2021.'
  source_name: EventLog_Core_Technologies
  url: https://www.coretechnologies.com/blog/windows-services/eventlog/
- description: 'Heiligenstein, L. (n.d.). REP-25: Disable Windows Event Logging. Retrieved April 7, 2022.'
  source_name: disable_win_evt_logging
  url: https://ptylu.github.io/content/report/report.html?report=25
- description: Microsoft. (n.d.). Retrieved April 15, 2026.
  source_name: Microsoft Audit Policy
  url: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/audit-policy
- description: Microsoft. (n.d.). Retrieved April 15, 2026.
  source_name: Microsoft Adv Security Settings
  url: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/advanced-security-audit-policy-settings
- description: Microsoft. (n.d.). Retrieved April 15, 2026.
  source_name: Microsoft auditpol
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol
- description: Naceri, A. (2021, November 7). Windows Server 2019 file overwrite bug. Retrieved April 7, 2022.
  source_name: winser19_file_overwrite_bug_twitter
  url: https://web.archive.org/web/20211107115646/https://twitter.com/klinix5/status/1457316029114327040
- description: redcanaryco. (2021, September 3). T1562.002 - Disable Windows Event Logging. Retrieved September 13, 2021.
  source_name: T1562.002_redcanaryco
  url: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.md
- description: STRONTIC. (n.d.). auditpol.exe. Retrieved September 9, 2021.
  source_name: auditpol.exe_STRONTIC
  url: https://strontic.github.io/xcyclopedia/library/auditpol.exe-214E0EA1F7F7C27C82D23F183F9D23F1.html
id: attack-pattern--1411e6b8-80a6-4465-9909-54eaa9c67ce0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:43:20.588Z'
name: Disable or Modify Windows Event Log
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Lucas Heiligenstein
- Prasanth Sadanala, Cigna Information Protection (CIP) - Threat Response Engineering Team
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.0'
```
