---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Forfiles Indirect Command Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1202-forfiles-indirect-command-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1202-forfiles-indirect-command-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Forfiles Indirect Command Execution](../../topics/offensive-security/forfiles-indirect-command-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-t1202-forfiles-indirect-command-execution |
| name | Forfiles Indirect Command Execution |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/t1202-forfiles-indirect-command-execution.md |

## Preserved Source Material

````yaml
_asset_filenames:
- forfiles-ancestry.png
- forfiles-cmdline.png
- forfiles-executed.png
_body: '---

  description: Defense Evasion

  ---


  # Forfiles Indirect Command Execution


  This technique launches an executable without a cmd.exe.


  ## Execution


  ```csharp

  forfiles /p c:\windows\system32 /m notepad.exe /c calc.exe

  ```


  ![](../../.gitbook/assets/forfiles-executed.png)


  ## Observations


  Defenders can monitor for process creation/commandline logs to detect this activity:


  ![](../../.gitbook/assets/forfiles-ancestry.png)


  ![](../../.gitbook/assets/forfiles-cmdline.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1202" %}'
_relative_path: offensive-security/code-execution/t1202-forfiles-indirect-command-execution.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1202-forfiles-indirect-command-execution.md
````
