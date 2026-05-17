---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data from Configuration Repository

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

## Generated Concept Page

- [Data from Configuration Repository](../../attack/techniques/T1602-data-from-configuration-repository.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1602 |
| name | Data from Configuration Repository |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1602 |

## Preserved Source Material

```yaml
created: '2020-10-19T23:46:13.931Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories
  are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories
  may also facilitate remote access and administration of devices.


  Adversaries may target these repositories in order to collect large quantities of sensitive system administration data.
  Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data,
  much of which may align with adversary Discovery objectives.(Citation: US-CERT-TA18-106A)(Citation: US-CERT TA17-156A SNMP
  Abuse 2017)'
external_references:
- external_id: T1602
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1602
- description: Cisco. (2008, June 10). Identifying and Mitigating Exploitation of the SNMP Version 3 Authentication Vulnerabilities.
    Retrieved October 19, 2020.
  source_name: Cisco Advisory SNMP v3 Authentication Vulnerabilities
  url: https://tools.cisco.com/security/center/content/CiscoAppliedMitigationBulletin/cisco-amb-20080610-SNMPv3
- description: US-CERT. (2017, June 5). Reducing the Risk of SNMP Abuse. Retrieved October 19, 2020.
  source_name: US-CERT TA17-156A SNMP Abuse 2017
  url: https://us-cert.cisa.gov/ncas/alerts/TA17-156A
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
id: attack-pattern--0ad7bc5c-235a-4048-944b-3b286676cb74
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:22.396Z'
name: Data from Configuration Repository
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
x_mitre_version: '1.1'
```
