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

## Summary

Users and roles:

## Preserved Body

```markdown
## Pentest Requirements

Users and roles:

* **Global Reader** and **Security Reader** roles in Azure AD
* **Reader** permission over the subscription

Subscriptions:

* [Azure Dev/Test](https://azure.microsoft.com/en-us/pricing/offers/dev-test) subscription.
* Visual Studio subscription determines the monthly Azure credits you receive
    * Visual Studio Enterprise: $150/month
    * MSDN Platforms: $100
    * Visual Studio Professional: $50
    * Visual Studio Test Professional: $50

## Powershell and Native Modules

* [Microsoft Graph](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0): `Install-Module Microsoft.Graph -Scope CurrentUser`
* [Azure AD](https://learn.microsoft.com/fr-fr/powershell/azure/active-directory/install-adv2?view=azureadps-2.0): `Install-Module AzureAD`
* [Azure AD Preview](https://learn.microsoft.com/fr-fr/powershell/azure/active-directory/install-adv2?view=azureadps-2.0): `Install-Module AzureADPreview`
* [Azure CLI](https://learn.microsoft.com/fr-fr/cli/azure/install-azure-cli-windows?tabs=winget): `winget install -e --id Microsoft.AzureCLI`

## Terminology

* **Tenant**: An instance of Azure AD and represents a single organization.
* **Azure AD Directory**: Each tenant has a dedicated Directory. This is used to perform identity and access management functions for resources.
* **Subscriptions**: It is used to pay for services. There can be multiple subscriptions in a Directory.
* **Core Domain**: The initial domain name `<tenant>.onmicrosoft.com` is the core domain. It is possible to define custom domain names too.

## References

* [Az - Permissions for a Pentest - HackTricks](https://cloud.hacktricks.xyz/pentesting-cloud/azure-security/az-permissions-for-a-pentest)
* [An introduction to penetration testing Azure - HollyGraceful - 06 August 2021](https://akimbocore.com/article/introduction-to-pentesting-azure/)
* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)
```

## Source Verification

[source record](../../sources/internalallthethings/azure-requirements.md)

## Evidence Excerpt

```text
_body: "# Azure - Requirements\n\n## Pentest Requirements\n\nUsers and roles:\n\n* **Global Reader** and **Security Reader**\
\ roles in Azure AD\n* **Reader** permission over the subscription\n\nSubscriptions:\n\n* [Azure Dev/Test](https://azure.microsoft.com/en-us/pricing/offers/dev-test)\
\ subscription.\n* Visual Studio subscription determines the monthly Azure credits you receive\n    * Visual Studio Enterprise:\
\ $150/month\n    * MSDN Platforms: $100\n    * Visual Studio Professional: $50\n    * Visual Studio Test Professional:\
\ $50\n\n## Powershell and Native Modules\n\n* [Microsoft Graph](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0):\
\ `Install-Module Microsoft.Graph -Scope CurrentUser`\n* [Azure AD](https://learn.microsoft.com/fr-fr/powershell/azure/active-directory/install-adv2?view=azureadps-2.0):\
\ `Install-Module AzureAD`\n* [Azure AD Preview](https://learn.microsoft.com/fr-fr/powershell/azure/active-directory/install-adv2?view=azureadps-2.0):\
\ `Install-Module AzureADPreview`\n* [Azure CLI](https://learn.microsoft.com/fr-fr/cli/azure/install-azure-cli-windows?tabs=winget):\
```
