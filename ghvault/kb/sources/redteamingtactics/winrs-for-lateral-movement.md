---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WinRS for Lateral Movement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-winrs-for-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/winrs-for-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WinRS for Lateral Movement](../../topics/offensive-security/winrs-for-lateral-movement.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-winrs-for-lateral-movement |
| name | WinRS for Lateral Movement |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/winrs-for-lateral-movement.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (669).png
_body: '# WinRS for Lateral Movement


  It''s possible to use a native Windows binary `winrs` to connect to a remote endpoint via `WinRM` like so:


  ```

  winrs -r:ws01 "cmd /c hostname & notepad"

  ```


  Below shows how we connect from `DC01` to `WS01` and execute two processes `hostname`,`notepad` and the process partent/child
  relationship for processes spawned by the `winrshost.exe`:


  ![](<../../.gitbook/assets/image (669).png>)


  ## References


  {% embed url="https://bohops.com/2020/05/12/ws-management-com-another-approach-for-winrm-lateral-movement/amp/" %}'
_relative_path: offensive-security/lateral-movement/winrs-for-lateral-movement.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/winrs-for-lateral-movement.md
````
