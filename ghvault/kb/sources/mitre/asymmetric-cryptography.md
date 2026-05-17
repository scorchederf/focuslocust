---
parsed_by: focuslocust
source: mitre
type: generated
---
# Asymmetric Cryptography

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1573.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1573.002 |
| name | Asymmetric Cryptography |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1573/002 |

## Preserved Source Material

```yaml
created: '2020-03-16T15:48:33.882Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic rather
  than relying on any inherent protections provided by a communication protocol. Asymmetric cryptography, also known as public
  key cryptography, uses a keypair per party: one public that can be freely distributed, and one private. Due to how the keys
  are generated, the sender encrypts data with the receiver’s public key and the receiver decrypts the data with their private
  key. This ensures that only the intended recipient can read the encrypted data. Common public key encryption algorithms
  include RSA and ElGamal.


  For efficiency, many protocols (including SSL/TLS) use symmetric cryptography once a connection is established, but use
  asymmetric cryptography to establish or transmit a key. As such, these protocols are classified as [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002).'
external_references:
- external_id: T1573.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1573/002
- description: Butler, M. (2013, November). Finding Hidden Threats by Decrypting SSL. Retrieved April 5, 2016.
  source_name: SANS Decrypting SSL
  url: http://www.sans.org/reading-room/whitepapers/analyst/finding-hidden-threats-decrypting-ssl-34840
- description: Dormann, W. (2015, March 13). The Risks of SSL Inspection. Retrieved April 5, 2016.
  source_name: SEI SSL Inspection Risks
  url: https://insights.sei.cmu.edu/cert/2015/03/the-risks-of-ssl-inspection.html
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--bf176076-b789-408e-8cba-7275e81c0ada
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:18.961Z'
name: Asymmetric Cryptography
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.2'
```
