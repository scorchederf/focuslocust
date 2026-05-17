---
parsed_by: focuslocust
source: mitre
type: generated
---
# Instance Stop

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

## Generated Concept Page

- [Instance Stop](../../attack/data-sources/DC0089-instance-stop.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0089 |
| name | Instance Stop |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0089 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The deactivation or shutdown of a virtual machine instance within a cloud infrastructure. This action typically\
  \ involves stopping a running instance, which halts its operation and releases certain associated resources, such as CPU\
  \ and memory. Examples: \n\n- Google Cloud Platform (GCP): `instance.stop` events recorded in GCP Audit Logs indicate the\
  \ deactivation of an instance.\n- Amazon Web Services (AWS): `StopInstances` actions in AWS CloudTrail indicate EC2 instances\
  \ being stopped.\n- Microsoft Azure: `Microsoft.Compute/virtualMachines/deallocate` or `stop` events in Azure Activity Logs\
  \ represent a virtual machine being stopped or deallocated."
external_references:
- external_id: DC0089
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0089
id: x-mitre-data-component--1361e324-b594-4c0e-a517-20cee32b8d7f
modified: '2025-10-21T15:14:37.816Z'
name: Instance Stop
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
- channel: TerminateInstances
  name: AWS:CloudTrail
- channel: StopInstances
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
