---
parsed_by: focuslocust
source: mitre
type: generated
---
# Authentication Package

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Authentication Package](../../attack/techniques/T1547.002-authentication-package.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.002 |
| name | Authentication Package |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/002 |

## Preserved Source Material

```yaml
created: '2020-01-24T14:54:42.757Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse authentication packages to execute DLLs when the system boots. Windows authentication
  package DLLs are loaded by the Local Security Authority (LSA) process at system start. They provide support for multiple
  logon processes and multiple security protocols to the operating system.(Citation: MSDN Authentication Packages)


  Adversaries can use the autostart mechanism provided by LSA authentication packages for persistence by placing a reference
  to a binary in the Windows Registry location <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\</code> with the key value
  of <code>"Authentication Packages"=&lt;target binary&gt;</code>. The binary will then be executed by the system when the
  authentication packages are loaded.'
external_references:
- external_id: T1547.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/002
- description: Graeber, M. (2014, October). Analysis of Malicious Security Support Provider DLLs. Retrieved March 1, 2017.
  source_name: Graeber 2014
  url: http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html
- description: Microsoft. (2013, July 31). Configuring Additional LSA Protection. Retrieved June 24, 2015.
  source_name: Microsoft Configure LSA
  url: https://technet.microsoft.com/en-us/library/dn408187.aspx
- description: Microsoft. (n.d.). Authentication Packages. Retrieved March 1, 2017.
  source_name: MSDN Authentication Packages
  url: https://msdn.microsoft.com/library/windows/desktop/aa374733.aspx
id: attack-pattern--b8cfed42-6a8a-4989-ad72-541af74475ec
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:17.208Z'
name: Authentication Package
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
x_mitre_version: '1.1'
```
