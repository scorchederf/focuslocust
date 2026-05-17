---
parsed_by: focuslocust
source: mitre
type: generated
---
# Script Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0029` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Script Execution](../../attack/data-sources/DC0029-script-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0029 |
| name | Script Execution |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0029 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The execution of a text file that contains code via the interpreter.
external_references:
- external_id: DC0029
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0029
id: x-mitre-data-component--9f387817-df83-432a-b56b-a8fb7f71eedd
modified: '2025-11-12T22:03:39.105Z'
name: Script Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Script
- channel: VBA auto_open, auto_close, or document_open events
  name: m365:office
- channel: log stream --predicate 'eventMessage contains "python"'
  name: macos:unifiedlog
- channel: /var/log/syslog
  name: linux:syslog
- channel: EventCode=1502, 1503
  name: WinEventLog:System
- channel: log stream --predicate 'eventMessage contains "wscript" OR "vbs"'
  name: macos:unifiedlog
- channel: osascript or AppleScript invocation modifying UI
  name: macos:unifiedlog
- channel: runtime
  name: networkdevice:runtime
- channel: log
  name: macos:unifiedlog
- channel: boot
  name: esxi:vmkernel
- channel: AppleScript creating login item via 'System Events' dictionary
  name: macos:unifiedlog
- channel: EventCode=4103, 4104, 4105, 4106
  name: WinEventLog:PowerShell
- channel: Stored procedure creation, modification, or xp_cmdshell invocation via SQL logs or SQL Server auditing
  name: WinEventLog:Application
- channel: Stored procedure creation or modification with shell invocation (e.g., system(), exec())
  name: ApplicationLogs:SQL
- channel: subsystem=launchservices
  name: macos:unifiedlog
- channel: Set-ADUser or Set-ADAuthenticationPolicy with MFA attributes disabled
  name: WinEventLog:PowerShell
- channel: Process Tree + Script Block Logging
  name: EDR:scriptblock
- channel: boot logs
  name: linux:syslog
- channel: ScriptBlockLogging + AMSI
  name: m365:defender
- channel: log stream with predicate 'eventMessage CONTAINS "osascript"'
  name: macos:unifiedlog
- channel: Amsi/Script content + API verdicts during in-memory staging
  name: etw:Microsoft-Antimalware-Scan-Interface
- channel: None
  name: esxi:shell
- channel: EventCode=4016, 5312
  name: WinEventLog:System
- channel: scripting loop invoking sleep/ping
  name: auditd:PROCTITLE
- channel: Scripts with references to XML parsing, AES decryption, or gpprefdecrypt logic
  name: WinEventLog:PowerShell
- channel: system.log, asl.log
  name: macos:syslog
- channel: 'exec: Unexpected execution of osascript or AppleScript targeting sensitive apps'
  name: macos:osquery
- channel: subsystem=com.apple.Security or com.apple.applescript
  name: macos:unifiedlog
- channel: 'Microsoft.Compute/virtualMachines/runCommand/action: Abnormal initiation of Azure RunCommand jobs or PowerShell/Bash
    payloads'
  name: azure:activity
- channel: Malicious inline C#/script blobs embedded in MSBuild projects if intercepted by AMSI-aware loaders (rare but possible
    via chained LOLBins)
  name: EDR:AMSI
- channel: osascript, AppleScript, or Python execution triggered immediately after HID connection
  name: macos:unifiedlog
- channel: Scripted Activity
  name: m365:unified
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
