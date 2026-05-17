---
parsed_by: focuslocust
source: mitre
type: generated
---
# MSBuild

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1127.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MSBuild](../../attack/techniques/T1127.001-msbuild.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1127.001 |
| name | MSBuild |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1127/001 |

## Preserved Source Material

```yaml
created: '2020-03-27T21:50:26.042Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use MSBuild to proxy execution of code through a trusted Windows utility. MSBuild.exe (Microsoft
  Build Engine) is a software build platform used by Visual Studio. It handles XML formatted project files that define requirements
  for loading and building various platforms and configurations.(Citation: MSDN MSBuild)


  Adversaries can abuse MSBuild to proxy execution of malicious code. The inline task capability of MSBuild that was introduced
  in .NET version 4 allows for C# or Visual Basic code to be inserted into an XML project file.(Citation: MSDN MSBuild)(Citation:
  Microsoft MSBuild Inline Tasks 2017) MSBuild will compile and execute the inline task. MSBuild.exe is a signed Microsoft
  binary, so when it is used this way it can execute arbitrary code and bypass application control defenses that are configured
  to allow MSBuild.exe execution.(Citation: LOLBAS Msbuild)'
external_references:
- external_id: T1127.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1127/001
- description: LOLBAS. (n.d.). Msbuild.exe. Retrieved July 31, 2019.
  source_name: LOLBAS Msbuild
  url: https://lolbas-project.github.io/lolbas/Binaries/Msbuild/
- description: Microsoft. (2017, September 21). MSBuild inline tasks. Retrieved March 5, 2021.
  source_name: Microsoft MSBuild Inline Tasks 2017
  url: https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-inline-tasks?view=vs-2019#code-element
- description: Microsoft. (n.d.). MSBuild1. Retrieved November 30, 2016.
  source_name: MSDN MSBuild
  url: https://msdn.microsoft.com/library/dd393574.aspx
id: attack-pattern--c92e3d68-2349-49e4-a341-7edca2deff96
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T22:45:30.815Z'
name: MSBuild
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- '@ionstorm'
- Carrie Roberts, @OrOneEqualsOne
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
