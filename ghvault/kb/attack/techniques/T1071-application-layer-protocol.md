---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1071 - Application Layer Protocol

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1071` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can utilize the Wireguard VPN protocol for command and control.(Citation: Cybereason Sliver Undated) |

## Source Verification

[source record](../../sources/mitre/application-layer-protocol.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:56.776Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending\
\ in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within\
\ the protocol traffic between the client and server. \n\nAdversaries may utilize many different protocols, including those\
\ used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur\
\ internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are\
\ SMB, SSH, or RDP.(Citation: Mandiant APT29 Eye Spy Email Nov 22) "
```
