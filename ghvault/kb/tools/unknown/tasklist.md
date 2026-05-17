---
parsed_by: focuslocust
source: mitre
type: generated
---
# Tasklist

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0057` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The Tasklist utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/tasklist.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1007 - System Service Discovery](../../attack/techniques/T1007-system-service-discovery.md) | explicit | source | [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover services running on a system.(Citation: Microsoft Tasklist) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover processes running on a system.(Citation: Microsoft Tasklist) |
| [T1518.001 - Security Software Discovery](../../attack/techniques/T1518.001-security-software-discovery.md) | explicit | source | [Tasklist](https://attack.mitre.org/software/S0057) can be used to enumerate security software currently running on a system by process name of known products.(Citation: Microsoft Tasklist) |

## Source Verification

[source record](../../sources/mitre/tasklist.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:39.233Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services
with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating
systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist)'
external_references:
- external_id: S0057
source_name: mitre-attack
```
