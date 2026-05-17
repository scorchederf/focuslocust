---
parsed_by: focuslocust
source: mitre
type: generated
---
# Shell History

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shell History](../../attack/techniques/T1552.003-shell-history.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1552.003 |
| name | Shell History |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1552/003 |

## Preserved Source Material

```yaml
created: '2020-02-04T13:02:11.685Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search the command history on compromised systems for insecurely stored credentials.


  On Linux and macOS systems, shells such as Bash and Zsh keep track of the commands users type on the command-line with the
  "history" utility. Once a user logs out, the history is flushed to the user''s history file. For each user, this file resides
  at the same location: for example, `~/.bash_history` or `~/.zsh_history`. Typically, these files keeps track of the user''s
  last 1000 commands.


  On Windows, PowerShell has both a command history that is wiped after the session ends, and one that contains commands used
  in all sessions and is persistent. The default location for persistent history can be found in `%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`,
  but command history can also be accessed with `Get-History`. Command Prompt (CMD) on Windows does not have persistent history.(Citation:
  Microsoft about_History)(Citation: Medium)


  Users often type usernames and passwords on the command-line as parameters to programs, which then get saved to this file
  when they log out. Adversaries can abuse this by looking through the file for potential credentials.(Citation: External
  to DA, the OS X Way)'
external_references:
- external_id: T1552.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1552/003
- description: Alex Rymdeko-Harvey, Steve Borosh. (2016, May 14). External to DA, the OS X Way. Retrieved September 12, 2024.
  source_name: External to DA, the OS X Way
  url: https://www.slideshare.net/slideshow/external-to-da-the-os-x-way/62021418
- description: Michael Koczwara. (2021, March 14). Windows privilege escalation via PowerShell History. Retrieved June 13,
    2025.
  source_name: Medium
  url: https://michaelkoczwara.medium.com/windows-privilege-escalation-dbb908cce8d4
- description: Microsoft. (2024, January 19). about_History. Retrieved June 13, 2025.
  source_name: Microsoft about_History
  url: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7.5
id: attack-pattern--8187bd2a-866f-4457-9009-86b0ddedffa3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:02.375Z'
name: Shell History
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Raja Singh (raja-singh-r3v-sh3ll)
- Avioo360
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
