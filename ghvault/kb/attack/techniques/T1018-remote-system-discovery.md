---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1018 - Remote System Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1018` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  Ping, <code>net view</code> using Net, or, on ESXi servers, `esxcli network diag ping`.

Adversaries may also analyze data from local host files (ex: <code>C:\Windows\System32\Drivers\etc\hosts</code> or <code>/etc/hosts</code>) or other passive means (such as local Arp cache entries) in order to discover the presence of remote systems in an environment.

Adversaries may also target discovery of network infrastructure as well as leverage Network Device CLI commands on network devices to gather detailed information about systems within a network (e.g. <code>show cdp neighbors</code>, <code>show arp</code>).

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AdFind](../../tools/unknown/adfind.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) has the ability to query Active Directory for computers.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Cybereason Bumblebee August 2022) |
| [Arp](../../tools/unknown/arp.md) | explicit | source | [Arp](https://attack.mitre.org/software/S0099) can be used to display a host's ARP cache, which may include address resolutions for remote systems.(Citation: TechNet Arp)(Citation: Palo Alto ARP) |
| [BloodHound](../../tools/unknown/bloodhound.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can enumerate and collect the properties of domain computers, including domain controllers.(Citation: CrowdStrike BloodHound April 2018) |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active IP addresses, along with the machine name, within a targeted network.(Citation: CME Github September 2018) |
| [NBTscan](../../tools/unknown/nbtscan.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can list NetBIOS computer names.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [Net](../../tools/unknown/net.md) | explicit | source | Commands such as <code>net view</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about available remote systems.(Citation: Savill 1999) |
| [Nltest](../../tools/unknown/nltest.md) | explicit | source | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate remote domain controllers using options such as <code>/dclist</code> and <code>/dsgetdc</code>.(Citation: Nltest Manual) |
| [Ping](../../tools/unknown/ping.md) | explicit | source | [Ping](https://attack.mitre.org/software/S0097) can be used to identify remote systems within a network.(Citation: TechNet Ping) |
| [ROADTools](../../tools/unknown/roadtools.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD systems and devices.(Citation: Roadtools) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate and collect the properties of domain computers.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/remote-system-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:28.187Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier\
\ on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access\
\ tools to enable this, but utilities available on the operating system could also be used such as  [Ping](https://attack.mitre.org/software/S0097),\
\ <code>net view</code> using [Net](https://attack.mitre.org/software/S0039), or, on ESXi servers, `esxcli network diag\
\ ping`.\n\nAdversaries may also analyze data from local host files (ex: <code>C:\\Windows\\System32\\Drivers\\etc\\hosts</code>\
\ or <code>/etc/hosts</code>) or other passive means (such as local [Arp](https://attack.mitre.org/software/S0099) cache\
```
