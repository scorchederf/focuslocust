---
parsed_by: focuslocust
source: mitre
type: generated
---
# Encrypt Sensitive Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1041` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Encrypt Sensitive Information](../../attack/mitigations/M1041-encrypt-sensitive-information.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1041 |
| name | Encrypt Sensitive Information |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1041 |

## Preserved Source Material

```yaml
created: '2019-06-11T16:43:44.834Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms.
  Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation
  can be implemented through the following measures:


  Encrypt Data at Rest:


  - Use Case: Use full-disk encryption or file-level encryption to secure sensitive data stored on devices.

  - Implementation: Implement BitLocker for Windows systems or FileVault for macOS devices to encrypt hard drives.


  Encrypt Data in Transit:


  - Use Case: Use secure communication protocols (e.g., TLS, HTTPS) to encrypt sensitive data as it travels over networks.

  - Implementation: Enable HTTPS for all web applications and configure mail servers to enforce STARTTLS for email encryption.


  Encrypt Backups:


  - Use Case: Ensure that backup data is encrypted both during storage and transfer to prevent unauthorized access.

  - Implementation: Encrypt cloud backups using AES-256 before uploading them to Amazon S3 or Google Cloud.


  Encrypt Application Secrets:


  - Use Case: Store sensitive credentials, API keys, and configuration files in encrypted vaults.

  - Implementation: Use HashiCorp Vault or AWS Secrets Manager to manage and encrypt secrets.


  Database Encryption:


  - Use Case: Enable Transparent Data Encryption (TDE) or column-level encryption in database management systems.

  - Implementation: Use MySQL’s built-in encryption features to encrypt sensitive database fields such as social security
  numbers.'
external_references:
- external_id: M1041
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1041
id: course-of-action--feff9142-e8c2-46f4-842b-bd6fb3d41157
modified: '2025-04-02T17:28:57.029Z'
name: Encrypt Sensitive Information
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.1'
```
