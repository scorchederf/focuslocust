---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1199 - Trusted Relationship

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1199` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.

Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, Valid Accounts used by the other party for access to internal network systems may be compromised and used.

In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions. By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant.

## Source Verification

[source record](../../sources/mitre/trusted-relationship.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through
trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than
standard mechanisms of gaining access to a network.
Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal
systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed
security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider''s access
```
