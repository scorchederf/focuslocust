---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0098
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0098-volume-deletion
---

## Description

The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated storage and may result in data loss if not backed up.<br><br>*Data Collection Measures:*<br><br>- Cloud Logging & APIs<br>    - AWS CloudTrail Logs<br>        - `eventName: DeleteVolume` (tracks volume deletions)<br>    - Azure Monitor Logs<br>        - `operationName: Microsoft.Compute/disks/delete`<br>        - `status: Success | Failure` (flag unauthorized delete attempts)<br>    - Google Cloud Audit Logs<br>        - `protoPayload.methodName: "v1.compute.disks.delete"`<br>        - `authenticationInfo.principalEmail` (identifies the user deleting the volume)<br>- System & Host-Based Logging<br>    - Linux & macOS Logs:<br>        - `/var/log/syslog` or `/var/log/messages` for volume detach/deletion actions<br>    - Windows Event Logs:<br>        - Event ID 98 (Storage Class Memory)<br>        - Event ID 225 (Volume Removal Detected)<br>        - Event ID 12 (Disk Removal Notification)
