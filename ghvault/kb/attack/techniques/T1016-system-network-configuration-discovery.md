---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1016 - System Network Configuration Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1016` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include Arp, ipconfig/ifconfig, nbtstat, and route.

Adversaries may also leverage a Network Device CLI on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. <code>show ip route</code>, <code>show ip interface</code>). On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the command `esxcli network nic list` will retrieve the MAC address, while `esxcli network ip interface ipv4 get` will retrieve the local IPv4 address.

Adversaries may use the information from System Network Configuration Discovery during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AdFind](../../tools/unknown/adfind.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) can extract subnet information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019) |
| [Arp](../../tools/unknown/arp.md) | explicit | source | [Arp](https://attack.mitre.org/software/S0099) can be used to display ARP configuration information on the host.(Citation: TechNet Arp) |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can enumerate the NetBIOS name on targeted machines.(Citation: ESET MirrorFace 2025) |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can collect DNS information from the targeted system.(Citation: CME Github September 2018) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can retrieve the contents of the IP routing table as well as information about the Windows domain.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [NBTscan](../../tools/unknown/nbtscan.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can be used to collect MAC addresses.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [Nltest](../../tools/unknown/nltest.md) | explicit | source | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate the parent domain of a local machine using <code>/parentdomain</code>.(Citation: Nltest Manual) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate network adapter information.(Citation: GitHub PoshC2) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.(Citation: GitHub Pupy) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host.(Citation: FOX-IT May 2016 Mofang) |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) has the ability to gather network configuration information.(Citation: GitHub Sliver Ifconfig) |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can capture information from each session with a victim including the public IP used to access the server and the user agent.(Citation: Sophos Evilginx MAR 2025) |
| [ifconfig](../../tools/unknown/ifconfig.md) | explicit | source | [ifconfig](https://attack.mitre.org/software/S0101) can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP. |
| [ipconfig](../../tools/unknown/ipconfig.md) | explicit | source | [ipconfig](https://attack.mitre.org/software/S0100) can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP. |
| [nbtstat](../../tools/unknown/nbtstat.md) | explicit | source | [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover local NetBIOS domain names. |
| [route](../../tools/unknown/route.md) | explicit | source | [route](https://attack.mitre.org/software/S0103) can be used to discover routing configuration information. |

## Source Verification

[source record](../../sources/mitre/system-network-configuration-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:27.342Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses,
of systems they access or through information discovery of remote systems. Several operating system administration utilities
exist that can be used to gather this information. Examples include [Arp](https://attack.mitre.org/software/S0099), [ipconfig](https://attack.mitre.org/software/S0100)/[ifconfig](https://attack.mitre.org/software/S0101),
[nbtstat](https://attack.mitre.org/software/S0102), and [route](https://attack.mitre.org/software/S0103).
Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to
gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes
```
