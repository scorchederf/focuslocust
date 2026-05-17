---
parsed_by: focuslocust
source: mitre
type: generated
---
# meek

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0175` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

meek is an open-source Tor plugin that tunnels Tor traffic through HTTPS connections.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/meek.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1090.004 - Domain Fronting](../../attack/techniques/T1090.004-domain-fronting.md) | explicit | source | [meek](https://attack.mitre.org/software/S0175) uses Domain Fronting to disguise the destination of network traffic as another server that is hosted in the same Content Delivery Network (CDN) as the intended destination. |

## Source Verification

[source record](../../sources/mitre/meek.md)

## Evidence Excerpt

```text
created: '2018-01-16T16:13:52.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[meek](https://attack.mitre.org/software/S0175) is an open-source Tor plugin that tunnels Tor traffic through
HTTPS connections.'
external_references:
- external_id: S0175
source_name: mitre-attack
url: https://attack.mitre.org/software/S0175
```
