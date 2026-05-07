---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0049
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0049-snapshot-deletion
---

## Description

The removal of a point-in-time backup of a cloud storage volume, virtual machine (VM), or database.<br><br>*Data Collection Measures:*<br><br>- AWS CloudTrail<br>    - Logs `DeleteSnapshot` API calls in EC2, RDS, and EBS services.<br>- Azure Monitor Logs<br>    - Tracks snapshot deletions via `Microsoft.Compute/snapshots/delete` API calls.<br>- Google Cloud Logging<br>    - Detects snapshot removal through `compute.disks.deleteSnapshot` events.
