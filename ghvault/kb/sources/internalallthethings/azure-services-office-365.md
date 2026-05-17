---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Office 365

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-office-365` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-office-365.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Office 365](../../topics/cloud/azure-services-office-365.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-office-365 |
| name | Azure Services - Office 365 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-office-365.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Office 365\n\n## Microsoft Teams Messages\n\n```ps1\nTokenTacticsV2> RefreshTo-MSTeamsToken -domain\
  \ domain.local\nAADInternals> Get-AADIntTeamsMessages -AccessToken $MSTeamsToken.access_token | Format-Table id,content,deletiontime,*type*,DisplayName\n\
  ```\n\n## Outlook Mails\n\n* Read user mails\n\n    ```ps1\n    Get-MgUserMessage -UserId <user-id> | ft\n    Get-MgUserMessageContent\
  \ -OutFile mail.txt -UserId <user-id> -MessageId <message-id>\n    ```\n\n## OneDrive Files\n\n```ps1\n$userId = \"<user-id>\"\
  \nImport-Module Microsoft.Graph.Files\nGet-MgUserDefaultDrive -UserId $userId\nGet-MgUserDrive -UserId $UserId  -Debug\n\
  Get-MgDrive -top 1\n```\n\n## References\n\n* [Pentesting Azure Mindmap - Alexis Danizan](https://github.com/synacktiv/Mindmaps)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-office-365.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-office-365.md
````
