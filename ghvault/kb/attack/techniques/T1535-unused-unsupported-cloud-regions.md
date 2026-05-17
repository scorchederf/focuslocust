---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1535 - Unused／Unsupported Cloud Regions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1535` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may create cloud instances in unused geographic service regions in order to evade detection. Access is usually obtained through compromising accounts used to manage cloud infrastructure.

Cloud service providers often provide infrastructure throughout the world in order to improve performance, provide redundancy, and allow customers to meet compliance requirements. Oftentimes, a customer will only use a subset of the available regions and may not actively monitor other regions. If an adversary creates resources in an unused region, they may be able to operate undetected.

A variation on this behavior takes advantage of differences in functionality across cloud regions. An adversary could utilize regions which do not support advanced detection services in order to avoid detection of their activity.

An example of adversary use of unused AWS regions is to mine cryptocurrency through Resource Hijacking, which can cost organizations substantial amounts of money over time depending on the processing power used.

## Source Verification

[source record](../../sources/mitre/unused-unsupported-cloud-regions.md)

## Evidence Excerpt

```text
created: '2019-09-04T14:35:04.617Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create cloud instances in unused geographic service regions in order to evade detection. Access
is usually obtained through compromising accounts used to manage cloud infrastructure.
Cloud service providers often provide infrastructure throughout the world in order to improve performance, provide redundancy,
and allow customers to meet compliance requirements. Oftentimes, a customer will only use a subset of the available regions
and may not actively monitor other regions. If an adversary creates resources in an unused region, they may be able to operate
undetected.
```
