---
parsed_by: focuslocust
source: mitre
type: generated
---
# Systeminfo

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0096` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Systeminfo is a Windows utility that can be used to gather detailed information about a computer.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/systeminfo.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather information about the operating system.(Citation: TechNet Systeminfo) |

## Source Verification

[source record](../../sources/mitre/systeminfo.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:00.969Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Systeminfo](https://attack.mitre.org/software/S0096) is a Windows utility that can be used to gather detailed
information about a computer. (Citation: TechNet Systeminfo)'
external_references:
- external_id: S0096
source_name: mitre-attack
url: https://attack.mitre.org/software/S0096
```
