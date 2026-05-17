---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1610 - Deploy Container

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

## Summary

Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases, adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user limitations, etc. to bypass existing defenses within the environment. In Kubernetes environments, an adversary may attempt to deploy a privileged or vulnerable container into a specific node in order to Escape to Host and access other containers running on the node. 

Containers can be deployed by various means, such as via Docker's <code>create</code> and <code>start</code> APIs or via a web application such as the Kubernetes dashboard or Kubeflow.  In Kubernetes environments, containers may be deployed through workloads such as ReplicaSets or DaemonSets, which can allow containers to be deployed across multiple nodes. Adversaries may deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious payloads at runtime.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Peirates](../../tools/unknown/peirates.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can deploy a pod that mounts its node’s root file system, then execute a command to create a reverse shell on the node.(Citation: Peirates GitHub) |

## Source Verification

[source record](../../sources/mitre/deploy-container.md)

## Evidence Excerpt

```text
created: '2021-03-29T16:51:26.020Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases,
adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes
that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user
limitations, etc. to bypass existing defenses within the environment. In Kubernetes environments, an adversary may attempt
to deploy a privileged or vulnerable container into a specific node in order to [Escape to Host](https://attack.mitre.org/techniques/T1611)
and access other containers running on the node. (Citation: AppSecco Kubernetes Namespace Breakout 2020)
```
