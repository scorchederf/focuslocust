---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0073
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0073-instance-modification
---

## Description

Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata, attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource policies, resizing instances, or modifying network configurations. Examples:<br><br>- AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`.<br>- Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`.<br>- GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or `instances.resize`.<br><br>*Data Collection Measures:*<br><br>- AWS CloudTrail: Log Location: Stored in S3 or forwarded to CloudWatch.<br>- Azure Activity Logs: Log Location: Accessible via Azure Monitor or exported to a storage account.<br>- GCP Audit Logs: Log Location: Logs Explorer or BigQuery.
