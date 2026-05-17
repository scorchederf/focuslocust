---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0080 - Instance Start

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0080` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The initiation or activation of a virtual machine instance within a cloud infrastructure. This action typically involves starting an existing instance that had been stopped or paused, allowing it to resume operation. Examples: 

- Google Cloud Platform (GCP): Starting an instance through `instance.start` API activity.
- AWS: Logging of `StartInstances` in AWS CloudTrail for EC2 instances.
- Azure: `Microsoft.Compute/virtualMachines/start` entries indicate a VM instance being started.

## Source Verification

[source record](../../sources/mitre/instance-start.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The initiation or activation of a virtual machine instance within a cloud infrastructure. This action typically\
\ involves starting an existing instance that had been stopped or paused, allowing it to resume operation. Examples: \n\n\
- Google Cloud Platform (GCP): Starting an instance through `instance.start` API activity.\n- AWS: Logging of `StartInstances`\
\ in AWS CloudTrail for EC2 instances.\n- Azure: `Microsoft.Compute/virtualMachines/start` entries indicate a VM instance\
\ being started."
external_references:
```
