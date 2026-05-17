---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Modifying .lnk Shortcuts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-modifying-.lnk-shortcuts` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/modifying-.lnk-shortcuts.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Modifying .lnk Shortcuts](../../topics/offensive-security/modifying-.lnk-shortcuts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-modifying-.lnk-shortcuts |
| name | Modifying .lnk Shortcuts |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/modifying-.lnk-shortcuts.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (432).png
- image (433).png
- image (434).png
- image (435).png
- image (436).png
- lnk-hijacking-minimized.gif
- lnk-hijacking.gif
_body: '# Modifying .lnk Shortcuts


  This is a quick lab showing how .lnk (shortcut files) can be used for persistence.


  ## Execution


  Say, there''s a shortcut on the compromised system for a program HxD64 as shown below:


  ![](<../../.gitbook/assets/image (432).png>)


  . That shortcut can be hijacked and used for persistence. Let''s change the shortcut''s target to this simple powershell:


  ```csharp

  powershell.exe -c "invoke-item \\VBOXSVR\Tools\HxD\HxD64.exe; invoke-item c:\windows\system32\calc.exe"

  ```


  It will launch the HxD64, but will also launch a program of our choice - a calc.exe in this case. Notice how the shortcut
  icon changed to powershell - that is expected:


  ![](<../../.gitbook/assets/image (433).png>)


  We can change it back by clicking "Change Icon" and specifying the original .exe of HxD64.exe:


  ![](<../../.gitbook/assets/image (434).png>)


  The original icon is now back:


  ![](<../../.gitbook/assets/image (435).png>)


  ## Demo


  Below shows the hijack demo in action:


  ![](../../.gitbook/assets/lnk-hijacking.gif)


  In the above gif, we can see the black cmd prompt for a brief moment, however, it can be easily be hidden by changing the
  `Run` option of the shortcut to `Minimized`:


  ![](<../../.gitbook/assets/image (436).png>)


  Running the demo again with the `Run: Minimized` shows the black prompt went away:


  ![](../../.gitbook/assets/lnk-hijacking-minimized.gif)


  {% hint style="warning" %}

  Note that hovering the shortcut reveals that the program to be launched is the powershell.

  {% endhint %}


  ## Reference


  {% embed url="https://attack.mitre.org/techniques/T1023/" %}'
_relative_path: offensive-security/persistence/modifying-.lnk-shortcuts.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/modifying-.lnk-shortcuts.md
````
