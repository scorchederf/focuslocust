---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0058
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0058-snapshot-modification
---

## Description

Changes made to a cloud snapshot's metadata, attributes, or control settings. These modifications may involve adjusting access permissions, changing retention policies, or altering encryption settings. <br><br>*Data Collection Measures:*<br><br>- AWS CloudTrail<br>    - Tracks API calls such as `ModifySnapshotAttribute`, `ResetSnapshotAttribute`, and `ModifySnapshotTier`.<br>- Azure Monitor Logs<br>    - Logs changes via `Microsoft.Compute/snapshots/write`.<br>- Google Cloud Logging<br>    - Captures modifications through `compute.snapshots.setIamPolicy` and `compute.snapshots.patch`.
