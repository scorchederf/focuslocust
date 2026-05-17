---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure - Requirements

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-requirements` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-requirements.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure - Requirements](../../topics/cloud/azure-requirements.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-requirements |
| name | Azure - Requirements |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-requirements.md |

## Preserved Source Material

```yaml
_body: "# Azure - Requirements\n\n## Pentest Requirements\n\nUsers and roles:\n\n* **Global Reader** and **Security Reader**\
  \ roles in Azure AD\n* **Reader** permission over the subscription\n\nSubscriptions:\n\n* [Azure Dev/Test](https://azure.microsoft.com/en-us/pricing/offers/dev-test)\
  \ subscription.\n* Visual Studio subscription determines the monthly Azure credits you receive\n    * Visual Studio Enterprise:\
  \ $150/month\n    * MSDN Platforms: $100\n    * Visual Studio Professional: $50\n    * Visual Studio Test Professional:\
  \ $50\n\n## Powershell and Native Modules\n\n* [Microsoft Graph](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0):\
  \ `Install-Module Microsoft.Graph -Scope CurrentUser`\n* [Azure AD](https://learn.microsoft.com/fr-fr/powershell/azure/active-directory/install-adv2?view=azureadps-2.0):\
  \ `Install-Module AzureAD`\n* [Azure AD Preview](https://learn.microsoft.com/fr-fr/powershell/azure/active-directory/install-adv2?view=azureadps-2.0):\
  \ `Install-Module AzureADPreview`\n* [Azure CLI](https://learn.microsoft.com/fr-fr/cli/azure/install-azure-cli-windows?tabs=winget):\
  \ `winget install -e --id Microsoft.AzureCLI`\n\n## Terminology\n\n* **Tenant**: An instance of Azure AD and represents\
  \ a single organization.\n* **Azure AD Directory**: Each tenant has a dedicated Directory. This is used to perform identity\
  \ and access management functions for resources.\n* **Subscriptions**: It is used to pay for services. There can be multiple\
  \ subscriptions in a Directory.\n* **Core Domain**: The initial domain name `<tenant>.onmicrosoft.com` is the core domain.\
  \ It is possible to define custom domain names too.\n\n## References\n\n* [Az - Permissions for a Pentest - HackTricks](https://cloud.hacktricks.xyz/pentesting-cloud/azure-security/az-permissions-for-a-pentest)\n\
  * [An introduction to penetration testing Azure - HollyGraceful - 06 August 2021](https://akimbocore.com/article/introduction-to-pentesting-azure/)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)"
_relative_path: cloud/azure/azure-requirements.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-requirements.md
```
