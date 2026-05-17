---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# TLS & Certificates

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-crypto-tls-and-certificates-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/crypto/tls-and-certificates/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [TLS & Certificates](../../topics/crypto/tls-and-certificates.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-crypto-tls-and-certificates-readme |
| name | TLS & Certificates |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/crypto/tls-and-certificates/README.md |

## Preserved Source Material

````yaml
_body: '# TLS & Certificates


  {{#include ../../banners/hacktricks-training.md}}


  This area is about **X.509 parsing, formats, conversions, and common mistakes**.


  ## X.509: parsing, formats & common mistakes


  ### Quick parsing


  ```bash

  openssl x509 -in cert.pem -noout -text

  openssl asn1parse -in cert.pem

  ```


  Useful fields to inspect:


  - Subject / Issuer / SAN

  - Key Usage / EKU

  - Basic Constraints (is it a CA?)

  - Validity window (NotBefore/NotAfter)

  - Signature algorithm (MD5? SHA1?)


  ### Formats & conversion


  - PEM (Base64 with BEGIN/END headers)

  - DER (binary)

  - PKCS#7 (`.p7b`) (cert chain, no private key)

  - PKCS#12 (`.pfx/.p12`) (cert + private key + chain)


  Conversions:


  ```bash

  openssl x509 -in cert.cer -outform PEM -out cert.pem

  openssl x509 -in cert.pem -outform der -out cert.der

  openssl pkcs12 -in file.pfx -out out.pem

  ```


  ### Common offensive angles


  - Trusting user-provided roots / missing chain validation

  - Weak signature algorithms (legacy)

  - Name constraints / SAN parsing bugs (implementation-specific)

  - Confused deputy issues with client-certificate authentication misbinding


  ### CT logs


  - [https://crt.sh/](https://crt.sh/)


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: crypto/tls-and-certificates/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/crypto/tls-and-certificates/README.md
````
