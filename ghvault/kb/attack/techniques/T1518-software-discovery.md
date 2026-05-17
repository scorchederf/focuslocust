---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1518 - Software Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1518` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from Software Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Such software may be deployed widely across the environment for configuration management or security reasons, such as Software Deployment Tools, and may allow adversaries broad access to infect devices or move laterally.

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to Exploitation for Privilege Escalation.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered a list of installed software on the infected host.(Citation: FOX-IT May 2016 Mofang) |

## Source Verification

[source record](../../sources/mitre/software-discovery.md)

## Evidence Excerpt

```text
created: '2019-09-16T17:52:44.147Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get a listing of software and software versions that are installed on a system or
in a cloud environment. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1518)
during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target
and/or attempts specific actions.
Such software may be deployed widely across the environment for configuration management or security reasons, such as [Software
Deployment Tools](https://attack.mitre.org/techniques/T1072), and may allow adversaries broad access to infect devices or
```
