---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0077 - Container Start

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0077` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

"Container Start" data component captures events related to the activation or invocation of a container within a containerized environment. This includes starting a previously stopped container, restarting an existing container, or initializing a container for runtime. Monitoring these activities is critical for identifying unauthorized or unexpected container activations, which may indicate potential adversarial activity or misconfigurations. Examples: 

- Docker Example: `docker start <container_name>`, `docker restart <container_name>`
- Kubernetes Example: Kubernetes automatically restarts containers as part of pod lifecycle management (e.g., due to health checks or configuration changes).
- Cloud-Native Example
    - AWS ECS: API Call: StartTask to activate a stopped ECS task.
    - Azure Container Instances: Command to restart a container group instance.
    - GCP Kubernetes Engine: Automatic restarts as part of node or pod management.

This data component can be collected through the following measures:

- Docker Audit Logging: Enable Docker logging to capture start and restart events. Use tools like auditd to monitor terminal activity involving container lifecycle commands.
- Kubernetes Audit Logs: Enable Kubernetes API server audit logging.
- Cloud Provider Logs
    - AWS CloudTrail: Capture StartTask or related API calls for ECS.
    - Azure Monitor: Track activity in container groups that indicate start or restart events.
    - GCP Cloud Logging: Record logs related to pod restarts or scaling events in Kubernetes Engine.
- SIEM Integration: Collect logs from Docker, Kubernetes, and cloud services to correlate container start events.

## Source Verification

[source record](../../sources/mitre/container-start.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "\"Container Start\" data component captures events related to the activation or invocation of a container within\
\ a containerized environment. This includes starting a previously stopped container, restarting an existing container,\
\ or initializing a container for runtime. Monitoring these activities is critical for identifying unauthorized or unexpected\
\ container activations, which may indicate potential adversarial activity or misconfigurations. Examples: \n\n- Docker\
\ Example: `docker start <container_name>`, `docker restart <container_name>`\n- Kubernetes Example: Kubernetes automatically\
\ restarts containers as part of pod lifecycle management (e.g., due to health checks or configuration changes).\n- Cloud-Native\
```
