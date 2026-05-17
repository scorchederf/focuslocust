---
parsed_by: focuslocust
source: mitre
type: generated
---
# Instance Creation

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

## Generated Concept Page

- [Instance Creation](../../attack/data-sources/DC0076-instance-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0076 |
| name | Instance Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0076 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'The initial provisioning and construction of a virtual machine (VM) or compute instance within a cloud infrastructure
  environment. This activity involves defining and allocating resources such as CPU, memory, storage, and networking to spin
  up a new compute instance. Examples:


  - AWS: creating an EC2 instance using RunInstances API calls.

  - Azure, creating a VM through the Azure Resource Manager (ARM).

  - GCP, an `instance.insert` action recorded.'
external_references:
- external_id: DC0076
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0076
id: x-mitre-data-component--b5b0e8ae-7436-4951-950a-7b83c4dd3f2c
modified: '2025-11-12T22:03:39.105Z'
name: Instance Creation
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
- channel: 'Microsoft.Compute/virtualMachines/write: imageReference publisher NOT IN allowlist OR plan is new/unknown'
  name: azure:activity
- channel: 'compute.instances.insert: sourceImage not in approved projects OR has external image link'
  name: gcp:audit
- channel: MICROSOFT.COMPUTE/VIRTUALMACHINES/WRITE
  name: azure:activity
- channel: compute.instances.insert
  name: gcp:audit
- channel: RunInstances,CreateImage
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
