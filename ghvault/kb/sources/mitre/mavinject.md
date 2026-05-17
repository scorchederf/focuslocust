---
parsed_by: focuslocust
source: mitre
type: generated
---
# Mavinject

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.013` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mavinject](../../attack/techniques/T1218.013-mavinject.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.013 |
| name | Mavinject |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/013 |

## Preserved Source Material

```yaml
created: '2021-09-22T17:45:10.241Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse mavinject.exe to proxy execution of malicious code. Mavinject.exe is the Microsoft Application\
  \ Virtualization Injector, a Windows utility that can inject code into external processes as part of Microsoft Application\
  \ Virtualization (App-V).(Citation: LOLBAS Mavinject)\n\nAdversaries may abuse mavinject.exe to inject malicious DLLs into\
  \ running processes (i.e. [Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001)), allowing for\
  \ arbitrary code execution (ex. <code>C:\\Windows\\system32\\mavinject.exe PID /INJECTRUNNING PATH_DLL</code>).(Citation:\
  \ ATT Lazarus TTP Evolution)(Citation: Reaqta Mavinject) Since mavinject.exe may be digitally signed by Microsoft, proxying\
  \ execution via this method may evade detection by security products because the execution is masked under a legitimate\
  \ process. \n\nIn addition to [Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001), Mavinject.exe\
  \ can also be abused to perform import descriptor injection via its  <code>/HMODULE</code> command-line parameter (ex. <code>mavinject.exe\
  \ PID /HMODULE=BASE_ADDRESS PATH_DLL ORDINAL_NUMBER</code>). This command would inject an import table entry consisting\
  \ of the specified DLL into the module at the given base address.(Citation: Mavinject Functionality Deconstructed)"
external_references:
- external_id: T1218.013
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/013
- description: Fernando Martinez. (2021, July 6). Lazarus campaign TTPs and evolution. Retrieved September 22, 2021.
  source_name: ATT Lazarus TTP Evolution
  url: https://cybersecurity.att.com/blogs/labs-research/lazarus-campaign-ttps-and-evolution
- description: LOLBAS. (n.d.). Mavinject.exe. Retrieved September 22, 2021.
  source_name: LOLBAS Mavinject
  url: https://lolbas-project.github.io/lolbas/Binaries/Mavinject/
- description: Matt Graeber. (2018, May 29). mavinject.exe Functionality Deconstructed. Retrieved September 22, 2021.
  source_name: Mavinject Functionality Deconstructed
  url: https://posts.specterops.io/mavinject-exe-functionality-deconstructed-c29ab2cf5c0e
- description: 'Reaqta. (2017, December 16). From False Positive to True Positive: the story of Mavinject.exe, the Microsoft
    Injector. Retrieved September 22, 2021.'
  source_name: Reaqta Mavinject
  url: https://reaqta.com/2017/12/mavinject-microsoft-injector/
id: attack-pattern--1bae753e-8e52-4055-a66d-2ead90303ca9
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:39:41.553Z'
name: Mavinject
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
