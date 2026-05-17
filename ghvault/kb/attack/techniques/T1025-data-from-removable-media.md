---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1025 - Data from Removable Media

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1025` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within cmd may be used to gather information. 

Some adversaries may also use Automated Collection on removable media.

## Source Verification

[source record](../../sources/mitre/data-from-removable-media.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:31.584Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may search connected removable media on computers they have compromised to find files of interest.\
\ Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised\
\ system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106)\
\ may be used to gather information. \n\nSome adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119)\
\ on removable media."
external_references:
```
