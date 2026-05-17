---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1678 - Delay Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1678` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny. Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems. 

Adversaries may utilize programmatic `sleep` commands or native system scheduling functionality, for example Scheduled Task/Job. Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time to execute properly. Loops or otherwise needless repetitions of commands, such as `ping`, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments. Another variation, commonly referred to as API hammering, involves making various calls to Native API functions in order to delay execution (while also potentially overloading analysis environments with junk data).

## Source Verification

[source record](../../sources/mitre/delay-execution.md)

## Evidence Excerpt

```text
created: '2025-09-24T18:03:15.021Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit\
\ system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny.\
\ Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems. \n\nAdversaries\
\ may utilize programmatic `sleep` commands or native system scheduling functionality, for example [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053).\
\ Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time\
\ to execute properly. Loops or otherwise needless repetitions of commands, such as `ping`, may be used to delay malware\
```
