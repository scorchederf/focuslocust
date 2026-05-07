---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0075
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0075-instance-enumeration
---

## Description

The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud infrastructure. This activity provides a view of all available or running instances, typically including their associated metadata such as instance ID, name, state, and configuration details. Examples:<br><br>- AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped EC2 instances.<br>- Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation.<br>- GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs.<br><br>*Data Collection Measures:*<br><br>- AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch.<br>- Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account.<br>- GCP Audit Logs: Logs Explorer or BigQuery.
