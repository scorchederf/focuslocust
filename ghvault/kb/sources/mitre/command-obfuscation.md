---
parsed_by: focuslocust
source: mitre
type: generated
---
# Command Obfuscation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.010` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Command Obfuscation](../../attack/techniques/T1027.010-command-obfuscation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.010 |
| name | Command Obfuscation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/010 |

## Preserved Source Material

```yaml
created: '2023-03-14T17:36:01.022Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may obfuscate content during command execution to impede detection. Command-line obfuscation is
  a method of making strings and patterns within commands and scripts more difficult to signature and analyze. This type of
  obfuscation can be included within commands executed by delivered payloads (e.g., [Phishing](https://attack.mitre.org/techniques/T1566)
  and [Drive-by Compromise](https://attack.mitre.org/techniques/T1189)) or interactively via [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059).(Citation:
  Akamai JS)(Citation: Malware Monday VBE)


  For example, adversaries may abuse syntax that utilizes various symbols and escape characters (such as spacing,  `^`, `+`.
  `$`, and `%`) to make commands difficult to analyze while maintaining the same intended functionality.(Citation: RC PowerShell)
  Many languages support built-in obfuscation in the form of base64 or URL encoding.(Citation: Microsoft PowerShellB64) Adversaries
  may also manually implement command obfuscation via string splitting (`“Wor”+“d.Application”`), order and casing of characters
  (`rev <<<''dwssap/cte/ tac''`), globing (`mkdir -p ''/tmp/:&$NiA''`), as well as various tricks involving passing strings
  through tokens/environment variables/input streams.(Citation: Bashfuscator Command Obfuscators)(Citation: FireEye Obfuscation
  June 2017)


  Adversaries may also use tricks such as directory traversals to obfuscate references to the binary being invoked by a command
  (`C:\voi\pcw\..\..\Windows\tei\qs\k\..\..\..\system32\erool\..\wbem\wg\je\..\..\wmic.exe shadowcopy delete`).(Citation:
  Twitter Richard WMIC)


  Tools such as <code>Invoke-Obfuscation</code> and <code>Invoke-DOSfucation</code> have also been used to obfuscate commands.(Citation:
  Invoke-DOSfuscation)(Citation: Invoke-Obfuscation)'
external_references:
- external_id: T1027.010
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/010
- description: Ackroyd, R. (2023, March 24). Twitter. Retrieved September 12, 2024.
  source_name: Twitter Richard WMIC
  url: https://x.com/rfackroyd/status/1639136000755765254
- description: Bohannon, D. (2016, September 24). Invoke-Obfuscation. Retrieved March 17, 2023.
  source_name: Invoke-Obfuscation
  url: https://github.com/danielbohannon/Invoke-Obfuscation
- description: Bohannon, D. (2018, March 19). Invoke-DOSfuscation. Retrieved March 17, 2023.
  source_name: Invoke-DOSfuscation
  url: https://github.com/danielbohannon/Invoke-DOSfuscation
- description: 'Bohannon, D. & Carr N. (2017, June 30). Obfuscation in the Wild: Targeted Attackers Lead the Way in Evasion
    Techniques. Retrieved February 12, 2018.'
  source_name: FireEye Obfuscation June 2017
  url: https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html
- description: 'Bromiley, M. (2016, December 27). Malware Monday: VBScript and VBE Files. Retrieved March 17, 2023.'
  source_name: Malware Monday VBE
  url: https://bromiley.medium.com/malware-monday-vbscript-and-vbe-files-292252c1a16
- description: Katz, O. (2020, October 26). Catch Me if You Can—JavaScript Obfuscation. Retrieved March 17, 2023.
  source_name: Akamai JS
  url: https://www.akamai.com/blog/security/catch-me-if-you-can-javascript-obfuscation
- description: LeFevre, A. (n.d.). Bashfuscator Command Obfuscators. Retrieved March 17, 2023.
  source_name: Bashfuscator Command Obfuscators
  url: https://bashfuscator.readthedocs.io/en/latest/Mutators/command_obfuscators/index.html
- description: 'Microsoft. (2023, February 8). about_PowerShell_exe: EncodedCommand. Retrieved March 17, 2023.'
  source_name: Microsoft PowerShellB64
  url: https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1#-encodedcommand-base64encodedcommand
- description: 'Red Canary. (n.d.). 2022 Threat Detection Report: PowerShell. Retrieved March 17, 2023.'
  source_name: RC PowerShell
  url: https://redcanary.com/threat-detection-report/techniques/powershell/
id: attack-pattern--d511a6f6-4a33-41d5-bc95-c343875d1377
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:16:39.249Z'
name: Command Obfuscation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- George Thomas
- Tim Peck
- TruKno
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
