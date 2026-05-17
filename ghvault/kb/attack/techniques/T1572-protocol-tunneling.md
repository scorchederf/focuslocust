---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1572 - Protocol Tunneling

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1572` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. 

There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel. 

Protocol Tunneling may also be abused by adversaries during Dynamic Resolution. Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets. 

Adversaries may also leverage Protocol Tunneling in conjunction with Proxy and/or Protocol or Service Impersonation to further conceal C2 communications and infrastructure.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use DNS over HTTPS for C2.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022) |
| [FRP](../../tools/unknown/frp.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can tunnel SSH and Unix Domain Socket communications over TCP between external nodes and exposed resources behind firewalls or NAT.(Citation: FRP GitHub) |
| [Mythic](../../tools/unknown/mythic.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) can use SOCKS proxies to tunnel traffic through another protocol.(Citation: Mythc Documentation) |
| [ngrok](../../tools/unknown/ngrok.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) can tunnel RDP and other services securely over internet connections.(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes Ngrok February 2020)(Citation: Trend Micro Ngrok September 2020) |

## Source Verification

[source record](../../sources/mitre/protocol-tunneling.md)

## Evidence Excerpt

```text
created: '2020-03-15T16:03:39.082Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid\
\ detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating\
\ a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide\
\ an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise\
\ not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances\
\ or not routed over the Internet. \n\nThere are various means to encapsulate a protocol within another protocol. For example,\
```
