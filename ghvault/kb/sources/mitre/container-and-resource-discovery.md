---
parsed_by: focuslocust
source: mitre
type: generated
---
# Container and Resource Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1613` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Container and Resource Discovery](../../attack/techniques/T1613-container-and-resource-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1613 |
| name | Container and Resource Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1613 |

## Preserved Source Material

```yaml
created: '2021-03-31T14:26:00.848Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to discover containers and other resources that are available within a containers environment.
  Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.


  These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker
  and Kubernetes APIs.(Citation: Docker API)(Citation: Kubernetes API) In Docker, logs may leak information about the environment,
  such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing.
  The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral
  movement and which methods to utilize for execution. '
external_references:
- external_id: T1613
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1613
- description: Docker. (n.d.). Docker Engine API v1.41 Reference. Retrieved March 31, 2021.
  source_name: Docker API
  url: https://docs.docker.com/engine/api/v1.41/
- description: The Kubernetes Authors. (n.d.). The Kubernetes API. Retrieved March 29, 2021.
  source_name: Kubernetes API
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
id: attack-pattern--0470e792-32f8-46b0-a351-652bc35e9336
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:20.661Z'
name: Container and Resource Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Vishwas Manral, McAfee
- Center for Threat-Informed Defense (CTID)
- Yossi Weizman, Azure Defender Research Team
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
x_mitre_version: '1.1'
```
