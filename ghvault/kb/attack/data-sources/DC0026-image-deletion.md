---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0026 - Image Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0026` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples: 

- Azure Compute Service Image Deletion
    - Example: Deleting a virtual machine image using Azure CLI: `az image delete --name MyImage --resource-group MyResourceGroup`
- AWS EC2 AMI (Amazon Machine Image) Deletion
    - Example: Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0`
- Google Cloud Compute Engine Image Deletion
    - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image`
- VMware vSphere
    - Example: Deleting a VM image/template from a vSphere environment:

This data component can be collected through the following measures:

Enable Cloud Platform Logging

- Azure: Enable "Activity Logs" to capture DELETE requests to `Microsoft.Compute/images`.
- AWS: Use AWS CloudTrail to monitor `DeregisterImage` or `DeleteSnapshot` API calls.
- Google Cloud: Enable "Cloud Audit Logs" to track image deletion events under `compute.googleapis.com/images`.

API Monitoring

- Monitor API activity to track the deletion of images using:
    - AWS SDK/CLI `DeregisterImage` or `DeleteSnapshot`.
    - Azure REST API DELETE operations for images.
    - Google Cloud Compute Engine APIs for image deletion.

Cloud SIEM Integration

- Ingest logs into a centralized SIEM platform for monitoring and alerting:

Event Correlation

- Correlate image deletion events with unusual account activity or concurrent unauthorized operations.

## Source Verification

[source record](../../sources/mitre/image-deletion.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples:\
\ \n\n- Azure Compute Service Image Deletion\n    - Example: Deleting a virtual machine image using Azure CLI: `az image\
\ delete --name MyImage --resource-group MyResourceGroup`\n- AWS EC2 AMI (Amazon Machine Image) Deletion\n    - Example:\
\ Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0`\n- Google Cloud Compute Engine\
\ Image Deletion\n    - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image`\n\
- VMware vSphere\n    - Example: Deleting a VM image/template from a vSphere environment:\n\nThis data component can be\
```
