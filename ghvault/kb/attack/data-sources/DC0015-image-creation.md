---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0015 - Image Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0015` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Initial construction of a virtual machine image within a cloud environment. Virtual machine images are templates containing an operating system and installed applications, which can be deployed to create new virtual machines. Monitoring the creation of these images is important because adversaries may create custom images to include malicious software or misconfigurations for later exploitation. Examples: 

- Azure Compute Service Image Creation
    - Example: Creating a virtual machine image in Azure using Azure CLI: `az image create --resource-group MyResourceGroup --name MyImage --source MyVM`
- AWS EC2 AMI (Amazon Machine Image) Creation
    - Example: Creating an AMI from an EC2 instance: `aws ec2 create-image --instance-id i-1234567890abcdef0 --name "MyAMI" --description "An AMI for my app"`
- Google Cloud Compute Engine Image Creation
    - Example: Creating a custom image using gcloud: `gcloud compute images create my-custom-image --source-disk my-disk --source-disk-zone us-central1-a`
- VMware vSphere
    - Example: Exporting a VM to create an OVF (Open Virtualization Format) template: This could later be imported into other environments with potential tampering.

## Source Verification

[source record](../../sources/mitre/image-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Initial construction of a virtual machine image within a cloud environment. Virtual machine images are templates\
\ containing an operating system and installed applications, which can be deployed to create new virtual machines. Monitoring\
\ the creation of these images is important because adversaries may create custom images to include malicious software or\
\ misconfigurations for later exploitation. Examples: \n\n- Azure Compute Service Image Creation\n    - Example: Creating\
\ a virtual machine image in Azure using Azure CLI: `az image create --resource-group MyResourceGroup --name MyImage --source\
\ MyVM`\n- AWS EC2 AMI (Amazon Machine Image) Creation\n    - Example: Creating an AMI from an EC2 instance: `aws ec2 create-image\
```
