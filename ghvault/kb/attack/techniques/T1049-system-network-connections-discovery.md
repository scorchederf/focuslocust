---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1049 - System Network Connections Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1049` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network. 

An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate. Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.

Utilities and commands that acquire this information include netstat, "net use," and "net session" with Net. In Mac and Linux, netstat and <code>lsof</code> can be used to list current connections. <code>who -a</code> and <code>w</code> can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and Network Device CLI may be used (e.g. <code>show ip sockets</code>, <code>show tcp brief</code>). On ESXi servers, the command `esxi network ip connection list` can be used to list active network connections.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active sessions for a targeted system.(Citation: CME Github September 2018) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate the current network connections of a host.(Citation: Github PowerShell Empire) |
| [FRP](../../tools/unknown/frp.md) | explicit | source | [FRP](https://attack.mitre.org/software/S1144) can use a dashboard and U/I to display the status of connections from the FRP client and server.(Citation: FRP GitHub) |
| [Net](../../tools/unknown/net.md) | explicit | source | Commands such as <code>net use</code> and <code>net session</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about network connections from a particular host.(Citation: Savill 1999) |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | Once inside a Virtual Private Cloud, [Pacu](https://attack.mitre.org/software/S1091) can attempt to identify DirectConnect, VPN, or VPC Peering.(Citation: GitHub Pacu) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [netstat](https://attack.mitre.org/software/S0104) to enumerate TCP and UDP connections.(Citation: GitHub PoshC2) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has a built-in utility command for <code>netstat</code>, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.(Citation: GitHub Pupy) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) used the Windows function <code>GetExtendedUdpTable</code> to detect connected UDP endpoints.(Citation: FOX-IT May 2016 Mofang) |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can collect network connection information.(Citation: GitHub Sliver Netstat) |
| [nbtstat](../../tools/unknown/nbtstat.md) | explicit | source | [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover current NetBIOS sessions. |
| [netstat](../../tools/unknown/netstat.md) | explicit | source | [netstat](https://attack.mitre.org/software/S0104) can be used to enumerate local network connections, including active TCP connections and other network statistics.(Citation: TechNet Netstat) |

## Source Verification

[source record](../../sources/mitre/system-network-connections-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:45.139Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently\
\ accessing or from remote systems by querying for information over the network. \n\nAn adversary who gains access to a\
\ system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine\
\ what systems and services are connected. The actions performed are likely the same types of discovery techniques depending\
\ on the operating system, but the resulting information may include details about the networked cloud environment relevant\
\ to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.(Citation: Amazon\
```
