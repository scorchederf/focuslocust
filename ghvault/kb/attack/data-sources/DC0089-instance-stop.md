---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0089 - Instance Stop

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0089` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The deactivation or shutdown of a virtual machine instance within a cloud infrastructure. This action typically involves stopping a running instance, which halts its operation and releases certain associated resources, such as CPU and memory. Examples: 

- Google Cloud Platform (GCP): `instance.stop` events recorded in GCP Audit Logs indicate the deactivation of an instance.
- Amazon Web Services (AWS): `StopInstances` actions in AWS CloudTrail indicate EC2 instances being stopped.
- Microsoft Azure: `Microsoft.Compute/virtualMachines/deallocate` or `stop` events in Azure Activity Logs represent a virtual machine being stopped or deallocated.

## Source Verification

[source record](../../sources/mitre/instance-stop.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The deactivation or shutdown of a virtual machine instance within a cloud infrastructure. This action typically\
\ involves stopping a running instance, which halts its operation and releases certain associated resources, such as CPU\
\ and memory. Examples: \n\n- Google Cloud Platform (GCP): `instance.stop` events recorded in GCP Audit Logs indicate the\
\ deactivation of an instance.\n- Amazon Web Services (AWS): `StopInstances` actions in AWS CloudTrail indicate EC2 instances\
\ being stopped.\n- Microsoft Azure: `Microsoft.Compute/virtualMachines/deallocate` or `stop` events in Azure Activity Logs\
\ represent a virtual machine being stopped or deallocated."
```
