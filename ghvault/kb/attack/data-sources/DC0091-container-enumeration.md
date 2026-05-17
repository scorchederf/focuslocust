---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0091 - Container Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0091` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

"Container Enumeration" data component captures events and actions related to listing and identifying active or available containers within a containerized environment. This includes information about running, stopped, or configured containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting unauthorized discovery or reconnaissance efforts. Examples: 

- Docker Example: `docker ps`, `docker ps -a`
- Kubernetes Example: `kubectl get pods`, `kubectl get deployments`
- Cloud Container Services Example
    - AWS ECS: API Call: ListTasks or ListContainers
    - Azure Kubernetes Service: API Call: List pod or container instances.
    - Google Kubernetes Engine (GKE): API Call: Retrieve deployments and their associated containers.

## Source Verification

[source record](../../sources/mitre/container-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "\"Container Enumeration\" data component captures events and actions related to listing and identifying active\
\ or available containers within a containerized environment. This includes information about running, stopped, or configured\
\ containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting\
\ unauthorized discovery or reconnaissance efforts. Examples: \n\n- Docker Example: `docker ps`, `docker ps -a`\n- Kubernetes\
\ Example: `kubectl get pods`, `kubectl get deployments`\n- Cloud Container Services Example\n    - AWS ECS: API Call: ListTasks\
\ or ListContainers\n    - Azure Kubernetes Service: API Call: List pod or container instances.\n    - Google Kubernetes\
```
