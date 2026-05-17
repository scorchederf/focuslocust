---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0072 - Container Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0072` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

"Container Creation" data component captures details about the initial construction of a container in a containerized environment. This includes events where a new container is instantiated, such as through Docker, Kubernetes, or other container orchestration platforms. Monitoring these events helps detect unauthorized or potentially malicious container creation. Examples:

- Docker Example: `docker create my-container`, `docker run --name=my-container nginx:latest`
- Kubernetes Example: `kubectl run my-pod --image=nginx`, `kubectl create deployment my-deployment --image=nginx`
- Cloud Container Services Example
    - AWS ECS: Task or service creation (`RunTask` or `CreateService`).
    - Azure Container Instances: Deployment of a container group.
    - Google Kubernetes Engine (GKE): Creation of new pods via GCP APIs.

## Source Verification

[source record](../../sources/mitre/container-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "\"Container Creation\" data component captures details about the initial construction of a container in a containerized\
\ environment. This includes events where a new container is instantiated, such as through Docker, Kubernetes, or other\
\ container orchestration platforms. Monitoring these events helps detect unauthorized or potentially malicious container\
\ creation. Examples:\n\n- Docker Example: `docker create my-container`, `docker run --name=my-container nginx:latest`\n\
- Kubernetes Example: `kubectl run my-pod --image=nginx`, `kubectl create deployment my-deployment --image=nginx`\n- Cloud\
\ Container Services Example\n    - AWS ECS: Task or service creation (`RunTask` or `CreateService`).\n    - Azure Container\
```
