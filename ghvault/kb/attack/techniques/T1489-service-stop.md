---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1489 - Service Stop

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1489` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment. 

Adversaries may accomplish this by disabling individual services of high importance to an organization, such as <code>MSExchangeIS</code>, which will make Exchange content inaccessible. In some cases, adversaries may stop or disable many or all services to render systems unusable. Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct Data Destruction or Data Encrypted for Impact on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure.

Threat actors may also disable or stop service in cloud environments. For example, by leveraging the `DisableAPIServiceAccess` API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization.

## Source Verification

[source record](../../sources/mitre/service-stop.md)

## Evidence Excerpt

```text
created: '2019-03-29T19:00:55.901Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may stop or disable services on a system to render those services unavailable to legitimate users.\
\ Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall\
\ objectives to cause damage to the environment.(Citation: Talos Olympic Destroyer 2018)(Citation: Novetta Blockbuster)\
\ \n\nAdversaries may accomplish this by disabling individual services of high importance to an organization, such as <code>MSExchangeIS</code>,\
\ which will make Exchange content inaccessible.(Citation: Novetta Blockbuster) In some cases, adversaries may stop or disable\
\ many or all services to render systems unusable.(Citation: Talos Olympic Destroyer 2018) Services or processes may not\
```
