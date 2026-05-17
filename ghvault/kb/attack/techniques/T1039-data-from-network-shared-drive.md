---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1039 - Data from Network Shared Drive

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1039` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within cmd may be used to gather information.

## Source Verification

[source record](../../sources/mitre/data-from-network-shared-drive.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:41.022Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive
data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that
are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality
within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information.
external_references:
- external_id: T1039
```
