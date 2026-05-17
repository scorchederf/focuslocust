---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Detecting Sysmon on the Victim Host

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-detecting-sysmon-on-the-victim-host` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/detecting-sysmon-on-the-victim-host.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

csharp

## Preserved Body

````markdown
## Processes
```csharp
PS C:\> Get-Process | Where-Object { $_.ProcessName -eq "Sysmon" }
```
![](<../../_assets/Screenshot from 2018-10-09 17-39-28.png>)
Note: process name can be changed during installation
## Services
```csharp
Get-CimInstance win32_service -Filter "Description = 'System Monitor service'"
# or
Get-Service | where-object {$_.DisplayName -like "*sysm*"}
```
![](<../../_assets/Screenshot from 2018-10-09 17-48-11.png>)
Note: display names and descriptions can be changed
## Windows Events
```csharp
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Sysmon/Operational
```
![](<../../_assets/Screenshot from 2018-10-09 17-50-47.png>)

## Filters
```
PS C:\> fltMC.exe
```
Note how even though you can change the sysmon service and driver names, the sysmon altitude is always the same - `385201`

![](<../../_assets/Screenshot from 2018-10-09 17-51-45.png>)

## Sysmon Tools + Accepted Eula
```
ls HKCU:\Software\Sysinternals
```
![](<../../_assets/Screenshot from 2018-10-09 17-56-33.png>)

## Sysmon -c

Once symon executable is found, the config file can be checked like so:

```
sysmon -c
```

![](<../../_assets/Screenshot from 2018-10-09 18-43-39.png>)

## Config File on the Disk

If you are lucky enough, you may be able to find the config file itself on the disk by using native windows utility findstr:
```csharp
findstr /si '<ProcessCreate onmatch="exclude">' C:\tools\*
```
![](<../../_assets/Screenshot from 2018-10-09 18-57-32.png>)

## Get-SysmonConfiguration

A powershell tool by @mattifestation that extracts sysmon rules from the registry:
```csharp
PS C:\tools> (Get-SysmonConfiguration).Rules
```
![](<../../_assets/Screenshot from 2018-10-09 18-12-09.png>)

As an example, looking a bit deeper into the `ProcessCreate` rules:
```csharp
(Get-SysmonConfiguration).Rules[0].Rules
```
We can see the rules almost as they were presented in the sysmon configuration XML file:

![](<../../_assets/Screenshot from 2018-10-09 18-13-37.png>)

A snippet from the actual sysmonconfig-export.xml file:

![](<../../_assets/Screenshot from 2018-10-09 18-14-57.png>)

## Bypassing Sysmon

Since [Get-SysmonConfiguration](detecting-sysmon-on-the-victim-host.md#get-sysmonconfiguration) gives you the ability to see the rules sysmon is monitoring on, you can play around those.

Another way to bypass the sysmon altogether is explored here:
[unloading-sysmon-driver.md](../defense-evasion/unloading-sysmon-driver.md)
## References
````

## Source Verification

[source record](../../sources/redteamingtactics/detecting-sysmon-on-the-victim-host.md)

## Evidence Excerpt

```text
_asset_filenames:
- Screenshot from 2018-10-09 17-39-28.png
- Screenshot from 2018-10-09 17-48-11.png
- Screenshot from 2018-10-09 17-50-47.png
- Screenshot from 2018-10-09 17-51-45.png
- Screenshot from 2018-10-09 17-56-33.png
- Screenshot from 2018-10-09 18-12-09.png
- Screenshot from 2018-10-09 18-13-37.png
```
