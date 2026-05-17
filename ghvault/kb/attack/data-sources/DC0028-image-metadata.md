---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0028 - Image Metadata

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

## Summary

contextual information associated with a virtual machine image, such as its name, resource group, status (active or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding the state and configuration of virtual machine images in cloud environments. Examples: 

- Azure Compute Service Image Metadata Example:
    - Name: MyCustomImage
    - Resource Group: MyResourceGroup
    - State: Available
    - Type: Managed Image
- AWS EC2 AMI Metadata Example:
    - Image ID: ami-1234567890abcdef0
    - Name: ProdImage
    - State: Available
    - Platform: Windows
- Google Cloud Compute Engine Image Metadata Example:
    - Image Name: webserver-image
    - Project: my-project-id
    - Family: webserver
    - Source Disk: my-disk-id
- VMware vSphere Template Metadata Example:
    - Name: LinuxTemplate
    - Disk Size: 40GB
    - Network Adapter: VM Network

## Source Verification

[source record](../../sources/mitre/image-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "contextual information associated with a virtual machine image, such as its name, resource group, status (active\
\ or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding\
\ the state and configuration of virtual machine images in cloud environments. Examples: \n\n- Azure Compute Service Image\
\ Metadata Example:\n    - Name: MyCustomImage\n    - Resource Group: MyResourceGroup\n    - State: Available\n    - Type:\
\ Managed Image\n- AWS EC2 AMI Metadata Example:\n    - Image ID: ami-1234567890abcdef0\n    - Name: ProdImage\n    - State:\
\ Available\n    - Platform: Windows\n- Google Cloud Compute Engine Image Metadata Example:\n    - Image Name: webserver-image\n\
```
