---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Device Configuration Dump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1602.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Device Configuration Dump](../../attack/techniques/T1602.002-network-device-configuration-dump.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1602.002 |
| name | Network Device Configuration Dump |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1602/002 |

## Preserved Source Material

```yaml
created: '2020-10-20T00:08:21.745Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may access network configuration files to collect sensitive data about the device and the network.
  The network configuration is a file containing parameters that determine the operation of the device. The device typically
  stores an in-memory copy of the configuration while operating, and a separate configuration on non-volatile storage to load
  after device reset. Adversaries can inspect the configuration files to reveal information about the target network and its
  layout, the network device and its software, or identifying legitimate accounts and credentials for later use.


  Adversaries can use common management tools and protocols, such as Simple Network Management Protocol (SNMP) and Smart Install
  (SMI), to access network configuration files.(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)(Citation:
  Cisco Blog Legacy Device Attacks) These tools may be used to query specific data from a configuration repository or configure
  the device to export the configuration for later analysis. '
external_references:
- external_id: T1602.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1602/002
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
- description: US-CERT. (2018, April 20). Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved
    October 19, 2020.
  source_name: US-CERT TA18-106A Network Infrastructure Devices 2018
  url: https://us-cert.cisa.gov/ncas/alerts/TA18-106A
- description: US-CERT. (2018, March 27). TA18-068A Brute Force Attacks Conducted by Cyber Actors. Retrieved October 2, 2019.
  source_name: US-CERT TA18-068A 2018
  url: https://www.us-cert.gov/ncas/alerts/TA18-086A
id: attack-pattern--52759bf1-fe12-4052-ace6-c5b0cf7dd7fd
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:47.219Z'
name: Network Device Configuration Dump
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
x_mitre_version: '1.1'
```
