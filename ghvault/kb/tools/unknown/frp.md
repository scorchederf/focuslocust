---
parsed_by: focuslocust
source: mitre
type: generated
---
# FRP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1144` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

FRP, which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. FRP can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/frp.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | As part of load balancing [FRP](https://attack.mitre.org/software/S1144) can set `healthCheck.type = "tcp"` or `healthCheck.type = "http"` to check service status on specific hosts with TCPing or an HTTP request.(Citation: FRP GitHub) |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can use a dashboard and U/I to display the status of connections from the FRP client and server.(Citation: FRP GitHub) |
| [T1059.007 - JavaScript](../../attack/techniques/T1059.007-javascript.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can support the use of a JSON configuration file.(Citation: FRP GitHub) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) has the ability to use HTTP and HTTPS to enable the forwarding of requests for internal services via domain name.(Citation: FRP GitHub) |
| [T1090 - Proxy](../../attack/techniques/T1090-proxy.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can proxy communications through a server in public IP space to local servers located behind a NAT or firewall.(Citation: FRP GitHub) |
| [T1090.003 - Multi-hop Proxy](../../attack/techniques/T1090.003-multi-hop-proxy.md) | explicit | source | The [FRP](https://attack.mitre.org/software/S1144) client can be configured to connect to the server through a proxy.(Citation: FRP GitHub) |
| [T1095 - Non-Application Layer Protocol](../../attack/techniques/T1095-non-application-layer-protocol.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can communicate over TCP, TCP stream multiplexing, KERN Communications Protocol (KCP), QUIC, and UDP.(Citation: FRP GitHub) |
| [T1572 - Protocol Tunneling](../../attack/techniques/T1572-protocol-tunneling.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can tunnel SSH and Unix Domain Socket communications over TCP between external nodes and exposed resources behind firewalls or NAT.(Citation: FRP GitHub) |
| [T1573.001 - Symmetric Cryptography](../../attack/techniques/T1573.001-symmetric-cryptography.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can use STCP (Secret TCP) with a preshared key to encrypt services exposed to public networks.(Citation: FRP GitHub) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can be configured to only accept TLS connections.(Citation: FRP GitHub) |

## Source Verification

[source record](../../sources/mitre/frp.md)

## Evidence Excerpt

```text
created: '2024-07-10T18:46:33.555Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[FRP](https://attack.mitre.org/software/S1144), which stands for Fast Reverse Proxy, is an openly available
tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet.
[FRP](https://attack.mitre.org/software/S1144) can support multiple protocols including TCP, UDP, and HTTP(S) and has been
abused by threat actors to proxy command and control communications.(Citation: FRP GitHub)(Citation: Joint Cybersecurity
Advisory Volt Typhoon June 2023)(Citation: RedCanary Mockingbird May 2020)(Citation: DFIR Phosphorus November 2021)'
external_references:
```
