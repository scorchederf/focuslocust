---
parsed_by: focuslocust
source: mitre
type: generated
---
# xCmd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0123` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

xCmd is an open source tool that is similar to PsExec and allows the user to execute applications on remote systems.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/xcmd.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | [xCmd](https://attack.mitre.org/software/S0123) can be used to execute binaries on remote systems by creating and starting a service.(Citation: xCmd) |

## Source Verification

[source record](../../sources/mitre/xcmd.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:11.941Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[xCmd](https://attack.mitre.org/software/S0123) is an open source tool that is similar to [PsExec](https://attack.mitre.org/software/S0029)
and allows the user to execute applications on remote systems. (Citation: xCmd)'
external_references:
- external_id: S0123
source_name: mitre-attack
url: https://attack.mitre.org/software/S0123
```
