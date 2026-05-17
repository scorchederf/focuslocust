---
parsed_by: focuslocust
source: mitre
type: generated
---
# Command and Scripting Interpreter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Command and Scripting Interpreter](../../attack/techniques/T1059-command-and-scripting-interpreter.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1059 |
| name | Command and Scripting Interpreter |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1059 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:49.546Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces
  and languages provide ways of interacting with computer systems and are a common feature across many different platforms.
  Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions
  include some flavor of [Unix Shell](https://attack.mitre.org/techniques/T1059/004) while Windows installations include the
  [Windows Command Shell](https://attack.mitre.org/techniques/T1059/003) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).


  There are also cross-platform interpreters such as [Python](https://attack.mitre.org/techniques/T1059/006), as well as those
  commonly associated with client applications such as [JavaScript](https://attack.mitre.org/techniques/T1059/007) and [Visual
  Basic](https://attack.mitre.org/techniques/T1059/005).


  Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts
  can be embedded in [Initial Access](https://attack.mitre.org/tactics/TA0001) payloads delivered to victims as lure documents
  or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells,
  as well as utilize various [Remote Services](https://attack.mitre.org/techniques/T1021) in order to achieve remote Execution.(Citation:
  Powershell Remote Commands)(Citation: Cisco IOS Software Integrity Assurance - Command History)(Citation: Remote Shell Execution
  in Python)'
external_references:
- external_id: T1059
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1059
- description: Abdou Rockikz. (2020, July). How to Execute Shell Commands in a Remote Machine in Python. Retrieved July 26,
    2021.
  source_name: Remote Shell Execution in Python
  url: https://www.thepythoncode.com/article/executing-bash-commands-remotely-in-python
- description: Cisco. (n.d.). Cisco IOS Software Integrity Assurance - Command History. Retrieved October 21, 2020.
  source_name: Cisco IOS Software Integrity Assurance - Command History
  url: https://tools.cisco.com/security/center/resources/integrity_assurance.html#23
- description: Microsoft. (2020, August 21). Running Remote Commands. Retrieved July 26, 2021.
  source_name: Powershell Remote Commands
  url: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.1
id: attack-pattern--7385dfaf-6886-4229-9ecd-6fd678040830
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-01-27T20:03:38.098Z'
name: Command and Scripting Interpreter
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
- Containers
- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Network Devices
- Office Suite
- SaaS
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.7'
```
