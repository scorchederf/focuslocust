---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Application Endpoint

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-application-endpoint` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-endpoint.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Application Endpoint](../../topics/cloud/azure-services-application-endpoint.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-application-endpoint |
| name | Azure Services - Application Endpoint |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-application-endpoint.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Application Endpoint\n\n## Enumerate\n\n* Enumerate possible endpoints for applications starting/ending\
  \ with PREFIX\n\n    ```powershell\n    PS C:\\Tools> Get-AzureADServicePrincipal -All $true -Filter \"startswith(displayName,'PREFIX')\"\
  \ | % {$_.ReplyUrls}\n    PS C:\\Tools> Get-AzureADApplication -All $true -Filter \"endswith(displayName,'PREFIX')\" | Select-Object\
  \ ReplyUrls,WwwHomePage,HomePage\n    ```\n\n## Access\n\n```ps1\nhttps://myapps.microsoft.com/signin/<App ID>?tenantId=<TenantID>\n\
  ```\n\n## References\n\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-application-endpoint.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-application-endpoint.md
````
