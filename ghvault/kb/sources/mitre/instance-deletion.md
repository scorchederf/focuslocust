---
parsed_by: focuslocust
source: mitre
type: generated
---
# Instance Deletion

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

## Generated Concept Page

- [Instance Deletion](../../attack/data-sources/DC0081-instance-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0081 |
| name | Instance Deletion |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0081 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Removal of a virtual machine (VM) or compute instance within a cloud infrastructure. This activity results in
  the termination and deletion of the allocated resources (e.g., CPU, memory, storage), making the instance unavailable for
  future use. Examples:


  - AWS: instance deletion involves the `TerminateInstances` API call, which is recorded in CloudTrail logs.

  - Azure: VM deletion can be monitored via Azure Activity Logs, showing the `Microsoft.Compute/virtualMachines/delete` operation.

  - GCP: instance deletion is logged as an instance.delete operation within GCP Audit Logs.'
external_references:
- external_id: DC0081
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0081
id: x-mitre-data-component--7561ed50-16cb-4826-82c7-c1ddca61785e
modified: '2025-11-12T22:03:39.105Z'
name: Instance Deletion
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
- channel: MICROSOFT.COMPUTE/VIRTUALMACHINES/DELETE
  name: azure:activity
- channel: compute.instances.delete
  name: gcp:audit
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
