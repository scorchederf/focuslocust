---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Unloading Sysmon Driver

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-unloading-sysmon-driver` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/unloading-sysmon-driver.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

fltMC.exe unload SysmonDrv

## Preserved Body

````markdown
## Execution
```
fltMC.exe unload SysmonDrv
```
![](<../../_assets/sysmon-cmd.png>)

## Observations

Windows event logs suggesting `SysmonDrv` was unloaded successfully:

![](<../../_assets/sysmon-unload-log1.png>)

As well as processes requesting special privileges:

![](<../../_assets/sysmon-unload-log2.png>)

Note how in the last 35 minutes since the driver was unloaded, no further process creation events were recorded, although I spawned new processes during that time:

![](<../../_assets/sysmon-last-event.png>)

Note how the system thinks that the sysmon is still running, which it is, but not doing anything useful:

![](<../../_assets/sysmon-running.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/unloading-sysmon-driver.md)

## Evidence Excerpt

````text
_asset_filenames:
- sysmon-cmd.png
- sysmon-last-event.png
- sysmon-running.png
- sysmon-unload-log1.png
- sysmon-unload-log2.png
_body: "---\ndescription: >-\n  Unload sysmon driver which causes the system to stop recording sysmon event\n  logs.\n---\n\
\n# Unloading Sysmon Driver\n\n## Execution\n\n{% code title=\"attacker@victim\" %}\n```\nfltMC.exe unload SysmonDrv\n```\n\
````
