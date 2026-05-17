---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data Backup

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1053` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data Backup](../../attack/mitigations/M1053-data-backup.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1053 |
| name | Data Backup |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1053 |

## Preserved Source Material

```yaml
created: '2019-07-19T14:33:33.543Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Data Backup involves taking and securely storing backups of data from end-user systems and critical servers.
  It ensures that data remains available in the event of system compromise, ransomware attacks, or other disruptions. Backup
  processes should include hardening backup systems, implementing secure storage solutions, and keeping backups isolated from
  the corporate network to prevent compromise during active incidents. This mitigation can be implemented through the following
  measures:


  Regular Backup Scheduling:

  - Use Case: Ensure timely and consistent backups of critical data.

  - Implementation: Schedule daily incremental backups and weekly full backups for all critical servers and systems.


  Immutable Backups:

  - Use Case: Protect backups from modification or deletion, even by attackers.

  - Implementation: Use write-once-read-many (WORM) storage for backups, preventing ransomware from encrypting or deleting
  backup files.


  Backup Encryption:

  - Use Case: Protect data integrity and confidentiality during transit and storage.

  - Implementation: Encrypt backups using strong encryption protocols (e.g., AES-256) before storing them in local, cloud,
  or remote locations.


  Offsite Backup Storage:

  - Use Case: Ensure data availability during physical disasters or onsite breaches.

  - Implementation: Use cloud-based solutions like AWS S3, Azure Backup, or physical offsite storage to maintain a copy of
  critical data.


  Backup Testing:

  - Use Case: Validate backup integrity and ensure recoverability.

  - Implementation: Regularly test data restoration processes to ensure that backups are not corrupted and can be recovered
  quickly.'
external_references:
- external_id: M1053
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1053
id: course-of-action--3efe43d1-6f3f-4fcb-ab39-4a730971f70b
modified: '2024-12-10T15:32:14.846Z'
name: Data Backup
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
x_mitre_version: '1.2'
```
