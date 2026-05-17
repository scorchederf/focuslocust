---
parsed_by: focuslocust
source: mitre
type: generated
---
# Prevent Command History Logging

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1690` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Prevent Command History Logging](../../attack/techniques/T1690-prevent-command-history-logging.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1690 |
| name | Prevent Command History Logging |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1690 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:53:28.653Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may impair command history logging to hide commands they run on a compromised system. Various command
  interpreters keep track of the commands users type in their terminal so that users can retrace what they have done.


  On Linux and macOS, command history is tracked in a file pointed to by the environment variable `HISTFILE`. When a user
  logs off a system, this information is flushed to a file in the user''s home directory called `~/.bash_history`. The `HISTCONTROL`
  environment variable keeps track of what should be saved by the history command and eventually into the `~/.bash_history`
  file when a user logs out. `HISTCONTROL` does not exist by default on macOS, but can be set by the user and will be respected.
  The `HISTFILE` environment variable is also used in some ESXi systems.(Citation: Google Cloud Threat Intelligence ESXi VIBs
  2022)


  Adversaries may clear the history environment variable (`unset HISTFILE`) or set the command history size to zero (`export
  HISTFILESIZE=0`) to prevent logging of commands. Additionally, `HISTCONTROL` can be configured to ignore commands that start
  with a space by simply setting it to "ignorespace". `HISTCONTROL` can also be set to ignore duplicate commands by setting
  it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples.
  This means that " ls" will not be saved, but "ls" would be saved by history. Adversaries can abuse this to operate without
  leaving traces by simply prepending a space to all of their terminal commands.


  On Windows systems, the `PSReadLine` module tracks commands used in all PowerShell sessions and writes them to a file (`$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`
  by default). Adversaries may change where these logs are saved using `Set-PSReadLineOption -HistorySavePath {File Path}`.
  This will cause `ConsoleHost_history.txt` to stop receiving logs. Additionally, it is possible to turn off logging to this
  file using the PowerShell command `Set-PSReadlineOption -HistorySaveStyle SaveNothing`.(Citation: Microsoft about_History
  prevent command history)(Citation: Sophos PowerShell Command History Forensics)


  Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to
  disable historical command logging (e.g. `no logging`).'
external_references:
- external_id: T1690
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1690
- description: 'Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part
    One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.'
  source_name: Google Cloud Threat Intelligence ESXi VIBs 2022
  url: https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- description: Microsoft. (n.d.). Retrieved April 15, 2026.
  source_name: Microsoft about_History prevent command history
  url: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7.6&viewFallbackFrom=powershell-7
- description: Vikas, S. (2020, August 26). PowerShell Command History Forensics. Retrieved November 17, 2024.
  source_name: Sophos PowerShell Command History Forensics
  url: https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics
id: attack-pattern--b831f51c-d22f-4724-bbab-60d056bd1150
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:45:06.768Z'
name: Prevent Command History Logging
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Austin Clark, @c2defense
- Emile Kenning, Sophos
- Vikas Singh, Sophos
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.0'
```
