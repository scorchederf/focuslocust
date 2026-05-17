---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1601 - Modify System Image

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1601` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide new capabilities for themselves.  On such devices, the operating systems are typically monolithic and most of the device functionality and capabilities are contained within a single file.

To change the operating system, the adversary typically only needs to affect this one file, replacing or modifying it.  This can either be done live in memory during system runtime for immediate effect, or in storage to implement the change on the next boot of the network device.

## Source Verification

[source record](../../sources/mitre/modify-system-image.md)

## Evidence Excerpt

```text
created: '2020-10-19T19:42:19.740Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide
new capabilities for themselves.  On such devices, the operating systems are typically monolithic and most of the device
functionality and capabilities are contained within a single file.
To change the operating system, the adversary typically only needs to affect this one file, replacing or modifying it.  This
can either be done live in memory during system runtime for immediate effect, or in storage to implement the change on the
next boot of the network device.'
```
