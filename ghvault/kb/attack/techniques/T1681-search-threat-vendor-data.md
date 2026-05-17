---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1681 - Search Threat Vendor Data

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1681` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives, or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their behavior when planning their future operations. 

Adversaries have been observed replacing atomic indicators mentioned in blog posts in under a week. Adversaries have also been seen searching for their own domain names in threat vendor data and then taking them down, likely to avoid seizure or further investigation.

This technique is distinct from Threat Intel Vendors in that it describes threat actors performing reconnaissance on their own activity, not in search of victim information.

## Source Verification

[source record](../../sources/mitre/search-threat-vendor-data.md)

## Evidence Excerpt

```text
created: '2025-09-26T15:42:30.468Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about\
\ their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives,\
\ or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic\
\ indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their\
\ behavior when planning their future operations. \n\nAdversaries have been observed replacing atomic indicators mentioned\
\ in blog posts in under a week.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) Adversaries have\
```
