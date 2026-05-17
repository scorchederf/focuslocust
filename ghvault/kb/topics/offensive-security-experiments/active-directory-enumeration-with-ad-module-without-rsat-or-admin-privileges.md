---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Active Directory Enumeration with AD Module without RSAT or Admin Privileges

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-active-directory-enumeration-with-ad-module-without-rsat-or-admin-privileges` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-enumeration-with-ad-module-without-rsat-or-admin-privileges.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This lab shows how it is possible to use Powershell to enumerate Active Directory with Powershell's Active Directory module on a domain joined machine that does not have Remote Server Administration Toolkit (RSAT) installed on it. Installin

## Preserved Body

````markdown
This lab shows how it is possible to use Powershell to enumerate Active Directory with Powershell's `Active Directory` module on a domain joined machine that does not have Remote Server Administration Toolkit (RSAT) installed on it. Installing RSAT requires admin privileges and is actually what makes the AD Powershell module available and this lab shows how to bypass this obstacle.

## Execution

The secret to being able to run AD enumeration commands from the AD Powershell module on a system without RSAT installed, is the DLL located in `C:\Windows\Microsoft.NET\assembly\GAC_64\Microsoft.ActiveDirectory.Management` on a system that **has the RSAT** installed:

![](<../../_assets/Screenshot from 2019-02-03 14-20-10.png>)

This means that we can just grab the DLL from the system with RSAT and drop it on the system we want to enumerate from (that does not have RSAT installed) and simply import that DLL as a module:

```csharp
Import-Module .\Microsoft.ActiveDirectory.Management.dll
```

Note how before we import the module, `Get-Command get-adcom*` returns nothing, but that changes once we import the module:

![](<../../_assets/Screenshot from 2019-02-03 14-23-34.png>)

As mentioned earlier, this does not require the user have admin privileges:

![](<../../_assets/Screenshot from 2019-02-03 14-37-35.png>)

## Download Management.DLL
Microsoft.ActiveDirectory.Management.dll
## Reference
````

## Source Verification

[source record](../../sources/redteamingtactics/active-directory-enumeration-with-ad-module-without-rsat-or-admin-privileges.md)

## Evidence Excerpt

```text
_asset_filenames:
- Screenshot from 2019-02-03 14-20-10.png
- Screenshot from 2019-02-03 14-23-34.png
- Screenshot from 2019-02-03 14-37-35.png
_body: '# Active Directory Enumeration with AD Module without RSAT or Admin Privileges
This lab shows how it is possible to use Powershell to enumerate Active Directory with Powershell''s `Active Directory`
module on a domain joined machine that does not have Remote Server Administration Toolkit (RSAT) installed on it. Installing
RSAT requires admin privileges and is actually what makes the AD Powershell module available and this lab shows how to bypass
```
