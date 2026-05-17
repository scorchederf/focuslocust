---
parsed_by: focuslocust
source: mitre
type: generated
---
# Container Enumeration

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

## Generated Concept Page

- [Container Enumeration](../../attack/data-sources/DC0091-container-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0091 |
| name | Container Enumeration |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0091 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "\"Container Enumeration\" data component captures events and actions related to listing and identifying active\
  \ or available containers within a containerized environment. This includes information about running, stopped, or configured\
  \ containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting\
  \ unauthorized discovery or reconnaissance efforts. Examples: \n\n- Docker Example: `docker ps`, `docker ps -a`\n- Kubernetes\
  \ Example: `kubectl get pods`, `kubectl get deployments`\n- Cloud Container Services Example\n    - AWS ECS: API Call: ListTasks\
  \ or ListContainers\n    - Azure Kubernetes Service: API Call: List pod or container instances.\n    - Google Kubernetes\
  \ Engine (GKE): API Call: Retrieve deployments and their associated containers."
external_references:
- external_id: DC0091
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0091
id: x-mitre-data-component--91b3ed33-d1b5-4c4b-a896-76c55eb3cfd8
modified: '2025-11-12T22:03:39.105Z'
name: Container Enumeration
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: docker ps, docker inspect, or docker images commands
  name: docker:daemon
- channel: DescribeCluster, ListClusters, ListNodegroups
  name: AWS:CloudTrail
- channel: e.g., containerd, Docker events
  name: containerd:runtime
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
