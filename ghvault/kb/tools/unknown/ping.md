---
parsed_by: focuslocust
source: mitre
type: generated
---
# Ping

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0097` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Ping is an operating system utility commonly used to troubleshoot and verify network connections.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/ping.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [Ping](https://attack.mitre.org/software/S0097) can be used to identify remote systems within a network.(Citation: TechNet Ping) |

## Source Verification

[source record](../../sources/mitre/ping.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:01.483Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot
and verify network connections. (Citation: TechNet Ping)'
external_references:
- external_id: S0097
source_name: mitre-attack
url: https://attack.mitre.org/software/S0097
```
