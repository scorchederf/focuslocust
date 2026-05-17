---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1619 - Cloud Storage Object Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1619` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to File and Directory Discovery on a local host, after identifying available storage services (i.e. Cloud Infrastructure Discovery) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS  and List Blobs in Azure .

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes.(Citation: GitHub Pacu) |
| [Peirates](../../tools/unknown/peirates.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can list AWS S3 buckets.(Citation: Peirates GitHub) |
| [TruffleHog](../../tools/unknown/trufflehog.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) |

## Source Verification

[source record](../../sources/mitre/cloud-storage-object-discovery.md)

## Evidence Excerpt

```text
created: '2021-10-01T17:58:26.445Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during
automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar
to [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) on a local host, after identifying available
storage services (i.e. [Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580)) adversaries may access
the contents/objects stored in cloud infrastructure.
Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2
```
