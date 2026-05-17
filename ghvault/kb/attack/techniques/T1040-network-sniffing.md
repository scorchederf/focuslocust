---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1040 - Network Sniffing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1040` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol. Techniques for name service resolution poisoning, such as Name Resolution Poisoning and SMB Relay, can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.

Network sniffing may reveal configuration details, such as running services, version numbers, and other network characteristics (e.g. IP addresses, hostnames, VLAN IDs) necessary for subsequent Lateral Movement and/or Stealth activities. Adversaries may likely also utilize network sniffing during Adversary-in-the-Middle (AiTM) to passively gain additional knowledge about the environment.

In cloud-based environments, adversaries may still be able to use traffic mirroring services to sniff network traffic from virtual machines. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to. Often, much of this traffic will be in cleartext due to the use of TLS termination at the load balancer level to reduce the strain of encrypting and decrypting traffic. The adversary can then use exfiltration techniques such as Transfer Data to Cloud Account in order to access the sniffed traffic.

On network devices, adversaries may perform network captures using Network Device CLI commands such as `monitor capture`.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can be used to conduct packet captures on target hosts.(Citation: Github PowerShell Empire) |
| [Impacket](../../tools/unknown/impacket.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) can be used to sniff network traffic via an interface or raw socket.(Citation: Impacket Tools) |
| [NBTscan](../../tools/unknown/nbtscan.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can dump and print whole packet content.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [Nmcap.exe](../../tools/windows/nmcap.exe.md) | explicit | source | Command metadata lists T1040: nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap} |
| [Pktmon.exe](../../tools/windows/pktmon.exe.md) | explicit | source | Command metadata lists T1040: pktmon.exe filter add -p 445 |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for taking packet captures on compromised hosts.(Citation: GitHub PoshC2) |
| [Responder](../../tools/unknown/responder.md) | explicit | source | [Responder](https://attack.mitre.org/software/S0174) captures hashes and credentials that are sent to the system after the name services have been poisoned.(Citation: GitHub Responder) |

## Source Verification

[source record](../../sources/mitre/network-sniffing.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:41.399Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may passively sniff network traffic to capture information about an environment, including authentication
material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture
information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to
passively access data in transit over the network, or use span ports to capture a larger amount of data.
Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol.
Techniques for name service resolution poisoning, such as [Name Resolution Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001),
```
