---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0017
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0017-cloud-storage-enumeration
---

## Description

Cloud Storage Enumeration involves retrieving a list of available cloud storage infrastructure, such as buckets, containers, or objects, within a cloud environment. This activity may be performed for legitimate administrative purposes or malicious reconnaissance by adversaries seeking to identify accessible storage resources.Examples:<br><br>- AWS S3 Bucket Enumeration: An AWS user lists all buckets using the `ListBuckets` API call.<br>- Azure Blob Storage Container Enumeration: A user retrieves a list of all containers within a storage account using the Azure Storage SDK or API.<br>- Google Cloud Storage Bucket Enumeration: A Google Cloud user lists all buckets within a project using the `storage.buckets.list` API.<br>- OpenStack Swift Container Enumeration: A user retrieves a list of containers in OpenStack Swift using the `GET` method on the storage endpoint.
