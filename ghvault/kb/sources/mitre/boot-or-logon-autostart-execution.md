---
parsed_by: focuslocust
source: mitre
type: generated
---
# Boot or Logon Autostart Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Boot or Logon Autostart Execution](../../attack/techniques/T1547-boot-or-logon-autostart-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547 |
| name | Boot or Logon Autostart Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547 |

## Preserved Source Material

```yaml
created: '2020-01-23T17:46:59.535Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may configure system settings to automatically execute a program during system boot or logon to
  maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically
  running a program on system boot or account logon.(Citation: Microsoft Run Key)(Citation: MSDN Authentication Packages)(Citation:
  Microsoft TimeProvider)(Citation: Cylance Reg Persistence Sept 2013)(Citation: Linux Kernel Programming) These mechanisms
  may include automatically executing programs that are placed in specially designated directories or are referenced by repositories
  that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying
  or extending features of the kernel.


  Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.'
external_references:
- external_id: T1547
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547
- description: 'Langendorf, S. (2013, September 24). Windows Registry Persistence, Part 2: The Run Keys and Search-Order.
    Retrieved November 17, 2024.'
  source_name: Cylance Reg Persistence Sept 2013
  url: https://web.archive.org/web/20160214140250/http://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order
- description: Microsoft. (n.d.). Authentication Packages. Retrieved March 1, 2017.
  source_name: MSDN Authentication Packages
  url: https://msdn.microsoft.com/library/windows/desktop/aa374733.aspx
- description: Microsoft. (n.d.). Run and RunOnce Registry Keys. Retrieved September 12, 2024.
  source_name: Microsoft Run Key
  url: https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys
- description: Microsoft. (n.d.). Time Provider. Retrieved March 26, 2018.
  source_name: Microsoft TimeProvider
  url: https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx
- description: Pomerantz, O., Salzman, P.. (2003, April 4). The Linux Kernel Module Programming Guide. Retrieved April 6,
    2018.
  source_name: Linux Kernel Programming
  url: https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf
- description: Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.
  source_name: TechNet Autoruns
  url: https://technet.microsoft.com/en-us/sysinternals/bb963902
id: attack-pattern--1ecb2399-e8ba-4f6b-8ba7-5c27d49405cf
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:48:29.846Z'
name: Boot or Logon Autostart Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- Network Devices
x_mitre_version: '1.3'
```
