---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0030 - Pod Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0030` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Changes made to a pod’s configuration or control data within a containerized cluster. This can include updating settings such as resource limits, environment variables, annotations, labels, or even the containers running within the pod. Pod modifications are often executed using commands like kubectl set, kubectl patch, or kubectl edit.

*Data Collection Measures:* 

- Kubernetes API Server Audit Logs:
    - Capture all API calls related to pod modification, such as PATCH, PUT, or UPDATE methods on v1/pods.
- Runtime Security Tools:
    - Tools like Falco, Sysdig, and Kube-bench can monitor pod modifications at runtime and alert on policy violations.
- Container Orchestration Logs:
    - Monitor events logged by Kubernetes itself (e.g., `kubectl logs -n kube-system kube-controller-manager`).
- SIEM and EDR Solutions:
    - Use SIEM platforms (e.g., Splunk) to aggregate API server logs and detect patterns of unauthorized or suspicious pod modifications.
    - Endpoint Detection and Response (EDR) tools configured with container visibility can monitor commands like `kubectl` set or `kubectl patch`.
- Host-Based Monitoring:
    - Collect and analyze logs for processes executing `kubectl` commands or interacting with Kubernetes configuration files (e.g., `.kube/config`).

## Source Verification

[source record](../../sources/mitre/pod-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to a pod’s configuration or control data within a containerized cluster. This can include updating\
\ settings such as resource limits, environment variables, annotations, labels, or even the containers running within the\
\ pod. Pod modifications are often executed using commands like kubectl set, kubectl patch, or kubectl edit.\n\n*Data Collection\
\ Measures:* \n\n- Kubernetes API Server Audit Logs:\n    - Capture all API calls related to pod modification, such as PATCH,\
\ PUT, or UPDATE methods on v1/pods.\n- Runtime Security Tools:\n    - Tools like Falco, Sysdig, and Kube-bench can monitor\
\ pod modifications at runtime and alert on policy violations.\n- Container Orchestration Logs:\n    - Monitor events logged\
```
