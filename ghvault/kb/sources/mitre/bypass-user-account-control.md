---
parsed_by: focuslocust
source: mitre
type: generated
---
# Bypass User Account Control

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1548.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1548.002 |
| name | Bypass User Account Control |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1548/002 |

## Preserved Source Material

```yaml
created: '2020-01-30T14:24:34.977Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control
  (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task
  under administrator-level permissions, possibly by prompting the user for confirmation. The impact to the user ranges from
  denying the operation under high enforcement to allowing the user to perform the action if they are in the local administrators
  group and click through the prompt or allowing them to enter an administrator password to complete the action.(Citation:
  TechNet How UAC Works)


  If the UAC protection level of a computer is set to anything but the highest level, certain Windows programs can elevate
  privileges or execute some elevated [Component Object Model](https://attack.mitre.org/techniques/T1559/001) objects without
  prompting the user through the UAC notification box.(Citation: TechNet Inside UAC)(Citation: MSDN COM Elevation) An example
  of this is use of [Rundll32](https://attack.mitre.org/techniques/T1218/011) to load a specifically crafted DLL which loads
  an auto-elevated [Component Object Model](https://attack.mitre.org/techniques/T1559/001) object and performs a file operation
  in a protected directory which would typically require elevated access. Malicious software may also be injected into a trusted
  process to gain elevated privileges without prompting a user.(Citation: Davidson Windows)


  Many methods have been discovered to bypass UAC. The Github readme page for UACME contains an extensive list of methods(Citation:
  Github UACMe) that have been discovered and implemented, but may not be a comprehensive list of bypasses. Additional bypass
  methods are regularly discovered and some used in the wild, such as:


  * <code>eventvwr.exe</code> can auto-elevate and execute a specified binary or script.(Citation: enigma0x3 Fileless UAC
  Bypass)(Citation: Fortinet Fareit)


  Another bypass is possible through some lateral movement techniques if credentials for an account with administrator privileges
  are known, since UAC is a single system security mechanism, and the privilege or integrity of a process running on one system
  will be unknown on remote systems and default to high integrity.(Citation: SANS UAC Bypass)'
external_references:
- external_id: T1548.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1548/002
- description: Davidson, L. (n.d.). Windows 7 UAC whitelist. Retrieved November 12, 2014.
  source_name: Davidson Windows
  url: http://www.pretentiousname.com/misc/win7_uac_whitelist2.html
- description: Lich, B. (2016, May 31). How User Account Control Works. Retrieved June 3, 2016.
  source_name: TechNet How UAC Works
  url: https://technet.microsoft.com/en-us/itpro/windows/keep-secure/how-user-account-control-works
- description: Medin, T. (2013, August 8). PsExec UAC Bypass. Retrieved June 3, 2016.
  source_name: SANS UAC Bypass
  url: http://pen-testing.sans.org/blog/pen-testing/2013/08/08/psexec-uac-bypass
- description: Microsoft. (n.d.). The COM Elevation Moniker. Retrieved July 26, 2016.
  source_name: MSDN COM Elevation
  url: https://msdn.microsoft.com/en-us/library/ms679687.aspx
- description: Nelson, M. (2016, August 15). "Fileless" UAC Bypass using eventvwr.exe and Registry Hijacking. Retrieved December
    27, 2016.
  source_name: enigma0x3 Fileless UAC Bypass
  url: https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
- description: 'Russinovich, M. (2009, July). User Account Control: Inside Windows 7 User Account Control. Retrieved July
    26, 2016.'
  source_name: TechNet Inside UAC
  url: https://technet.microsoft.com/en-US/magazine/2009.07.uac.aspx
- description: Salvio, J., Joven, R. (2016, December 16). Malicious Macro Bypasses UAC to Elevate Privilege for Fareit Malware.
    Retrieved December 27, 2016.
  source_name: Fortinet Fareit
  url: https://blog.fortinet.com/2016/12/16/malicious-macro-bypasses-uac-to-elevate-privilege-for-fareit-malware
- description: UACME Project. (2016, June 16). UACMe. Retrieved July 26, 2016.
  source_name: Github UACMe
  url: https://github.com/hfiref0x/UACME
id: attack-pattern--120d5519-3098-4e1c-9191-2aa61232f073
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:51:31.419Z'
name: Bypass User Account Control
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Stefan Kanthak
- Casey Smith
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
