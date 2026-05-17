---
parsed_by: focuslocust
source: mitre
type: generated
---
# Security Support Provider

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Security Support Provider](../../attack/techniques/T1547.005-security-support-provider.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.005 |
| name | Security Support Provider |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/005 |

## Preserved Source Material

```yaml
created: '2020-01-24T17:16:11.806Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse security support providers (SSPs) to execute DLLs when the system boots. Windows SSP DLLs
  are loaded into the Local Security Authority (LSA) process at system start. Once loaded into the LSA, SSP DLLs have access
  to encrypted and plaintext passwords that are stored in Windows, such as any logged-on user''s Domain password or smart
  card PINs.


  The SSP configuration is stored in two Registry keys: <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages</code>
  and <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages</code>. An adversary may modify these Registry
  keys to add new SSPs, which will be loaded the next time the system boots, or when the AddSecurityPackage Windows API function
  is called.(Citation: Graeber 2014)'
external_references:
- external_id: T1547.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/005
- description: Graeber, M. (2014, October). Analysis of Malicious Security Support Provider DLLs. Retrieved March 1, 2017.
  source_name: Graeber 2014
  url: http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html
- description: Microsoft. (2013, July 31). Configuring Additional LSA Protection. Retrieved June 24, 2015.
  source_name: Microsoft Configure LSA
  url: https://technet.microsoft.com/en-us/library/dn408187.aspx
id: attack-pattern--5095a853-299c-4876-abd7-ac0050fb5462
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:48:46.245Z'
name: Security Support Provider
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
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
