---
parsed_by: focuslocust
source: mitre
type: generated
---
# AppDomainManager

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574.014` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AppDomainManager](../../attack/techniques/T1574.014-appdomainmanager.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574.014 |
| name | AppDomainManager |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574/014 |

## Preserved Source Material

```yaml
created: '2024-03-28T15:36:34.141Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may execute their own malicious payloads by hijacking how the .NET `AppDomainManager` loads assemblies.\
  \ The .NET framework uses the `AppDomainManager` class to create and manage one or more isolated runtime environments (called\
  \ application domains) inside a process to host the execution of .NET applications. Assemblies (`.exe` or `.dll` binaries\
  \ compiled to run as .NET code) may be loaded into an application domain as executable code.(Citation: Microsoft App Domains)\
  \ \n\nKnown as \"AppDomainManager injection,\" adversaries may execute arbitrary code by hijacking how .NET applications\
  \ load assemblies. For example, malware may create a custom application domain inside a target process to load and execute\
  \ an arbitrary assembly. Alternatively, configuration files (`.config`) or process environment variables that define .NET\
  \ runtime settings may be tampered with to instruct otherwise benign .NET applications to load a malicious assembly (identified\
  \ by name) into the target process.(Citation: PenTestLabs AppDomainManagerInject)(Citation: PwC Yellow Liderc)(Citation:\
  \ Rapid7 AppDomain Manager Injection)"
external_references:
- external_id: T1574.014
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574/014
- description: Administrator. (2020, May 26). APPDOMAINMANAGER INJECTION AND DETECTION. Retrieved March 28, 2024.
  source_name: PenTestLabs AppDomainManagerInject
  url: https://pentestlaboratories.com/2020/05/26/appdomainmanager-injection-and-detection/
- description: Microsoft. (2021, September 15). Application domains. Retrieved March 28, 2024.
  source_name: Microsoft App Domains
  url: https://learn.microsoft.com/dotnet/framework/app-domains/application-domains
- description: PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware.
    Retrieved March 29, 2024.
  source_name: PwC Yellow Liderc
  url: https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html
- description: 'Spagnola, N. (2023, May 5). AppDomain Manager Injection: New Techniques For Red Teams. Retrieved March 29,
    2024.'
  source_name: Rapid7 AppDomain Manager Injection
  url: https://www.rapid7.com/blog/post/2023/05/05/appdomain-manager-injection-new-techniques-for-red-teams/
id: attack-pattern--356662f7-e315-4759-86c9-6214e2a50ff8
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T22:57:09.601Z'
name: AppDomainManager
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Ivy Drexel
- Thomas B
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
