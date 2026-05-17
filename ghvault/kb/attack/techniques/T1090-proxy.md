---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1090 - Proxy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1090` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including HTRAN, ZXProxy, and ZXPortMap.  Adversaries use these types of proxies to manage command and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries may chain together multiple proxies to further disguise the source of malicious traffic.

Adversaries can also take advantage of routing schemes in Content Delivery Networks (CDNs) to proxy command and control traffic.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [FRP](../../tools/unknown/frp.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can proxy communications through a server in public IP space to local servers located behind a NAT or firewall.(Citation: FRP GitHub) |
| [HTRAN](../../tools/unknown/htran.md) | explicit | source | [HTRAN](https://attack.mitre.org/software/S0040) can proxy TCP socket connections to obfuscate command and control infrastructure.(Citation: Operation Quantum Entanglement)(Citation: NCSC Joint Report Public Tools) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains modules that allow for use of proxies in command and control.(Citation: GitHub PoshC2) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can communicate over a reverse proxy using SOCKS5.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [netsh](../../tools/unknown/netsh.md) | explicit | source | [netsh](https://attack.mitre.org/software/S0108) can be used to set up a proxy tunnel to allow remote host access to an infected host.(Citation: Securelist fileless attacks Feb 2017) |
| [ngrok](../../tools/unknown/ngrok.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) can be used to proxy connections to machines located behind NAT or firewalls.(Citation: MalwareBytes Ngrok February 2020)(Citation: Zdnet Ngrok September 2018) |

## Source Verification

[source record](../../sources/mitre/proxy.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:08.479Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for
network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist
that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040),
ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command
and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face
of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries
```
