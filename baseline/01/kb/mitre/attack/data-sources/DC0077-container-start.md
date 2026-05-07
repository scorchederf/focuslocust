---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0077
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0077-container-start
---

## Description

"Container Start" data component captures events related to the activation or invocation of a container within a containerized environment. This includes starting a previously stopped container, restarting an existing container, or initializing a container for runtime. Monitoring these activities is critical for identifying unauthorized or unexpected container activations, which may indicate potential adversarial activity or misconfigurations. Examples: <br><br>- Docker Example: `docker start <container_name>`, `docker restart <container_name>`<br>- Kubernetes Example: Kubernetes automatically restarts containers as part of pod lifecycle management (e.g., due to health checks or configuration changes).<br>- Cloud-Native Example<br>    - AWS ECS: API Call: StartTask to activate a stopped ECS task.<br>    - Azure Container Instances: Command to restart a container group instance.<br>    - GCP Kubernetes Engine: Automatic restarts as part of node or pod management.<br><br>This data component can be collected through the following measures:<br><br>- Docker Audit Logging: Enable Docker logging to capture start and restart events. Use tools like auditd to monitor terminal activity involving container lifecycle commands.<br>- Kubernetes Audit Logs: Enable Kubernetes API server audit logging.<br>- Cloud Provider Logs<br>    - AWS CloudTrail: Capture StartTask or related API calls for ECS.<br>    - Azure Monitor: Track activity in container groups that indicate start or restart events.<br>    - GCP Cloud Logging: Record logs related to pod restarts or scaling events in Kubernetes Engine.<br>- SIEM Integration: Collect logs from Docker, Kubernetes, and cloud services to correlate container start events.
