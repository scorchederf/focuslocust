---
parsed_by: focuslocust
source: mitre
type: generated
---
# Shared Modules

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1129` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shared Modules](../../attack/techniques/T1129-shared-modules.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1129 |
| name | Shared Modules |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1129 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:40.542Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that
  are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions
  (i.e., [Native API](https://attack.mitre.org/techniques/T1106)).


  Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries
  can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network
  communications or execution of specific actions on objective.


  The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides
  in `dlfcn.h` in functions such as `dlopen` and `dlsym`. Although macOS can execute `.so` files, common practice uses `.dylib`
  files.(Citation: Apple Dev Dynamic Libraries)(Citation: Linux Shared Libraries)(Citation: RotaJakiro 2021 netlab360 analysis)(Citation:
  Unit42 OceanLotus 2017)


  The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention
  (UNC) network paths. This functionality resides in `NTDLL.dll` and is part of the Windows [Native API](https://attack.mitre.org/techniques/T1106)
  which is called from functions like `LoadLibrary` at run time.(Citation: Microsoft DLL)'
external_references:
- external_id: T1129
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1129
- description: ' Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved
    June 14, 2023.'
  source_name: RotaJakiro 2021 netlab360 analysis
  url: https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/
- description: Apple. (2012, July 23). Overview of Dynamic Libraries. Retrieved September 7, 2023.
  source_name: Apple Dev Dynamic Libraries
  url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/OverviewOfDynamicLibraries.html
- description: Erye Hernandez and Danny Tsechansky. (2017, June 22). The New and Improved macOS Backdoor from OceanLotus.
    Retrieved September 8, 2023.
  source_name: Unit42 OceanLotus 2017
  url: https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/
- description: Microsoft. (2023, April 28). What is a DLL. Retrieved September 7, 2023.
  source_name: Microsoft DLL
  url: https://learn.microsoft.com/troubleshoot/windows-client/deployment/dynamic-link-library
- description: Wheeler, D. (2003, April 11). Shared Libraries. Retrieved September 7, 2023.
  source_name: Linux Shared Libraries
  url: https://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html
id: attack-pattern--0a5231ec-41af-4a35-83d0-6bdf11f28c65
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:48:22.302Z'
name: Shared Modules
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Stefan Kanthak
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.3'
```
