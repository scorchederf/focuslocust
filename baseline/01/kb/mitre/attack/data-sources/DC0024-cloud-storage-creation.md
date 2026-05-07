---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0024
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0024-cloud-storage-creation
---

## Description

Cloud Storage Creation refers to the initial creation of a new cloud storage resource, such as buckets, containers, or directories, within a cloud environment. This action is critical to track as it might indicate the legitimate provisioning of resources or unauthorized actions taken by adversaries to stage, store, or exfiltrate data. Examples: <br><br>- AWS S3 Bucket Creation: An AWS user creates a new S3 bucket using the `CreateBucket` API call.<br>- Azure Blob Storage Container Creation: A user creates a new container in Azure Blob Storage using the `Create Container` operation.<br>- Google Cloud Storage Bucket Creation: A Google Cloud user creates a new bucket using `storage.buckets.create`.<br>- OpenStack Swift Container Creation: A user creates a new container in OpenStack Swift using the `PUT` method.
