---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1558 - Steal or Forge Kerberos Tickets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1558` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable Pass the Ticket. Kerberos is an authentication protocol widely used in modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants: client, service, and Key Distribution Center (KDC). Clients request access to a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos by stealing tickets or forging tickets to enable unauthorized access.

On Windows, the built-in <code>klist</code> utility can be used to list and analyze cached Kerberos tickets.

## Source Verification

[source record](../../sources/mitre/steal-or-forge-kerberos-tickets.md)

## Evidence Excerpt

```text
created: '2020-02-11T19:12:46.830Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable
[Pass the Ticket](https://attack.mitre.org/techniques/T1550/003). Kerberos is an authentication protocol widely used in
modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants:
client, service, and Key Distribution Center (KDC).(Citation: ADSecurity Kerberos Ring Decoder) Clients request access to
a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully
authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos
```
