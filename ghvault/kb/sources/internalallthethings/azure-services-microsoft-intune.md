---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Microsoft Intune

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-microsoft-intune` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-microsoft-intune.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Microsoft Intune](../../topics/cloud/azure-services-microsoft-intune.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-microsoft-intune |
| name | Azure Services - Microsoft Intune |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-microsoft-intune.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Microsoft Intune\n\nMicrosoft Intune is a cloud-based service that provides mobile device management\
  \ (MDM) and mobile application management (MAM). It allows organizations to control and secure access to corporate data\
  \ on mobile devices, including smartphones, tablets, and PCs. With Intune, businesses can enforce security policies, manage\
  \ apps, and ensure that devices comply with organizational requirements, whether they are company-owned or personal (BYOD).\n\
  \n## Intunes Administration\n\n**Requirements**:\n\n* **Global Administrator** or **Intune Administrator** Privilege\n\n\
  \    ```powershell\n    Get-AzureADGroup -Filter \"DisplayName eq 'Intune Administrators'\"\n    ```\n\n**Walkthrough**\n\
  \n1. Login into <https://endpoint.microsoft.com/#home> or use Pass-The-PRT\n2. Go to **Devices** -> **All Devices** to check\
  \ devices enrolled to Intune\n3. Go to **Scripts** and click on **Add** for Windows 10.\n4. Add a **Powershell script**\n\
  5. Specify **Add all users** and **Add all devices** in the **Assignments** page.\n\n:warning: It will take up to one hour\
  \ before you script is executed !\n\n## Intune Scripts\n\n**Requirements**:\n\n* App with permission: `DeviceManagementConfiguration.Read.All`\n\
  * `Microsoft.Graph.Intune` dependency installed: `Install-Module Microsoft.Graph.Intune`\n\n**Extract Intune scripts**:\n\
  \nThe following scripts are deprecated, use `MgGraph` instead of `MsGraph`, and change the appropriate function `InvokeMgGraph`\
  \ too.\n\n* [okieselbach/Get-DeviceManagementScripts.ps1](https://raw.githubusercontent.com/okieselbach/Intune/master/Get-DeviceManagementScripts.ps1)\
  \ - Get all or individual Intune PowerShell scripts and save them in specified folder.\n\n    ```ps1\n    Get-DeviceManagementScripts\
  \ -FolderPath C:\\temp -FileName myScript.ps1\n    ```\n\n* [okieselbach/Get-DeviceHealthScripts.ps1](https://raw.githubusercontent.com/okieselbach/Intune/master/Get-DeviceHealthScripts.ps1)\
  \ - Get all or individual Intune PowerShell Health scripts (aka Proactive Remediation scripts) and save them in specified\
  \ folder.\n\n    ```ps1\n    Get-DeviceHealthScripts -FolderPath C:\\temp\\HealthScripts\n    ```\n\n* [secureworks/pytune](https://github.com/secureworks/pytune)\
  \ - Pytune is a post-exploitation tool for enrolling a fake device into Intune with mulitple platform support.\n\n    ```ps1\n\
  \    python3 pytune.py entra_join -o Windows -d Windows_pytune -u testuser@*******.onmicrosoft.com -p ***********  \n  \
  \  python3 pytune.py enroll_intune -o Windows -d Windows_pytune -c Windows_pytune.pfx -u testuser@*******.onmicrosoft.com\
  \ -p *********** \n    python3 pytune.py download_apps -d Windows_pytune -m Windows_pytune_mdm.pfx\n    ```\n\n## LAPS\n\
  \nSome organization have recreated LAPS for Azure devices using Intune scripts.\n\n```ps1\n#requires -modules Microsoft.Graph.Authentication\n\
  #requires -modules Microsoft.Graph.Intune\n#requires -modules LAPS\n#requires -modules ImportExcel\n\n$DaysBack = 30\nConnect-MgGraph\n\
  Get-IntuneManagedDevice -Filter \"Platform eq 'Windows'\" |\n    Foreach-Object {Get-LapsAADPassword -DevicesIds $_.DisplayName}\
  \ |\n        Where-Object {$_.PasswordExpirationTime -lt (Get-Date).AddDays(-$DaysBack)} |\n            Export-Excel -Path\
  \ \"c:\\temp\\lapsdata.xlsx\" - ClearSheet -AutoSize -Show\n```\n\n## References\n\n* [Microsoft Intune - Microsoft Intune\
  \ support for Windows LAPS](https://learn.microsoft.com/en-us/mem/intune/protect/windows-laps-overview)\n* [Training - Attacking\
  \ and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)\n* [Get back your Intune Proactive\
  \ Remediation Scripts - Oliver Kieselbach - September 7, 2022](https://oliverkieselbach.com/2022/09/07/get-back-your-intune-proactive-remediation-scripts/)\n\
  * [Get back your Intune PowerShell Scripts - Oliver Kieselbach - February 6, 2020](https://oliverkieselbach.com/2020/02/06/get-back-your-intune-powershell-scripts/)"
_relative_path: cloud/azure/azure-services-microsoft-intune.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-microsoft-intune.md
````
