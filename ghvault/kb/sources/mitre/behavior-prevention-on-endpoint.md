---
parsed_by: focuslocust
source: mitre
type: generated
---
# Behavior Prevention on Endpoint

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1040` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Behavior Prevention on Endpoint](../../attack/mitigations/M1040-behavior-prevention-on-endpoint.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1040 |
| name | Behavior Prevention on Endpoint |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1040 |

## Preserved Source Material

```yaml
created: '2019-06-11T16:43:05.712Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially
  malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying
  solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous
  patterns indicative of an attack. This mitigation can be implemented through the following measures:


  Suspicious Process Behavior:


  - Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior,
  such as privilege escalation attempts.

  - Use Case: An attacker uses a known vulnerability to spawn a privileged process from a user-level application. The endpoint
  tool detects the abnormal parent-child process relationship and blocks the action.


  Unauthorized File Access:


  - Implementation: Leverage Data Loss Prevention (DLP) or endpoint tools to block processes attempting to access sensitive
  files without proper authorization.

  - Use Case: A process tries to read or modify a sensitive file located in a restricted directory, such as /etc/shadow on
  Linux or the SAM registry hive on Windows. The endpoint tool identifies this anomalous behavior and prevents it.


  Abnormal API Calls:


  - Implementation: Implement runtime analysis tools to monitor API calls and block those associated with malicious activities.

  - Use Case: A process dynamically injects itself into another process to hijack its execution. The endpoint detects the
  abnormal use of APIs like `OpenProcess` and `WriteProcessMemory` and terminates the offending process.


  Exploit Prevention:


  - Implementation: Use behavioral exploit prevention tools to detect and block exploits attempting to gain unauthorized access.

  - Use Case: A buffer overflow exploit is launched against a vulnerable application. The endpoint detects the anomalous memory
  write operation and halts the process.'
external_references:
- external_id: M1040
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1040
id: course-of-action--90f39ee1-d5a3-4aaa-9f28-3b42815b0d46
modified: '2024-12-10T16:29:44.429Z'
name: Behavior Prevention on Endpoint
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
