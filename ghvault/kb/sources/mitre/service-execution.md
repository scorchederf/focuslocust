---
parsed_by: focuslocust
source: mitre
type: generated
---
# Service Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1569.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Service Execution](../../attack/techniques/T1569.002-service-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1569.002 |
| name | Service Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1569/002 |

## Preserved Source Material

```yaml
created: '2020-03-10T18:33:36.159Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse the Windows service control manager to execute malicious commands or payloads. The Windows
  service control manager (<code>services.exe</code>) is an interface to manage and manipulate services.(Citation: Microsoft
  Service Control Manager) The service control manager is accessible to users via GUI components as well as system utilities
  such as <code>sc.exe</code> and [Net](https://attack.mitre.org/software/S0039).


  [PsExec](https://attack.mitre.org/software/S0029) can also be used to execute commands or payloads via a temporary Windows
  service created through the service control manager API.(Citation: Russinovich Sysinternals) Tools such as [PsExec](https://attack.mitre.org/software/S0029)
  and <code>sc.exe</code> can accept remote servers as arguments and may be used to conduct remote execution.


  Adversaries may leverage these mechanisms to execute malicious content. This can be done by either executing a new or modified
  service. This technique is the execution used in conjunction with [Windows Service](https://attack.mitre.org/techniques/T1543/003)
  during service persistence or privilege escalation.'
external_references:
- external_id: T1569.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1569/002
- description: Microsoft. (2018, May 31). Service Control Manager. Retrieved March 28, 2020.
  source_name: Microsoft Service Control Manager
  url: https://docs.microsoft.com/windows/win32/services/service-control-manager
- description: Russinovich, M. (2014, May 2). Windows Sysinternals PsExec v2.11. Retrieved May 13, 2015.
  source_name: Russinovich Sysinternals
  url: https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx
id: attack-pattern--f1951e8a-500e-4a26-8803-76d95c4554b4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:49:35.506Z'
name: Service Execution
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
x_mitre_remote_support: false
x_mitre_version: '1.3'
```
