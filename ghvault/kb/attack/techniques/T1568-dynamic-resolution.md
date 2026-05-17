---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1568 - Dynamic Resolution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1568` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculations can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

Adversaries may use dynamic resolution for the purpose of Fallback Channels. When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing command and control.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can be configured to use dynamic DNS.(Citation: AsyncRAT GitHub) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has used dynamic DNS domains in C2 communications.(Citation: Check Point Blind Eagle MAR 2025) |

## Source Verification

[source record](../../sources/mitre/dynamic-resolution.md)

## Evidence Excerpt

```text
created: '2020-03-10T17:28:11.747Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may dynamically establish connections to command and control infrastructure to evade common detections
and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary
uses to receive the malware''s communications. These calculations can be used to dynamically adjust parameters such as the
domain name, IP address, or port number the malware uses for command and control.
Adversaries may use dynamic resolution for the purpose of [Fallback Channels](https://attack.mitre.org/techniques/T1008).
When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing
```
