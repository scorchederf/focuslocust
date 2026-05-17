---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1612 - Build Image on Host

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1612` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval of malicious images from a public registry. A remote <code>build</code> request may be sent to the Docker API that includes a Dockerfile that pulls a vanilla base image, such as alpine, from a public or local registry and then builds a custom image upon it.

An adversary may take advantage of that <code>build</code> API to build a custom image on the host that includes malware downloaded from their C2 server, and then they may utilize Deploy Container using that custom image. If the base image is pulled from a public registry, defenses will likely not detect the image as malicious since it’s a vanilla image. If the base image already resides in a local registry, the pull may be considered even less suspicious since the image is already in the environment.

## Source Verification

[source record](../../sources/mitre/build-image-on-host.md)

## Evidence Excerpt

```text
created: '2021-03-30T17:54:03.944Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval
of malicious images from a public registry. A remote <code>build</code> request may be sent to the Docker API that includes
a Dockerfile that pulls a vanilla base image, such as alpine, from a public or local registry and then builds a custom image
upon it.(Citation: Docker Build Image)
An adversary may take advantage of that <code>build</code> API to build a custom image on the host that includes malware
downloaded from their C2 server, and then they may utilize [Deploy Container](https://attack.mitre.org/techniques/T1610)
```
