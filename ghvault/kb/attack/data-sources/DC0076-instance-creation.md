---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0076 - Instance Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0076` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The initial provisioning and construction of a virtual machine (VM) or compute instance within a cloud infrastructure environment. This activity involves defining and allocating resources such as CPU, memory, storage, and networking to spin up a new compute instance. Examples:

- AWS: creating an EC2 instance using RunInstances API calls.
- Azure, creating a VM through the Azure Resource Manager (ARM).
- GCP, an `instance.insert` action recorded.

## Source Verification

[source record](../../sources/mitre/instance-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'The initial provisioning and construction of a virtual machine (VM) or compute instance within a cloud infrastructure
environment. This activity involves defining and allocating resources such as CPU, memory, storage, and networking to spin
up a new compute instance. Examples:
- AWS: creating an EC2 instance using RunInstances API calls.
- Azure, creating a VM through the Azure Resource Manager (ARM).
- GCP, an `instance.insert` action recorded.'
```
