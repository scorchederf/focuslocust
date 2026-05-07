---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0091
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0091-container-enumeration
---

## Description

"Container Enumeration" data component captures events and actions related to listing and identifying active or available containers within a containerized environment. This includes information about running, stopped, or configured containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting unauthorized discovery or reconnaissance efforts. Examples: <br><br>- Docker Example: `docker ps`, `docker ps -a`<br>- Kubernetes Example: `kubectl get pods`, `kubectl get deployments`<br>- Cloud Container Services Example<br>    - AWS ECS: API Call: ListTasks or ListContainers<br>    - Azure Kubernetes Service: API Call: List pod or container instances.<br>    - Google Kubernetes Engine (GKE): API Call: Retrieve deployments and their associated containers.
