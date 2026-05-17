---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1040 - Behavior Prevention on Endpoint

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

## Summary

Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:

Suspicious Process Behavior:

- Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior, such as privilege escalation attempts.
- Use Case: An attacker uses a known vulnerability to spawn a privileged process from a user-level application. The endpoint tool detects the abnormal parent-child process relationship and blocks the action.

Unauthorized File Access:

- Implementation: Leverage Data Loss Prevention (DLP) or endpoint tools to block processes attempting to access sensitive files without proper authorization.
- Use Case: A process tries to read or modify a sensitive file located in a restricted directory, such as /etc/shadow on Linux or the SAM registry hive on Windows. The endpoint tool identifies this anomalous behavior and prevents it.

Abnormal API Calls:

- Implementation: Implement runtime analysis tools to monitor API calls and block those associated with malicious activities.
- Use Case: A process dynamically injects itself into another process to hijack its execution. The endpoint detects the abnormal use of APIs like `OpenProcess` and `WriteProcessMemory` and terminates the offending process.

Exploit Prevention:

- Implementation: Use behavioral exploit prevention tools to detect and block exploits attempting to gain unauthorized access.
- Use Case: A buffer overflow exploit is launched against a vulnerable application. The endpoint detects the anomalous memory write operation and halts the process.

## Source Verification

[source record](../../sources/mitre/behavior-prevention-on-endpoint.md)

## Evidence Excerpt

```text
created: '2019-06-11T16:43:05.712Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially
malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying
solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous
patterns indicative of an attack. This mitigation can be implemented through the following measures:
Suspicious Process Behavior:
- Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior,
```
