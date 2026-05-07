---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0030
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0030-pod-modification
---

## Description

Changes made to a pod’s configuration or control data within a containerized cluster. This can include updating settings such as resource limits, environment variables, annotations, labels, or even the containers running within the pod. Pod modifications are often executed using commands like kubectl set, kubectl patch, or kubectl edit.<br><br>*Data Collection Measures:* <br><br>- Kubernetes API Server Audit Logs:<br>    - Capture all API calls related to pod modification, such as PATCH, PUT, or UPDATE methods on v1/pods.<br>- Runtime Security Tools:<br>    - Tools like Falco, Sysdig, and Kube-bench can monitor pod modifications at runtime and alert on policy violations.<br>- Container Orchestration Logs:<br>    - Monitor events logged by Kubernetes itself (e.g., `kubectl logs -n kube-system kube-controller-manager`).<br>- SIEM and EDR Solutions:<br>    - Use SIEM platforms (e.g., Splunk) to aggregate API server logs and detect patterns of unauthorized or suspicious pod modifications.<br>    - Endpoint Detection and Response (EDR) tools configured with container visibility can monitor commands like `kubectl` set or `kubectl patch`.<br>- Host-Based Monitoring:<br>    - Collect and analyze logs for processes executing `kubectl` commands or interacting with Kubernetes configuration files (e.g., `.kube/config`).
