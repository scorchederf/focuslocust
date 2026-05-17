---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1029 - Remote Data Storage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1029` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures:

Centralized Log Management:

- Configure endpoints to forward security logs to a centralized log collector or SIEM.
- Use tools like Splunk Graylog, or Security Onion to aggregate and store logs.
- Example command (Linux): `sudo auditd | tee /var/log/audit/audit.log | nc <remote-log-server> 514`

Remote File Storage Solutions:

- Utilize cloud storage solutions like AWS S3, Google Cloud Storage, or Azure Blob Storage for sensitive data.
- Ensure proper encryption at rest and access control policies (IAM roles, ACLs).

Intrusion Detection Log Forwarding:

- Forward logs from IDS/IPS systems (e.g., Zeek/Suricata) to a remote security information system.
- Example for Suricata log forwarding:
`outputs:
  - type: syslog
    protocol: tls
    address: <remote-syslog-server>`

Immutable Backup Configurations:

- Enable immutable storage settings for backups to prevent adversaries from modifying or deleting data.
- Example: AWS S3 Object Lock.

Data Encryption:

- Ensure encryption for sensitive data using AES-256 at rest and TLS 1.2+ for data in transit.
Tools: OpenSSL, BitLocker, LUKS for Linux.

## Source Verification

[source record](../../sources/mitre/remote-data-storage.md)

## Evidence Excerpt

```text
created: '2019-06-06T21:21:13.027Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host\
\ locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions,\
\ organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation\
\ can be implemented through the following measures:\n\nCentralized Log Management:\n\n- Configure endpoints to forward\
\ security logs to a centralized log collector or SIEM.\n- Use tools like Splunk Graylog, or Security Onion to aggregate\
\ and store logs.\n- Example command (Linux): `sudo auditd | tee /var/log/audit/audit.log | nc <remote-log-server> 514`\n\
```
