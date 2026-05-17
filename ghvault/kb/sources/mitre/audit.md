---
parsed_by: focuslocust
source: mitre
type: generated
---
# Audit

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

## Generated Concept Page

- [Audit](../../attack/mitigations/M1047-audit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1047 |
| name | Audit |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1047 |

## Preserved Source Material

```yaml
created: '2019-06-11T17:06:14.029Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system\
  \ configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in\
  \ the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing\
  \ encompasses regular analysis of user behaviors and system logs in support of proactive security measures.\n\nAuditing\
  \ is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver.\
  \ It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements\
  \ demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures:\
  \ \n\nSystem Audit:\n\n- Use Case: Regularly assess system configurations to ensure compliance with organizational security\
  \ policies.\n- Implementation: Use tools to scan for deviations from established benchmarks.\n\nPermission Audits:\n\n-\
  \ Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation.\n- Implementation:\
  \ Run access reviews to identify users or groups with excessive permissions.\n\nSoftware Audits:\n\n- Use Case: Identify\
  \ outdated, unsupported, or insecure software that could serve as an attack vector.\n- Implementation: Use inventory and\
  \ vulnerability scanning tools to detect outdated versions and recommend secure alternatives.\n\nConfiguration Audits:\n\
  \n- Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA).\n\
  - Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify\
  \ non-compliant systems.\n\nNetwork Audits:\n\n- Use Case: Examine network traffic, firewall rules, and endpoint communications\
  \ to identify unauthorized or insecure connections.\n- Implementation: Utilize tools such as Wireshark, or Zeek to monitor\
  \ and log suspicious network behavior."
external_references:
- external_id: M1047
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1047
id: course-of-action--cc2399fd-3cd3-4319-8d0a-fbd6420cdaf8
modified: '2024-12-10T16:28:27.046Z'
name: Audit
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
x_mitre_version: '1.3'
```
