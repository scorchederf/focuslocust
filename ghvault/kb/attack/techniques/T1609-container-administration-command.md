---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1609 - Container Administration Command

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1609` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.

In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as <code>docker exec</code> to execute a command within a running container. In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as <code>kubectl exec</code>.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Peirates](../../tools/unknown/peirates.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can use `kubectl` or the Kubernetes API to run commands.(Citation: Peirates GitHub) |

## Source Verification

[source record](../../sources/mitre/container-administration-command.md)

## Evidence Excerpt

```text
created: '2021-03-29T16:39:26.183Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse a container administration service to execute commands within a container. A container
administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management
of containers within an environment.(Citation: Docker Daemon CLI)(Citation: Kubernetes API)(Citation: Kubernetes Kubelet)
In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they
may use a command such as <code>docker exec</code> to execute a command within a running container.(Citation: Docker Entrypoint)(Citation:
Docker Exec) In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in
```
