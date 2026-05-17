---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1007 - System Service Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1007` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as <code>sc query</code>, <code>tasklist /svc</code>, <code>systemctl --type=service</code>, and <code>net start</code>. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.

Adversaries may use the information from System Service Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Net](../../tools/unknown/net.md) | explicit | source | The <code>net start</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to find information about Windows services.(Citation: Savill 1999) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate service and service permission information.(Citation: GitHub PoshC2) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can search for modifiable services that could be used for privilege escalation.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [Tasklist](../../tools/unknown/tasklist.md) | explicit | source | [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover services running on a system.(Citation: Microsoft Tasklist) |

## Source Verification

[source record](../../sources/mitre/system-service-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:21.315Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may try to gather information about registered local system services. Adversaries may obtain information
about services using tools as well as OS utility commands such as <code>sc query</code>, <code>tasklist /svc</code>, <code>systemctl
--type=service</code>, and <code>net start</code>. Adversaries may also gather information about schedule tasks via commands
such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation:
SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)
Adversaries may use the information from [System Service Discovery](https://attack.mitre.org/techniques/T1007) during automated
```
