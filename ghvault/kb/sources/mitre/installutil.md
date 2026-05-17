---
parsed_by: focuslocust
source: mitre
type: generated
---
# InstallUtil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [InstallUtil](../../attack/techniques/T1218.004-installutil.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.004 |
| name | InstallUtil |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/004 |

## Preserved Source Material

```yaml
created: '2020-01-23T19:09:48.811Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil is
  a command-line utility that allows for installation and uninstallation of resources by executing specific installer components
  specified in .NET binaries. (Citation: MSDN InstallUtil) The InstallUtil binary may also be digitally signed by Microsoft
  and located in the .NET directories on a Windows system: <code>C:\Windows\Microsoft.NET\Framework\v<version>\InstallUtil.exe</code>
  and <code>C:\Windows\Microsoft.NET\Framework64\v<version>\InstallUtil.exe</code>.


  InstallUtil may also be used to bypass application control through use of attributes within the binary that execute the
  class decorated with the attribute <code>[System.ComponentModel.RunInstaller(true)]</code>. (Citation: LOLBAS Installutil)'
external_references:
- external_id: T1218.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/004
- description: LOLBAS. (n.d.). Installutil.exe. Retrieved July 31, 2019.
  source_name: LOLBAS Installutil
  url: https://lolbas-project.github.io/lolbas/Binaries/Installutil/
- description: Microsoft. (n.d.). Installutil.exe (Installer Tool). Retrieved July 1, 2016.
  source_name: MSDN InstallUtil
  url: https://msdn.microsoft.com/en-us/library/50614e95.aspx
id: attack-pattern--2cd950a6-16c4-404a-aa01-044322395107
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:39:41.457Z'
name: InstallUtil
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Casey Smith
- Travis Smith, Tripwire
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
