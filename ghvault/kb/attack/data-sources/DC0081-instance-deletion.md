---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0081 - Instance Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0081` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Removal of a virtual machine (VM) or compute instance within a cloud infrastructure. This activity results in the termination and deletion of the allocated resources (e.g., CPU, memory, storage), making the instance unavailable for future use. Examples:

- AWS: instance deletion involves the `TerminateInstances` API call, which is recorded in CloudTrail logs.
- Azure: VM deletion can be monitored via Azure Activity Logs, showing the `Microsoft.Compute/virtualMachines/delete` operation.
- GCP: instance deletion is logged as an instance.delete operation within GCP Audit Logs.

## Source Verification

[source record](../../sources/mitre/instance-deletion.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Removal of a virtual machine (VM) or compute instance within a cloud infrastructure. This activity results in
the termination and deletion of the allocated resources (e.g., CPU, memory, storage), making the instance unavailable for
future use. Examples:
- AWS: instance deletion involves the `TerminateInstances` API call, which is recorded in CloudTrail logs.
- Azure: VM deletion can be monitored via Azure Activity Logs, showing the `Microsoft.Compute/virtualMachines/delete` operation.
- GCP: instance deletion is logged as an instance.delete operation within GCP Audit Logs.'
```
