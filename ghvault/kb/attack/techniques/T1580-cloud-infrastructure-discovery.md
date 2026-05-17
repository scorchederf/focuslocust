---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1580 - Cloud Infrastructure Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1580` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-as-a-service (IaaS) environment. This includes compute service resources such as instances, virtual machines, and snapshots as well as resources of other services including the storage and database services.

Cloud providers offer methods such as APIs and commands issued through CLIs to serve information about infrastructure. For example, AWS provides a <code>DescribeInstances</code> API within the Amazon EC2 API that can return information about one or more instances within an account, the <code>ListBuckets</code> API that returns a list of all buckets owned by the authenticated sender of the request, the <code>HeadBucket</code> API to determine a bucket’s existence along with access permissions of the request sender, or the <code>GetPublicAccessBlock</code> API to retrieve access block configuration for a bucket. Similarly, GCP's Cloud SDK CLI provides the <code>gcloud compute instances list</code> command to list all Google Compute Engine instances in a project , and Azure's CLI command <code>az vm list</code> lists details of virtual machines. In addition to API commands, adversaries can utilize open source tools to discover cloud storage infrastructure through Wordlist Scanning.

An adversary may enumerate resources using a compromised user's access keys to determine which are available to that user. The discovery of these available resources may help adversaries determine their next steps in the Cloud environment, such as establishing Persistence.An adversary may also use this information to change the configuration to make the bucket publicly accessible, allowing data to be accessed without authentication. Adversaries have also may use infrastructure discovery APIs such as <code>DescribeDBInstances</code> to determine size, owner, permissions, and network ACLs of database resources.  Adversaries can use this information to determine the potential value of databases and discover the requirements to access them. Unlike in Cloud Service Discovery, this technique focuses on the discovery of components of the provided services rather than the services themselves.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS infrastructure, such as EC2 instances.(Citation: GitHub Pacu) |
| [TruffleHog](../../tools/unknown/trufflehog.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate AWS Infrastructure to include EC2 instances.(Citation: Github TruffleSecurity Trufflehog April 2025) |

## Source Verification

[source record](../../sources/mitre/cloud-infrastructure-discovery.md)

## Evidence Excerpt

```text
created: '2020-08-20T17:51:25.671Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-as-a-service
(IaaS) environment. This includes compute service resources such as instances, virtual machines, and snapshots as well as
resources of other services including the storage and database services.
Cloud providers offer methods such as APIs and commands issued through CLIs to serve information about infrastructure. For
example, AWS provides a <code>DescribeInstances</code> API within the Amazon EC2 API that can return information about one
or more instances within an account, the <code>ListBuckets</code> API that returns a list of all buckets owned by the authenticated
```
