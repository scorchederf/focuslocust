---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0072
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0072-container-creation
---

## Description

"Container Creation" data component captures details about the initial construction of a container in a containerized environment. This includes events where a new container is instantiated, such as through Docker, Kubernetes, or other container orchestration platforms. Monitoring these events helps detect unauthorized or potentially malicious container creation. Examples:<br><br>- Docker Example: `docker create my-container`, `docker run --name=my-container nginx:latest`<br>- Kubernetes Example: `kubectl run my-pod --image=nginx`, `kubectl create deployment my-deployment --image=nginx`<br>- Cloud Container Services Example<br>    - AWS ECS: Task or service creation (`RunTask` or `CreateService`).<br>    - Azure Container Instances: Deployment of a container group.<br>    - Google Kubernetes Engine (GKE): Creation of new pods via GCP APIs.
