---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data Loss Prevention

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1057` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data Loss Prevention](../../attack/mitigations/M1057-data-loss-prevention.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1057 |
| name | Data Loss Prevention |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1057 |

## Preserved Source Material

```yaml
created: '2021-08-04T21:22:11.612Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor,
  and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally
  Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration.
  DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental
  or malicious data leaks. (Citation: PurpleSec Data Loss Prevention) This mitigation can be implemented through the following
  measures:


  Sensitive Data Categorization:


  - Use Case: Identify and classify data based on sensitivity (e.g., PII, financial data, trade secrets).

  - Implementation: Use DLP solutions to scan and tag files containing sensitive information using predefined patterns, such
  as Social Security Numbers or credit card details.


  Exfiltration Restrictions:


  - Use Case: Prevent unauthorized transmission of sensitive data.

  - Implementation: Enforce policies to block unapproved email attachments, unauthorized USB usage, or unencrypted data uploads
  to cloud storage.


  Data-in-Transit Monitoring:


  - Use Case: Detect and prevent the transmission of sensitive data over unapproved channels.

  - Implementation: Deploy network-based DLP tools to inspect outbound traffic for sensitive content (e.g., financial records
  or PII) and block unapproved transmissions.


  Endpoint Data Protection:


  - Use Case: Monitor and control sensitive data usage on endpoints.

  - Implementation: Use endpoint-based DLP agents to block copy-paste actions of sensitive data and unauthorized printing
  or file sharing.


  Cloud Data Security:


  - Use Case: Protect data stored in cloud platforms.

  - Implementation: Integrate DLP with cloud storage platforms like Google Drive, OneDrive, or AWS to monitor and restrict
  sensitive data sharing or downloads.'
external_references:
- external_id: M1057
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1057
- description: Michael Swanagan. (2020, October 24). 7 Data Loss Prevention Best Practices & Strategies. Retrieved August
    30, 2021.
  source_name: PurpleSec Data Loss Prevention
  url: https://purplesec.us/data-loss-prevention/
id: course-of-action--65401701-019d-44ff-b223-08d520bb0e7b
modified: '2024-12-10T19:10:54.180Z'
name: Data Loss Prevention
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
