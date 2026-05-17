---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0032 - Process Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0032` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Refers to the event in which a new process (executable) is initialized by an operating system. This can involve parent-child process relationships, process arguments, and environmental variables. Monitoring process creation is crucial for detecting malicious behaviors, such as execution of unauthorized binaries, scripting abuse, or privilege escalation attempts..

## Source Verification

[source record](../../sources/mitre/process-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Refers to the event in which a new process (executable) is initialized by an operating system. This can involve
parent-child process relationships, process arguments, and environmental variables. Monitoring process creation is crucial
for detecting malicious behaviors, such as execution of unauthorized binaries, scripting abuse, or privilege escalation
attempts.. '
external_references:
- external_id: DC0032
```
