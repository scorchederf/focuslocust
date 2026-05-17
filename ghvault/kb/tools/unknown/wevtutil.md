---
parsed_by: focuslocust
source: mitre
type: generated
---
# Wevtutil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0645` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Wevtutil is a Windows command-line utility that enables administrators to retrieve information about event logs and publishers.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/wevtutil.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to export events from a specific log.(Citation: Wevtutil Microsoft Documentation)(Citation: F-Secure Lazarus Cryptocurrency Aug 2020) |
| [T1685.001 - Disable or Modify Windows Event Log](../../attack/techniques/T1685.001-disable-or-modify-windows-event-log.md) | explicit | source | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to disable specific event logs on the system.(Citation: Wevtutil Microsoft Documentation) |
| [T1685.005 - Clear Windows Event Logs](../../attack/techniques/T1685.005-clear-windows-event-logs.md) | explicit | source | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to clear system and security event logs from the system.(Citation: Wevtutil Microsoft Documentation)(Citation: Crowdstrike DNC June 2016) |

## Source Verification

[source record](../../sources/mitre/wevtutil.md)

## Evidence Excerpt

```text
created: '2021-09-14T21:45:30.280Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Wevtutil](https://attack.mitre.org/software/S0645) is a Windows command-line utility that enables administrators
to retrieve information about event logs and publishers.(Citation: Wevtutil Microsoft Documentation)'
external_references:
- external_id: S0645
source_name: mitre-attack
url: https://attack.mitre.org/software/S0645
```
