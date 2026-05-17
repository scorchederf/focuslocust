---
parsed_by: focuslocust
source: mitre
type: generated
---
# Private Keys

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Private Keys](../../attack/techniques/T1552.004-private-keys.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1552.004 |
| name | Private Keys |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1552/004 |

## Preserved Source Material

```yaml
created: '2020-02-04T13:06:49.258Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials.\
  \ Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures.(Citation:\
  \ Wikipedia Public Key Crypto) Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem,\
  \ .pfx, .cer, .p7b, .asc. \n\nAdversaries may also look in common key directories, such as <code>~/.ssh</code> for SSH keys\
  \ on * nix-based systems or <code>C:&#92;Users&#92;(username)&#92;.ssh&#92;</code> on Windows. Adversary tools may also\
  \ search compromised systems for file extensions relating to cryptographic keys and certificates.(Citation: Kaspersky Careto)(Citation:\
  \ Palo Alto Prince of Persia)\n\nWhen a device is registered to Entra ID, a device key and a transport key are generated\
  \ and used to verify the device’s identity.(Citation: Microsoft Primary Refresh Token) An adversary with access to the device\
  \ may be able to export the keys in order to impersonate the device.(Citation: AADInternals Azure AD Device Identities)\n\
  \nOn network devices, private keys may be exported via [Network Device CLI](https://attack.mitre.org/techniques/T1059/008)\
  \ commands such as `crypto pki export`.(Citation: cisco_deploy_rsa_keys) \n\nSome private keys require a password or passphrase\
  \ for operation, so an adversary may also use [Input Capture](https://attack.mitre.org/techniques/T1056) for keylogging\
  \ or attempt to [Brute Force](https://attack.mitre.org/techniques/T1110) the passphrase off-line. These private keys can\
  \ be used to authenticate to [Remote Services](https://attack.mitre.org/techniques/T1021) like SSH or for use in decrypting\
  \ other collected files such as email."
external_references:
- external_id: T1552.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1552/004
- description: Bar, T., Conant, S., Efraim, L. (2016, June 28). Prince of Persia – Game Over. Retrieved July 5, 2017.
  source_name: Palo Alto Prince of Persia
  url: https://researchcenter.paloaltonetworks.com/2016/06/unit42-prince-of-persia-game-over/
- description: 'Cisco. (2023, February 17). Chapter: Deploying RSA Keys Within a PKI . Retrieved March 27, 2023.'
  source_name: cisco_deploy_rsa_keys
  url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436
- description: Dr. Nestori Syynimaa. (2022, February 15). Stealing and faking Azure AD device identities. Retrieved February
    21, 2023.
  source_name: AADInternals Azure AD Device Identities
  url: https://aadinternals.com/post/deviceidentity/
- description: Kaspersky Labs. (2014, February 11). Unveiling “Careto” - The Masked APT. Retrieved July 5, 2017.
  source_name: Kaspersky Careto
  url: https://web.archive.org/web/20141031134104/http://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/unveilingthemask_v1.0.pdf
- description: Microsoft. (2022, September 9). What is a Primary Refresh Token?. Retrieved February 21, 2023.
  source_name: Microsoft Primary Refresh Token
  url: https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token
- description: Wikipedia. (2017, June 29). Public-key cryptography. Retrieved July 5, 2017.
  source_name: Wikipedia Public Key Crypto
  url: https://en.wikipedia.org/wiki/Public-key_cryptography
id: attack-pattern--60b508a1-6a5e-46b1-821a-9f7b78752abf
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:50.819Z'
name: Private Keys
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Itzik Kotler, SafeBreach
- Austin Clark, @c2defense
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.3'
```
