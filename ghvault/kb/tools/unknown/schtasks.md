---
parsed_by: focuslocust
source: mitre
type: generated
---
# schtasks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0111` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

schtasks is used to schedule execution of programs or scripts on a Windows system to run at a specific date and time.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/schtasks.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [schtasks](https://attack.mitre.org/software/S0111) is used to schedule tasks on a Windows system to run at a specific date and time.(Citation: TechNet Schtasks) |

## Source Verification

[source record](../../sources/mitre/schtasks.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:07.218Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[schtasks](https://attack.mitre.org/software/S0111) is used to schedule execution of programs or scripts on
a Windows system to run at a specific date and time. (Citation: TechNet Schtasks)'
external_references:
- external_id: S0111
source_name: mitre-attack
url: https://attack.mitre.org/software/S0111
```
