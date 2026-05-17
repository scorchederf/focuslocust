---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1074 - Data Staged

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1074` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as Archive Collected Data. Interactive command shells may be used, and common functionality within cmd and bash may be used to copy data into a staging location.

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may Create Cloud Instance and stage data in that instance.

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Source Verification

[source record](../../sources/mitre/data-staged.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:58.938Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept
in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560).
Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and
bash may be used to copy data into a staging location.(Citation: PWC Cloud Hopper April 2017)
In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An
adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation:
```
