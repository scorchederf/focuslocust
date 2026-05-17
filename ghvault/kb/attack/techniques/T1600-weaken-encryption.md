---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1600 - Weaken Encryption

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1600` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would otherwise protect data communications.

Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer keys increase the cost of cryptanalysis, or decryption without the key.

Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors such as Modify System Image, Reduce Key Space, and Disable Crypto Hardware, an adversary can negatively effect and/or eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and may help facilitate data manipulation, Credential Access, or Collection efforts.

## Source Verification

[source record](../../sources/mitre/weaken-encryption.md)

## Evidence Excerpt

```text
created: '2020-10-19T18:47:08.759Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would
otherwise protect data communications.(Citation: Cisco Synful Knock Evolution)
Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized
disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message
to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer
keys increase the cost of cryptanalysis, or decryption without the key.
```
