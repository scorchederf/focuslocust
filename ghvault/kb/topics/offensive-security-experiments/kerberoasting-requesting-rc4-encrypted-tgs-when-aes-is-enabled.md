---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Kerberoasting: Requesting RC4 Encrypted TGS when AES is Enabled

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-kerberoasting-requesting-rc4-encrypted-tgs-when-aes-is-enabled` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/kerberoasting-requesting-rc4-encrypted-tgs-when-aes-is-enabled.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It is possible to kerberoast a user account with SPN even if the account supports Kerberos AES encryption by requesting an RC4 ecnrypted (instead of AES) TGS which easier to crack.

## Preserved Body

````markdown
It is possible to kerberoast a user account with SPN even if the account supports Kerberos AES encryption by requesting an RC4 ecnrypted (instead of AES) TGS which easier to crack.

## Execution

First off, let's confirm we have at least one user with an SPN set:
```
Get-NetUser -SPN sandy
```
![](<../../_assets/Screenshot from 2019-05-06 15-37-30.png>)

Since the user account does not support Kerberos AES ecnryption by default, when requesting a TGS ticket for kerberoasting with rubeus, we will get an RC4 encrypted ticket:
```
F:\Rubeus\Rubeus.exe kerberoast /user:sandy
```
![](<../../_assets/Screenshot from 2019-05-06 15-39-53.png>)

If the user is now set to support AES encryption:

![](<../../_assets/Screenshot from 2019-05-06 15-40-51.png>)

By default, returned tickets will be encrypted with the highest possible encryption algorithm, which is AES:
```
F:\Rubeus\Rubeus.exe kerberoast /user:sandy
```
![](<../../_assets/Screenshot from 2019-05-06 15-58-37.png>)

## Requesting RC4 Encrypted Ticket

As mentioned in the beginning, it's still possible to request an RC4 ecnrypted ticket (if RC4 is not disabled in the environment, which does not seem to be common yet):
```
F:\Rubeus\Rubeus.exe kerberoast /tgtdeleg
```
Even though AES encryption is supported by both parties, a TGS ticket encrypted with RC4 (encryption type 0x17/23) was returned. Note that SOCs may be monitoring for tickets encrypted with RC4:

![](<../../_assets/Screenshot from 2019-05-06 16-03-06.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/kerberoasting-requesting-rc4-encrypted-tgs-when-aes-is-enabled.md)

## Evidence Excerpt

```text
_asset_filenames:
- Screenshot from 2019-05-06 15-37-30.png
- Screenshot from 2019-05-06 15-39-53.png
- Screenshot from 2019-05-06 15-40-51.png
- Screenshot from 2019-05-06 15-58-37.png
- Screenshot from 2019-05-06 16-03-06.png
_body: '# Kerberoasting: Requesting RC4 Encrypted TGS when AES is Enabled
It is possible to kerberoast a user account with SPN even if the account supports Kerberos AES encryption by requesting
```
