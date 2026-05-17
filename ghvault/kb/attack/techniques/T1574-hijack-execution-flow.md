---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1574 - Hijack Execution Flow

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions on execution.

There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs/resources, such as file directories and in the case of Windows the Registry, could also be poisoned to include malicious payloads.

## Source Verification

[source record](../../sources/mitre/hijack-execution-flow.md)

## Evidence Excerpt

```text
created: '2020-03-12T20:38:12.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking
execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries
may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions
on execution.
There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates
programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations
```
