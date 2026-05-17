---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure AD - Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-persistence` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-persistence.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure AD - Persistence](../../topics/cloud/azure-ad-persistence.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-persistence |
| name | Azure AD - Persistence |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-persistence.md |

## Preserved Source Material

````yaml
_body: "# Azure AD - Persistence\n\n## Add Secrets to Application\n\n* Add secrets with [lutzenfried/OffensiveCloud/Add-AzADAppSecret.ps1](https://github.com/lutzenfried/OffensiveCloud/blob/main/Azure/Tools/Add-AzADAppSecret.ps1)\n\
  \n    ```powershell\n    PS > . C:\\Tools\\Add-AzADAppSecret.ps1\n    PS > Add-AzADAppSecret -GraphToken $graphtoken -Verbose\n\
  \    ```\n\n* Use secrets to authenticate as Service Principal\n\n    ```ps1\n    PS > $password = ConvertTo-SecureString\
  \ '<SECRET/PASSWORD>' -AsPlainText -Force\n    PS > $creds = New-Object System.Management.Automation.PSCredential('<AppID>',\
  \ $password)\n    PS > Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '<TenantID>'\n    ```\n\n## Add Service\
  \ Principal\n\n* Generate a new service principal password/secret\n\n    ```ps1\n    Import-Module Microsoft.Graph.Applications\n\
  \    Connect-MgGraph \n    $servicePrincipalId = \"<service-principal-id>\"\n\n    $params = @{\n        passwordCredential\
  \ = @{\n            displayName = \"NewCreds\"\n        }\n    }\n    Add-MgServicePrincipalPassword -ServicePrincipalId\
  \ $servicePrincipalId -BodyParameter $params\n    ```\n\n## Add User to Group\n\n```ps1\nAdd-AzureADGroupMember -ObjectId\
  \ <group_id> -RefObjectId <user_id> -Verbose\n```\n\n## PowerShell Profile Backdoor Using KFM\n\nOneDrive for Business Known\
  \ Folder Move (KFM) is a feature in Microsoft OneDrive for Business that enables users and organizations to automatically\
  \ redirect the contents of key Windows user folders; Desktop, Documents, and Pictures from their local PC to OneDrive.\n\
  \nA PowerShell profile is a script file that loads whenever you start a new PowerShell session (such as opening PowerShell\
  \ or Windows Terminal). Users and administrators often customize their profiles to set aliases, environment variables, functions,\
  \ or pre-load modules.\n\n**Requirements**:\n\n* `Files.ReadWrite.All` privilege\n\n**Methodology**:\n\nKnown Folder Move\
  \ moves the user's Documents (and/or Desktop, Pictures) folder to OneDrive for Business, typically syncing:\n\n```ps1\n\
  C:\\Users\\<username>\\Documents → C:\\Users\\<username>\\OneDrive - <TenantName>\\Documents\n```\n\nThis means the PowerShell\
  \ profile file (`Documents\\PowerShell\\Microsoft.PowerShell_profile.ps1`) will now be synced to OneDrive.\n\nPush a malicious\
  \ PowerShell profile at `$HOME\\Documents\\PowerShell\\Microsoft.PowerShell_profile.ps1`.\n\n## References\n\n* [High-Profile\
  \ Cloud Privesc - Leonidas Tsaousis - July 15, 2025](https://labs.reversec.com/posts/2025/07/high-profile-cloud-privesc)\n\
  * [Maintaining Azure Persistence via automation accounts - Karl Fosaaen - September 12, 2019](https://blog.netspi.com/maintaining-azure-persistence-via-automation-accounts/)\n\
  * [Microsoft Graph - servicePrincipal: addPassword](https://learn.microsoft.com/en-us/graph/api/serviceprincipal-addpassword?view=graph-rest-1.0&tabs=powershell)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-persistence.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-persistence.md
````
