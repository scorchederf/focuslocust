---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1613 - Container and Resource Discovery

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

## Summary

Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs. In Docker, logs may leak information about the environment, such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing. The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral movement and which methods to utilize for execution.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Peirates](../../tools/unknown/peirates.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can enumerate Kubernetes pods in a given namespace.(Citation: Peirates GitHub) |

## Source Verification

[source record](../../sources/mitre/container-and-resource-discovery.md)

## Evidence Excerpt

```text
created: '2021-03-31T14:26:00.848Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to discover containers and other resources that are available within a containers environment.
Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.
These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker
and Kubernetes APIs.(Citation: Docker API)(Citation: Kubernetes API) In Docker, logs may leak information about the environment,
such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing.
The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral
```
