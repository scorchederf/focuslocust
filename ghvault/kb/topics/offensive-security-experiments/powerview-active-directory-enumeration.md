---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# PowerView: Active Directory Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-active-directory-enumeration-with-powerview` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-enumeration-with-powerview.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This lab explores a couple of common cmdlets of PowerView that allows for Active Directory/Domain enumeration.

## Preserved Body

````markdown
This lab explores a couple of common cmdlets of PowerView that allows for Active Directory/Domain enumeration.

## Get-NetDomain

Get current user's domain:

![](<../../_assets/powerview-getnetdomain.png>)

## Get-NetForest

Get information about the forest the current user's domain is in:

![](<../../_assets/powerview-forestinfo.png>)

## Get-NetForestDomain

Get all domains of the forest the current user is in:

![](<../../_assets/powerview-forest-domains.png>)

## Get-NetDomainController

Get info about the DC of the domain the current user belongs to:

![](<../../_assets/powerview-getdc.png>)

## Get-NetGroupMember

Get a list of domain members that belong to a given group:

![](<../../_assets/powerview-groups.png>)

## Get-NetLoggedon

Get users that are logged on to a given computer:

![](<../../_assets/powerview-connected-users.png>)

## Get-NetDomainTrust

Enumerate domain trust relationships of the current user's domain:

![](<../../_assets/powerview-domain-trusts.png>)

## Get-NetForestTrust

Enumerate forest trusts from the current domain's perspective:

![](<../../_assets/powerview-foresttrusts.png>)

## Get-NetProcess

Get running processes for a given remote machine:

```csharp
Get-NetProcess -ComputerName dc01 -RemoteUserName offense\administrator -RemotePassword 123456 | ft
```

![](<../../_assets/Screenshot from 2018-11-02 10-11-17.png>)

## Invoke-MapDomainTrust

Enumerate and map all domain trusts:

![](<../../_assets/powerview-all-domain-trusts.png>)

## Invoke-ShareFinder

Enumerate shares on a given PC - could be easily combines with other scripts to enumerate all machines in the domain:

![](<../../_assets/powerview-enumerate-shares.png>)

## Invoke-UserHunter

Find machines on a domain or users on a given machine that are logged on:

![](<../../_assets/powerview-invoke-user-hunter.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/powerview-active-directory-enumeration.md)

## Evidence Excerpt

```text
_asset_filenames:
- Screenshot from 2018-11-02 10-11-17.png
- powerview-all-domain-trusts.png
- powerview-connected-users.png
- powerview-domain-trusts.png
- powerview-enumerate-shares.png
- powerview-forest-domains.png
- powerview-forestinfo.png
```
