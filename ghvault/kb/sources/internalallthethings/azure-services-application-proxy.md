---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Application Proxy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-application-proxy` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-proxy.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Application Proxy](../../topics/cloud/azure-services-application-proxy.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-application-proxy |
| name | Azure Services - Application Proxy |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-application-proxy.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Application Proxy\n\n## Enumerate\n\n* Enumerate applications that have Proxy\n\n    ```powershell\n\
  \    PS C:\\Tools> Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}\n\
  \    PS C:\\Tools> Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq \"Finance Management System\"}\n\n    PS\
  \ C:\\Tools> . C:\\Tools\\GetApplicationProxyAssignedUsersAndGroups.ps1\n    PS C:\\Tools> Get-ApplicationProxyAssignedUsersAndGroups\
  \ -ObjectId <OBJECT-ID>\n    ```\n\n## References\n\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-application-proxy.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-proxy.md
````
