---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1008 - Fallback Channels

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1008` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Mythic](../../tools/unknown/mythic.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked.(Citation: Mythc Documentation)	 |

## Source Verification

[source record](../../sources/mitre/fallback-channels.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:21.689Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible
in order to maintain reliable command and control and to avoid data transfer thresholds.
external_references:
- external_id: T1008
source_name: mitre-attack
url: https://attack.mitre.org/techniques/T1008
```
