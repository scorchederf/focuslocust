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

## Generated Concept Page

- [Unloading Sysmon Driver](../../topics/offensive-security/unloading-sysmon-driver.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-unloading-sysmon-driver |
| name | Unloading Sysmon Driver |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/unloading-sysmon-driver.md |

## Preserved Source Material

````yaml
_asset_filenames:
- sysmon-cmd.png
- sysmon-last-event.png
- sysmon-running.png
- sysmon-unload-log1.png
- sysmon-unload-log2.png
_body: "---\ndescription: >-\n  Unload sysmon driver which causes the system to stop recording sysmon event\n  logs.\n---\n\
  \n# Unloading Sysmon Driver\n\n## Execution\n\n{% code title=\"attacker@victim\" %}\n```\nfltMC.exe unload SysmonDrv\n```\n\
  {% endcode %}\n\n![](../../.gitbook/assets/sysmon-cmd.png)\n\n## Observations\n\nWindows event logs suggesting `SysmonDrv`\
  \ was unloaded successfully:\n\n![](../../.gitbook/assets/sysmon-unload-log1.png)\n\nAs well as processes requesting special\
  \ privileges:\n\n![](../../.gitbook/assets/sysmon-unload-log2.png)\n\nNote how in the last 35 minutes since the driver was\
  \ unloaded, no further process creation events were recorded, although I spawned new processes during that time:\n\n![](../../.gitbook/assets/sysmon-last-event.png)\n\
  \nNote how the system thinks that the sysmon is still running, which it is, but not doing anything useful:\n\n![](../../.gitbook/assets/sysmon-running.png)\n\
  \n## References\n\n{% embed url=\"https://twitter.com/Moti_B/status/1019307375847723008\" %}"
_relative_path: offensive-security/defense-evasion/unloading-sysmon-driver.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/unloading-sysmon-driver.md
````
