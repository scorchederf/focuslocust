---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1047 - Audit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1047` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.

Auditing is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver. It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures: 

System Audit:

- Use Case: Regularly assess system configurations to ensure compliance with organizational security policies.
- Implementation: Use tools to scan for deviations from established benchmarks.

Permission Audits:

- Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation.
- Implementation: Run access reviews to identify users or groups with excessive permissions.

Software Audits:

- Use Case: Identify outdated, unsupported, or insecure software that could serve as an attack vector.
- Implementation: Use inventory and vulnerability scanning tools to detect outdated versions and recommend secure alternatives.

Configuration Audits:

- Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA).
- Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify non-compliant systems.

Network Audits:

- Use Case: Examine network traffic, firewall rules, and endpoint communications to identify unauthorized or insecure connections.
- Implementation: Utilize tools such as Wireshark, or Zeek to monitor and log suspicious network behavior.

## Source Verification

[source record](../../sources/mitre/audit.md)

## Evidence Excerpt

```text
created: '2019-06-11T17:06:14.029Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system\
\ configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in\
\ the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing\
\ encompasses regular analysis of user behaviors and system logs in support of proactive security measures.\n\nAuditing\
\ is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver.\
\ It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements\
```
