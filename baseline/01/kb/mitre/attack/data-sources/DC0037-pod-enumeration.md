---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0037
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0037-pod-enumeration
---

## Description

Extracting a list of running or existing pods within a containerized cluster environment. Pods are the smallest deployable units in a Kubernetes cluster and typically represent an application or workload. Enumeration of pods provides insight into the structure and state of applications running in the cluster, such as the names of pods, their namespaces, and their associated metadata.<br><br>*Data Collection Measures:*<br><br>- Kubernetes API Server Audit Logs:<br>    - Enable Audit Logging in Kubernetes to capture API requests, such as GET `/api/v1/pods`.<br>- Container Runtime Logs:<br>    - Collect runtime-level logs from tools like CRI-O, containerd, or Docker, which might show relevant API calls for pod enumeration.<br>- EDR and SIEM:<br>    - Endpoint Detection and Response (EDR) tools, if configured with cluster-level visibility, can monitor user commands like `kubectl get pods`.<br>    - SIEM platforms (e.g., Splunk) can ingest Kubernetes API logs to detect enumeration patterns.<br>- Host-Based Monitoring:<br>    - Monitor processes and commands executed on nodes where `kubectl` is installed using tools like auditd, Sysmon for Linux, or kernel modules.
