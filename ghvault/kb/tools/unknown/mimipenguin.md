---
parsed_by: focuslocust
source: mitre
type: generated
---
# MimiPenguin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0179` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

MimiPenguin is a credential dumper, similar to Mimikatz, designed specifically for Linux platforms.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/mimipenguin.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.007 - Proc Filesystem](../../attack/techniques/T1003.007-proc-filesystem.md) | explicit | source | [MimiPenguin](https://attack.mitre.org/software/S0179) can use the `<PID>/maps` and `<PID>/mem` file to search for regex patterns and dump the process memory.(Citation: MimiPenguin GitHub May 2017)(Citation: Picus Labs Proc cump 2022) |

## Source Verification

[source record](../../sources/mitre/mimipenguin.md)

## Evidence Excerpt

```text
created: '2018-01-16T16:13:52.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[MimiPenguin](https://attack.mitre.org/software/S0179) is a credential dumper, similar to [Mimikatz](https://attack.mitre.org/software/S0002),
designed specifically for Linux platforms. (Citation: MimiPenguin GitHub May 2017)'
external_references:
- external_id: S0179
source_name: mitre-attack
url: https://attack.mitre.org/software/S0179
```
