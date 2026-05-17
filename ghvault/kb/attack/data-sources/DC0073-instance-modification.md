---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0073 - Instance Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0073` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata, attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource policies, resizing instances, or modifying network configurations. Examples:

- AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`.
- Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`.
- GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or `instances.resize`.

*Data Collection Measures:*

- AWS CloudTrail: Log Location: Stored in S3 or forwarded to CloudWatch.
- Azure Activity Logs: Log Location: Accessible via Azure Monitor or exported to a storage account.
- GCP Audit Logs: Log Location: Logs Explorer or BigQuery.

## Source Verification

[source record](../../sources/mitre/instance-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata,
attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource
policies, resizing instances, or modifying network configurations. Examples:
- AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`.
- Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`.
- GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or
```
