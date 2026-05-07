---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0026
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0026-image-deletion
---

## Description

Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples: <br><br>- Azure Compute Service Image Deletion<br>    - Example: Deleting a virtual machine image using Azure CLI: `az image delete --name MyImage --resource-group MyResourceGroup`<br>- AWS EC2 AMI (Amazon Machine Image) Deletion<br>    - Example: Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0`<br>- Google Cloud Compute Engine Image Deletion<br>    - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image`<br>- VMware vSphere<br>    - Example: Deleting a VM image/template from a vSphere environment:<br><br>This data component can be collected through the following measures:<br><br>Enable Cloud Platform Logging<br><br>- Azure: Enable "Activity Logs" to capture DELETE requests to `Microsoft.Compute/images`.<br>- AWS: Use AWS CloudTrail to monitor `DeregisterImage` or `DeleteSnapshot` API calls.<br>- Google Cloud: Enable "Cloud Audit Logs" to track image deletion events under `compute.googleapis.com/images`.<br><br>API Monitoring<br><br>- Monitor API activity to track the deletion of images using:<br>    - AWS SDK/CLI `DeregisterImage` or `DeleteSnapshot`.<br>    - Azure REST API DELETE operations for images.<br>    - Google Cloud Compute Engine APIs for image deletion.<br><br>Cloud SIEM Integration<br><br>- Ingest logs into a centralized SIEM platform for monitoring and alerting:<br><br>Event Correlation<br><br>- Correlate image deletion events with unusual account activity or concurrent unauthorized operations.<br>
