---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0081
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0081-instance-deletion
---

## Description

Removal of a virtual machine (VM) or compute instance within a cloud infrastructure. This activity results in the termination and deletion of the allocated resources (e.g., CPU, memory, storage), making the instance unavailable for future use. Examples:<br><br>- AWS: instance deletion involves the `TerminateInstances` API call, which is recorded in CloudTrail logs.<br>- Azure: VM deletion can be monitored via Azure Activity Logs, showing the `Microsoft.Compute/virtualMachines/delete` operation.<br>- GCP: instance deletion is logged as an instance.delete operation within GCP Audit Logs.
