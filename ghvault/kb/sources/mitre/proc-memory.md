---
parsed_by: focuslocust
source: mitre
type: generated
---
# Proc Memory

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1055.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Proc Memory](../../attack/techniques/T1055.009-proc-memory.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1055.009 |
| name | Proc Memory |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1055/009 |

## Preserved Source Material

```yaml
created: '2020-01-14T01:34:10.588Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may inject malicious code into processes via the /proc filesystem in order to evade process-based\
  \ defenses as well as possibly elevate privileges. Proc memory injection is a method of executing arbitrary code in the\
  \ address space of a separate live process. \n\nProc memory injection involves enumerating the memory of a process via the\
  \ /proc filesystem (<code>/proc/[pid]</code>) then crafting a return-oriented programming (ROP) payload with available gadgets/instructions.\
  \ Each running process has its own directory, which includes memory mappings. Proc memory injection is commonly performed\
  \ by overwriting the target processes’ stack using memory mappings provided by the /proc filesystem. This information can\
  \ be used to enumerate offsets (including the stack) and gadgets (or instructions within the program that can be used to\
  \ build a malicious payload) otherwise hidden by process memory protections such as address space layout randomization (ASLR).\
  \ Once enumerated, the target processes’ memory map within <code>/proc/[pid]/maps</code> can be overwritten using dd.(Citation:\
  \ Uninformed Needle)(Citation: GDS Linux Injection)(Citation: DD Man) \n\nOther techniques such as [Dynamic Linker Hijacking](https://attack.mitre.org/techniques/T1574/006)\
  \ may be used to populate a target process with more available gadgets. Similar to [Process Hollowing](https://attack.mitre.org/techniques/T1055/012),\
  \ proc memory injection may target child processes (such as a backgrounded copy of sleep).(Citation: GDS Linux Injection)\
  \ \n\nRunning code in the context of another process may allow access to the process's memory, system/network resources,\
  \ and possibly elevated privileges. Execution via proc memory injection may also evade detection from security products\
  \ since the execution is masked under a legitimate process. "
external_references:
- external_id: T1055.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1055/009
- description: Kerrisk, M. (2020, February 2). DD(1) User Commands. Retrieved February 21, 2020.
  source_name: DD Man
  url: http://man7.org/linux/man-pages/man1/dd.1.html
- description: McNamara, R. (2017, September 5). Linux Based Inter-Process Code Injection Without Ptrace(2). Retrieved February
    21, 2020.
  source_name: GDS Linux Injection
  url: https://blog.gdssecurity.com/labs/2017/9/5/linux-based-inter-process-code-injection-without-ptrace2.html
- description: skape. (2003, January 19). Linux x86 run-time process manipulation. Retrieved December 20, 2017.
  source_name: Uninformed Needle
  url: http://hick.org/code/skape/papers/needle.txt
id: attack-pattern--d201d4cc-214d-4a74-a1ba-b3fa09fd4591
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T22:28:52.682Z'
name: Proc Memory
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
