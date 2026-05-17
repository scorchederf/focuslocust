---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1020 - Automated Exfiltration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1020` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after being gathered during Collection. 

When automated exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration Over C2 Channel and Exfiltration Over Alternative Protocol.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has the ability to automatically send collected data back to the threat actors' C2.(Citation: Talos Frankenstein June 2019) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) sent collected system and network information compiled into a report to an adversary-controlled C2.(Citation: FOX-IT May 2016 Mofang) |

## Source Verification

[source record](../../sources/mitre/automated-exfiltration.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:29.458Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after\
\ being gathered during Collection.(Citation: ESET Gamaredon June 2020) \n\nWhen automated exfiltration is used, other exfiltration\
\ techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041)\
\ and [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048)."
external_references:
- external_id: T1020
```
