---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1602 - Data from Configuration Repository

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1602` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.

Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives.

## Source Verification

[source record](../../sources/mitre/data-from-configuration-repository.md)

## Evidence Excerpt

```text
created: '2020-10-19T23:46:13.931Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories
are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories
may also facilitate remote access and administration of devices.
Adversaries may target these repositories in order to collect large quantities of sensitive system administration data.
Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data,
much of which may align with adversary Discovery objectives.(Citation: US-CERT-TA18-106A)(Citation: US-CERT TA17-156A SNMP
```
