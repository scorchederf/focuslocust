---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1497 - Virtualization／Sandbox Evasion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1497` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from Virtualization/Sandbox Evasion during automated discovery to shape follow-on behaviors.

Adversaries may use several methods to accomplish Virtualization/Sandbox Evasion such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox.

## Source Verification

[source record](../../sources/mitre/virtualization-sandbox-evasion.md)

## Evidence Excerpt

```text
created: '2019-04-17T22:22:24.505Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may
include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine
environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim
or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional
payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497)
during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)
```
