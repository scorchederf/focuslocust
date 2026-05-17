---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1069 - Permission Groups Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1069` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the local privileges for the infected host.(Citation: FOX-IT May 2016 Mofang) |

## Source Verification

[source record](../../sources/mitre/permission-groups-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:55.471Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to discover group and permission settings. This information can help adversaries determine
which user accounts and groups are available, the membership of users in particular groups, and which users and groups have
elevated permissions.
Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary
with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike
BloodHound April 2018)'
```
