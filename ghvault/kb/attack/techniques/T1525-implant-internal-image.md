---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1525 - Implant Internal Image

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1525` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike Upload Malware, this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image.

A tool has been developed to facilitate planting backdoors in cloud container images. If an adversary has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a Web Shell.

## Source Verification

[source record](../../sources/mitre/implant-internal-image.md)

## Evidence Excerpt

```text
created: '2019-09-04T12:04:03.552Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may implant cloud or container images with malicious code to establish persistence after gaining
access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and
Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike [Upload Malware](https://attack.mitre.org/techniques/T1608/001),
this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how
the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed
to always use the latest image.(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)
```
