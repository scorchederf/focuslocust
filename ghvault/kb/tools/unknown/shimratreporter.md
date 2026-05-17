---
parsed_by: focuslocust
source: mitre
type: generated
---
# ShimRatReporter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0445` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ShimRatReporter is a tool used by suspected Chinese adversary Mofang to automatically conduct initial discovery. The details from this discovery are used to customize follow-on payloads (such as ShimRat) as well as set up faux infrastructure which mimics the adversary's targets. ShimRatReporter has been used in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/shimratreporter.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host.(Citation: FOX-IT May 2016 Mofang) |
| [T1020 - Automated Exfiltration](../../attack/techniques/T1020-automated-exfiltration.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) sent collected system and network information compiled into a report to an adversary-controlled C2.(Citation: FOX-IT May 2016 Mofang) |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) encrypted gathered information with a combination of shifting and XOR using a static key.(Citation: FOX-IT May 2016 Mofang) |
| [T1036.005 - Match Legitimate Resource Name or Location](../../attack/techniques/T1036.005-match-legitimate-resource-name-or-location.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) spoofed itself as <code>AlphaZawgyl_font.exe</code>, a specialized Unicode font.(Citation: FOX-IT May 2016 Mofang) |
| [T1041 - Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) sent generated reports to the C2 via HTTP POST requests.(Citation: FOX-IT May 2016 Mofang) |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) used the Windows function <code>GetExtendedUdpTable</code> to detect connected UDP endpoints.(Citation: FOX-IT May 2016 Mofang) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) listed all running processes on the machine.(Citation: FOX-IT May 2016 Mofang) |
| [T1069 - Permission Groups Discovery](../../attack/techniques/T1069-permission-groups-discovery.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the local privileges for the infected host.(Citation: FOX-IT May 2016 Mofang) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) communicated over HTTP with preconfigured C2 servers.(Citation: FOX-IT May 2016 Mofang) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the operating system name and specific Windows version of an infected machine.(Citation: FOX-IT May 2016 Mofang) |
| [T1087 - Account Discovery](../../attack/techniques/T1087-account-discovery.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) listed all non-privileged and privileged accounts available on the machine.(Citation: FOX-IT May 2016 Mofang) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) had the ability to download additional payloads.(Citation: FOX-IT May 2016 Mofang) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) used several Windows API functions to gather information from the infected system.(Citation: FOX-IT May 2016 Mofang) |
| [T1119 - Automated Collection](../../attack/techniques/T1119-automated-collection.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered information automatically, without instruction from a C2, related to the user and host machine that is compiled into a report and sent to the operators.(Citation: FOX-IT May 2016 Mofang) |
| [T1518 - Software Discovery](../../attack/techniques/T1518-software-discovery.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered a list of installed software on the infected host.(Citation: FOX-IT May 2016 Mofang) |
| [T1560 - Archive Collected Data](../../attack/techniques/T1560-archive-collected-data.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) used LZ compression to compress initial reconnaissance reports before sending to the C2.(Citation: FOX-IT May 2016 Mofang)	 |

## Source Verification

[source record](../../sources/mitre/shimratreporter.md)

## Evidence Excerpt

```text
created: '2020-05-12T21:29:48.294Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[ShimRatReporter](https://attack.mitre.org/software/S0445) is a tool used by suspected Chinese adversary [Mofang](https://attack.mitre.org/groups/G0103)
to automatically conduct initial discovery. The details from this discovery are used to customize follow-on payloads (such
as [ShimRat](https://attack.mitre.org/software/S0444)) as well as set up faux infrastructure which mimics the adversary''s
targets. [ShimRatReporter](https://attack.mitre.org/software/S0445) has been used in campaigns targeting multiple countries
and sectors including government, military, critical infrastructure, automobile, and weapons development.(Citation: FOX-IT
May 2016 Mofang)'
```
