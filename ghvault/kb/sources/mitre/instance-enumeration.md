---
parsed_by: focuslocust
source: mitre
type: generated
---
# Instance Enumeration

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

## Generated Concept Page

- [Instance Enumeration](../../attack/data-sources/DC0075-instance-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0075 |
| name | Instance Enumeration |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0075 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud
  infrastructure. This activity provides a view of all available or running instances, typically including their associated
  metadata such as instance ID, name, state, and configuration details. Examples:


  - AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped
  EC2 instances.

  - Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation.

  - GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs.


  *Data Collection Measures:*


  - AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch.

  - Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account.

  - GCP Audit Logs: Logs Explorer or BigQuery.'
external_references:
- external_id: DC0075
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0075
id: x-mitre-data-component--2a80d95f-08c4-48e3-833e-151ef19d90f5
modified: '2025-10-21T15:14:38.969Z'
name: Instance Enumeration
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: DescribeDBInstances
  name: AWS:CloudTrail
- channel: MICROSOFT.COMPUTE/VIRTUALMACHINES/LIST
  name: azure:activity
- channel: compute.instances.list OR storage.buckets.list
  name: gcp:audit
- channel: DescribeInstances, GetConsoleOutput, DescribeImages
  name: AWS:CloudTrail
- channel: Microsoft.Compute/virtualMachines/read
  name: azure:activity
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
