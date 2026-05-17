---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1538 - Cloud Service Dashboard

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1538` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public IP addresses and open ports.

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This also allows the adversary to gain information without manually making any API requests.

## Source Verification

[source record](../../sources/mitre/cloud-service-dashboard.md)

## Evidence Excerpt

```text
created: '2019-08-30T18:11:24.582Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an
operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can
be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public
IP addresses and open ports.(Citation: Google Command Center Dashboard)
Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical
dashboard than an API. This also allows the adversary to gain information without manually making any API requests.'
```
