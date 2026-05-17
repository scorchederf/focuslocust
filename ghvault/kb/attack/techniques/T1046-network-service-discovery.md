---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1046 - Network Service Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1046` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as <code>dns-sd -B _ssh._tcp .</code>) to find other systems broadcasting the ssh service.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can conduct port scanning against targeted systems.(Citation: Palo Alto Brute Ratel July 2022) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can perform port scans from an infected host.(Citation: Github PowerShell Empire) |
| [FRP](../../tools/unknown/frp.md) | explicit | source | As part of load balancing [FRP](https://attack.mitre.org/software/S1144) can set `healthCheck.type = "tcp"` or `healthCheck.type = "http"` to check service status on specific hosts with TCPing or an HTTP request.(Citation: FRP GitHub) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can scan for open TCP ports on the target network.(Citation: Github Koadic) |
| [NBTscan](../../tools/unknown/nbtscan.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can be used to scan IP networks.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003) |
| [Peirates](../../tools/unknown/peirates.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can initiate a port scan against a given IP address.(Citation: Peirates GitHub) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can perform port scans from an infected host.(Citation: GitHub PoshC2) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has a built-in module for port scanning.(Citation: GitHub Pupy) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can scan for open ports on a compromised machine.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/network-service-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:43.915Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure\
\ devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information\
\ include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A\
\ FIVEHANDS May 2021)   \n\nWithin cloud environments, adversaries may attempt to discover services running on other cloud\
\ hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify\
\ services running on non-cloud systems as well.\n\nWithin macOS environments, adversaries may use the native Bonjour application\
```
