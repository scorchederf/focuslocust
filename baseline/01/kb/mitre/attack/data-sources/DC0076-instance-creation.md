---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0076
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0076-instance-creation
---

## Description

The initial provisioning and construction of a virtual machine (VM) or compute instance within a cloud infrastructure environment. This activity involves defining and allocating resources such as CPU, memory, storage, and networking to spin up a new compute instance. Examples:<br><br>- AWS: creating an EC2 instance using RunInstances API calls.<br>- Azure, creating a VM through the Azure Resource Manager (ARM).<br>- GCP, an `instance.insert` action recorded.
