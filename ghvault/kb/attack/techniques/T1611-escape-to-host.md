---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1611 - Escape to Host

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1611` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may break out of a container or virtualized environment to gain access to the underlying host. This can allow an adversary access to other containerized or virtualized resources from the host level or to the host itself. In principle, containerized / virtualized resources should provide a clear separation of application functionality and be isolated from the host environment.

There are multiple ways an adversary may escape from a container to a host environment. Examples include creating a container configured to mount the host’s filesystem using the bind parameter, which allows the adversary to drop payloads and execute control utilities such as cron on the host; utilizing a privileged container to run commands or load a malicious kernel module on the underlying host; or abusing system calls such as `unshare` and `keyctl` to escalate privileges and steal secrets.

Additionally, an adversary may be able to exploit a compromised container with a mounted container management socket, such as `docker.sock`, to break out of the container via a Container Administration Command. Adversaries may also escape via Exploitation for Privilege Escalation, such as exploiting vulnerabilities in global symbolic links in order to access the root directory of a host machine.

In ESXi environments, an adversary may exploit a vulnerability in order to escape from a virtual machine into the hypervisor.

Gaining access to the host may provide the adversary with the opportunity to achieve follow-on objectives, such as establishing persistence, moving laterally within the environment, accessing other containers or virtual machines running on the host, or setting up a command and control channel on the host.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Peirates](../../tools/unknown/peirates.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can gain a reverse shell on a host node by mounting the Kubernetes hostPath.(Citation: Peirates GitHub) |

## Source Verification

[source record](../../sources/mitre/escape-to-host.md)

## Evidence Excerpt

```text
created: '2021-03-30T17:38:34.277Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may break out of a container or virtualized environment to gain access to the underlying host. This
can allow an adversary access to other containerized or virtualized resources from the host level or to the host itself.
In principle, containerized / virtualized resources should provide a clear separation of application functionality and be
isolated from the host environment.(Citation: Docker Overview)
There are multiple ways an adversary may escape from a container to a host environment. Examples include creating a container
configured to mount the host’s filesystem using the bind parameter, which allows the adversary to drop payloads and execute
```
