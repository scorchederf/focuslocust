---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1029 - Scheduled Transfer

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1029` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration Over C2 Channel or Exfiltration Over Alternative Protocol.

## Source Verification

[source record](../../sources/mitre/scheduled-transfer.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:34.139Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals.
This could be done to blend traffic patterns with normal activity or availability.
When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out
of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) or [Exfiltration Over
Alternative Protocol](https://attack.mitre.org/techniques/T1048).'
external_references:
```
