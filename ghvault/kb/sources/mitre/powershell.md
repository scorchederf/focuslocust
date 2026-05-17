---
parsed_by: focuslocust
source: mitre
type: generated
---
# PowerShell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PowerShell](../../attack/techniques/T1059.001-powershell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1059.001 |
| name | PowerShell |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1059/001 |

## Preserved Source Material

```yaml
created: '2020-03-09T13:48:55.078Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line
  interface and scripting environment included in the Windows operating system.(Citation: TechNet PowerShell) Adversaries
  can use PowerShell to perform a number of actions, including discovery of information and execution of code. Examples include
  the <code>Start-Process</code> cmdlet which can be used to run an executable and the <code>Invoke-Command</code> cmdlet
  which runs a command locally or on a remote computer (though administrator permissions are required to use PowerShell to
  connect to remote systems).


  PowerShell may also be used to download and run executables from the Internet, which can be executed from disk or in memory
  without touching disk.


  A number of PowerShell-based offensive testing tools are available, including [Empire](https://attack.mitre.org/software/S0363),  [PowerSploit](https://attack.mitre.org/software/S0194),
  [PoshC2](https://attack.mitre.org/software/S0378), and PSAttack.(Citation: Github PSAttack)


  PowerShell commands/scripts can also be executed without directly invoking the <code>powershell.exe</code> binary through
  interfaces to PowerShell''s underlying <code>System.Management.Automation</code> assembly DLL exposed through the .NET framework
  and Windows Common Language Interface (CLI).(Citation: Sixdub PowerPick Jan 2016)(Citation: SilentBreak Offensive PS Dec
  2015)(Citation: Microsoft PSfromCsharp APR 2014)'
external_references:
- external_id: T1059.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1059/001
- description: Babinec, K. (2014, April 28). Executing PowerShell scripts from C#. Retrieved April 22, 2019.
  source_name: Microsoft PSfromCsharp APR 2014
  url: https://blogs.msdn.microsoft.com/kebab/2014/04/28/executing-powershell-scripts-from-c/
- description: Christensen, L.. (2015, December 28). The Evolution of Offensive PowerShell Invocation. Retrieved December
    8, 2018.
  source_name: SilentBreak Offensive PS Dec 2015
  url: https://web.archive.org/web/20190508170150/https://silentbreaksecurity.com/powershell-jobs-without-powershell-exe/
- description: Dunwoody, M. (2016, February 11). GREATER VISIBILITY THROUGH POWERSHELL LOGGING. Retrieved February 16, 2016.
  source_name: FireEye PowerShell Logging 2016
  url: https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html
- description: Haight, J. (2016, April 21). PS>Attack. Retrieved September 27, 2024.
  source_name: Github PSAttack
  url: https://github.com/Exploit-install/PSAttack-1
- description: Hastings, M. (2014, July 16). Investigating PowerShell Attacks. Retrieved December 1, 2021.
  source_name: inv_ps_attacks
  url: https://powershellmagazine.com/2014/07/16/investigating-powershell-attacks/
- description: Malware Archaeology. (2016, June). WINDOWS POWERSHELL LOGGING CHEAT SHEET - Win 7/Win 2008 or later. Retrieved
    June 24, 2016.
  source_name: Malware Archaeology PowerShell Cheat Sheet
  url: http://www.malwarearchaeology.com/s/Windows-PowerShell-Logging-Cheat-Sheet-ver-June-2016-v2.pdf
- description: Microsoft. (n.d.). Windows PowerShell Scripting. Retrieved April 28, 2016.
  source_name: TechNet PowerShell
  url: https://technet.microsoft.com/en-us/scriptcenter/dd742419.aspx
- description: Warner, J.. (2015, January 6). Inexorable PowerShell – A Red Teamer’s Tale of Overcoming Simple AppLocker Policies.
    Retrieved December 8, 2018.
  source_name: Sixdub PowerPick Jan 2016
  url: https://web.archive.org/web/20160327101330/http://www.sixdub.net/?p=367
id: attack-pattern--970a3432-3237-47ad-bcca-7d8cbb217736
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:49:07.660Z'
name: PowerShell
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Mayuresh Dani, Qualys
- Praetorian
- Ross Brittain
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '1.5'
```
