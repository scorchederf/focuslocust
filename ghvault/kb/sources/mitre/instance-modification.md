---
parsed_by: focuslocust
source: mitre
type: generated
---
# Instance Modification

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

## Generated Concept Page

- [Instance Modification](../../attack/data-sources/DC0073-instance-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0073 |
| name | Instance Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0073 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata,
  attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource
  policies, resizing instances, or modifying network configurations. Examples:


  - AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`.

  - Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`.

  - GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or
  `instances.resize`.


  *Data Collection Measures:*


  - AWS CloudTrail: Log Location: Stored in S3 or forwarded to CloudWatch.

  - Azure Activity Logs: Log Location: Accessible via Azure Monitor or exported to a storage account.

  - GCP Audit Logs: Log Location: Logs Explorer or BigQuery.'
external_references:
- external_id: DC0073
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0073
id: x-mitre-data-component--45d0ff14-b9c4-41f5-8603-156657c20b75
modified: '2026-04-16T17:07:21.897Z'
name: Instance Modification
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
- channel: RevertSnapshot
  name: AWS:CloudTrail
- channel: MICROSOFT.COMPUTE/VIRTUALMACHINES/RESTORE
  name: azure:activity
- channel: compute.instances.restore
  name: gcp:audit
- channel: ModifyInstanceAttribute
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
