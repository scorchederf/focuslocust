---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0047
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0047-snapshot-enumeration
---

## Description

The process of listing or retrieving metadata about existing snapshots in a cloud environment.<br><br>*Data Collection Measures:*<br><br>- AWS CloudTrail<br>    - Logs API calls such as `DescribeSnapshots`, `ListSnapshots`, and `GetSnapshotAttributes`.<br>- Azure Monitor Logs<br>    - Tracks snapshot enumeration via `Microsoft.Compute/snapshots/read`.<br>- Google Cloud Logging<br>    - Detects snapshot listing through `compute.disks.listSnapshots`.<br>
