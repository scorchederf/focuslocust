---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0080
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0080-instance-start
---

## Description

The initiation or activation of a virtual machine instance within a cloud infrastructure. This action typically involves starting an existing instance that had been stopped or paused, allowing it to resume operation. Examples: <br><br>- Google Cloud Platform (GCP): Starting an instance through `instance.start` API activity.<br>- AWS: Logging of `StartInstances` in AWS CloudTrail for EC2 instances.<br>- Azure: `Microsoft.Compute/virtualMachines/start` entries indicate a VM instance being started.
