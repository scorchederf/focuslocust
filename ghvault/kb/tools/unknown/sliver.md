---
parsed_by: focuslocust
source: mitre
type: generated
---
# Sliver

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0633` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Sliver is an open source, cross-platform, red team command and control (C2) framework written in Golang. Sliver includes its own package manager, "armory," for staging and downloading additional tools and payloads to the primary C2 framework.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/sliver.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1001.002 - Steganography](../../attack/techniques/T1001.002-steganography.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can encode binary data into a .PNG file for C2 communication.(Citation: GitHub Sliver HTTP) |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) has a built-in `procdump` command allowing for retrieval of memory from processes such as `lsass.exe` for credential harvesting.(Citation: Cybereason Sliver Undated) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) has the ability to gather network configuration information.(Citation: GitHub Sliver Ifconfig) |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.(Citation: Microsoft Sliver 2022) |
| [T1027.004 - Compile After Delivery](../../attack/techniques/T1027.004-compile-after-delivery.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) includes functionality to retrieve source code and compile locally prior to execution in victim environments.(Citation: Cybereason Sliver Undated) |
| [T1027.013 - Encrypted／Encoded File](../../attack/techniques/T1027.013-encrypted-encoded-file.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can encrypt strings at compile time.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2) |
| [T1041 - Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can exfiltrate files from the victim using the <code>download</code> command.(Citation: GitHub Sliver Download) |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can collect network connection information.(Citation: GitHub Sliver Netstat) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.(Citation: Microsoft Sliver 2022)(Citation: Cybereason Sliver Undated)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) has built-in functionality to launch a Powershell command prompt.(Citation: Cybereason Sliver Undated) |
| [T1071 - Application Layer Protocol](../../attack/techniques/T1071-application-layer-protocol.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can utilize the Wireguard VPN protocol for command and control.(Citation: Cybereason Sliver Undated) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source |  [Sliver](https://attack.mitre.org/software/S0633) has the ability to support C2 communications over HTTP and HTTPS.(Citation: Cybersecurity Advisory SVR TTP May 2021)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2)(Citation: Cybereason Sliver Undated)(Citation: Microsoft Sliver 2022) |
| [T1071.004 - DNS](../../attack/techniques/T1071.004-dns.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can support C2 communications over DNS.(Citation: Cybersecurity Advisory SVR TTP May 2021)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2 DNS)(Citation: Cybereason Sliver Undated)(Citation: Microsoft Sliver 2022) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can enumerate files on a target system.(Citation: GitHub Sliver File System August 2021) |
| [T1090.001 - Internal Proxy](../../attack/techniques/T1090.001-internal-proxy.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) has a built-in SOCKS5 proxying capability allowing for [Sliver](https://attack.mitre.org/software/S0633) clients to proxy network traffic through other clients within a victim network.(Citation: Cybereason Sliver Undated) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can download additional content and files from the [Sliver](https://attack.mitre.org/software/S0633) server to the client residing on the victim machine using the <code>upload</code> command.(Citation: GitHub Sliver Upload)(Citation: Cybereason Sliver Undated) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can take screenshots of the victim’s active display.(Citation: GitHub Sliver Screen) |
| [T1132.001 - Standard Encoding](../../attack/techniques/T1132.001-standard-encoding.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can use standard encoding techniques like gzip and hex to ASCII to encode the C2 communication payload.(Citation: GitHub Sliver HTTP) |
| [T1134 - Access Token Manipulation](../../attack/techniques/T1134-access-token-manipulation.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) has the ability to manipulate user tokens on targeted Windows systems.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can leverage multiple techniques to bypass User Account Control (UAC) on Windows systems.(Citation: Cybereason Sliver Undated) |
| [T1558.001 - Golden Ticket](../../attack/techniques/T1558.001-golden-ticket.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) incorporates the [Rubeus](https://attack.mitre.org/software/S1071) framework to allow for Kerberos ticket manipulation, specifically for forging Kerberos Golden Tickets.(Citation: Cybereason Sliver Undated) |
| [T1573.001 - Symmetric Cryptography](../../attack/techniques/T1573.001-symmetric-cryptography.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can use AES-GCM-256 to encrypt a session key for C2 message exchange.(Citation: GitHub Sliver Encryption) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can use mutual TLS and RSA  cryptography to exchange a session key.(Citation: Cybersecurity Advisory SVR TTP May 2021)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver Encryption)(Citation: Cybereason Sliver Undated)(Citation: Microsoft Sliver 2022) |

## Source Verification

[source record](../../sources/mitre/sliver.md)

## Evidence Excerpt

```text
created: '2021-07-30T15:43:17.770Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Sliver](https://attack.mitre.org/software/S0633) is an open source, cross-platform, red team command and control
(C2) framework written in Golang. [Sliver](https://attack.mitre.org/software/S0633) includes its own package manager, "armory,"
for staging and downloading additional tools and payloads to the primary C2 framework.(Citation: Bishop Fox Sliver Framework
August 2019)(Citation: Cybereason Sliver Undated)'
external_references:
- external_id: S0633
```
