---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0075 - Instance Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0075` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud infrastructure. This activity provides a view of all available or running instances, typically including their associated metadata such as instance ID, name, state, and configuration details. Examples:

- AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped EC2 instances.
- Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation.
- GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs.

*Data Collection Measures:*

- AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch.
- Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account.
- GCP Audit Logs: Logs Explorer or BigQuery.

## Source Verification

[source record](../../sources/mitre/instance-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud
infrastructure. This activity provides a view of all available or running instances, typically including their associated
metadata such as instance ID, name, state, and configuration details. Examples:
- AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped
EC2 instances.
- Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation.
```
