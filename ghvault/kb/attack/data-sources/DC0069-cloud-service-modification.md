---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0069 - Cloud Service Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0069` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud service modification refers to changes made to the configuration, settings, or data of a cloud service. These modifications can include administrative changes such as enabling or disabling features, altering permissions, or deleting critical components. Monitoring these changes is critical to detect potential misconfigurations or malicious activity. Examples: 

- AWS Cloud Service Modifications: A user disables AWS CloudTrail logging (StopLogging) or deletes a CloudWatch configuration rule (DeleteConfigRule).
- Azure Cloud Service Modifications: Changes to Azure Role-Based Access Control (RBAC) roles, such as adding a new Contributor role to a sensitive resource.
- Google Cloud Service Modifications: Deletion of a Google Cloud Storage bucket or disabling a Google Cloud Function.
- Office 365 Cloud Service Modifications: Altering mailbox permissions or disabling auditing in Microsoft 365.

## Source Verification

[source record](../../sources/mitre/cloud-service-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud service modification refers to changes made to the configuration, settings, or data of a cloud service.\
\ These modifications can include administrative changes such as enabling or disabling features, altering permissions, or\
\ deleting critical components. Monitoring these changes is critical to detect potential misconfigurations or malicious\
\ activity. Examples: \n\n- AWS Cloud Service Modifications: A user disables AWS CloudTrail logging (StopLogging) or deletes\
\ a CloudWatch configuration rule (DeleteConfigRule).\n- Azure Cloud Service Modifications: Changes to Azure Role-Based\
\ Access Control (RBAC) roles, such as adding a new Contributor role to a sensitive resource.\n- Google Cloud Service Modifications:\
```
