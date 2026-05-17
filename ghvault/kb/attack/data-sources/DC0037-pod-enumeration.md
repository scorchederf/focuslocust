---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0037 - Pod Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0037` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Extracting a list of running or existing pods within a containerized cluster environment. Pods are the smallest deployable units in a Kubernetes cluster and typically represent an application or workload. Enumeration of pods provides insight into the structure and state of applications running in the cluster, such as the names of pods, their namespaces, and their associated metadata.

*Data Collection Measures:*

- Kubernetes API Server Audit Logs:
    - Enable Audit Logging in Kubernetes to capture API requests, such as GET `/api/v1/pods`.
- Container Runtime Logs:
    - Collect runtime-level logs from tools like CRI-O, containerd, or Docker, which might show relevant API calls for pod enumeration.
- EDR and SIEM:
    - Endpoint Detection and Response (EDR) tools, if configured with cluster-level visibility, can monitor user commands like `kubectl get pods`.
    - SIEM platforms (e.g., Splunk) can ingest Kubernetes API logs to detect enumeration patterns.
- Host-Based Monitoring:
    - Monitor processes and commands executed on nodes where `kubectl` is installed using tools like auditd, Sysmon for Linux, or kernel modules.

## Source Verification

[source record](../../sources/mitre/pod-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Extracting a list of running or existing pods within a containerized cluster environment. Pods are the smallest\
\ deployable units in a Kubernetes cluster and typically represent an application or workload. Enumeration of pods provides\
\ insight into the structure and state of applications running in the cluster, such as the names of pods, their namespaces,\
\ and their associated metadata.\n\n*Data Collection Measures:*\n\n- Kubernetes API Server Audit Logs:\n    - Enable Audit\
\ Logging in Kubernetes to capture API requests, such as GET `/api/v1/pods`.\n- Container Runtime Logs:\n    - Collect runtime-level\
\ logs from tools like CRI-O, containerd, or Docker, which might show relevant API calls for pod enumeration.\n- EDR and\
```
