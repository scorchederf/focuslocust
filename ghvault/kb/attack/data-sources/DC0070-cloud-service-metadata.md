---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0070 - Cloud Service Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0070` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud service metadata refers to the contextual and descriptive information about cloud services, including their name, type, purpose, configuration, and activity around them. This metadata is essential for understanding the roles and functions of cloud services, their operational status, and their potential misuse. Examples: 

- Azure Service Metadata: Metadata describing a resource in Azure, such as an Azure Storage Account or a Virtual Machine.
- AWS Cloud Service Metadata: Metadata for an AWS EC2 instance collected using the `DescribeInstances` API call.
- Google Cloud Service Metadata: Metadata for a Google Compute Engine instance collected using `gcloud compute instances describe`.
- Office 365 Metadata: Metadata about an Office 365 SharePoint site.

## Source Verification

[source record](../../sources/mitre/cloud-service-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud service metadata refers to the contextual and descriptive information about cloud services, including\
\ their name, type, purpose, configuration, and activity around them. This metadata is essential for understanding the roles\
\ and functions of cloud services, their operational status, and their potential misuse. Examples: \n\n- Azure Service Metadata:\
\ Metadata describing a resource in Azure, such as an Azure Storage Account or a Virtual Machine.\n- AWS Cloud Service Metadata:\
\ Metadata for an AWS EC2 instance collected using the `DescribeInstances` API call.\n- Google Cloud Service Metadata: Metadata\
\ for a Google Compute Engine instance collected using `gcloud compute instances describe`.\n- Office 365 Metadata: Metadata\
```
