---
parsed_by: focuslocust
source: mitre
type: generated
---
# Container Creation

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

## Generated Concept Page

- [Container Creation](../../attack/data-sources/DC0072-container-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0072 |
| name | Container Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0072 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "\"Container Creation\" data component captures details about the initial construction of a container in a containerized\
  \ environment. This includes events where a new container is instantiated, such as through Docker, Kubernetes, or other\
  \ container orchestration platforms. Monitoring these events helps detect unauthorized or potentially malicious container\
  \ creation. Examples:\n\n- Docker Example: `docker create my-container`, `docker run --name=my-container nginx:latest`\n\
  - Kubernetes Example: `kubectl run my-pod --image=nginx`, `kubectl create deployment my-deployment --image=nginx`\n- Cloud\
  \ Container Services Example\n    - AWS ECS: Task or service creation (`RunTask` or `CreateService`).\n    - Azure Container\
  \ Instances: Deployment of a container group.\n    - Google Kubernetes Engine (GKE): Creation of new pods via GCP APIs."
external_references:
- external_id: DC0072
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0072
id: x-mitre-data-component--a5ae90ca-0c4b-481c-959f-0eb18a7ff953
modified: '2025-11-12T22:03:39.105Z'
name: Container Creation
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
- channel: 'create/exec: Kubernetes API calls to exec into containers or create pods from curl, kubectl, or SDK clients'
  name: kubernetes:apiserver
- channel: container start/stop activity via Docker, containerd, or CRI-O
  name: kubernetes:events
- channel: container create/start with privileged flag or host volume mount
  name: docker:daemon
- channel: 'create: Pod/Container created with image tag ''latest'' or mutable tag; imagePullPolicy=Always; noDigest=true'
  name: kubernetes:audit
- channel: container run with restart policy set to 'always' or 'unless-stopped'
  name: systemd:unit
- channel: 'created,started: new container from untrusted registry or unexpected entrypoint'
  name: docker:events
- channel: create
  name: containerd:events
- channel: docker run with restart=always or modifying init
  name: docker:events
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
