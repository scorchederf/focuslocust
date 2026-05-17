---
parsed_by: focuslocust
source: mitre
type: generated
---
# Dynamic Linker Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dynamic Linker Hijacking](../../attack/techniques/T1574.006-dynamic-linker-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574.006 |
| name | Dynamic Linker Hijacking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574/006 |

## Preserved Source Material

```yaml
created: '2020-03-13T20:09:59.569Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute their own malicious payloads by hijacking environment variables the dynamic linker uses
  to load shared libraries. During the execution preparation phase of a program, the dynamic linker loads specified absolute
  paths of shared libraries from various environment variables and files, such as <code>LD_PRELOAD</code> on Linux or <code>DYLD_INSERT_LIBRARIES</code>
  on macOS.(Citation: TheEvilBit DYLD_INSERT_LIBRARIES)(Citation: Timac DYLD_INSERT_LIBRARIES)(Citation: Gabilondo DYLD_INSERT_LIBRARIES
  Catalina Bypass) Libraries specified in environment variables are loaded first, taking precedence over system libraries
  with the same function name.(Citation: Man LD.SO)(Citation: TLDP Shared Libraries)(Citation: Apple Doco Archive Dynamic
  Libraries) Each platform''s linker uses an extensive list of environment variables at different points in execution. These
  variables are often used by developers to debug binaries without needing to recompile, deconflict mapped symbols, and implement
  custom functions in the original library.(Citation: Baeldung LD_PRELOAD)


  Hijacking dynamic linker variables may grant access to the victim process''s memory, system/network resources, and possibly
  elevated privileges. On Linux, adversaries may set <code>LD_PRELOAD</code> to point to malicious libraries that match the
  name of legitimate libraries which are requested by a victim program, causing the operating system to load the adversary''s
  malicious code upon execution of the victim program. For example, adversaries have used `LD_PRELOAD` to inject a malicious
  library into every descendant process of the `sshd` daemon, resulting in execution under a legitimate process. When the
  executing sub-process calls the `execve` function, for example, the malicious library’s `execve` function is executed rather
  than the system function `execve` contained in the system library on disk. This allows adversaries to [Hide Artifacts](https://attack.mitre.org/techniques/T1564)
  from detection, as hooking system functions such as `execve` and `readdir` enables malware to scrub its own artifacts from
  the results of commands such as `ls`, `ldd`, `iptables`, and `dmesg`.(Citation: ESET Ebury Oct 2017)(Citation: Intezer Symbiote
  2022)(Citation: Elastic Security Labs Pumakit 2024)


  Hijacking dynamic linker variables may grant access to the victim process''s memory, system/network resources, and possibly
  elevated privileges.'
external_references:
- external_id: T1574.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574/006
- description: Apple Inc.. (2012, July 23). Overview of Dynamic Libraries. Retrieved March 24, 2021.
  source_name: Apple Doco Archive Dynamic Libraries
  url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/OverviewOfDynamicLibraries.html
- description: baeldung. (2020, August 9). What Is the LD_PRELOAD Trick?. Retrieved March 24, 2021.
  source_name: Baeldung LD_PRELOAD
  url: https://www.baeldung.com/linux/ld_preload-trick-what-is
- description: Fitzl, C. (2019, July 9). DYLD_INSERT_LIBRARIES DYLIB injection in macOS / OSX. Retrieved March 26, 2020.
  source_name: TheEvilBit DYLD_INSERT_LIBRARIES
  url: https://theevilbit.github.io/posts/dyld_insert_libraries_dylib_injection_in_macos_osx_deep_dive/
- description: 'Joakim Kennedy and The BlackBerry Threat Research & Intelligence Team. (2022, June 9). Symbiote Deep-Dive:
    Analysis of a New, Nearly-Impossible-to-Detect Linux Threat. Retrieved March 24, 2025.'
  source_name: Intezer Symbiote 2022
  url: https://intezer.com/blog/research/new-linux-threat-symbiote/
- description: Jon Gabilondo. (2019, September 22). How to Inject Code into Mach-O Apps. Part II.. Retrieved March 24, 2021.
  source_name: Gabilondo DYLD_INSERT_LIBRARIES Catalina Bypass
  url: https://jon-gabilondo-angulo-7635.medium.com/how-to-inject-code-into-mach-o-apps-part-ii-ddb13ebc8191
- description: Kerrisk, M. (2020, June 13). Linux Programmer's Manual. Retrieved June 15, 2020.
  source_name: Man LD.SO
  url: https://www.man7.org/linux/man-pages/man8/ld.so.8.html
- description: Remco Sprooten and Ruben Groenewoud. (2024, December 11). Declawing PUMAKIT. Retrieved March 24, 2025.
  source_name: Elastic Security Labs Pumakit 2024
  url: https://www.elastic.co/security-labs/declawing-pumakit
- description: The Linux Documentation Project. (n.d.). Shared Libraries. Retrieved January 31, 2020.
  source_name: TLDP Shared Libraries
  url: https://www.tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html
- description: Timac. (2012, December 18). Simple code injection using DYLD_INSERT_LIBRARIES. Retrieved March 26, 2020.
  source_name: Timac DYLD_INSERT_LIBRARIES
  url: https://blog.timac.org/2012/1218-simple-code-injection-using-dyld_insert_libraries/
- description: 'Vachon, F. (2017, October 30). Windigo Still not Windigone: An Ebury Update . Retrieved February 10, 2021.'
  source_name: ESET Ebury Oct 2017
  url: https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/
id: attack-pattern--633a100c-b2c9-41bf-9be5-905c1b16c825
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T22:57:21.530Z'
name: Dynamic Linker Hijacking
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
- Linux
- macOS
x_mitre_remote_support: false
x_mitre_version: '3.0'
```
