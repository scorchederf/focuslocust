---
parsed_by: focuslocust
source: mitre
type: generated
---
# Deploy Container

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1610` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Deploy Container](../../attack/techniques/T1610-deploy-container.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1610 |
| name | Deploy Container |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1610 |

## Preserved Source Material

```yaml
created: '2021-03-29T16:51:26.020Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases,
  adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes
  that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user
  limitations, etc. to bypass existing defenses within the environment. In Kubernetes environments, an adversary may attempt
  to deploy a privileged or vulnerable container into a specific node in order to [Escape to Host](https://attack.mitre.org/techniques/T1611)
  and access other containers running on the node. (Citation: AppSecco Kubernetes Namespace Breakout 2020)


  Containers can be deployed by various means, such as via Docker''s <code>create</code> and <code>start</code> APIs or via
  a web application such as the Kubernetes dashboard or Kubeflow. (Citation: Docker Container)(Citation: Kubernetes Dashboard)(Citation:
  Kubeflow Pipelines) In Kubernetes environments, containers may be deployed through workloads such as ReplicaSets or DaemonSets,
  which can allow containers to be deployed across multiple nodes.(Citation: Kubernetes Workload Management) Adversaries may
  deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious
  payloads at runtime.(Citation: Aqua Build Images on Hosts)'
external_references:
- external_id: T1610
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1610
- description: Abhisek Datta. (2020, March 18). Kubernetes Namespace Breakout using Insecure Host Path Volume — Part 1. Retrieved
    January 16, 2024.
  source_name: AppSecco Kubernetes Namespace Breakout 2020
  url: https://blog.appsecco.com/kubernetes-namespace-breakout-using-insecure-host-path-volume-part-1-b382f2a6e216
- description: 'Assaf Morag. (2020, July 15). Threat Alert: Attackers Building Malicious Images on Your Hosts. Retrieved March
    29, 2021.'
  source_name: Aqua Build Images on Hosts
  url: https://blog.aquasec.com/malicious-container-image-docker-container-host
- description: DockerDocs. (n.d.). Retrieved December 8, 2025.
  source_name: Docker Container
  url: https://docs.docker.com/reference/cli/docker/container/create/
- description: Kubernetes. (n.d.). Workload Management. Retrieved March 28, 2024.
  source_name: Kubernetes Workload Management
  url: https://kubernetes.io/docs/concepts/workloads/controllers/
- description: The Kubeflow Authors. (n.d.). Overview of Kubeflow Pipelines. Retrieved March 29, 2021.
  source_name: Kubeflow Pipelines
  url: https://www.kubeflow.org/docs/components/pipelines/overview/pipelines-overview/
- description: The Kubernetes Authors. (n.d.). Kubernetes Web UI (Dashboard). Retrieved March 29, 2021.
  source_name: Kubernetes Dashboard
  url: https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
id: attack-pattern--56e0d8b8-3e25-49dd-9050-3aa252f5aa92
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T19:59:11.024Z'
name: Deploy Container
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Alfredo Oliveira, Trend Micro
- Ariel Shuper, Cisco
- Center for Threat-Informed Defense (CTID)
- Idan Frimark, Cisco
- Joas Antonio dos Santos, @C0d3Cr4zy
- Magno Logan, @magnologan, Trend Micro
- Pawan Kinger, @kingerpawan, Trend Micro
- Vishwas Manral, McAfee
- Yossi Weizman, Azure Defender Research Team
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
