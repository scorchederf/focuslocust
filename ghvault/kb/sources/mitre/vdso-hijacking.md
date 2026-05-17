---
parsed_by: focuslocust
source: mitre
type: generated
---
# VDSO Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1055.014` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [VDSO Hijacking](../../attack/techniques/T1055.014-vdso-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1055.014 |
| name | VDSO Hijacking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1055/014 |

## Preserved Source Material

```yaml
created: '2020-01-14T01:35:00.781Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may inject malicious code into processes via VDSO hijacking in order to evade process-based defenses\
  \ as well as possibly elevate privileges. Virtual dynamic shared object (vdso) hijacking is a method of executing arbitrary\
  \ code in the address space of a separate live process. \n\nVDSO hijacking involves redirecting calls to dynamically linked\
  \ shared libraries. Memory protections may prevent writing executable code to a process via [Ptrace System Calls](https://attack.mitre.org/techniques/T1055/008).\
  \ However, an adversary may hijack the syscall interface code stubs mapped into a process from the vdso shared object to\
  \ execute syscalls to open and map a malicious shared object. This code can then be invoked by redirecting the execution\
  \ flow of the process via patched memory address references stored in a process' global offset table (which store absolute\
  \ addresses of mapped library functions).(Citation: ELF Injection May 2009)(Citation: Backtrace VDSO)(Citation: VDSO Aug\
  \ 2005)(Citation: Syscall 2014)\n\nRunning code in the context of another process may allow access to the process's memory,\
  \ system/network resources, and possibly elevated privileges. Execution via VDSO hijacking may also evade detection from\
  \ security products since the execution is masked under a legitimate process.  "
external_references:
- external_id: T1055.014
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1055/014
- description: backtrace. (2016, April 22). ELF SHARED LIBRARY INJECTION FORENSICS. Retrieved November 17, 2024.
  source_name: Backtrace VDSO
  url: https://web.archive.org/web/20210205211142/https://backtrace.io/blog/backtrace/elf-shared-library-injection-forensics/
- description: Drysdale, D. (2014, July 16). Anatomy of a system call, part 2. Retrieved June 16, 2020.
  source_name: Syscall 2014
  url: https://lwn.net/Articles/604515/
- description: O'Neill, R. (2009, May). Modern Day ELF Runtime infection via GOT poisoning. Retrieved March 15, 2020.
  source_name: ELF Injection May 2009
  url: https://web.archive.org/web/20150711051625/http://vxer.org/lib/vrn00.html
- description: Petersson, J. (2005, August 14). What is linux-gate.so.1?. Retrieved June 16, 2020.
  source_name: VDSO Aug 2005
  url: https://web.archive.org/web/20051013084246/http://www.trilithium.com/johan/2005/08/linux-gate/
id: attack-pattern--98be40f2-c86b-4ade-b6fc-4964932040e5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T22:30:51.756Z'
name: VDSO Hijacking
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
x_mitre_version: '2.0'
```
