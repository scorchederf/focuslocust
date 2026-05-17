---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Deployment Template

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-deployment-template` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-deployment-template.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Deployment Template](../../topics/cloud/azure-services-deployment-template.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-deployment-template |
| name | Azure Services - Deployment Template |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-deployment-template.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Deployment Template\n\n* List the deployments\n\n    ```powershell\n    PS Az> Get-AzResourceGroup\n\
  \    PS Az> Get-AzResourceGroupDeployment -ResourceGroupName SAP\n    ```\n\n* Export the deployment template\n\n    ```ps1\n\
  \    PS Az> Save-AzResourceGroupDeploymentTemplate -ResourceGroupName <RESOURCE GROUP> -DeploymentName <DEPLOYMENT NAME>\n\
  \    \n    # search for hardcoded password\n    cat <DEPLOYMENT NAME>.json \n    cat <PATH TO .json FILE> | Select-String\
  \ password\n    ```\n\n## References\n\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-deployment-template.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-deployment-template.md
````
