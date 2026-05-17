---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1129 - Shared Modules

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

## Summary

Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions (i.e., Native API).

Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network communications or execution of specific actions on objective.

The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides in `dlfcn.h` in functions such as `dlopen` and `dlsym`. Although macOS can execute `.so` files, common practice uses `.dylib` files.

The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in `NTDLL.dll` and is part of the Windows Native API which is called from functions like `LoadLibrary` at run time.

## Source Verification

[source record](../../sources/mitre/shared-modules.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:40.542Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that
are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions
(i.e., [Native API](https://attack.mitre.org/techniques/T1106)).
Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries
can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network
communications or execution of specific actions on objective.
```
