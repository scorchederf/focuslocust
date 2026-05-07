---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0022
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0022-cloud-storage-deletion
---

## Description

Cloud Storage Deletion refers to the removal or destruction of cloud storage infrastructure, such as buckets, containers, or directories, within a cloud environment. Monitoring this activity is critical to detecting potential unauthorized or malicious actions, such as data destruction by adversaries or accidental deletions that may lead to data loss. Examples: <br><br>- AWS S3 Bucket Deletion: An AWS user deletes an S3 bucket using the `DeleteBucket` API call.<br>- Azure Blob Storage Container Deletion: A user deletes a container in Azure Blob Storage using the `Delete Container` operation.<br>- Google Cloud Storage Bucket Deletion: A Google Cloud user deletes a bucket using the `storage.buckets.delete` API.<br>- OpenStack Swift Container Deletion: A user deletes a container in OpenStack Swift using the `DELETE` method.<br><br>This data component can be collected through the following measures:<br><br>Enable Logging for Cloud Storage Services<br><br>- AWS S3: Enable AWS CloudTrail to log DeleteBucket API actions.<br>- Azure Blob Storage: Enable Azure Monitor and Diagnostic Logs to capture Delete Container operations. Use Azure Event Grid to capture and trigger alerts for container deletion.<br>- Google Cloud Storage: Enable Data Access logs in Cloud Audit Logs to monitor storage.buckets.delete API calls.<br>- OpenStack Swift: Configure Swift logging to capture DELETE requests for containers.<br><br>Centralized Logging and Analysis<br><br>- Use platforms like Splunk or native SIEMs to forward and analyze logs for anomalies in cloud storage deletions.
