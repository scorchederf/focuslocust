---
parsed_by: focuslocust
source: mitre
type: generated
---
# Image Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0028` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Image Metadata](../../attack/data-sources/DC0028-image-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0028 |
| name | Image Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0028 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "contextual information associated with a virtual machine image, such as its name, resource group, status (active\
  \ or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding\
  \ the state and configuration of virtual machine images in cloud environments. Examples: \n\n- Azure Compute Service Image\
  \ Metadata Example:\n    - Name: MyCustomImage\n    - Resource Group: MyResourceGroup\n    - State: Available\n    - Type:\
  \ Managed Image\n- AWS EC2 AMI Metadata Example:\n    - Image ID: ami-1234567890abcdef0\n    - Name: ProdImage\n    - State:\
  \ Available\n    - Platform: Windows\n- Google Cloud Compute Engine Image Metadata Example:\n    - Image Name: webserver-image\n\
  \    - Project: my-project-id\n    - Family: webserver\n    - Source Disk: my-disk-id\n- VMware vSphere Template Metadata\
  \ Example:\n    - Name: LinuxTemplate\n    - Disk Size: 40GB\n    - Network Adapter: VM Network"
external_references:
- external_id: DC0028
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0028
id: x-mitre-data-component--b597a220-6510-4397-b0d8-342cd2c58827
modified: '2025-11-12T22:03:39.105Z'
name: Image Metadata
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
- channel: docker.events.json
  name: docker:events
- channel: VMX startup messages without associated vCenter inventory records
  name: esxi:vmkernel
- channel: Resource creation and update logs
  name: kubernetes:apiserver
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
